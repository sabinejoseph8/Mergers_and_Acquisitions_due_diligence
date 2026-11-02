#!/usr/bin/env python3
"""Download a real public company's SEC filings and financial data, as of a cutoff date, into a target folder.

The owner runs this before a diligence run. The agents never do: they stay offline and read only what it saved.
Standard library only.

  export SEC_USER_AGENT="Your Name your.address@example.com"
  python3 tools/fetch_edgar.py --company <ticker or CIK> --cutoff 2023-03-01 --target <name>

Options:
  --forms "10-K,10-Q,8-K,DEF 14A"   forms to keep; amendments (10-K/A and so on) are kept too
  --since 2020-03-01                 earliest filing date (default: three years before the cutoff)
  --force                            replace filings already downloaded for this target

It writes, under targets/<name>/:
  data/README.md                   the real-target label, the cutoff and what each folder holds
  data/sec-filings/index.md        every filing with its date, accession number, section files and SEC address
  data/sec-filings/<form>_<filed>_<accession>/
                                   the filing as plain text: one file per Item for a 10-K or 10-Q,
                                   the main document and its EX-99 exhibits for an 8-K, else full.txt
  data/financials/                 values from SEC's company facts data, each filed before the cutoff
  data/news/NO-SOURCES.md and data/litigation/NO-SOURCES.md
                                   these sources are not collected for a real target
  checks.json                      {"real": true, "cutoff": ...} for the automated checks
It never writes the deal brief or the answer key: the case session writes those.

SEC asks every request to name a contact (the SEC_USER_AGENT variable) and allows up to 10 requests a second.
A ticker is looked up in SEC's current ticker list; for a company that has since changed its ticker, pass the CIK.
"""
import argparse
import csv
import datetime as dt
import gzip
import json
import os
import pathlib
import re
import shutil
import sys
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent
SEC = "https://www.sec.gov"
DATA = "https://data.sec.gov"
DEFAULT_FORMS = ("10-K", "10-Q", "8-K", "DEF 14A")
REQUESTS_PER_SECOND = 5  # SEC allows 10; stay well under it
LABEL = "Real public company, hypothetical deal, as of {cutoff}."

# Item order in a 10-K, and (part, item) order in a 10-Q.
TEN_K = ["1", "1A", "1B", "1C", "2", "3", "4", "5", "6", "7", "7A", "8", "9", "9A", "9B", "9C", "10", "11", "12", "13", "14", "15", "16"]
TEN_Q = ["I-1", "I-2", "I-3", "I-4", "II-1", "II-1A", "II-2", "II-3", "II-4", "II-5", "II-6"]
ITEM_LINE = re.compile(r"^items?\s*(\d{1,2}[a-c]?)\b[\s.:\-–—]*(.*)$", re.I)
PART_LINE = re.compile(r"^part\s+(iv|iii|ii|i)\b", re.I)
SUBSTANTIVE = 250  # characters of text after a heading that mark it as a real section, not a contents entry

# Financial data: (row label, US-GAAP concepts in order of preference, unit, scale).
FINANCIALS = {
    "income_statement.csv": [
        ("Revenue", ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet",
                     "RevenueFromContractWithCustomerIncludingAssessedTax"], "USD", 1e6),
        ("Cost of revenue", ["CostOfRevenue", "CostOfGoodsAndServicesSold", "CostOfGoodsSold"], "USD", 1e6),
        ("Gross profit", ["GrossProfit"], "USD", 1e6),
        ("Research and development", ["ResearchAndDevelopmentExpense"], "USD", 1e6),
        ("Selling, general and administrative", ["SellingGeneralAndAdministrativeExpense"], "USD", 1e6),
        ("Operating income (loss)", ["OperatingIncomeLoss"], "USD", 1e6),
        ("Interest expense", ["InterestExpense", "InterestExpenseNonoperating", "InterestExpenseDebt"], "USD", 1e6),
        ("Income tax expense (benefit)", ["IncomeTaxExpenseBenefit"], "USD", 1e6),
        ("Net income (loss)", ["NetIncomeLoss", "ProfitLoss"], "USD", 1e6),
        ("Diluted EPS (US$ per share)", ["EarningsPerShareDiluted"], "USD/shares", 1),
        ("Diluted shares (millions)", ["WeightedAverageNumberOfDilutedSharesOutstanding"], "shares", 1e6),
    ],
    "balance_sheet.csv": [
        ("Cash and cash equivalents", ["CashAndCashEquivalentsAtCarryingValue"], "USD", 1e6),
        ("Accounts receivable, net", ["AccountsReceivableNetCurrent"], "USD", 1e6),
        ("Inventory", ["InventoryNet"], "USD", 1e6),
        ("Total current assets", ["AssetsCurrent"], "USD", 1e6),
        ("Goodwill", ["Goodwill"], "USD", 1e6),
        ("Intangible assets, net", ["IntangibleAssetsNetExcludingGoodwill", "FiniteLivedIntangibleAssetsNet"], "USD", 1e6),
        ("Total assets", ["Assets"], "USD", 1e6),
        ("Accounts payable", ["AccountsPayableCurrent"], "USD", 1e6),
        ("Total current liabilities", ["LiabilitiesCurrent"], "USD", 1e6),
        ("Long-term debt, noncurrent", ["LongTermDebtNoncurrent", "LongTermDebtAndCapitalLeaseObligations"], "USD", 1e6),
        ("Total liabilities", ["Liabilities"], "USD", 1e6),
        ("Total stockholders' equity", ["StockholdersEquity",
                                        "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"], "USD", 1e6),
    ],
    "cash_flow.csv": [
        ("Net cash from operating activities", ["NetCashProvidedByUsedInOperatingActivities"], "USD", 1e6),
        ("Capital expenditures", ["PaymentsToAcquirePropertyPlantAndEquipment"], "USD", 1e6),
        ("Net cash from investing activities", ["NetCashProvidedByUsedInInvestingActivities"], "USD", 1e6),
        ("Net cash from financing activities", ["NetCashProvidedByUsedInFinancingActivities"], "USD", 1e6),
        ("Depreciation and amortization", ["DepreciationDepletionAndAmortization", "DepreciationAndAmortization",
                                           "DepreciationAmortizationAndAccretionNet"], "USD", 1e6),
        ("Share-based compensation", ["ShareBasedCompensation"], "USD", 1e6),
    ],
}
PERIODIC_FORMS = {"10-K", "10-Q", "10-K/A", "10-Q/A", "10-KT", "10-KT/A"}


class Fetcher:
    """Gets SEC addresses with the contact header SEC requires, a few requests a second at most."""

    def __init__(self, user_agent):
        self.user_agent = user_agent
        self.last = 0.0

    def get(self, url):
        for attempt in range(4):
            wait = self.last + 1 / REQUESTS_PER_SECOND - time.monotonic()
            if wait > 0:
                time.sleep(wait)
            self.last = time.monotonic()
            request = urllib.request.Request(url, headers={"User-Agent": self.user_agent, "Accept-Encoding": "gzip"})
            try:
                with urllib.request.urlopen(request, timeout=60) as response:
                    body = response.read()
                    return gzip.decompress(body) if response.headers.get("Content-Encoding") == "gzip" else body
            except urllib.error.HTTPError as error:
                if error.code not in (429, 500, 502, 503, 504) or attempt == 3:
                    raise
                time.sleep(2 ** attempt)


def make_fetcher(env=None):
    """A Fetcher using SEC_USER_AGENT; stops with instructions if the contact is missing."""
    agent = (os.environ if env is None else env).get("SEC_USER_AGENT", "").strip()
    if "@" not in agent or " " not in agent:
        sys.exit('Set SEC_USER_AGENT to your name and email address first, for example:\n'
                 '  export SEC_USER_AGENT="Your Name your.address@example.com"\n'
                 'SEC asks every request to name a contact. Never commit it to the repository.')
    return Fetcher(agent)


# ---------------------------------------------------------------- filings

def decode(raw):
    for encoding in ("utf-8", "cp1252"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1")


class _Text(HTMLParser):
    """HTML to plain text: one line per block, table cells separated by " | ", hidden XBRL headers dropped."""
    BLOCK = {"p", "div", "br", "tr", "li", "h1", "h2", "h3", "h4", "h5", "h6", "table", "section", "ul", "ol",
             "center", "pre", "hr", "title"}
    SKIP = {"script", "style", "head", "ix:header", "noscript"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        elif tag in ("td", "th"):
            self.parts.append(" | ")
        elif tag in self.BLOCK:
            self.parts.append("\n")

    def handle_startendtag(self, tag, attrs):
        if tag in ("br", "hr"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            self.skip = max(0, self.skip - 1)
        elif tag in self.BLOCK:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def to_text(raw):
    """Plain text from an HTML or text document: one line per paragraph or table row, no empty lines."""
    text = decode(raw) if isinstance(raw, bytes) else raw
    if re.search(r"<(html|p|div|table)\b", text, re.I):
        parser = _Text()
        parser.feed(text)
        parser.close()
        text = "".join(parser.parts)
    else:
        text = re.sub(r"</?(PAGE|S|C|FN|CAPTION|TABLE)>", "", text)
    lines = []
    for line in text.replace("\xa0", " ").replace("​", "").splitlines():
        line = re.sub(r"[ \t]+", " ", line).strip()
        line = re.sub(r"(\s*\|\s*)+", " | ", line).strip(" |")
        if line:
            lines.append(line)
    return lines


def headings(lines, form):
    """Candidate Item headings as (line number, order key, title)."""
    order = TEN_Q if form.startswith("10-Q") else TEN_K
    part, found = "I", []
    for n, line in enumerate(lines):
        if len(line) > 200:
            continue
        p = PART_LINE.match(line)
        if p and len(line) <= 80:
            part = p.group(1).upper()
            continue
        m = ITEM_LINE.match(line)
        if not m:
            continue
        key = m.group(1).upper()
        key = f"{part}-{key}" if order is TEN_Q else key
        if key in order:
            found.append((n, order.index(key), key, line))
    return found


def split_items(lines, form):
    """Split a 10-K or 10-Q into Item sections, skipping the table of contents.

    Picks the in-order run of headings that covers the most substantive text, preferring the later run,
    so contents entries (headings with almost no text after them) are not mistaken for sections.
    Returns [(key, heading line, section lines)], with the text before the first Item as key "cover",
    or [] when fewer than three Items are found.
    """
    cands = headings(lines, form)
    if not cands:
        return []
    sizes = [sum(len(l) for l in lines[c[0] + 1:(cands[i + 1][0] if i + 1 < len(cands) else len(lines))])
             for i, c in enumerate(cands)]
    weight = [1.0 if s >= SUBSTANTIVE else 0.05 for s in sizes]
    best = [0.0] * len(cands)
    for i in range(len(cands) - 1, -1, -1):
        tail = [best[j] for j in range(i + 1, len(cands)) if cands[j][1] > cands[i][1]]
        best[i] = round(weight[i] + (max(tail) if tail else 0.0), 6)
    top = max(best)
    i = max(k for k in range(len(cands)) if best[k] == top)
    chosen = [i]
    while True:
        need = round(best[i] - weight[i], 6)
        nxt = next((j for j in range(i + 1, len(cands)) if cands[j][1] > cands[i][1] and best[j] == need), None)
        if nxt is None or need <= 0:
            break
        chosen.append(nxt)
        i = nxt
    if len(chosen) < 3:
        return []
    sections = [("cover", "Cover page and contents", lines[:cands[chosen[0]][0]])]
    for k, idx in enumerate(chosen):
        start = cands[idx][0]
        end = cands[chosen[k + 1]][0] if k + 1 < len(chosen) else len(lines)
        sections.append((cands[idx][2], cands[idx][3], lines[start:end]))
    return sections


def documents(raw):
    """(type, file name, content) for each document in an EDGAR complete submission text file."""
    for block in re.findall(r"<DOCUMENT>(.*?)</DOCUMENT>", decode(raw), re.S):
        kind = re.search(r"<TYPE>([^\n<]+)", block)
        name = re.search(r"<FILENAME>([^\n<]+)", block)
        body = re.search(r"<TEXT>(.*)</TEXT>", block, re.S)
        yield (kind.group(1).strip() if kind else "", name.group(1).strip() if name else "", body.group(1) if body else "")


def plain(text):
    """A filing's heading for the project's Markdown, which never uses em or en dashes."""
    return re.sub(r"\s*[–—]\s*", " - ", text)


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def list_filings(cik, fetcher, since):
    """Company name and every filing (accession, form, filed, period, primary document), newest pages only as needed."""
    sub = json.loads(fetcher.get(f"{DATA}/submissions/CIK{cik:010d}.json"))
    pages = [sub["filings"]["recent"]]
    for extra in sub["filings"].get("files", []):
        if extra.get("filingTo", "9999") >= since:
            pages.append(json.loads(fetcher.get(f"{DATA}/submissions/{extra['name']}")))
    rows = []
    for page in pages:
        for i, accession in enumerate(page["accessionNumber"]):
            rows.append({"accession": accession, "form": page["form"][i], "filed": page["filingDate"][i],
                         "period": (page.get("reportDate") or [""] * len(page["form"]))[i] or "",
                         "primary": page["primaryDocument"][i]})
    return sub.get("name", f"CIK {cik}"), rows


def save_filing(filing, cik, fetcher, folder):
    """Save one filing as text files in `folder`. Returns [(file name, title, kilobytes)]."""
    acc = filing["accession"]
    base = f"{SEC}/Archives/edgar/data/{cik}/{acc.replace('-', '')}"
    folder.mkdir(parents=True, exist_ok=True)
    files = []

    def write(name, title, lines):
        body = "\n".join(lines) + "\n"
        (folder / name).write_text(body, encoding="utf-8")
        files.append((name, title, max(1, round(len(body.encode("utf-8")) / 1024))))

    form = filing["form"]
    if form.startswith("8-K"):
        n = 0
        for kind, name, body in documents(fetcher.get(f"{base}/{acc}.txt")):
            if kind.startswith("8-K") or kind.upper().startswith("EX-99"):
                n += 1
                label = "main" if kind.startswith("8-K") else slug(kind)
                write(f"{n:02d}_{label}.txt", f"{kind} ({name})", to_text(body))
        if files:
            return files
    if filing["primary"]:
        lines = to_text(fetcher.get(f"{base}/{filing['primary']}"))
    else:  # no primary document listed: take the main document from the complete submission
        main_doc = next((body for kind, _, body in documents(fetcher.get(f"{base}/{acc}.txt")) if kind == form), "")
        lines = to_text(main_doc)
    sections = split_items(lines, form) if form.startswith(("10-K", "10-Q")) else []
    if not sections:
        write("full.txt", f"{form}, full text", lines)
        return files
    for n, (key, heading, body) in enumerate(sections):
        if key == "cover":
            name = "00_cover.txt"
        elif "-" in key:  # 10-Q: part and item
            part, item = key.split("-")
            name = f"{n:02d}_part-{part.lower()}_item-{item.lower()}.txt"
        else:
            name = f"{n:02d}_item-{key.lower()}.txt"
        write(name, heading, body)
    return files


# ---------------------------------------------------------------- financial data

def period_kind(fact):
    if "start" not in fact:
        return "instant"
    days = (dt.date.fromisoformat(fact["end"]) - dt.date.fromisoformat(fact["start"])).days + 1
    if 350 <= days <= 380:
        return "annual"
    if 80 <= days <= 100:
        return "quarter"
    return None


def save_financials(facts, cutoff, since, folder):
    """Write the statement CSVs and xbrl_facts.csv from company facts, using only values filed before the cutoff.

    For each concept and period, the value used is the latest one filed before the cutoff, so a restatement
    filed later cannot leak in. Returns the number of facts written to xbrl_facts.csv.
    """
    folder.mkdir(parents=True, exist_ok=True)
    gaap = facts.get("facts", {}).get("us-gaap", {})
    window = (dt.date.fromisoformat(since) - dt.timedelta(days=366)).isoformat()
    log, count = [], 0
    for filename, rows in FINANCIALS.items():
        chosen = {}  # (label, kind, start, end) -> fact
        for label, concepts, unit, scale in rows:
            for rank, concept in enumerate(concepts):
                for fact in gaap.get(concept, {}).get("units", {}).get(unit, []):
                    kind = period_kind(fact)
                    if (fact.get("filed", "9999") >= cutoff or fact.get("form") not in PERIODIC_FORMS
                            or kind is None or fact["end"] < window or fact["end"] >= cutoff):
                        continue
                    if (filename == "balance_sheet.csv") != (kind == "instant"):
                        continue
                    log.append([label, concept, unit, fact.get("start", ""), fact["end"], fact["val"], fact.get("form", ""),
                                fact.get("fy", ""), fact.get("fp", ""), fact["filed"], fact.get("accn", "")])
                    # Prefer the first concept listed; for the same concept, the latest value filed before the cutoff.
                    key = (label, kind, fact.get("start", ""), fact["end"])
                    best = chosen.get(key)
                    newer = best is not None and (fact["filed"], fact.get("accn", "")) >= (best[1]["filed"], best[1].get("accn", ""))
                    if best is None or rank < best[0] or (rank == best[0] and newer):
                        chosen[key] = (rank, fact, scale)
        periods = sorted({(k[1], k[2], k[3]) for k in chosen}, key=lambda p: ({"annual": 0, "quarter": 1, "instant": 0}[p[0]], p[2]))
        heads = [("FY_" if kind == "annual" else "Q_" if kind == "quarter" else "At_") + end for kind, _, end in periods]
        with open(folder / filename, "w", newline="", encoding="utf-8") as fh:
            out = csv.writer(fh)
            out.writerow(["line_item"] + heads)
            for label, _, _, scale in rows:
                cells = []
                for kind, start, end in periods:
                    hit = chosen.get((label, kind, start, end))
                    if hit is None:
                        cells.append("")
                    else:
                        value = hit[1]["val"] / hit[2]
                        cells.append(f"{value:.2f}" if hit[2] == 1 else f"{value:.1f}")
                out.writerow([label] + cells)
    with open(folder / "xbrl_facts.csv", "w", newline="", encoding="utf-8") as fh:
        out = csv.writer(fh)
        out.writerow(["line_item", "concept", "unit", "start", "end", "value", "form", "fiscal_year", "fiscal_period", "filed", "accession"])
        for row in sorted(log, key=lambda r: (r[0], r[4], r[9])):
            out.writerow(row)
            count += 1
    return count


# ---------------------------------------------------------------- the target folder

def write_readmes(data, label, name, cik, cutoff, since, forms, today):
    (data / "README.md").write_text(
        f"# Sources for a real public company\n\n> {label} {name} (CIK {cik}) is a real company. The deal is hypothetical. "
        f"Only sources dated before {cutoff} are included, downloaded from SEC EDGAR on {today} by `tools/fetch_edgar.py`. "
        "Use nothing else, including anything you may know about the company from elsewhere.\n\n"
        "| Folder | Holds | Specialist subagent |\n|---|---|---|\n"
        f"| `sec-filings/` | Filings ({', '.join(forms)}) filed from {since} to before {cutoff}, as plain text. Start with `sec-filings/index.md` | sec-filings-analyst |\n"
        "| `news/` | No sources (see `news/NO-SOURCES.md`) | news-media-analyst |\n"
        "| `litigation/` | No sources (see `litigation/NO-SOURCES.md`) | litigation-analyst |\n"
        "| `financials/` | Values from the company's structured filings data, each filed before the cutoff | financial-analyst |\n"
        "| `deal-brief.md` | The hypothetical deal and the Investment Committee's questions (written by the case session) | lead agent |\n\n"
        "Conventions: US$ millions unless stated. Negative numbers use a leading minus sign.\n", encoding="utf-8")
    (data / "financials" / "README.md").write_text(
        f"# Financial data\n\n> {label} Values from SEC's company facts data for {name}, each filed before {cutoff}.\n\n"
        "US$ millions unless stated. Columns: `FY_<end>` is the fiscal year ended on that date, `Q_<end>` the three months "
        "ended on that date, `At_<end>` a balance sheet date. A fourth quarter is usually reported only as part of the year: "
        "derive it as the year minus the first three quarters, and show the working.\n\n"
        "| File | Contents |\n|---|---|\n"
        "| `income_statement.csv` | Revenue, costs, operating income, interest, tax, net income, diluted EPS and shares |\n"
        "| `balance_sheet.csv` | Cash, receivables, inventory, goodwill, intangibles, debt, liabilities and equity |\n"
        "| `cash_flow.csv` | Operating, investing and financing cash flow, capital expenditures, depreciation and amortization, share-based pay |\n"
        "| `xbrl_facts.csv` | Every value behind those tables, with the filing it came from and its filing date |\n\n"
        "Where a filing restated a number before the cutoff, the tables show the latest value filed before the cutoff. "
        "Not available: customer-level revenue, segment detail, Adjusted EBITDA and operating KPIs. Look for them in the filings.\n",
        encoding="utf-8")
    for source in ("news", "litigation"):
        folder = data / source
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "NO-SOURCES.md").write_text(
            f"# No {source} sources\n\n> {label}\n\nFor a real company, {source} sources are not collected, so nothing here "
            "can be used as evidence. Report this as a gap in one line and return no findings. Never fill the gap from memory.\n",
            encoding="utf-8")


def write_index(data, label, name, cik, cutoff, since, forms, today, saved):
    out = ["# SEC filings index", "", f"> {label} Downloaded from SEC EDGAR on {today} by `tools/fetch_edgar.py`. "
           f"Only filings filed before {cutoff} are included.", "",
           f"Company: {name} (CIK {cik}). Forms: {', '.join(forms)}, with amendments. Filed from {since} to before {cutoff}.", "",
           "Start here. Each filing is a folder of plain-text files. A 10-K or 10-Q is split into one file per Item, so "
           "search with Grep, then read the sections you need. A filing marked \"not split\" is in `full.txt`.", "",
           "| Form | Filed | Period | Folder |", "|---|---|---|---|"]
    for filing, folder, _ in saved:
        out.append(f"| {filing['form']} | {filing['filed']} | {filing['period'] or 'n/a'} | `{folder}/` |")
    for filing, folder, files in saved:
        acc = filing["accession"]
        url = f"{SEC}/Archives/edgar/data/{cik}/{acc.replace('-', '')}/{filing['primary']}"
        split = any(fname != "full.txt" for fname, _, _ in files)
        out += ["", f"## {filing['form']} filed {filing['filed']}", "",
                f"- Accession {acc}. Period: {filing['period'] or 'n/a'}. SEC address: {url}"]
        if filing["form"].startswith(("10-K", "10-Q")) and not split:
            out.append("- Not split into sections: the Item headings could not be found. Read `full.txt`.")
        out += [f"- `{folder}/{fname}`: {plain(title)} ({kb} KB)" for fname, title, kb in files]
    (data / "sec-filings" / "index.md").write_text("\n".join(out) + "\n", encoding="utf-8")


def fetch(company, cutoff, target, fetcher, forms=DEFAULT_FORMS, since=None, root=ROOT, force=False, today=None):
    """Download everything for one real target. Returns the target folder."""
    cutoff_date = dt.date.fromisoformat(cutoff)
    since = since or (cutoff_date - dt.timedelta(days=1096)).isoformat()
    if since >= cutoff:
        sys.exit("--since must be before --cutoff")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", target):
        sys.exit("--target must be lower-case letters, digits and hyphens, for example: backtest-1")
    today = today or dt.date.today().isoformat()
    folder = pathlib.Path(root) / "targets" / target
    data = folder / "data"
    filings_dir = data / "sec-filings"
    brief = data / "deal-brief.md"
    if brief.exists() and "real public company" not in brief.read_text(encoding="utf-8").lower():
        sys.exit(f"{folder} looks like a fictional target. Pick a new target name.")
    if filings_dir.exists() and any(filings_dir.iterdir()):
        if not force:
            sys.exit(f"{filings_dir} already has filings. Use --force to download them again.")
        shutil.rmtree(filings_dir)

    if company.isdigit():
        cik = int(company)
    else:
        tickers = json.loads(fetcher.get(f"{SEC}/files/company_tickers.json"))
        match = next((r for r in tickers.values() if r["ticker"].upper() == company.upper()), None)
        if match is None:
            sys.exit(f"Ticker {company} is not in SEC's current ticker list. Pass the company's CIK instead.")
        cik = int(match["cik_str"])

    name, rows = list_filings(cik, fetcher, since)
    wanted = {f.upper() for f in forms}
    keep = sorted((r for r in rows if r["form"].upper().split("/")[0] in wanted and since <= r["filed"] < cutoff),
                  key=lambda r: (r["filed"], r["accession"]))
    label = LABEL.format(cutoff=cutoff)
    filings_dir.mkdir(parents=True, exist_ok=True)
    saved = []
    for filing in keep:
        sub = f"{filing['form'].replace(' ', '').replace('/', '-')}_{filing['filed']}_{filing['accession']}"
        print(f"  {filing['form']} filed {filing['filed']}")
        saved.append((filing, sub, save_filing(filing, cik, fetcher, filings_dir / sub)))

    facts = json.loads(fetcher.get(f"{DATA}/api/xbrl/companyfacts/CIK{cik:010d}.json"))
    count = save_financials(facts, cutoff, since, data / "financials")
    write_readmes(data, label, name, cik, cutoff, since, list(forms), today)
    write_index(data, label, name, cik, cutoff, since, list(forms), today, saved)

    checks_path = folder / "checks.json"
    checks = json.loads(checks_path.read_text(encoding="utf-8")) if checks_path.exists() else {}
    checks.update({"real": True, "cutoff": cutoff, "company": name, "cik": cik})
    checks_path.write_text(json.dumps(checks, indent=2) + "\n", encoding="utf-8")
    print(f"Saved {len(saved)} filings and {count} financial values for {name} in {folder}.")
    return folder


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--company", required=True, help="ticker or CIK")
    parser.add_argument("--cutoff", required=True, help="YYYY-MM-DD: keep only filings filed before this date")
    parser.add_argument("--target", required=True, help="name of the new folder in targets/")
    parser.add_argument("--forms", default=",".join(DEFAULT_FORMS), help="comma-separated forms to keep")
    parser.add_argument("--since", help="YYYY-MM-DD: earliest filing date (default: three years before the cutoff)")
    parser.add_argument("--force", action="store_true", help="replace filings already downloaded for this target")
    args = parser.parse_args(argv)
    fetcher = make_fetcher()
    forms = tuple(f.strip() for f in args.forms.split(",") if f.strip())
    folder = fetch(args.company, args.cutoff, args.target, fetcher, forms=forms, since=args.since, force=args.force)
    print("Next: the case session writes data/deal-brief.md and evaluation/answer-key.md, then run:\n"
          f"  python3 tests/run_all.py --write-manifest --target {folder.name}")


if __name__ == "__main__":
    main()

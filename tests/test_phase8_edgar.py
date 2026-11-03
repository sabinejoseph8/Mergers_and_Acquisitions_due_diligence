"""Phase 8: the EDGAR download tool keeps to its cutoff, splits filings into sections and labels a real target.
Runs on built-in sample responses, with no network."""
import contextlib
import csv
import importlib.util
import io
import json
import pathlib
import re
import tempfile
import unittest

from _common import ROOT

CIK = 1234567
CUTOFF = "2023-03-01"
BASE = f"https://www.sec.gov/Archives/edgar/data/{CIK}"
FILLER = "The company designs, makes and sells industrial sensors to customers in North America and Europe. " * 4

# (accession, form, filed, period, primary document); the last three are on or after the cutoff, or not a kept form.
FILINGS = [
    ("0001234567-22-000010", "10-K", "2022-02-25", "2021-12-31", "tst-20211231.htm"),
    ("0001234567-22-000020", "10-Q", "2022-05-05", "2022-03-31", "tst-20220331.htm"),
    ("0001234567-22-000030", "8-K", "2022-11-01", "2022-11-01", "tst-8k.htm"),
    ("0001234567-23-000010", "10-K", "2023-02-28", "2022-12-31", "tst-20221231.htm"),
    ("0001234567-23-000020", "10-K/A", "2023-03-01", "2022-12-31", "tst-20221231a.htm"),
    ("0001234567-23-000030", "8-K", "2023-06-01", "2023-06-01", "tst-8k-later.htm"),
    ("0001234567-22-000040", "4", "2022-06-01", "", "form4.xml"),
]
LATER = {"0001234567-23-000020", "0001234567-23-000030", "0001234567-22-000040"}
LATER_NAME = "Renamed Holdings Corp."  # the name SEC shows today, adopted after the cutoff


def ten_k(year, messy=False):
    """A small 10-K with a table of contents. A messy one is like real filings that broke the first version:
    the body drops one Item's "Item n." label (so the contents list more Items than the body shows), the source
    HTML breaks lines inside each heading, and the financial statements come after the signatures."""
    items = [("1", "Business"), ("1A", "Risk Factors"), ("2", "Properties"), ("3", "Legal Proceedings"),
             ("7", "Management's Discussion and Analysis"), ("8", "Financial Statements"), ("9A", "Controls and Procedures")]
    contents = "".join(f"<tr><td>Item {k}.</td><td>{t}</td><td>{n + 3}</td></tr>" for n, (k, t) in enumerate(items))
    label = (lambda k: "" if k == "2" else f"Item\n      {k}. ") if messy else (lambda k: f"Item {k}. ")
    body = "".join(f"<p><b>{label(k)}{t}</b></p><p>{t} text for {year}. {FILLER}</p>" for k, t in items)
    if messy:
        body += ("<p>SIGNATURES</p><p>Signed on behalf of the registrant.</p><p>CONSOLIDATED BALANCE SHEETS</p>"
                 f"<p>{FILLER * 6}</p><p>NOTES TO CONSOLIDATED FINANCIAL STATEMENTS</p><p>Note text for {year}. {FILLER * 40}</p>")
    return (f"<html><head><title>10-K</title></head><body><ix:header><ix:hidden>hidden-xbrl-text</ix:hidden></ix:header>"
            f"<p>ANNUAL REPORT FOR {year}</p><p>Table of Contents</p><table>{contents}</table>{body}</body></html>").encode()


def ten_q():
    """A 10-Q whose body never repeats "PART I" after the contents page, so only the Item titles say which part
    each Item belongs to. One heading has its title on the next line."""
    contents = "".join(f"<tr><td>{h}</td><td>{p}</td></tr>" for h, p in [
        ("PART I. FINANCIAL INFORMATION", ""), ("Item 1. Financial Statements", 3), ("Item 2. Management's Discussion and Analysis", 12),
        ("Item 4. Controls and Procedures", 20), ("PART II. OTHER INFORMATION", ""), ("Item 1. Legal Proceedings", 21),
        ("Item 1A. Risk Factors", 21)])
    sections = [("Item 1. Financial Statements", None), ("CONDENSED CONSOLIDATED BALANCE SHEETS", f"statements section. {FILLER * 14}"),
                ("Item 2.", None), ("Management's Discussion and Analysis", "discussion"), ("Item 4. Controls and Procedures", "controls"),
                ("PART II. OTHER INFORMATION", None), ("Item 1. Legal Proceedings", "legal"), ("Item 1A. Risk Factors", "quarterly risk")]
    body = "".join(f"<p>{h}</p>" + (f"<p>The {t} section. {FILLER}</p>" if t else "") for h, t in sections)
    return f"<html><body><p>QUARTERLY REPORT</p><table>{contents}</table>{body}</body></html>".encode()


EIGHT_K = (
    "<SEC-DOCUMENT>\n<DOCUMENT>\n<TYPE>8-K\n<SEQUENCE>1\n<FILENAME>tst-8k.htm\n<TEXT>\n"
    "<html><body><p>Item 2.02 Results of Operations and Financial Condition.</p><p>See Exhibit 99.1.</p></body></html>\n"
    "</TEXT>\n</DOCUMENT>\n<DOCUMENT>\n<TYPE>EX-99.1\n<SEQUENCE>2\n<FILENAME>ex991.htm\n<TEXT>\n"
    "<html><body><p>Press release: third quarter revenue of $31.0 million.</p></body></html>\n"
    "</TEXT>\n</DOCUMENT>\n<DOCUMENT>\n<TYPE>GRAPHIC\n<SEQUENCE>3\n<FILENAME>logo.jpg\n<TEXT>\nbegin 644 logo.jpg\n</TEXT>\n</DOCUMENT>\n"
    "</SEC-DOCUMENT>\n").encode()


def fact(start, end, val, filed, form, accn):
    row = {"end": end, "val": val, "filed": filed, "form": form, "accn": accn, "fy": int(end[:4]), "fp": "FY"}
    if start:
        row["start"] = start
    return row


FACTS = {"cik": CIK, "entityName": "Sample Sensors Inc.", "facts": {"us-gaap": {
    "Revenues": {"units": {"USD": [
        fact("2021-01-01", "2021-12-31", 100e6, "2022-02-25", "10-K", "0001234567-22-000010"),
        fact("2021-01-01", "2021-12-31", 90e6, "2023-05-01", "10-K/A", "0001234567-23-000040"),  # restated after the cutoff
        fact("2022-01-01", "2022-03-31", 25e6, "2022-05-05", "10-Q", "0001234567-22-000020"),
        fact("2022-01-01", "2022-12-31", 120e6, "2023-02-28", "10-K", "0001234567-23-000010"),
    ]}},
    "Assets": {"units": {"USD": [
        fact(None, "2021-12-31", 500e6, "2022-02-25", "10-K", "0001234567-22-000010"),
        fact(None, "2022-12-31", 520e6, "2023-02-28", "10-K", "0001234567-23-000010"),
    ]}},
}}}


def responses():
    recent = {key: [] for key in ("accessionNumber", "form", "filingDate", "reportDate", "primaryDocument")}
    for acc, form, filed, period, primary in FILINGS:
        for key, value in zip(recent, (acc, form, filed, period, primary)):
            recent[key].append(value)
    pages = {
        "https://www.sec.gov/files/company_tickers.json": {"0": {"cik_str": CIK, "ticker": "TST", "title": "Sample Sensors Inc."}},
        # SEC lists a company under its current name; this one was renamed after the cutoff.
        f"https://data.sec.gov/submissions/CIK{CIK:010d}.json": {
            "name": LATER_NAME, "formerNames": [{"name": "Sample Sensors Inc.", "from": "2005-03-01T00:00:00.000Z", "to": "2024-01-15T00:00:00.000Z"}],
            "filings": {"recent": recent, "files": []}},
        f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK:010d}.json": FACTS,
    }
    out = {url: json.dumps(body).encode() for url, body in pages.items()}
    out[f"{BASE}/000123456722000010/tst-20211231.htm"] = ten_k(2021, messy=True)
    out[f"{BASE}/000123456723000010/tst-20221231.htm"] = ten_k(2022)
    out[f"{BASE}/000123456722000020/tst-20220331.htm"] = ten_q()
    out[f"{BASE}/000123456722000030/0001234567-22-000030.txt"] = EIGHT_K
    return out


class FakeFetcher:
    """Answers from the sample responses and records every address asked for."""

    def __init__(self):
        self.pages, self.requested = responses(), []

    def get(self, url):
        self.requested.append(url)
        if url not in self.pages:
            raise AssertionError(f"unexpected request: {url}")
        return self.pages[url]


def load_tool():
    spec = importlib.util.spec_from_file_location("fetch_edgar", ROOT / "tools" / "fetch_edgar.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def table(path):
    with open(path, encoding="utf-8") as fh:
        rows = list(csv.reader(fh))
    return rows[0], {r[0]: r for r in rows[1:]}


class TestFetchEdgar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tool = load_tool()
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = pathlib.Path(cls.tmp.name)
        cls.fetcher = FakeFetcher()
        with contextlib.redirect_stdout(io.StringIO()):
            cls.folder = cls.tool.fetch("TST", CUTOFF, "backtest-sample", cls.fetcher, root=cls.root, today="2026-11-02")
        cls.data = cls.folder / "data"
        cls.filings = cls.data / "sec-filings"
        cls.index = (cls.filings / "index.md").read_text(encoding="utf-8")

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def filing(self, prefix):
        return next(p for p in self.filings.iterdir() if p.is_dir() and p.name.startswith(prefix))

    def test_keeps_no_filing_filed_on_or_after_the_cutoff(self):
        folders = sorted(p.name for p in self.filings.iterdir() if p.is_dir())
        self.assertEqual(len(folders), 4, folders)
        self.assertTrue(all(name.split("_")[1] < CUTOFF for name in folders), folders)
        dates = re.findall(r"^\| [^|]+ \| (\d{4}-\d{2}-\d{2}) \|", self.index, re.M)
        self.assertEqual(len(dates), 4)
        self.assertTrue(all(d < CUTOFF for d in dates), dates)
        asked = " ".join(self.fetcher.requested)
        for acc in LATER:
            self.assertNotIn(acc.replace("-", ""), asked, f"downloaded a filing it should have skipped: {acc}")

    def test_splits_filings_into_items_and_indexes_every_file(self):
        names = sorted(p.name for p in self.filing("10-K_2023-02-28").iterdir())
        for item in ("item-1", "item-1a", "item-7", "item-8", "item-9a"):
            self.assertTrue(any(n.endswith(f"_{item}.txt") for n in names), f"10-K has no {item}: {names}")
        for prefix, year in (("10-K_2023-02-28", 2022), ("10-K_2022-02-25", 2021)):
            risk = next(self.filing(prefix).glob("*_item-1a.txt")).read_text(encoding="utf-8")
            self.assertTrue(risk.startswith("Item 1A. Risk Factors"), f"{year}: section must start at its heading, not the contents entry")
            self.assertIn(f"Risk Factors text for {year}", risk)
        quarter = sorted(p.name for p in self.filing("10-Q_").iterdir())
        self.assertTrue(any(n.endswith("_part-ii_item-1a.txt") for n in quarter), quarter)
        self.assertEqual(sorted(p.name for p in self.filing("8-K_").iterdir()), ["01_main.txt", "02_ex-99-1.txt"])
        everything = "".join(p.read_text(encoding="utf-8") for p in self.filings.rglob("*.txt"))
        self.assertNotIn("hidden-xbrl-text", everything, "hidden XBRL header text leaked into the filing text")
        for path in self.filings.rglob("*.txt"):
            self.assertIn(f"`{path.parent.name}/{path.name}`", self.index, f"index.md does not list {path.name}")

    def test_puts_statements_after_the_signatures_in_their_own_file(self):
        folder = self.filing("10-K_2022-02-25")
        after = list(folder.glob("*_after-signatures.txt"))
        self.assertEqual(len(after), 1, sorted(p.name for p in folder.iterdir()))
        self.assertIn("NOTES TO CONSOLIDATED FINANCIAL STATEMENTS", after[0].read_text(encoding="utf-8"))
        last_item = next(folder.glob("*_item-9a.txt")).read_text(encoding="utf-8")
        self.assertNotIn("NOTES TO CONSOLIDATED", last_item, "the statements padded the last Item")
        line = next(l for l in self.index.splitlines() if after[0].name in l)
        self.assertIn("includes financial statements", line)

    def test_labels_quarterly_items_by_title_when_the_part_heading_is_missing(self):
        folder = self.filing("10-Q_")
        statements = next(folder.glob("*_part-i_item-1.txt")).read_text(encoding="utf-8")
        self.assertIn("The statements section", statements)
        self.assertTrue(list(folder.glob("*_part-i_item-2.txt")), sorted(p.name for p in folder.iterdir()))
        line = next(l for l in self.index.splitlines() if "_part-i_item-1.txt" in l and folder.name in l)
        self.assertIn("includes financial statements", line)
        risk = next(l for l in self.index.splitlines() if "_part-ii_item-1a.txt" in l and folder.name in l)
        self.assertNotIn("includes financial statements", risk)

    def test_stops_without_the_sec_contact(self):
        for env in ({}, {"SEC_USER_AGENT": "nobody"}, {"SEC_USER_AGENT": "Your Name your.address@example.com"}):
            with self.assertRaises(SystemExit) as raised:
                self.tool.make_fetcher(env=env)
            self.assertIn("SEC_USER_AGENT", str(raised.exception.code))
        self.assertIsNotNone(self.tool.make_fetcher(env={"SEC_USER_AGENT": "Test Owner owner@sample-firm.test"}))

    def test_financial_values_were_filed_before_the_cutoff(self):
        with open(self.data / "financials" / "xbrl_facts.csv", encoding="utf-8") as fh:
            rows = list(csv.DictReader(fh))
        self.assertTrue(rows, "xbrl_facts.csv is empty")
        self.assertTrue(all(r["filed"] < CUTOFF for r in rows), "a value filed on or after the cutoff was kept")
        heads, income = table(self.data / "financials" / "income_statement.csv")
        self.assertEqual(income["Revenue"][heads.index("FY_2021-12-31")], "100.0", "used a restatement filed after the cutoff")
        self.assertEqual(income["Revenue"][heads.index("Q_2022-03-31")], "25.0")
        heads, balance = table(self.data / "financials" / "balance_sheet.csv")
        self.assertEqual(balance["Total assets"][heads.index("At_2022-12-31")], "520.0")

    def test_marks_and_labels_a_real_target(self):
        checks = json.loads((self.folder / "checks.json").read_text(encoding="utf-8"))
        self.assertIs(checks["real"], True)
        self.assertEqual(checks["cutoff"], CUTOFF)
        for path in self.data.rglob("*.md"):
            text = path.read_text(encoding="utf-8").upper()
            for phrase in ("REAL PUBLIC COMPANY", "HYPOTHETICAL DEAL"):
                self.assertIn(phrase, text, f"{path.name} lacks the real-target label")
        for source in ("news", "litigation"):
            self.assertTrue((self.data / source / "NO-SOURCES.md").exists(), f"{source}/ must say it has no sources")
        self.assertFalse((self.data / "deal-brief.md").exists(), "the deal brief is the case session's job")
        self.assertFalse((self.folder / "evaluation").exists(), "the tool must never write the answer key")

    def test_labels_the_target_with_its_name_on_the_cutoff_date(self):
        written = [self.folder / "checks.json"] + list(self.data.rglob("*.md"))
        for path in written:
            self.assertNotIn(LATER_NAME, path.read_text(encoding="utf-8"), f"{path.name} names the company as it was after the cutoff")
        self.assertIn("Sample Sensors Inc.", (self.data / "README.md").read_text(encoding="utf-8"))
        self.assertEqual(json.loads((self.folder / "checks.json").read_text(encoding="utf-8"))["company"], "Sample Sensors Inc.")
        names = [{"name": "First Co", "from": "2000-01-01T00:00:00.000Z", "to": "2012-05-01T00:00:00.000Z"},
                 {"name": "Middle Co", "from": "2012-05-01T00:00:00.000Z", "to": "2020-02-01T00:00:00.000Z"}]
        for cutoff, expected in (("2010-06-01", "First Co"), ("2015-06-01", "Middle Co"), ("2022-06-01", "Current Co")):
            self.assertEqual(self.tool.name_at({"name": "Current Co", "formerNames": names}, cutoff, CIK), expected, cutoff)
        self.assertEqual(self.tool.name_at({"name": "Current Co"}, "2015-06-01", CIK), "Current Co", "no former names")

    def test_will_not_overwrite_a_download_without_force(self):
        with contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit):
            self.tool.fetch("TST", CUTOFF, "backtest-sample", FakeFetcher(), root=self.root, today="2026-11-02")


if __name__ == "__main__":
    unittest.main()

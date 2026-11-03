#!/usr/bin/env python3
"""Build a read-only committee dashboard from a finished run's working memory.

Standard library only, like tools/md2html.py, so it works on any computer with Python 3.

  python3 tools/make_dashboard.py                             # memory/ -> output/Project-<Codename>-Dashboard.html
  python3 tools/make_dashboard.py runs/<date>/memory          # -> runs/<date>/output/Project-<Codename>-Dashboard.html
  python3 tools/make_dashboard.py runs/<date>/memory out.html

The page is one self-contained HTML file: no libraries, no network, opens offline and prints.
It reads memory/findings.md, memory/datasets/key-metrics.md and memory/open-questions.md and
shows a chart of findings by severity and status (with the same counts as a table), the top
red flags, the key metrics tables and the open questions. Nothing is recalculated or reworded:
the counts come from the register's Severity and Status cells, and every text and figure is
copied from the memory files, so the dashboard matches the report. It only displays a finished
run; nothing on it can be edited.

The status colors are categorical slots 1 to 4 of the dataviz skill's reference palette,
checked with its validator in light and dark mode. Two light-mode colors are below 3:1 contrast
on the surface, so every count is also printed in the table under the chart.
"""
import datetime
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SEVERITIES = ["Critical", "High", "Medium", "Low"]
STATUSES = ["Verified", "Partially verified", "Open", "Rejected"]
FINDING_ID = re.compile(r"^(SEC|NEWS|LIT|FIN|X)-[A-Z]?\d+$")

TABLE_SEP = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")
NUMBER = re.compile(r"^-?\d{1,3}(,\d{3})*(\.\d+)?$|^-?\d+(\.\d+)?$")
PERCENT = re.compile(r"^-?\d+(\.\d+)?%$")
CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
# Status order on the chart; each status takes categorical slot n (CSS --s<n>, text inside it --on-s<n>).
STATUS_SLOTS = {"Verified": 1, "Partially verified": 2, "Open": 3, "Rejected": 4}
SEV_ICON = {"Critical": "▲", "High": "◆", "Medium": "●", "Low": "○"}


def plain(text):
    """Markdown cell text as plain text: links, bold, italics and code marks removed."""
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"(?<!\w)\*(.+?)\*(?!\w)", r"\1", text)
    text = text.replace("`", "").replace("<br>", "; ").replace("\\|", "|")
    return CONTROL.sub("", text).strip()


def split_row(line):
    cells = re.split(r"(?<!\\)\|", line.strip().strip("|"))
    return [plain(c) for c in cells]


def tables(md):
    """Yield (heading, header, rows) for every pipe table, with the nearest heading above it."""
    lines = md.splitlines()
    heading, i = "", 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("#"):
            heading = plain(line.lstrip("#"))
        if line.lstrip().startswith("|") and i + 1 < len(lines) and TABLE_SEP.match(lines[i + 1]):
            header, rows, i = split_row(line), [], i + 2
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            yield heading, header, rows
            continue
        i += 1


def list_items(md):
    """Yield (heading, number, text) for each top-level list item; indented lines join its text.

    A numbered item keeps its number; a bulleted item has None. Plain paragraphs are skipped."""
    heading, current = "", None
    for line in md.splitlines():
        if line.startswith("#"):
            if current:
                yield tuple(current)
                current = None
            heading = plain(line.lstrip("#"))
            continue
        numbered = re.match(r"^(\d+)[.)]\s+(.*)$", line)
        bullet = re.match(r"^[-*+]\s+(.*)$", line)
        if numbered or bullet:
            if current:
                yield tuple(current)
            current = [heading, int(numbered.group(1)), plain(numbered.group(2))] if numbered else [heading, None, plain(bullet.group(1))]
        elif current and line.strip() and line[:1].isspace():
            current[2] += " " + plain(re.sub(r"^\s*([-*+]|\d+[.)])\s+", "", line))
        elif current and not line.strip():
            continue
        elif current:
            yield tuple(current)
            current = None
    if current:
        yield tuple(current)


def group(text, words):
    """The canonical word a cell starts with ("Critical (test: ...)" -> "Critical"), or None."""
    for word in sorted(words, key=len, reverse=True):
        if text.lower().startswith(word.lower()):
            return word
    return None


def numeric(text):
    """True for a clean number or percentage (1,561.0, US$25.50, 9.1%), which is right-aligned."""
    t = text.replace("US$", "").strip()
    return bool(PERCENT.match(t) or NUMBER.match(t))


def read(path):
    return path.read_text(encoding="utf-8") if path.exists() else ""


class Run:
    """A finished run's memory files, parsed once."""

    def __init__(self, memory):
        self.memory = pathlib.Path(memory)
        self.target = read(self.memory / "target.txt").strip()
        if not self.target and (self.memory / "findings.md").exists():
            self.target = "falcon"  # runs archived before target.txt existed were all Falcon runs
        if not self.target:
            raise SystemExit(f"No run found: {self.memory / 'target.txt'} is missing or empty. Run /diligence first.")
        data = ROOT / "targets" / self.target / "data"
        m = re.search(r"Project\s+([A-Z][\w-]*)", read(data / "deal-brief.md"))
        self.codename = m.group(1) if m else self.target.capitalize()
        self.real = "Real public company, hypothetical deal" in read(data / "README.md")

        # Findings: every register row from every table whose header has ID and Severity.
        self.findings = []
        for heading, header, rows in tables(read(self.memory / "findings.md")):
            if "ID" not in header or "Severity" not in header:
                continue
            for row in rows:
                rec = dict(zip(header, row))
                if FINDING_ID.match(rec.get("ID", "")):
                    rec["Section"] = heading
                    rec["severity_group"] = group(rec.get("Severity", ""), SEVERITIES)
                    rec["status_group"] = group(rec.get("Status", ""), STATUSES)
                    self.findings.append(rec)
        if not self.findings:
            raise SystemExit(f"No findings register rows in {self.memory / 'findings.md'}.")

        # Key metrics: (heading, header, rows) for each table, as written.
        self.metrics = list(tables(read(self.memory / "datasets" / "key-metrics.md")))
        # Open questions: (section, number or None, text) for each top-level list item.
        self.questions = list(list_items(read(self.memory / "open-questions.md")))

    def count(self, severity=None, status=None):
        return sum(1 for f in self.findings
                   if (severity is None and f["severity_group"] or f["severity_group"] == severity)
                   and (status is None or f["status_group"] == status))

    def nonstandard_status(self):
        """Findings whose status cell does not start with one of the four status words."""
        return [f for f in self.findings if f["severity_group"] and not f["status_group"]]

    def red_flags(self):
        """Critical and High findings the verifier did not reject: Critical first, X- parents first."""
        flags = [f for f in self.findings if f["severity_group"] in ("Critical", "High") and f["status_group"] != "Rejected"]
        return sorted(flags, key=lambda f: (SEVERITIES.index(f["severity_group"]), not f["ID"].startswith("X-")))


def default_out(memory, codename, suffix):
    """output/ next to the memory folder: output/ for memory/, runs/<date>/output/ for an archived run."""
    return pathlib.Path(memory).resolve().parent / "output" / f"Project-{codename}-{suffix}"


CSS = """
:root { color-scheme: light;
  --page: #f9f9f7; --surface: #fcfcfb; --ink: #0b0b0b; --ink-2: #52514e; --muted: #6f6d68;
  --grid: #e1e0d9; --axis: #c3c2b7; --ring: rgba(11,11,11,0.10); --head: #0b1f5c;
  --s1: #2a78d6; --s2: #eb6834; --s3: #1baf7a; --s4: #eda100;
  --on-s1: #ffffff; --on-s2: #ffffff; --on-s3: #ffffff; --on-s4: #0b0b0b;
  --critical: #d03b3b; --serious: #ec835a; --warning: #fab219; --neutral: #898781; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { color-scheme: dark;
  --page: #0d0d0d; --surface: #1a1a19; --ink: #f0efec; --ink-2: #c3c2b7; --muted: #a3a197;
  --grid: #2c2c2a; --axis: #383835; --ring: rgba(255,255,255,0.10); --head: #c9d4f5;
  --s1: #3987e5; --s2: #d95926; --s3: #199e70; --s4: #c98500;
  --on-s4: #0b0b0b; } }
:root[data-theme="dark"] { color-scheme: dark;
  --page: #0d0d0d; --surface: #1a1a19; --ink: #f0efec; --ink-2: #c3c2b7; --muted: #a3a197;
  --grid: #2c2c2a; --axis: #383835; --ring: rgba(255,255,255,0.10); --head: #c9d4f5;
  --s1: #3987e5; --s2: #d95926; --s3: #199e70; --s4: #c98500; --on-s4: #0b0b0b; }
* { box-sizing: border-box; }
body { margin: 0; background: var(--page); color: var(--ink);
  font: 15px/1.45 system-ui, -apple-system, "Segoe UI", sans-serif; }
main { max-width: 1080px; margin: 0 auto; padding: 24px 16px 48px; }
header h1 { margin: 0 0 4px; font-size: 26px; color: var(--head); }
header p { margin: 2px 0; color: var(--ink-2); }
.tag { display: inline-block; margin-top: 6px; padding: 2px 8px; border-radius: 4px; border: 1px solid var(--ring);
  font-size: 13px; color: var(--ink-2); }
h2 { margin: 0 0 12px; font-size: 18px; color: var(--head); }
h3 { margin: 16px 0 6px; font-size: 15px; color: var(--ink); }
section.card { background: var(--surface); border: 1px solid var(--ring); border-radius: 8px; padding: 18px; margin-top: 18px; }
.tiles { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin-top: 18px; }
.tile { background: var(--surface); border: 1px solid var(--ring); border-radius: 8px; padding: 12px 14px; }
.tile .label { color: var(--ink-2); font-size: 13px; }
.tile .value { font-size: 28px; font-weight: 600; }
.legend { display: flex; flex-wrap: wrap; gap: 6px 16px; margin: 0 0 8px; font-size: 13px; color: var(--ink-2); padding: 0; list-style: none; }
.legend li { display: flex; align-items: center; gap: 6px; }
.swatch { width: 12px; height: 12px; border-radius: 3px; display: inline-block; }
svg.chart { width: 100%; min-width: 520px; height: auto; display: block; }
svg .axis-label { fill: var(--ink-2); font-size: 13px; }
svg .total { fill: var(--ink); font-size: 13px; font-weight: 600; }
svg .seg-label { font-size: 12px; font-weight: 600; pointer-events: none; }
svg .seg { cursor: default; }
svg .seg:hover { opacity: 0.85; }
svg .grid { stroke: var(--grid); stroke-width: 1; }
svg .base { stroke: var(--axis); stroke-width: 1; }
#tip { position: fixed; pointer-events: none; background: var(--surface); color: var(--ink); border: 1px solid var(--ring);
  box-shadow: 0 2px 8px rgba(0,0,0,0.15); border-radius: 6px; padding: 6px 9px; font-size: 13px; display: none; z-index: 10; }
.table-wrap { overflow-x: auto; }
table { border-collapse: collapse; width: 100%; font-size: 13.5px; }
th { text-align: left; color: var(--ink-2); font-weight: 600; border-bottom: 1px solid var(--axis); padding: 6px 8px; vertical-align: bottom; }
td { border-bottom: 1px solid var(--grid); padding: 6px 8px; vertical-align: top; }
td.num, th.num { text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }
td.id { white-space: nowrap; font-weight: 600; }
.sev { white-space: nowrap; font-weight: 600; }
.sev .icon { margin-right: 4px; }
.sev-Critical .icon { color: var(--critical); } .sev-High .icon { color: var(--serious); }
.sev-Medium .icon { color: var(--warning); } .sev-Low .icon { color: var(--neutral); }
.note { color: var(--muted); font-size: 13px; margin: 8px 0 0; }
details { border-top: 1px solid var(--grid); padding: 8px 0; }
details:first-of-type { border-top: 0; }
summary { cursor: pointer; font-weight: 600; }
ol.q, ul.q { margin: 4px 0 10px; padding-left: 22px; }
ol.q li, ul.q li { margin: 4px 0; }
footer { margin-top: 24px; color: var(--muted); font-size: 13px; }
@media print {
  :root { color-scheme: light; }
  body { background: #fff; font-size: 11px; }
  main { max-width: none; padding: 0; }
  section.card, .tile { break-inside: avoid; border-color: #ccc; }
  section.flags, section.metrics, section.questions { break-inside: auto; }
  details > *:not(summary) { display: block; }
}
"""

TIP_JS = """
(function () {
  var tip = document.getElementById('tip');
  document.querySelectorAll('[data-tip]').forEach(function (el) {
    el.addEventListener('mousemove', function (e) {
      tip.textContent = el.getAttribute('data-tip');
      tip.style.display = 'block';
      tip.style.left = Math.min(e.clientX + 12, window.innerWidth - tip.offsetWidth - 8) + 'px';
      tip.style.top = (e.clientY + 14) + 'px';
    });
    el.addEventListener('mouseleave', function () { tip.style.display = 'none'; });
  });
  window.addEventListener('beforeprint', function () {
    document.querySelectorAll('details').forEach(function (d) { d.open = true; });
  });
})();
"""


def esc(text):
    return html.escape(str(text), quote=True)


def chart(run):
    """Horizontal stacked bars: one bar per severity, one segment per status."""
    label_w, bar_w, bar_h, gap_y, top = 96, 560, 26, 14, 8
    width = label_w + bar_w + 48
    height = top + len(SEVERITIES) * (bar_h + gap_y) + 4
    biggest = max(sum(run.count(s, st) for st in STATUSES) for s in SEVERITIES) or 1
    unit = bar_w / biggest
    out = ['<svg class="chart" viewBox="0 0 %d %d" role="img" aria-labelledby="chart-title">' % (width, height)]
    out.append('<line class="base" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (label_w, top - 4, label_w, height - gap_y + 4))
    for i, sev in enumerate(SEVERITIES):
        y = top + i * (bar_h + gap_y)
        out.append('<text class="axis-label" x="%d" y="%.1f" text-anchor="end" dominant-baseline="middle">%s</text>'
                   % (label_w - 10, y + bar_h / 2, sev))
        parts = [(st, run.count(sev, st)) for st in STATUSES if run.count(sev, st)]
        x = label_w
        for j, (st, n) in enumerate(parts):
            w = n * unit - (2 if j < len(parts) - 1 else 0)  # 2px surface gap between segments
            slot = STATUS_SLOTS[st]
            tipt = "%s, %s: %d" % (sev, st, n)
            if j == len(parts) - 1:  # round only the data end
                r = min(4, w / 2)
                d = "M%.1f,%d h%.1f a%.1f,%.1f 0 0 1 %.1f,%.1f v%.1f a%.1f,%.1f 0 0 1 -%.1f,%.1f h-%.1f z" % (
                    x, y, w - r, r, r, r, r, bar_h - 2 * r, r, r, r, r, w - r)
                out.append('<path class="seg" d="%s" fill="var(--s%d)" data-tip="%s"><title>%s</title></path>' % (d, slot, esc(tipt), esc(tipt)))
            else:
                out.append('<rect class="seg" x="%.1f" y="%d" width="%.1f" height="%d" fill="var(--s%d)" data-tip="%s"><title>%s</title></rect>'
                           % (x, y, w, bar_h, slot, esc(tipt), esc(tipt)))
            if w >= 8 * len(str(n)) + 12:  # label inside only when it fits with padding
                out.append('<text class="seg-label" x="%.1f" y="%.1f" text-anchor="middle" dominant-baseline="middle" fill="var(--on-s%d)">%d</text>'
                           % (x + w / 2, y + bar_h / 2 + 0.5, slot, n))
            x += n * unit
        total = sum(n for _, n in parts)
        out.append('<text class="total" x="%.1f" y="%.1f" dominant-baseline="middle">%d</text>' % (x + 8, y + bar_h / 2, total))
    out.append("</svg>")
    return "".join(out)


def count_table(run):
    head = "".join('<th class="num">%s</th>' % esc(s) for s in STATUSES)
    rows = []
    for sev in SEVERITIES:
        cells = "".join('<td class="num">%d</td>' % run.count(sev, st) for st in STATUSES)
        rows.append('<tr><td>%s</td>%s<td class="num">%d</td></tr>' % (sev_badge(sev), cells, sum(run.count(sev, st) for st in STATUSES)))
    totals = "".join('<td class="num"><strong>%d</strong></td>' % run.count(None, st) for st in STATUSES)
    rows.append('<tr><td><strong>Total</strong></td>%s<td class="num"><strong>%d</strong></td></tr>'
                % (totals, sum(run.count(None, st) for st in STATUSES)))
    return ('<div class="table-wrap"><table><thead><tr><th>Severity</th>%s<th class="num">Total</th></tr></thead><tbody>%s</tbody></table></div>'
            % (head, "".join(rows)))


def sev_badge(sev, text=None):
    group = sev if sev in SEV_ICON else None
    icon = '<span class="icon" aria-hidden="true">%s</span>' % SEV_ICON[group] if group else ""
    return '<span class="sev sev-%s">%s%s</span>' % (esc(group or "other"), icon, esc(text or sev))


def red_flags(run):
    flags = run.red_flags()
    shown = [f for f in flags if f["severity_group"] == "Critical" or f["ID"].startswith("X-")]
    rest = len(flags) - len(shown)
    rows = "".join(
        '<tr><td class="id">%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'
        % (esc(f["ID"]), esc(f.get("Finding", "")), sev_badge(f["severity_group"], f.get("Severity", "")),
           esc(f.get("Confidence", "")), esc(f.get("Status", "")))
        for f in shown)
    note = ("Every Critical finding and every High cross-source (X-) finding, Critical first, from the findings register. "
            "Rejected findings are left out.")
    if rest:
        note += " %d other High %s in the findings register and the report." % (rest, "finding is" if rest == 1 else "findings are")
    return ('<div class="table-wrap"><table><thead><tr><th>ID</th><th>Finding</th><th>Severity</th><th>Confidence</th><th>Status</th></tr></thead>'
            '<tbody>%s</tbody></table></div><p class="note">%s</p>' % (rows, esc(note)))


def metrics(run):
    if not run.metrics:
        return '<p class="note">No key metrics file in this run.</p>'
    out = []
    for i, (heading, header, rows) in enumerate(run.metrics):
        head = "".join("<th>%s</th>" % esc(h) for h in header)
        body = "".join("<tr>%s</tr>" % "".join(('<td class="num">%s</td>' if c and numeric(v) else "<td>%s</td>") % esc(v)
                                               for c, v in enumerate(row)) for row in rows)
        out.append('<details%s><summary>%s</summary><div class="table-wrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div></details>'
                   % (" open" if i < 2 else "", esc(heading or "Key metrics"), head, body))
    return "".join(out)


def questions(run):
    if not run.questions:
        return '<p class="note">No open questions file in this run.</p>'
    out, section, items = [], None, []

    def flush():
        if items:
            tag = "ol" if all(n is not None for n, _ in items) else "ul"
            out.append("<h3>%s</h3><%s class=\"q\">%s</%s>" % (
                esc(section), tag, "".join('<li%s>%s</li>' % (' value="%d"' % n if n is not None and tag == "ol" else "", esc(t)) for n, t in items), tag))

    for heading, num, text in run.questions:
        if heading != section:
            flush()
            section, items = heading, []
        items.append((num, text))
    flush()
    return "".join(out)


def page(run, source):
    title = "Project %s: committee dashboard" % run.codename
    label = "Real public company, hypothetical deal. Not investment advice." if run.real else "Fictional case study"
    legend = "".join('<li><span class="swatch" style="background: var(--s%d)"></span>%s</li>' % (STATUS_SLOTS[s], esc(s)) for s in STATUSES)
    tiles = [("Findings in the register", len(run.findings)),
             ("Critical", run.count("Critical")), ("High", run.count("High")),
             ("Verified", run.count(None, "Verified")), ("Partially verified", run.count(None, "Partially verified"))]
    odd = run.nonstandard_status()
    odd_note = ("<p class=\"note\">Not counted in the chart: %d findings whose status is not one of the four status words (%s).</p>"
                % (len(odd), esc("; ".join("%s: %s" % (f["ID"], f.get("Status", "")) for f in odd)))) if odd else ""
    return """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Project %(codename)s Dashboard</title><style>%(css)s</style></head>
<body><main>
<header><h1>%(title)s</h1>
<p>Draft for Investment Committee discussion. Read-only view of a finished diligence run.</p>
<p>%(date)s. Built from <code>%(source)s</code>.</p>
<span class="tag">%(label)s</span> <span class="tag">Prepared by an AI multi-agent diligence system with human review</span></header>
<div class="tiles">%(tiles)s</div>
<section class="card"><h2 id="chart-title">Findings by severity and verification status</h2>
<ul class="legend">%(legend)s</ul><div class="table-wrap">%(chart)s</div>
<h3>The same counts as a table</h3>%(counts)s
<p class="note">Rejected findings stay in the register but are left out of the report. Open Low findings were not sent to the verifier.</p>%(odd)s</section>
<section class="card flags"><h2>Top red flags</h2>%(flags)s</section>
<section class="card metrics"><h2>Key metrics</h2><p class="note">US$ millions unless stated, copied from the run's key metrics file.</p>%(metrics)s</section>
<section class="card questions"><h2>Open questions and management requests</h2>%(questions)s</section>
<footer>Every figure is copied from the run's working memory, so it matches the report.
This is a draft for human decision-makers, not investment, legal or accounting advice.</footer>
</main><div id="tip" role="tooltip"></div><script>%(js)s</script></body></html>
""" % dict(codename=esc(run.codename), css=CSS, title=esc(title), date=datetime.date.today().strftime("%B %-d, %Y"),
           source=esc(source), label=esc(label),
           tiles="".join('<div class="tile"><div class="label">%s</div><div class="value">%d</div></div>' % (esc(k), v) for k, v in tiles),
           legend=legend, chart=chart(run), counts=count_table(run), odd=odd_note,
           flags=red_flags(run), metrics=metrics(run), questions=questions(run), js=TIP_JS)


def main(argv):
    memory = pathlib.Path(argv[1]) if len(argv) > 1 else ROOT / "memory"
    run = Run(memory)
    out = pathlib.Path(argv[2]) if len(argv) > 2 else default_out(memory, run.codename, "Dashboard.html")
    try:
        source = str(memory.resolve().relative_to(ROOT))
    except ValueError:
        source = str(memory)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(run, source), encoding="utf-8")
    print(f"wrote {out}: {len(run.findings)} findings, {len(run.red_flags())} Critical and High red flags, {len(run.questions)} open questions")


if __name__ == "__main__":
    main(sys.argv)

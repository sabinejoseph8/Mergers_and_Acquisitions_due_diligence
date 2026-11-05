"""Build the case study as a readable web page from docs/case-study.html.

    python3 tools/case_study_page.py [--out docs/case-study/index.html]

The words and numbers stay in docs/case-study.html, which also makes the two-page PDF. This script
reads that file, puts the architecture diagram in as a drawing (docs/architecture.svg) instead of an
image, and wraps the same sections in a page that reads on a phone and in light and dark. GitHub Pages
serves the result from docs/, so the README can link a page instead of a PDF. After editing
docs/case-study.html, rebuild the PDF and run this again. Standard library only.
"""
import argparse
import html
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = "https://github.com/sabinejoseph8/Mergers_and_Acquisitions_due_diligence"
SITE = "https://sabinejoseph8.github.io/Mergers_and_Acquisitions_due_diligence"

CSS = """
  /* Layout: one reading column on a phone, the PDF's two columns from 860px. Colours are the case study's own. */
  :root {
    --bg: #FFFFFF; --ink: #1F2430; --muted: #5B6170; --line: #D9DDE5; --mist: #F3F5F8;
    --navy: #0B1F5C; --teal: #00B3C8; --ember: #B5491F; --gold: #E5B53C; --cream: #FFF8E6;
    --verdict: #0B1F5C; --track: #FFFFFF; --s-hi: #9BDDE6; --m-hi: #E4B19C;
    --sans: "Helvetica Neue", Helvetica, Arial, "Liberation Sans", sans-serif;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --bg: #10151D; --ink: #E6E9EF; --muted: #A3ACBA; --line: #2B3442; --mist: #18202B;
      --navy: #A9BCE8; --teal: #33C9DB; --ember: #F29467; --gold: #C79A2E; --cream: #2A2314;
      --verdict: #162A6B; --track: #222C3A; --s-hi: #2E6E78; --m-hi: #7A4A3A; color-scheme: dark;
    }
  }
  :root[data-theme="dark"] {
    --bg: #10151D; --ink: #E6E9EF; --muted: #A3ACBA; --line: #2B3442; --mist: #18202B;
    --navy: #A9BCE8; --teal: #33C9DB; --ember: #F29467; --gold: #C79A2E; --cream: #2A2314;
    --verdict: #162A6B; --track: #222C3A; --s-hi: #2E6E78; --m-hi: #7A4A3A; color-scheme: dark;
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--bg); color: var(--ink); font-family: var(--sans); font-size: 16px; line-height: 1.55;
         padding-block: 28px 48px; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
  .page { max-width: 980px; margin: 0 auto; }
  h1, h2, h3 { color: var(--navy); margin: 0; line-height: 1.2; text-wrap: balance; }
  .head { border-left: 6px solid var(--navy); padding: 2px 0 2px 16px; margin-bottom: 22px; }
  .eyebrow { font-size: 12px; font-weight: 700; letter-spacing: 0.09em; text-transform: uppercase; color: var(--ember); margin-bottom: 8px; }
  h1 { font-size: clamp(34px, 7vw, 48px); }
  .sub { font-size: clamp(18px, 3.4vw, 22px); font-weight: 600; color: var(--navy); margin: 6px 0 12px; }
  .lede { margin: 0; max-width: 68ch; }
  .kpis { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin: 0 0 30px; }
  .kpi { background: var(--mist); border-top: 3px solid var(--teal); border-radius: 4px; padding: 12px 14px; min-width: 0; }
  .kpi b { display: block; font-size: 26px; color: var(--navy); line-height: 1.1; font-variant-numeric: tabular-nums; }
  .kpi span { display: block; font-size: 13px; color: var(--muted); margin-top: 6px; line-height: 1.4; }
  .cols { display: grid; grid-template-columns: minmax(0, 1.08fr) minmax(0, 1fr); gap: 36px; }
  .cols > div { min-width: 0; }
  h2 { font-size: 19px; padding-bottom: 5px; border-bottom: 2px solid var(--navy); margin: 0 0 10px; }
  section { margin-bottom: 26px; }
  p { margin: 0 0 10px; }
  ul, ol { margin: 0; padding-left: 20px; }
  li { margin: 0 0 7px; }
  strong { color: var(--navy); }
  code { font-family: Menlo, Consolas, monospace; font-size: 0.9em; background: var(--mist); padding: 0 3px; border-radius: 3px; }
  .figure { border: 1px solid var(--line); border-radius: 6px; padding: 10px; margin: 0 0 30px; min-width: 0; }
  .figure .hint { display: none; font-size: 13px; color: var(--muted); margin-top: 6px; }
  .diagram { overflow-x: auto; border-radius: 4px; background: #FFFFFF; }
  .diagram svg { display: block; width: 100%; min-width: 820px; height: auto; }
  .figure .cap { font-size: 13px; color: var(--muted); margin-top: 8px; }
  .verdict { background: var(--verdict); color: #FFFFFF; border-radius: 4px; padding: 12px 14px; margin-bottom: 10px; }
  .verdict strong { color: #FFFFFF; }
  .learn li::marker { color: var(--teal); }
  .note { background: var(--cream); border-left: 4px solid var(--gold); padding: 12px 14px; font-size: 15px; margin: 4px 0 30px; }
  .cost { border-top: 2px solid var(--navy); padding-top: 22px; }
  .cost h2 { font-size: 22px; border-bottom: 0; padding-bottom: 0; margin-bottom: 4px; }
  .dsub { color: var(--muted); margin: 0 0 16px; }
  .dk { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin: 0 0 22px; }
  .dk .kpi b { font-size: 20px; }
  .dk .kpi.sys { border-top-color: var(--teal); }
  .dk .kpi.man { border-top-color: var(--ember); }
  .dk .kpi:not(.sys):not(.man) { border-top-color: var(--navy); }
  .charts { display: grid; grid-template-columns: 1fr 1fr; gap: 10px 32px; background: var(--mist); border-radius: 6px; padding: 14px 18px; margin-bottom: 22px; }
  .chart .ct { font-weight: 700; color: var(--navy); font-size: 15px; margin-bottom: 8px; }
  .rrow { display: grid; grid-template-columns: 92px 1fr; align-items: center; margin: 6px 0; font-size: 14px; }
  .track { height: 18px; background: var(--track); border-radius: 3px; display: flex; }
  .track span, .mb span { display: block; height: 100%; }
  .s.lo { background: var(--teal); } .s.hi { background: var(--s-hi); }
  .m.lo { background: var(--ember); } .m.hi { background: var(--m-hi); }
  .track span:last-child, .mb span:last-child { border-radius: 0 3px 3px 0; }
  .axis { margin-left: 92px; display: flex; justify-content: space-between; font-size: 12px; color: var(--muted); border-top: 1px solid var(--line); padding-top: 3px; }
  .legend { grid-column: 1 / -1; font-size: 13px; color: var(--muted); display: flex; flex-wrap: wrap; gap: 6px 20px; }
  .legend i { display: inline-block; width: 14px; height: 11px; margin-right: 5px; vertical-align: -1px; border-radius: 2px; }
  .legend i.g { background: linear-gradient(90deg, var(--s-hi) 50%, var(--m-hi) 50%); }
  .dcols { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 10px 32px; margin-bottom: 14px; }
  .dcols > div { min-width: 0; }
  .dash h3 { font-size: 16px; margin: 0 0 6px; }
  .scroll { overflow-x: auto; margin-bottom: 12px; }
  .items { width: 100%; border-collapse: collapse; font-size: 14px; }
  .items th, .items td { text-align: left; padding: 6px 8px; border-bottom: 1px solid var(--line); vertical-align: top; }
  .items th { background: var(--mist); color: var(--navy); font-size: 13px; }
  .items td .d { display: block; color: var(--muted); font-size: 12px; line-height: 1.35; }
  .items .r { text-align: right; white-space: nowrap; }
  .items td:nth-child(3) { width: 30%; min-width: 120px; vertical-align: middle; }
  .items tr.tot td { border-top: 2px solid var(--navy); font-weight: 700; color: var(--navy); }
  .items.time td:nth-child(3) { width: auto; min-width: 0; vertical-align: top; }
  .mb { height: 10px; background: var(--mist); border-radius: 2px; display: flex; }
  .foot { border-top: 1px solid var(--line); margin-top: 8px; padding-top: 16px; font-size: 14px; color: var(--muted); display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px 32px; }
  .foot strong { color: var(--ink); }
  .foot a { color: inherit; overflow-wrap: anywhere; }
  .more { margin-top: 18px; font-size: 15px; display: flex; flex-wrap: wrap; gap: 8px 20px; }
  .more a { color: var(--navy); font-weight: 600; text-underline-offset: 3px; }
  a:focus-visible { outline: 2px solid var(--teal); outline-offset: 2px; }
  @media (max-width: 859px) {
    .cols, .dcols { grid-template-columns: minmax(0, 1fr); gap: 0; }
    .dcols { gap: 10px; }
  }
  @media (max-width: 700px) {
    .figure .hint { display: block; }
    .charts { grid-template-columns: 1fr; }
  }
  @media (max-width: 560px) {
    .foot { grid-template-columns: minmax(0, 1fr); }
  }
  @media (max-width: 480px) {
    .kpis .kpi:nth-child(5), .dk .kpi:nth-child(5) { grid-column: 1 / -1; }
  }
"""

LINKS = [
    ("The repository", REPO),
    ("Demo video (under 2 minutes)", REPO + "#ma-due-diligence-video-demo-1-minute-44-seconds-with-sound"),
    ("Sample report (PDF)", REPO + "/blob/main/examples/sample-run/output/Project-Falcon-Due-Diligence-Report.pdf"),
    ("Project Memory (specs and plan)", SITE + "/project-memory/"),
    ("How to run it", REPO + "/blob/main/docs/how-to-run.md"),
    ("PDF version of this page", SITE + "/case-study.pdf"),
]


def between(text, start, end):
    i = text.index(start)
    return text[i:text.index(end, i)]


def build():
    src = open(os.path.join(ROOT, "docs", "case-study.html"), encoding="utf-8").read()
    body = between(src, "<body>", "</body>")[len("<body>"):]
    head = between(body, '<header class="head">', "</header>") + "</header>"
    kpis = between(body, '<div class="kpis">', '<div class="cols">').rstrip()
    cols = between(body, '<div class="cols">', '<div class="note">').rstrip()
    note = between(body, '<div class="note">', "</div>") + "</div>"
    cost = between(body, '<section class="cost dash">', "</section>") + "</section>"
    foot = between(body, '<footer class="foot">', "</footer>") + "</footer>"

    # The diagram leaves the right column and goes full width, as a drawing that scales.
    figure = re.search(r'<div class="figure">.*?<div class="cap">.*?</div>\s*</div>', cols, flags=re.S).group(0)
    cols = cols.replace(figure, "", 1)
    svg = open(os.path.join(ROOT, "docs", "architecture.svg"), encoding="utf-8").read().strip()
    svg = re.sub(r"<\?xml[^>]*\?>\s*", "", svg)
    img = re.search(r'<img src="architecture.png" alt="([^"]*)">', figure)
    assert img, "the architecture image tag moved in docs/case-study.html"
    svg = svg.replace("<svg ", f'<svg role="img" aria-label="{img.group(1)}" ', 1)
    figure = figure.replace(img.group(0), '<div class="diagram">' + svg + "</div>")
    figure = figure.replace('<div class="cap">', '<div class="hint">Swipe sideways to see the whole drawing.</div><div class="cap">', 1)

    # Web wording: there are no pages here.
    assert "(page 2)" in kpis, "the page 2 pointer moved in docs/case-study.html"
    kpis = kpis.replace("(page 2)", "(details below)")
    cost = re.sub(r"(<table[^>]*>.*?</table>)", r'<div class="scroll">\1</div>', cost, flags=re.S)

    title = re.search(r"<title>(.*?)</title>", src).group(1)
    lede = re.search(r'<p class="lede">(.*?)</p>', head, flags=re.S).group(1)
    description = html.escape(html.unescape(re.sub(r"<[^>]+>", "", lede)), quote=True)
    links = '<nav class="more" aria-label="More">' + "".join(f'<a href="{u}">{t}</a>' for t, u in LINKS) + "</nav>"

    return (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
        f"<title>{title}</title>\n<meta name=\"description\" content=\"{description}\">\n"
        f"<style>{CSS}</style>\n</head>\n<body>\n<div class=\"page\">\n{head}\n{kpis}\n{figure}\n{cols}\n{note}\n{cost}\n{foot}\n{links}\n</div>\n</body>\n</html>\n"
    )


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(ROOT, "docs", "case-study", "index.html"))
    args = ap.parse_args()
    page = build()
    assert "—" not in page, "em dash in the page"
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    open(args.out, "w", encoding="utf-8").write(page)
    print(f"Wrote {args.out} ({len(page):,} bytes)")

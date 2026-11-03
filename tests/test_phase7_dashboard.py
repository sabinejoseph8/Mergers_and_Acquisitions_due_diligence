"""Phase 7: the read-only committee dashboard copies a finished run's figures.
Runs on a small built-in run, and on the --run folder when it holds findings."""
import contextlib
import importlib.util
import io
import pathlib
import re
import tempfile
import unittest

from _common import EM_DASH, ROOT, read, run_dir

TOOL = ROOT / "tools" / "make_dashboard.py"
STDLIB = {"datetime", "html", "pathlib", "re", "sys"}
# The status colors validated with the dataviz skill's validator (light and dark slots 1 to 4).
VALIDATED = {"#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#3987e5", "#d95926", "#199e70", "#c98500"}
# Register rows have seven cells and a finding ID first; other tables (cards, parent mapping) are shorter.
REGISTER_ROW = re.compile(r"^\| *\[?((?:SEC|NEWS|LIT|FIN|X)-[A-Z]?\d+)\b")

FINDINGS = """# Findings register

## Cross-source findings (lead agent)

| ID | Finding | Workstream | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|---|
| [X-001](#x-001) | Reserve release of US$15.4m inflates **LTM** Adjusted EBITDA | Cross-source | Critical (test: more than 10% of value) | High | SEC-01 ([card](#x-001)) | Verified |
| X-02 | Vote risk under the majority-of-unaffiliated condition | Cross-source | High | Medium | NEWS-002 | Partially verified |

## Analyst findings

| ID | Finding | Workstream | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|---|
| SEC-01 | Change in estimate of US$15.4m in Q2 2026 | SEC | High | High | 10-Q Note 4 | Verified |
| NEWS-002 | A rumor the company denies | News | High | Low | blog.md | Rejected |
| LIT-F01 | Dismissed dealer suit | Litigation | Low | High | docket_index.csv row 3 | Open |
| FIN-001 | Lease liabilities differ by US$2.0m | Financial | Medium | High | balance_sheet.csv | Not verified (Low) |

## Finding cards

| Card | Note |
|---|---|
| X-001 | not a register row |
"""
METRICS = """# Key metrics

## Deal
| Item | Value | Source |
|---|---|---|
| EV | 1,561.0 | deal brief |
| Price per share | US$25.50 | deal brief |
| Revenue growth | 9.1% | kpis.csv |
| Shares | 52.0m | DEF 14A |
"""
QUESTIONS = """# Open questions

## Conflicts between sources

1. **Size of the release.** The 10-Q says US$15.4m.
   - The data pack shows US$14.7m.
2. Founder's shares.

## Gaps

- Q3 2026 results.
- HSR status.
"""


def load():
    spec = importlib.util.spec_from_file_location("make_dashboard", TOOL)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build(tool, memory, out):
    with contextlib.redirect_stdout(io.StringIO()):
        tool.main(["make_dashboard.py", str(memory), str(out)])
    return read(out)


def count_table(page):
    """The counts in the table under the chart: rows Critical, High, Medium, Low, Total; four statuses and Total."""
    table = page.split("The same counts as a table", 1)[1].split("</table>", 1)[0]
    return [int(n) for n in re.findall(r'<td class="num">(?:<strong>)?(\d+)', table)]


class TestDashboard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tool = load()
        cls.tmp = tempfile.TemporaryDirectory()
        memory = pathlib.Path(cls.tmp.name) / "memory"
        (memory / "datasets").mkdir(parents=True)
        (memory / "target.txt").write_text("falcon\n")
        (memory / "findings.md").write_text(FINDINGS)
        (memory / "datasets" / "key-metrics.md").write_text(METRICS)
        (memory / "open-questions.md").write_text(QUESTIONS)
        cls.parsed = cls.tool.Run(memory)
        cls.page = build(cls.tool, memory, pathlib.Path(cls.tmp.name) / "dashboard.html")

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_uses_only_the_standard_library(self):
        imported = set(re.findall(r"^(?:import|from) (\w+)", read(TOOL), re.M))
        self.assertLessEqual(imported, STDLIB, "make_dashboard.py imports more than the standard library")

    def test_reads_every_finding_id_format_and_status(self):
        self.assertEqual([f["ID"] for f in self.parsed.findings], ["X-001", "X-02", "SEC-01", "NEWS-002", "LIT-F01", "FIN-001"])
        self.assertEqual([f["status_group"] for f in self.parsed.findings],
                         ["Verified", "Partially verified", "Verified", "Rejected", "Open", None])
        self.assertEqual(self.parsed.findings[0]["severity_group"], "Critical")
        self.assertEqual([f["ID"] for f in self.parsed.nonstandard_status()], ["FIN-001"])

    def test_counts_severity_by_status(self):
        self.assertEqual(count_table(self.page), [1, 0, 0, 0, 1,
                                                  1, 1, 0, 1, 3,
                                                  0, 0, 0, 0, 0,
                                                  0, 0, 1, 0, 1,
                                                  2, 1, 1, 1, 5])
        self.assertIn("FIN-001: Not verified (Low)", self.page, "a status outside the four words must be named, not dropped")

    def test_chart_draws_the_same_counts(self):
        tips = re.findall(r'data-tip="([A-Za-z]+), ([A-Za-z ]+): (\d+)"', self.page)
        self.assertEqual(sorted(tips), sorted([("Critical", "Verified", "1"), ("High", "Verified", "1"),
                                               ("High", "Partially verified", "1"), ("High", "Rejected", "1"),
                                               ("Low", "Open", "1")]))

    def test_red_flags_leave_out_rejected_findings(self):
        self.assertEqual([f["ID"] for f in self.parsed.red_flags()], ["X-001", "X-02", "SEC-01"])
        flags = self.page.split("Top red flags", 1)[1].split("</table>", 1)[0]
        self.assertEqual(re.findall(r'<td class="id">([^<]+)</td>', flags), ["X-001", "X-02"])
        self.assertNotIn("NEWS-002", flags)
        self.assertIn("1 other High finding is", self.page)

    def test_copies_text_and_figures_as_written(self):
        for text in ("Reserve release of US$15.4m inflates LTM Adjusted EBITDA", "Critical (test: more than 10% of value)",
                     '<td class="num">1,561.0</td>', '<td class="num">US$25.50</td>', '<td class="num">9.1%</td>',
                     "<td>52.0m</td>", "<td>deal brief</td>"):
            self.assertIn(text, self.page)

    def test_open_questions_keep_numbers_bullets_and_sub_items(self):
        self.assertEqual([(q[0], q[1]) for q in self.parsed.questions],
                         [("Conflicts between sources", 1), ("Conflicts between sources", 2), ("Gaps", None), ("Gaps", None)])
        self.assertEqual(self.parsed.questions[0][2], "Size of the release. The 10-Q says US$15.4m. The data pack shows US$14.7m.")
        self.assertIn("<li>HSR status.</li>", self.page)

    def test_is_self_contained_and_read_only(self):
        self.assertNotRegex(self.page, r'(?:src|href)="(?:https?:)?//')
        self.assertNotRegex(self.page, r"<(?:form|input|textarea|select|button)\b")
        self.assertNotIn(EM_DASH, self.page)

    def test_uses_the_validated_status_colors(self):
        self.assertEqual(set(re.findall(r"--s[1-4]: (#[0-9a-f]{6})", self.page)), VALIDATED)


RUN = run_dir()
FINDINGS_FILE = RUN / "memory" / "findings.md"
REGISTER = [m.group(1) for line in (read(FINDINGS_FILE).splitlines() if FINDINGS_FILE.exists() else [])
            if line.count("|") - line.count("\\|") >= 8 for m in [REGISTER_ROW.match(line)] if m]


@unittest.skipUnless(REGISTER, f"no findings in {RUN / 'memory'}")
class TestDashboardForTheRun(unittest.TestCase):
    def test_dashboard_builds_from_the_run(self):
        tool = load()
        run = tool.Run(RUN / "memory")
        self.assertEqual([f["ID"] for f in run.findings], REGISTER, "a register row was not read")
        with tempfile.TemporaryDirectory() as tmp:
            page = build(tool, RUN / "memory", pathlib.Path(tmp) / "dashboard.html")
        self.assertEqual(count_table(page)[-1], len(run.findings) - len(run.nonstandard_status()))
        self.assertIn(">%d</div>" % len(run.findings), page)


if __name__ == "__main__":
    unittest.main()

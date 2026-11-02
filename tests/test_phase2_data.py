"""Phase 2: each target's sources are complete, consistent and unchanged.
Runs for every folder in targets/ that has a data_manifest.json. A real target (Phase 8) has real filings
instead of simulated statements, so the tie-out checks skip it and its own cutoff check runs instead."""
import csv
import json
import re
import unittest

from _common import MANIFEST_NAME, checksums, is_real, read, target_checks, targets

TARGETS = targets()
REAL = [t for t in TARGETS if is_real(t)]


def load(fin, name):
    with open(fin / name, encoding="utf-8") as fh:
        rows = list(csv.reader(fh))
    return rows[0][1:], {r[0]: r[1:] for r in rows[1:]}, [r[0] for r in rows[1:]]


def num(value):
    return float(value.replace("%", "")) if value not in ("", None) else 0.0


def between(labels, start, end):
    """Row labels after `start` (or from the top when None) and before `end`."""
    first = labels.index(start) + 1 if start else 0
    return labels[first:labels.index(end)]


class TestTargetsExist(unittest.TestCase):
    def test_at_least_one_target_has_a_manifest(self):
        self.assertTrue(TARGETS, f"no targets/<name>/{MANIFEST_NAME}: run tests/run_all.py --write-manifest once")


class TestFinancialsTieOut(unittest.TestCase):
    def each(self):
        for target in TARGETS:
            fin = target / "data" / "financials"
            if fin.is_dir() and not is_real(target):
                with self.subTest(target=target.name):
                    yield target.name, fin

    def test_balance_sheets_balance(self):
        for name, fin in self.each():
            cols, bs, labels = load(fin, "balance_sheet.csv")
            assets = between(labels, None, "Total assets")
            liabilities = between(labels, "Total assets", "Total liabilities")
            for i, col in enumerate(cols):
                a = sum(num(bs[k][i]) for k in assets)
                l = sum(num(bs[k][i]) for k in liabilities)
                self.assertAlmostEqual(a, num(bs["Total assets"][i]), places=1, msg=f"{name} assets {col}")
                self.assertAlmostEqual(a, l + num(bs["Total stockholders' equity"][i]), places=1, msg=f"{name} balance {col}")

    def test_income_statement_adds_up(self):
        for name, fin in self.each():
            cols, inc, labels = load(fin, "income_statement.csv")
            revenue_lines = [k for k in labels if k.startswith("Revenue:")]
            self.assertTrue(revenue_lines, f"{name}: no 'Revenue: <segment>' rows")
            for i, col in enumerate(cols):
                g = lambda k: num(inc[k][i])
                self.assertAlmostEqual(sum(g(k) for k in revenue_lines), g("Total revenue"), places=1, msg=f"{name} {col}")
                self.assertAlmostEqual(g("Total revenue") - g("Cost of revenue"), g("Gross profit"), places=1, msg=f"{name} {col}")
                pretax = g("Operating income (loss)") - g("Interest expense") + g("Other income (expense) net")
                self.assertAlmostEqual(pretax - g("Income tax expense (benefit)"), g("Net income (loss)"), places=1, msg=f"{name} {col}")

    def test_cash_flow_ties_to_change_in_cash(self):
        for name, fin in self.each():
            cols, cf, _ = load(fin, "cash_flow.csv")
            for i, col in enumerate(cols):
                g = lambda k: num(cf[k][i])
                total = g("Net cash from operating activities") + g("Net cash used in investing activities") + g("Net cash from (used in) financing activities")
                self.assertAlmostEqual(total, g("Net change in cash"), places=1, msg=f"{name} {col}")

    def test_adjusted_ebitda_reconciles(self):
        for name, fin in self.each():
            cols, eb, labels = load(fin, "adjusted_ebitda_reconciliation.csv")
            for i, col in enumerate(cols):
                g = lambda k: num(eb[k][i])
                adjusted = g("EBITDA") + sum(g(k) for k in labels if k.startswith("Add:"))
                self.assertAlmostEqual(adjusted, g("Adjusted EBITDA (company definition)"), places=1, msg=f"{name} {col}")
                detail = sum(num(eb[k][i]) for k in labels if k.startswith("Detail:"))
                self.assertAlmostEqual(detail, g("Add: Other non-recurring items (detail below)"), places=1, msg=f"{name} detail {col}")

    def test_quarters_sum_to_years(self):
        for name, fin in self.each():
            cols, inc, _ = load(fin, "income_statement.csv")
            with open(fin / "revenue_quarterly.csv", encoding="utf-8") as fh:
                q = {r["quarter"]: float(r["total_revenue"]) for r in csv.DictReader(fh)}
            checked = 0
            for i, col in enumerate(cols):
                match = re.fullmatch(r"(FY|H1_)(\d{4})", col)
                quarters = [f"Q{n} {match.group(2)}" for n in ((1, 2, 3, 4) if match.group(1) == "FY" else (1, 2))] if match else []
                if quarters and all(k in q for k in quarters):
                    self.assertAlmostEqual(sum(q[k] for k in quarters), num(inc["Total revenue"][i]), places=1, msg=f"{name} {col}")
                    checked += 1
            self.assertGreater(checked, 0, f"{name}: no year or half-year has all its quarters in revenue_quarterly.csv")


class TestSourcesComplete(unittest.TestCase):
    def test_every_document_is_labeled_fictional_or_real(self):
        for target in TARGETS:
            labels = ("REAL PUBLIC COMPANY", "HYPOTHETICAL DEAL") if is_real(target) else ("FICTIONAL",)
            for path in (target / "data").rglob("*.md"):
                for label in labels:
                    self.assertIn(label, read(path).upper(), f"{target.name}: {path.name} is not labeled {label.lower()}")

    def test_deal_brief_and_readme_exist(self):
        for target in TARGETS:
            for name in ("deal-brief.md", "README.md"):
                self.assertTrue((target / "data" / name).exists(), f"{target.name}: missing data/{name}")

    def test_docket_detail_files_exist(self):
        for target in TARGETS:
            index = target / "data" / "litigation" / "docket_index.csv"
            if not index.exists():
                continue
            with open(index, encoding="utf-8") as fh:
                for row in csv.DictReader(fh):
                    if row["detail_file"]:
                        self.assertTrue((index.parent / row["detail_file"]).exists(), f"{target.name}: {row['detail_file']}")

    def test_answer_key_lists_all_planted_items(self):
        for target in TARGETS:
            key = target / "evaluation" / "answer-key.md"
            self.assertTrue(key.exists(), f"{target.name}: missing evaluation/answer-key.md")
            ids = re.findall(r"^\| (P\d{2}|D\d) \|", read(key), re.M)
            planted = sorted({i for i in ids if i.startswith("P")})
            distractors = sorted({i for i in ids if i.startswith("D")})
            self.assertEqual(planted, [f"P{n:02d}" for n in range(1, len(planted) + 1)], f"{target.name}: planted IDs must run P01, P02, ... with no gaps")
            self.assertEqual(distractors, [f"D{n}" for n in range(1, len(distractors) + 1)], f"{target.name}: distractor IDs must run D1, D2, ... with no gaps")
            # A real target's answer key lists warning signs only: nothing was planted, so it has no distractors.
            self.assertTrue(planted and (distractors or is_real(target)), f"{target.name}: the answer key needs planted issues and distractors")
            expected = target_checks(target).get("answer_key", {})
            if "planted_issues" in expected:
                self.assertEqual(len([i for i in ids if i.startswith("P")]), expected["planted_issues"], target.name)
            if "distractors" in expected:
                self.assertEqual(len([i for i in ids if i.startswith("D")]), expected["distractors"], target.name)


class TestRealTargets(unittest.TestCase):
    @unittest.skipUnless(REAL, "no real target yet")
    def test_real_target_data_predates_its_cutoff(self):
        for target in REAL:
            cutoff = target_checks(target).get("cutoff", "")
            self.assertRegex(cutoff, r"^\d{4}-\d{2}-\d{2}$", f"{target.name}: checks.json needs a cutoff date")
            filings = target / "data" / "sec-filings"
            index = read(filings / "index.md")
            dates = re.findall(r"^\| [^|]+ \| (\d{4}-\d{2}-\d{2}) \|", index, re.M)
            folders = [p.name.split("_")[1] for p in filings.iterdir() if p.is_dir()]
            self.assertTrue(dates and folders, f"{target.name}: no filings listed")
            late = sorted(d for d in dates + folders if d >= cutoff)
            self.assertFalse(late, f"{target.name}: filings dated on or after the cutoff {cutoff}: {late}")
            with open(target / "data" / "financials" / "xbrl_facts.csv", encoding="utf-8") as fh:
                filed = [row["filed"] for row in csv.DictReader(fh)]
            self.assertFalse([d for d in filed if d >= cutoff], f"{target.name}: financial values filed on or after {cutoff}")


class TestSourcesUnchanged(unittest.TestCase):
    def test_protected_files_match_the_manifest(self):
        for target in TARGETS:
            expected = json.loads(read(target / MANIFEST_NAME))
            actual = checksums(target)
            changed = sorted(k for k in expected if actual.get(k) != expected[k])
            added = sorted(set(actual) - set(expected))
            self.assertFalse(changed, f"{target.name}: changed since the manifest was written: {changed}")
            self.assertFalse(added, f"{target.name}: new files not in the manifest: {added}")


if __name__ == "__main__":
    unittest.main()

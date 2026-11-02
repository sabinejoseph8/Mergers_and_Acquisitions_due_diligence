---
description: Grade the latest diligence run against the target's answer key of planted issues
argument-hint: "[target, default falcon]"
---

You are grading this system's latest diligence run. This is the only command allowed to read a target's `evaluation/answer-key.md`.

**Target:** the target is "$ARGUMENTS" if that names a folder in `targets/`; if it is empty, use the name in `memory/target.txt`, or `falcon` if that file does not exist. If `memory/target.txt` names a different target from the one given, tell the user and stop: a run can only be graded against its own answer key. Below, `<target>` means that name.

1. Read `targets/<target>/evaluation/answer-key.md` (Claude Code will ask the user to approve this, by design), `memory/findings.md`, and the report in `output/`.
2. For each planted issue in the answer key, decide whether the run found it. Use exactly these definitions:
   - **Found:** the issue's main point is in the verified findings with a correct citation, and the highest severity among its matching verified findings is within one level of a severity the answer key accepts for it.
   - **Partially found:** only part of the main point was found, a needed cross-source link or citation is missing or weak, or the severity is more than one level away from every accepted severity.
   - **Missed:** not found.
   A severity that is one level away from an accepted severity does not make an issue Partially found. It shows only in the exact-match severity line. Use the fixed grading rules below for every number.
3. If the answer key has a planted-positives row (the row that lists strengths and mitigating points rather than an issue), grade it as its own row, under the ID the answer key gives it:
   - **Present:** every planted positive in the row appears in the report;
   - **Partly present:** some of them appear;
   - **Absent:** none of them appear.
   Name any positive that is missing. This row is not a planted issue, so it stays out of recall and severity accuracy.
4. For each distractor in the answer key, check whether the run wrongly rated it Medium or above.
5. Check for false findings: any finding in the report that the sources do not support (use the verifier results in memory).
6. **A real target** (its `data/README.md` says "Real public company, hypothetical deal"): count **hindsight leaks**, findings in the report that rely on anything dated on or after the cutoff in `targets/<target>/checks.json`, or on facts that are not in `targets/<target>/data/`. List their IDs. Its answer key lists warning signs as `P` rows and has no distractors: grade the `P` rows exactly as for any target, and write "Distractors: none in this answer key".
7. Write `targets/<target>/evaluation/scorecard.md` with:
   - recall overall, for the Critical and High group, and for each severity group, with the IDs in each group listed;
   - severity accuracy, in two lines: within one level, and exact match;
   - unsupported findings that reached the report (target: zero);
   - distractors rated too high;
   - for a real target, hindsight leaks (target: zero);
   - a table of every planted issue with its result and the matching finding IDs, one row per issue that starts with its answer key ID (`| Pnn |`), plus the planted-positives row in the same format, with its result (Present, Partly present or Absent) and any missing positives;
   - the three most useful improvements to the agent instructions.
8. Show the user a short summary.

Do not change the answer key or the data.

## Fixed grading rules

Apply these exactly, so every run is graded the same way:

- **Severity group:** each planted issue belongs to the first severity listed in its expected severity in the answer key. For example, "Critical or High" counts as Critical and "Medium (High ok)" counts as Medium. The planted-positives row has no severity group.
- **Accepted severities:** every severity named in an issue's expected severity in the answer key. For example, "Medium (High ok)" accepts Medium and High.
- **Critical and High group:** every issue whose first-listed severity is Critical or High. Count it from the answer key each time, and list its IDs in the scorecard.
- **Scoring:** Found = 1, Partially found = 0.5, Missed = 0. Recall uses only the Found, Partially found and Missed definitions in step 2, so a one-level severity difference never lowers recall. Write every recall figure as numerator / denominator = percentage, with one decimal place, and check that each denominator equals the number of IDs listed for that group.
- **Severity accuracy:** report two lines, each as numerator / denominator = percentage, with one decimal place. Both use the same denominator: the number of Found and Partially found issues. Missed issues are left out.
  - **Within one level:** issues whose highest severity among their matching verified findings is within one level of a severity the answer key accepts for them.
  - **Exact match:** issues whose highest severity among their matching verified findings is one the answer key accepts exactly.
- **Distractors:** too high means rated Medium or above anywhere in the register or the report.
- **Unsupported findings:** a finding in the report that the verifier marked Not supported, or that you cannot match to its cited source.
- **Positives:** grade the planted-positives row in its own table row, under its answer key ID, as Present, Partly present or Absent. Leave it out of recall, every severity group and severity accuracy.
- Grade from this run's files only. Do not open earlier scorecards or runs.

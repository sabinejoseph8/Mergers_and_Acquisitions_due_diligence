---
description: Archive the current run and its scorecard, then reset working memory for a fresh diligence run
---

1. Read the target name from `memory/target.txt` (use `falcon` if the file does not exist). Below, `<target>` means that name.
2. Choose the archive folder, `<archive>`, using the current date and time:
   - For a fictional target: `runs/<YYYY-MM-DD_HHMM>/`.
   - For a real target (`targets/<target>/checks.json` has `"real": true`, or `targets/<target>/data/README.md` says "Real public company, hypothetical deal"): `targets/<target>/evaluation/runs/<YYYY-MM-DD_HHMM>/`. A real target's report and scorecard must never be published, and `runs/` is tracked by Git. First run `git check-ignore -q targets/<target>/`. If Git does not ignore that folder, stop and tell the user: archiving there would let the next commit publish the run. Inside `evaluation/`, the run stays covered by the rule that a diligence run never reads a target's `evaluation/` folder.
3. Create `<archive>`. Move the current contents of `memory/` and `output/` into it (keep the subfolder names). `memory/target.txt` moves with them, so the run folder records which target it used; if the file did not exist, write `<target>` to `<archive>/memory/target.txt`. Leave `output/.gitkeep` in place.
4. If `targets/<target>/evaluation/scorecard.md` exists, move it to `<archive>/evaluation/scorecard.md` (in `runs/`, or in the real target's `evaluation/runs/`) with a shell `mv` command, without opening it. Each run keeps its own grade, the next `/evaluate` cannot overwrite it, and the next run cannot read it.
5. Copy the blank templates from `templates/memory/` into `memory/`, and make sure `output/` is empty apart from `.gitkeep`.
6. Confirm what was archived and where, including the target and whether a scorecard was moved, and that memory is now blank. For a real target, also confirm with `git status --short` that nothing from the run is listed.

Do not touch `targets/*/data/`, `.claude/` or any `targets/*/evaluation/answer-key.md`. The scorecard is the only file in a target's `evaluation/` folder that this command moves.

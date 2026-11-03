# How to run Project Falcon in Claude Code

No coding needed. You type plain-English replies at three checkpoints.

## Before you start

1. Install Claude Code and sign in (see the official setup guide at https://code.claude.com/docs).
2. Download or clone this project folder to your computer.
3. Open a terminal in the project folder (the folder that contains `CLAUDE.md`) and type `claude`.

## Check the setup (1 minute)

- Type `/agents`. You should see five project agents: `sec-filings-analyst`, `news-media-analyst`, `litigation-analyst`, `financial-analyst` and `citation-verifier`.
- Type `/` and look for the project commands: `/diligence`, `/diligence-status`, `/evaluate`, `/reset-memory` and `/run-tests`.
- Type `/run-tests`. Claude runs the automated checks and should report 0 failures (checks that need a finished run are skipped).

## Pick a target

Each fictional target has its own folder in `targets/`, for example `targets/falcon/`. It holds the sources (`data/`, starting with `data/deal-brief.md`), the answer key (`evaluation/answer-key.md`) and a checksum manifest (`data_manifest.json`). A run works on one target. Name it when you start: `/diligence falcon`. With no name, the run uses `falcon`. The run records its target in `memory/target.txt`, and `/evaluate` and `/reset-memory` read it from there.

## Run the diligence (about 60 to 90 minutes)

| Step | You type | What happens |
|---|---|---|
| Start | `/diligence` or `/diligence <target>` | The lead agent records the target, reads its deal brief and writes a plan to `memory/plan.md`. |
| Checkpoint 1 | `approve` (or ask for changes) | Four analysts start in parallel: SEC filings, news, litigation, financials. |
| Checkpoint 2 | `proceed`, or `dig deeper on <topic>` | The lead agent shows the red flags and the conflicts between sources. You decide whether to loop again (maximum 3 loops). |
| Checkpoint 3 | `approve report` (or ask for changes) | The citation verifier has checked every key finding. You sign off before the report is written. |
| Report | nothing | The report is saved in `output/` as Markdown, HTML and (if your computer has a PDF tool) PDF. |

Claude Code may ask your permission before some actions (for example converting the report to HTML and PDF). Read the request and approve it if it makes sense.

Claude Code also asks before anything opens a file in any target's `evaluation/` folder, `examples/` or `runs/`. During a diligence run, **deny** these requests: the agents must not see the answer key, a scorecard or an earlier run. Approve the answer key request only when you run `/evaluate`.

The sample run in `examples/sample-run/` took 69 minutes from the approved plan to sign-off.

At any time, type `/diligence-status` to see where the run is, how many findings there are and what is still open.

## Make the committee dashboard (1 minute)

In a terminal in the project folder, run:

```
python3 tools/make_dashboard.py
```

It writes `output/Project-<Codename>-Dashboard.html`, one file that opens in any browser, offline. It shows the findings by severity and verification status (as a chart and a table), the top red flags, the key metrics and the open questions. Every figure is copied from `memory/`, so it matches the report. It is read-only: change the run's memory files, not the page. To make one for an archived run, name its memory folder, for example `python3 tools/make_dashboard.py runs/2026-11-02_2237/memory`; the page goes into that run's own `output/` folder.

## Grade the run

Type `/evaluate` (or `/evaluate <target>`) and approve the request to open the answer key. Claude compares the run with `targets/<target>/evaluation/answer-key.md` (the issues planted in the fictional data) and writes `targets/<target>/evaluation/scorecard.md`. With no target named, it grades against the run's own target from `memory/target.txt`.

## Run it again

Type `/reset-memory`. Your previous run, its target name and its scorecard are archived together in a dated folder in `runs/`, and working memory is cleared. To check an archived run later, type `python3 tests/run_all.py --run runs/<folder>`. A real target's run is private, so it is archived instead in `targets/<target>/evaluation/runs/<folder>`, which Git must ignore; the command stops if it does not.

## If you have no PDF tool

Open the HTML report in `output/` (for the Falcon target, `output/Project-Falcon-Due-Diligence-Report.html`) in your browser, choose Print, then Save as PDF.

## Add a new target

1. Create `targets/<name>/data/` with a `deal-brief.md`, a `README.md` and the four source folders (`sec-filings/`, `news/`, `litigation/` with a `docket_index.csv`, and `financials/` using the same CSV files and row labels as Falcon's, so the tie-out checks can run). Label every document fictional.
2. Write `targets/<name>/evaluation/answer-key.md` with planted issues `P01`, `P02`, ... and distractors `D1`, `D2`, ...
3. Record the baseline: `python3 tests/run_all.py --write-manifest --target <name>`.
4. Optionally add `targets/<name>/checks.json` to pin the answer key's counts (see `targets/falcon/checks.json`).
5. Run `python3 tests/run_all.py`. The data checks now cover the new target too.

## Add a real company (Phase 8)

A real target uses a real public company's SEC filings as of a cutoff date, with a hypothetical deal. The agents still work offline: you download the filings before the run.

1. A separate case session picks the company and the cutoff and runs the contamination check (see the tech spec). It tells you only the company and the cutoff, not what happened later.
2. In a terminal in the project folder, download the filings:
   ```bash
   python3 tools/fetch_edgar.py --company <ticker or CIK> --cutoff <YYYY-MM-DD> --target <name>
   ```
   SEC asks every request to name a contact, so the tool asks for your name and email address. It does not save them, and the example contact is refused.
   This writes `targets/<name>/checks.json` and `targets/<name>/data/`: the filings as plain text, split into one file per Item with an index (`sec-filings/index.md`), financial data filed before the cutoff, and empty news and litigation folders marked `NO-SOURCES.md`.
3. The case session writes `targets/<name>/data/deal-brief.md`, labeled "Real public company, hypothetical deal, as of <cutoff>", and `targets/<name>/evaluation/answer-key.md`, with warning signs `P01`, `P02`, ... and no distractors.
4. Record the baseline: `python3 tests/run_all.py --write-manifest --target <name>`.
5. In a fresh session, run `/diligence <name>`, and approve each checkpoint without steering.

## Tips for your portfolio

- Record your screen during a run (especially the three checkpoints). A two-minute video of the agents working is very persuasive.
- Keep your own scorecard from `/evaluate`, and note what you changed in the agent instructions to improve it.

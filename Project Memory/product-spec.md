# Product Spec: Project Falcon

**Status:** Agreed, version 1.26 (November 4, 2026: the overview describes what the project demonstrates, not who built it; a goal, a user, three user stories and a success criterion are removed, and the public files no longer say who reviews the project).

## Overview

Project Falcon is an AI "due diligence team" for M&A deals. A person gives it a deal brief and a set of sources about a target company. A lead agent plans the work, four specialist agents research the sources in parallel, the lead agent connects what they find, an independent checker verifies every important claim, and the person approves the work at three checkpoints. The output is an Investment Committee-ready report.

It is also a portfolio piece demonstrating design, control and measurement of an agentic workflow for high-stakes work. The six targets in the repository, Talonfield Systems among them, are fictional. The two backtests used a real company's public filings, which stay out of the repository.

## Goals

1. Cut the first pass of due diligence from weeks of manual research to one supervised session.
2. Catch the red flags that only appear when sources are combined, such as an event a company left out of its filings.
3. Keep a human in control of every important step, with a clear audit trail.
4. Prove quality with a score, not a claim, by testing against planted red flags.

## Users

| User | What they do | Sign-in |
|---|---|---|
| **Operator** (deal team analyst or associate) | Starts a run, answers the three checkpoints, reads the report, grades the run | Uses their own Claude Code account. No other sign-in. |
| **Decision maker** (Investment Committee member, deal lead) | Reads the report and decides | None. Receives the PDF. |

## User stories

**Starting a run**
- As an operator, I can start a full diligence run with one command, so I don't need to remember steps.
- As an operator, I am asked whether to continue or start fresh if a previous run exists, so I never mix two runs by accident.

**Planning and approval**
- As an operator, I see the plan (questions, hypotheses, assignments) before any research starts, so I can correct the scope early.

**Research**
- As an operator, I see which specialists are working and when each one reports, so I know the run is progressing.
- As a decision maker, I can trust that every finding names its source, so I can check anything myself.

**Reviewing red flags**
- As an operator, I see the most serious findings and the conflicts between sources at one stop, so I can decide whether to dig deeper.

**Verification and sign-off**
- As an operator, I see which findings were verified, corrected or rejected before the report is written, so nothing unsupported reaches the committee.

**The report**
- As a decision maker, I get a clear recommendation, the top red flags, answers to the committee's questions and recommended deal protections, so I can decide quickly.
- As a decision maker, I can tell facts from allegations and rumors, so I weigh them correctly.

**Status and audit**
- As an operator, I can ask for the status of a run at any time.
- As anyone reviewing the work, I can read every finding, decision and checkpoint in plain files.

**Grading and re-running**
- As an operator, I can grade a run against the answer key and see what was missed.
- As an operator, I can archive a run and start a clean one.

## Functional requirements

**Running a diligence**
- **R1.** One command starts a run. If no previous run exists, it begins with the plan. If one exists, it asks whether to continue or start fresh.
- **R2.** The plan is saved before any research. It maps all six committee questions to specialists, lists 2 to 4 hypotheses, gives each specialist a task list, and states the 3-loop limit.
- **R3.** Checkpoint 1: the run stops after the plan and does nothing until the operator approves or asks for changes. The plan summary (questions, hypotheses, assignments) is printed in chat in the same message as the question, before it, and the run log says it was shown.
- **R4.** Four specialists (SEC filings, news and media, litigation, financial) work in parallel. Each reads only its own source.
- **R5.** While specialists work, the operator sees which ones are running and is told when each reports (loading state).
- **R6.** Every finding has an ID, a severity (Critical, High, Medium, Low), a confidence level (High, Medium, Low), a source file and section or row, and a status that is exactly one of Open, Verified, Partially verified or Rejected. A Low finding that is not verified stays Open; "not verified" appears only in the report appendix.
- **R7.** Findings are never deleted. Only their status changes.
- **R8.** Each specialist's full report is saved unedited before it is summarized.
- **R9.** The lead agent compares sources and records cross-source findings, conflicts, disclosure gaps and stale assumptions. When three or more findings describe the same trend, it combines them into one cross-source finding, which states only the trend's own headline numbers and cites any part that is its own issue by ID instead of restating it. Every customer, supplier or litigant named in a source is sized against the customer revenue data. Each dated accounting judgment in the filings (for example an impairment test or a reserve level) is compared with later news, market or financial data, and the change is stated with numbers.
- **R10.** The research loop runs at most 3 times. Every extra loop is logged with its reason.
- **R11.** Checkpoint 2: the run stops and shows a table of Critical and High findings, the main conflicts and what is still open. It waits for "proceed" or "dig deeper on <topic>".
- **R12.** An independent checker verifies every Critical and High finding and every Medium finding that appears anywhere in the report, and gives each a verdict. Low findings may stay unverified. Every correction for a Partially verified finding is applied to the register before Checkpoint 3.
- **R13.** Findings judged Not supported are kept in the register but left out of the report.
- **R14.** Checkpoint 3: the run stops and shows the verification results and the draft recommendation. It waits for approval.
- **R15.** The report has nine parts: cover, executive summary, answers to the six questions, risk matrix, workstream detail, cross-source insights, deal protections, open questions, appendix. The executive summary includes the main positive and mitigating points, checked against a fixed list that includes the internal controls conclusion and auditor tenure and opinion. A positive that another finding puts in doubt is still listed, as a qualified positive with both finding IDs. The appendix includes an index of verified findings and a list of the findings that were not verified (Low only), each labeled "not verified".
- **R16.** The report is saved as Markdown, as a web page and, when the computer has a PDF tool, as a PDF. Without a PDF tool, the operator is told how to save the web page as a PDF (error state).

**Status, grading and reset**
- **R17.** A status command shows the current step, loops used, findings by severity and status, and the top open questions. With no run, it says so (empty state).
- **R18.** A grading command scores the latest run: recall overall and for Critical and High issues, severity accuracy, unsupported findings and distractors rated too high, using one fixed grading rule so every run is scored the same way. An issue is found when its main point is in the verified findings, correctly cited, with a severity within one level of one the answer key accepts; severity is reported in two lines, within one level and exact match. The planted positives are graded in their own row (Present, Partly present or Absent), outside recall. It asks permission before opening the answer key. With no run, it tells the operator to run a diligence first (empty state).
- **R19.** A reset command archives the current run and its scorecard with a date and time, and restores blank working memory. It never changes the sources, the answer key or the setup.

**Safety and quality**
- **R20.** The agents cannot use the web and cannot change source files.
- **R21.** The specialists can only read files.
- **R22.** Allegations and rumors are always labeled as such.
- **R23.** If a specialist fails or returns findings without sources, the lead agent asks again once. If that fails, the gap is recorded as an open question (error state).
- **R24.** If a source file is missing or empty, the specialist reports it under "Files reviewed" and as a gap (error state).
- **R25.** All outputs use plain English, US$ millions with one decimal place, and no em dashes.
- **R29.** The agents cannot open anything in `evaluation/` (the answer key and the latest scorecard) or an earlier run (`examples/`, `runs/`) unless the operator approves, so a new run stays blind.

**Project materials**
- **R26.** The project includes a README with the problem, a demo video under 2 minutes long, the architecture diagram, how a run works, sample results and how to run it. The video is recreated from a saved blind run's output, says so on screen, and shows aggregate scores only, never the answer key.
- **R27.** The project includes a complete sample run: working memory, report PDF and scorecard.
- **R28.** The project keeps `interview-notes.md` in first person, updated after significant features, major bug fixes and meaningful design changes.
- **R35.** Every public page the README links to can be read without a sign-in: the Project Memory website is served as a public static page (GitHub Pages) linked from the README, the case study is read as a web page on the same host (the PDF stays, as one of the page's own links), names the author and the repository, and the README leads with the author, one results table and a line on what the author did and what Claude Code did.

**Real data (Phase 8, built and run on two real companies, November 2, 2026)**
- **R30.** The system can run on a real public company's SEC filings and financial data as of a cutoff date. A download tool, run by the owner before the run, saves them into a target folder; the agents stay offline and read-only.
- **R31.** For a real target, the agents use nothing dated after the cutoff and nothing from outside the data folder, including what the model may know about the company from training. The report says it is a historical backtest of a hypothetical deal.
- **R32.** An empty source folder is reported as a gap and listed in the report's limitations, never filled from memory.
- **R33.** Grading a real target uses the same rule as the fictional targets, and also counts hindsight leaks: findings that rely on anything dated after the cutoff.

**Committee view (Phase 7, built November 2, 2026)**
- **R34.** After a run, one command turns its memory files into a read-only dashboard: a single HTML file with findings by severity and verification status (chart and table), the top red flags, the key metrics and the open questions. It copies every figure and does not recompute or reword anything, so it matches the report. It works offline, prints, and works on a phone.

## Layout and responsiveness

- **Desktop:** runs happen in Claude Code in a terminal. Checkpoint messages fit in a normal terminal window, with tables of no more than 5 columns.
- **Report (PDF):** US Letter, portrait, printable in color or black and white. Tables repeat their header row across pages.
- **Report (web page):** readable on a phone. Text reflows, and wide tables scroll sideways instead of shrinking.
- **README and diagram:** read well on GitHub on desktop and phone. The diagram is legible when zoomed on a phone.

## Out of scope for v1

- Live connections to real sources (SEC EDGAR, news services, court systems, data rooms). The agents never connect to anything. Since Phase 8, after v1, the owner can download a real company's SEC filings into a target folder before a run (R30), so the agents still read only local files.
- Real client data. Real public company data is used only in Phase 8's backtests, after v1, as a hypothetical deal, and those reports stay private.
- A custom web app or dashboard. The read-only dashboard file added after v1 (R34) only displays a finished run; nothing on it can be edited.
- Several people working on one run at the same time.
- A full valuation model (for example a discounted cash flow model).
- Legal, accounting or investment advice.
- Scheduled or continuous monitoring of a target.

## Future features (and what v1 does to leave room)

| Future feature | What v1 does now |
|---|---|
| Real sources through connectors | Each source sits behind one specialist and one folder, so a source can be swapped without changing the others. Phase 8 added the first one: SEC filings, downloaded before the run, tested on two real companies. |
| More specialists (tax, people, IP, ESG) | Every specialist uses the same finding format and rubrics. |
| Several deals at once | The deal brief is a single file, and each run is archived separately. |
| A committee view of a run | Done after v1 as a read-only dashboard (R34), built from the working dataset and the findings register. An Excel data pack was built from the same data and compared; the owner kept the dashboard only. |
| Better scores over time | The grading command and answer key make improvements measurable. |

## Success criteria (checkable by using it)

1. An operator can finish a full run with three replies (approve, proceed, approve report) in under 90 minutes.
2. Every run stops at all three checkpoints and does nothing until the operator replies.
3. The report contains all nine parts, and every finding in it names a source.
4. Grading the sample run shows: at least 80% recall on Critical and High issues, zero unsupported findings in the report, and zero distractors rated Medium or above. (Default targets.)
5. No source file changes during a run.

**Phase 8 targets for the real-company backtest (set November 2, 2026, before any result, and confirmed by the owner the same day):**
1. At least 2 in 3 of the answer key's warning signs are found (main point verified and correctly cited, by the same rule `/evaluate` uses).
2. The warning sign most directly tied to the later event is among the top five red flags.
3. Zero unsupported findings in the report.
4. Zero hindsight leaks: no finding relies on anything dated after the cutoff.
5. All three checkpoints held and shown in chat, all nine report parts, and the empty sources listed as gaps.

Time and tokens are recorded with no target, because this is the first run on full-length filings.

## Decisions

| Date | Decision |
|---|---|
| 2026-10-17 | Build with Claude Code features only. No Agent SDK and no application code. |
| 2026-10-17 | Use Claude Code rather than Cowork or Managed Agents (control, readability, and the data-retention options for real client data). |
| 2026-10-18 | Use a fictional public company (Talonfield Systems) with simulated sources and planted red flags. |
| 2026-10-18 | Organize specialists by source to match the architecture: SEC filings, news, litigation, financials. |
| 2026-10-18 | Three mandatory human checkpoints and a 3-loop limit. |
| 2026-10-18 | Add an independent citation checker and an answer key with a grading command. |
| 2026-10-18 | Keep first-person interview notes for the project story. |
| 2026-10-18 | `interview-notes.md` stays private. A `.gitignore` rule keeps it out of GitHub. |
| 2026-10-18 | The project lives in the GitHub repository `sabinejoseph8/Falcon_M-A_Due_Diligence` (renamed `sabinejoseph8/Mergers_and_Acquisitions_due_diligence` on October 19, 2026), plus the one-page case study PDF for applications. |
| 2026-10-18 | Show results with their limits up front: the scorecard and README say how blind the first test run was. |
| 2026-10-18 | After the first grading: the report appendix lists findings that were not verified, trend findings are combined, and verifier corrections are applied before Checkpoint 3 (R9, R12, R15). |
| 2026-10-18 | Earlier runs are protected like the answer key, so a new run stays blind (R29). |
| 2026-10-18 | Time target for a full run raised from 45 to 90 minutes (success criterion 1): the first test run took 69 minutes from the approved plan to sign-off, plus about 10 minutes for the report. Faster runs are a later improvement. |
| 2026-10-18 | The README and case study lead with product skills: framing the problem, specs and a phased plan, evaluation, safety and iteration. The M&A depth is the proof of domain judgment. |
| 2026-10-18 | Each run's scorecard is archived with the run, and everything in `evaluation/` needs approval to open, so one run's grade cannot leak into the next run or be overwritten by the next grading (R19, R29). |
| 2026-10-18 | Fully blind run graded. It meets success criteria 2 to 5: all three checkpoints held (an early "approve" was logged but not treated as sign-off), all nine report parts, 96.2% recall on Critical and High issues, 0 unsupported findings, 0 distractors too high, no source file changed. Criterion 1 (under 90 minutes) was not measured fairly: elapsed time was about 7 hours, mostly gaps between operator replies and one stalled turn, so timing needs a cleaner measurement next run. |
| 2026-10-18 | Three blind graded runs with a frozen setup meet success criterion 4 every time: Critical and High recall 96.2%, 96.2% and 100% (average 97.4%), 0 unsupported findings and 0 distractors too high in each. |
| 2026-10-18 | Fixes from the graded runs (R9, R12, R15): size every named counterparty against the customer data, verify the Medium findings the report relies on, put positives and mitigating points in the executive summary, and calibrate debt severity. `/evaluate` gets one fixed grading rule (R18). They take effect from the next run and have not been measured yet. |
| 2026-10-18 | Graded run 4, the first with the fixes, meets success criteria 2 to 5: 100% recall on all 18 planted issues and on the 13 Critical and High issues, 100% severity accuracy, 0 unsupported findings, 0 distractors too high. Every repeated gap from runs 1 to 3 closed (R9, R12, R15). One run only, so no range yet. Next quality fixes, held for now: severity drift toward Critical, a self-check of cross-source findings, folding duplicate findings. |
| 2026-10-18 | Quality fixes from run 4 (R9, R11, R12, R15): Critical needs a named test and the number that meets it; the lead agent self-checks its cross-source findings; duplicates are folded into a parent finding so the risk matrix shows each fact once. Not yet measured; graded run 5 will check that recall holds and quality improves. |
| 2026-10-18 | Graded run 5, with the quality fixes, meets success criteria 3 to 5 and every quality target: 100% recall on the 13 Critical and High issues (97.2% on all 18), 100% severity accuracy, 0 unsupported findings, 0 distractors too high, 3 Critical issues, 5 of 14 cross-source findings corrected, a 14-row risk matrix and a 17-page report. Criterion 2 held only in part: the run stopped at all three checkpoints, but the Checkpoint 1 plan summary was not shown in chat. Fixed after the run (R3, R16): checkpoint content is printed before the question, and the report converter is committed. |
| 2026-10-18 | Run 5's two remaining suggestions (R9, R12, R15): every Medium finding that appears anywhere in the report is verified, so only Low findings can be listed as "not verified"; and the lead agent checks each dated accounting judgment in the filings (an impairment test, a reserve, a materiality call) against later news, market or financial data and states the change with numbers. Not yet measured; graded run 6 will check them. |
| 2026-10-19 | Graded run 6, with run 5's last two suggestions (R9, R12, R15), meets success criteria 2 to 5: all three checkpoints held and were shown in chat, 100% recall on all 18 planted issues and on the 13 Critical and High issues, 100% severity accuracy, 0 unsupported findings, 0 distractors too high, no source file changed. Goodwill (P18) is fully found again. Quality slipped a little: 7 of 13 cross-source findings corrected (5 of 14 in run 5) and an 18-row risk matrix (14). |
| 2026-10-19 | Grading rule chosen by the owner (option A): an issue counts as found when its main point is in the verified findings, correctly cited, with a severity within one level of a severity the answer key accepts. Exact severity matches are reported separately, so a near-miss on severity is not counted twice. This matches how runs 1 to 6 and Kestrel were graded; under it, Heron's held-out run is 100% recall with 77.8% exact severity matches. To be written into `/evaluate` by a session that has not seen a scorecard (R18). |
| 2026-10-19 | Option A written into `/evaluate` by a session that had not opened an answer key or scorecard (R18): exact Found, Partially found and Missed definitions, recall unaffected by a one-level severity difference, and severity reported as within one level and exact match. Three recurring process gaps fixed at the same time: the planted-positives row is graded as its own scorecard row (Present, Partly present or Absent) and kept out of recall; a register status is always exactly one of the four values, so an unverified Low finding stays Open (R6); and Checkpoint 1 prints the plan summary in chat before the question, in the same message (R3). Not yet measured; the next blind run will check them. |
| 2026-10-31 | Three rule changes from Plover's scorecard, written by a session that had not opened any answer key or scorecard (R9, R15): known deal costs (equity-award cash-outs, break fees, change-in-control severance) are rated Medium and put in the price, unless all of them together pass 5% of value; a trend finding states only its own headline numbers and cites a separate issue by ID, so that issue keeps its own severity; and the positives checklist adds the internal controls conclusion and auditor tenure and opinion, with a positive that another finding puts in doubt listed as qualified. Not yet measured; the next blind graded run will check them. |
| 2026-10-31 | The demo video is recreated from the blind Plover run's saved output instead of screen-recorded live, because a full run takes over an hour (R26). The owner records the voice-over; the video plays in the README from a GitHub attachment, and its sources and build script stay private, outside the repository. |
| 2026-10-31 | v1 is complete at the end of Phase 6. Phase 7 becomes an optional roadmap (a real data source, an Excel data pack, more specialists), kept out of the progress count; each item gets its own plan, targets and checks when it starts. |
| 2026-11-02 | Plan for the first real source (Phase 8, R30 to R33): a real public company's SEC filings and EDGAR's structured financial data, downloaded before the run so the agents stay offline and read-only ("connect at the folder, not the agent"). It is measured by a backtest: warning signs visible in the filings before a later public problem. News and litigation stay empty for a real company rather than simulated. A live web search API for news (for example Tavily) was considered and left for a current company, because in a backtest it would leak hindsight. |
| 2026-11-02 | The owner accepted the recommended defaults for Phase 8's open questions 1 to 3: the five success targets; a separate case session that tells the owner only the company and the cutoff; and only the method, scores and answer-key categories published, with the full report kept private. Open question 4 (news and litigation for a real company) is still open. |
| 2026-11-02 | Later the same day, the owner accepted the recommended default for open question 4: news and litigation stay empty for the backtest and are listed as gaps. Real court records are a candidate next roadmap item; a news search API waits for a current company. All four Phase 8 questions are now decided. |
| 2026-11-02 | Committee view (R34): a read-only dashboard and an Excel data pack were both built from a finished run's memory files and compared on Wren and Plover, with the same counts in each. The owner kept the dashboard only, so the committee gets one view instead of two that could drift apart. The Excel draft stays outside the repository in `../extras/dashboard-draft/`. |
| 2026-11-03 | The demo video is remade, still from the blind Plover run, with a committee dashboard scene and the graded results for Wren and Avocet, so it no longer ends on the best score. It grows from 89 to 105 seconds, so R26 now says under 2 minutes. The owner re-recorded all nine lines so tone and volume match. |
| 2026-11-04 | Review of the public files, signed out, as a first-time reader sees them. Fixes: the README leads with the author, one headline result, a links row and a results table, with the run-by-run history folded into collapsible blocks; the case study's tiles lead with the held-out recall range and the per-deal saving, and its footer names the author and the repository; the public link to the Project Memory website moves to GitHub Pages, because the claude.ai page showed a blank screen and then a sign-in banner to anyone signed out (R35); the GitHub About box gets a description, topics and a homepage. The repository name is kept, the author is named without a link, and no license file is added, by the owner's choice. The status lines of all four planning files are trimmed to one note each; this table already holds the earlier notes (the video remade; R34 and the Excel data pack dropped; the out-of-scope list split between live connections and downloaded real data; R30 to R33 built; Phase 8 planned). |
| 2026-11-04 | Wording fixes after the owner re-read the public files: "fictional" now covers only the six targets in the repository, with the two real-filing backtests named as the exception (README, diagram footer, this overview); the README intro, the case study subtitle and the diagram subtitle drop "without application code"; the problem statement says 2 associates, not 5 to 10, in the README and the diagram; the demo video paragraph drops "with my own voice-over". |
| 2026-11-04 | The README links the case study as a web page (`docs/case-study/index.html` on GitHub Pages, built from the same `docs/case-study.html` as the PDF), not as a PDF, on the pattern of the Clarivi case study: a page opens in place on a phone and reads at any width, while a PDF link downloads or opens a viewer. The PDF stays, offered in the page's own links row. R35 updated. |
| 2026-11-04 | The overview now says what the project demonstrates (design, control and measurement of an agentic workflow for high-stakes work) instead of who built it; goal 5, one of the three users, three user stories and success criterion 6 are removed, so the goals, users, stories and success criteria describe the product only. Requirements R26 to R28 and R35 stay, now grouped as Project materials. The four Project Memory files also stop naming who reviews the project: R35 now covers every public page the README links to, and past entries describe the review as a first-time reader's. The README, the run guide's tips and the diagram footer likewise describe the project, not its audience. The owner's wording and decision. |

## Open questions (with recommended defaults)

1. **Are the Phase 8 success targets right?** Decided (November 2, 2026): yes, the five targets under Success criteria. Recall is set lower than the fictional runs' 80%, because real warning signs are subtler and nobody planted them.
2. **Who picks the backtest case?** Decided (November 2, 2026): a separate case session picks it by the tech spec's criteria and tells the owner only the company and the cutoff. The owner still knows the company, so they approve each checkpoint without steering, and the write-up says so.
3. **What gets published?** Decided (November 2, 2026): the method, the scores and the answer key's categories go public; the full report stays private, because it is an AI's red-flag list about a real, named company, and AI output can still be wrong.
4. **What about news and litigation for a real company?** Decided (November 2, 2026): leave both empty for the backtest and list them as gaps. Real court records (for example CourtListener) can be the next roadmap item. A web search API for news fits a current company, saved as a dated snapshot before the run, but not a backtest, because today's web already knows how the story ended.

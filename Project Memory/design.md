# Design: Project Falcon

**Status:** Agreed, version 1.17 (November 5, 2026: the README's architecture diagram moves below "At a glance", and the demo video's heading gives its length and says it has sound).

Project Falcon has no custom app screen. People experience it in three places: **the Claude Code conversation** (commands, progress messages and checkpoints), **the documents it produces** (report, findings register, scorecard), and **the project materials** (README, demo video, architecture diagram, case study, Project Memory website). This file sets one design language for all three.

## Design principles

- **Evidence first.** Every claim shows where it came from: file and section, or docket date.
- **Humans decide.** The system recommends. A person approves at every checkpoint.
- **Bounded autonomy.** Clear stops, clear limits (3 loops), nothing hidden.
- **Plain English.** A busy committee member understands each page in one read.
- **Severity is not certainty.** Every finding carries both how much it matters and how sure we are.
- **Show your work.** Calculations appear with their inputs.
- **Audit trail by default.** Decisions live in files anyone can open, not only in chat history.
- **One look everywhere.** The same colors, labels and terms in the diagram, report and docs.
- **Print first.** Documents look right on paper and in black and white.

## Visual design language

### Color palette

| Name | Hex | Used for |
|---|---|---|
| Falcon Navy | `#0B1F5C` | Headings, header bands, table headers, Agent Core block, bottom-line box, text on light accent colors |
| Memory Teal | `#00B3C8` | Working Memory block, loop circles, callout borders |
| Report Orange | `#E07B4F` | Final report block and accent fills. Text on it is always Falcon Navy (5.2:1) |
| Ember | `#B5491F` | Orange text on white (agent names, cover subtitle, High severity). 5.3:1 on white |
| Checkpoint Gold | `#F6C344` | Human checkpoint pills. Text on it is Falcon Navy |
| Checkpoint Border | `#E5B53C` | Checkpoint panel border, allegation callout border |
| Checkpoint Cream | `#FFF8E6` | Checkpoint panel and allegation callout background |
| Ink | `#1F2430` | Body text |
| Slate | `#4A5060` | Secondary text in the diagram |
| Muted | `#5B6170` | Captions, small print, Low severity |
| Line | `#D9DDE5` | Table borders and dividers |
| Mist | `#F3F5F8` | Zebra table rows, soft panels |
| Panel | `#EEF0F3` | Problem strip and verifier block in the diagram |
| Haze | `#C9D3F0` | Subtitles on Falcon Navy |
| White | `#FFFFFF` | Page background |

**Severity colors** (text labels in reports; always paired with the word, never color alone):

| Severity | Hex | Contrast on white |
|---|---|---|
| Critical | `#B42318` | 6.6:1 |
| High | `#B5491F` (Ember) | 5.3:1 |
| Medium | `#8A5A00` | 5.9:1 |
| Low | `#5B6170` (Muted) | 6.2:1 |

**Contrast rule:** all text meets at least 4.5:1. Never put white text on Report Orange, and never use Report Orange for text on white.

### Typography

- **Typeface:** Helvetica Neue, then Helvetica, then Arial, then Liberation Sans on Linux (built into every computer, prints cleanly).
- **Monospace:** Menlo, then Consolas, for agent names, commands and file paths.

| Style | Report (pt) | Diagram (px at 1400 wide) |
|---|---|---|
| Cover title | 28, bold | n/a |
| Title / H1 | 20, bold | 30, bold |
| Section / H2 | 14.5, bold, navy rule underneath | 18 to 24, bold |
| Sub-section / H3 | 11.5, bold | 15 to 16, bold |
| Body | 10.5, line height 1.45 | 13 to 14 |
| Tables | 8.8 | n/a |
| Small print, captions | 8.5 | 11 to 12.5 |
| Code and paths | 9, monospace | 14, monospace |

### Spacing, shape and depth

- **Spacing:** report uses steps of 4, 7, 10, 14 and 20 pt. Page margins 0.65 in (top) and 0.7 in (sides and bottom). The diagram uses a 20 px gutter between blocks.
- **Corner radius:** 3 px (inline code), 4 px (callouts, bottom-line box), 6 to 8 px (diagram blocks), fully rounded (checkpoint pills).
- **Shadows:** none. Flat design prints well and stays calm.
- **Motion:** none. Documents are static. Progress in the terminal is shown with short text updates.
- **Page breaks:** headings stay with the text that follows. Small tables (up to 7 rows) stay on one page; longer tables repeat their header row on every page.

## Main UI components

| Component | Where | States | How it behaves |
|---|---|---|---|
| **Command** (`/diligence`, `/diligence-status`, `/evaluate`, `/reset-memory`, `/run-tests`) | Claude Code | Ready, running, waiting for permission, error | One word starts each job. Errors say what to do next (for example "No run yet. Type /diligence first."). |
| **Checkpoint message** | Claude Code | Waiting, approved, changes requested, skipped | Opens with "Checkpoint N of 3: name", gives a short summary and at most one table, and ends with the exact replies to type. The content is printed as chat text first and the question is the last thing in the message, never only in a question box, which ends the turn in the desktop app. Changes requested: the plan or draft is revised and shown again. Skipped only if the user says so, and logged. |
| **Progress update** (loading state) | Claude Code | Working, partly reported, all reported, analyst failed | Names the specialists that are running. Reports each one as it finishes with its finding count and number of Critical items. A failed analyst is retried once, then recorded as a gap. |
| **Red-flag table** | Checkpoint 2, report | Populated, empty | Columns: ID, Finding, Severity, Confidence. Critical first. If empty: "No Critical or High findings." |
| **Finding card** | Analyst reports | Open, Verified, Partially verified, Rejected | Fixed field order: Finding, Evidence, Source, Severity, Confidence, Deal impact, Cross-check. Never deleted. |
| **Findings register** | `memory/findings.md` | Empty, growing, final | One row per finding with status. Cross-source findings have their own section. |
| **Labels** | Everywhere | n/a | Severity: Critical, High, Medium, Low (colored word). Confidence: High, Medium, Low (plain word). Claim type: Fact, Allegation, Rumor. |
| **Cover page** | Report | Fictional target, real target (Phase 8) | Title, "Draft for Investment Committee discussion", date, "Fictional case study", preparer line. Navy bar on the left. For a real target, "Fictional case study" becomes "Historical backtest using public filings as of <cutoff>" and "Hypothetical deal". |
| **Bottom-line box** | Report, executive summary | n/a | Navy box with white text. One recommendation and one sentence of reasoning. |
| **Risk matrix** | Report | n/a | ID, finding, severity, confidence, verification verdict and recommended action, Critical first. With many findings, it shows the consolidated cross-source findings and the appendix index lists every verified finding. Repeats its header on every page. |
| **Callout** | Report | Note, allegation | Teal border for notes. Cream background with gold border for allegations and rumors. |
| **Key metrics table** | Report | n/a | Reported and adjusted figures side by side, with the source finding ID. |
| **Scorecard** | `evaluation/scorecard.md`, then the archived run in `runs/` | No run, graded, archived | Recall summary first, then one row per planted issue: Found, Partially found or Missed. `/reset-memory` moves it into the archived run, so every run keeps its own grade. |
| **Finding ID** | Everywhere | n/a | Never breaks across a line ("SEC-01" stays whole). Ranges are written "LIT-01 to LIT-03". |
| **Findings index** | Report appendix | Verified, partially verified | One table per workstream: ID, finding (with the corrected wording), severity and verdict. Built from the findings register. |
| **Not-verified list** | Report appendix | Empty, populated | Medium and Low findings that were not checked, each labeled "not verified", so nothing found is dropped silently. If empty: "Every finding was verified." |
| **KPI tile** | Case study, README | n/a | One large number with a short label (for example "13 of 13 Critical and High planted issues found"). Teal top border on Mist. |
| **Caveat note** | Scorecard, README, case study | n/a | Cream background with a gold border. States the limits of a result (for example how blind a test was) right next to the result, never in a footnote. |
| **Diagram blocks** | Architecture diagram | n/a | Agent Core (navy), Working Memory (teal), Specialist card (white, navy border, Ember agent name), Verifier card (panel gray), Report block (orange, navy text), Checkpoint pill (gold), Controls band (navy). |

## Screens and layouts

1. **The run in Claude Code** (one scrolling conversation):
   `/diligence` -> plan summary -> **Checkpoint 1** -> progress updates while four specialists work -> red-flag table and conflicts -> **Checkpoint 2** -> verification results and draft recommendation -> **Checkpoint 3** -> "Report saved" with file locations.
2. **The report** (US Letter, portrait): page 1 cover; page 2 executive summary (bottom-line box, top five red flags, valuation implications); then the answers to the six committee questions, the risk matrix, workstream detail, cross-source insights, deal protections, open questions and appendix (methodology, checkpoint log, verification statistics, findings index, sources, limitations). The sample report runs to 15 pages. The blind run's report ran to 27 pages, because its risk matrix lists all 68 verified findings. The executive summary now has a "Main positive and mitigating points" section (built after the graded runs; first shown in run 4), so strengths found by the analysts are not dropped. Graded run 4's report runs to 38 pages, because its risk matrix lists 90 verified findings, several of them restating the same fact; folding duplicates into a parent finding is the proposed next fix.
3. **The architecture diagram** (`docs/architecture.png`): follows the layout of your original architecture slide. Agent Core and Working Memory on the left, the four specialist tools in the middle, the verifier and report on the right, the checkpoint lane below, and the controls band at the bottom.
4. **The README** (GitHub, desktop and phone): one-paragraph summary, the author line (what the author did and what Claude Code did), one headline result, a links row (case study, Project Memory site, sample report, how to run it), the problem statement, the demo video under the heading "M&A due diligence video demo, 1 minute 44 seconds with sound", "at a glance" bullets with one results table and a contents line, the architecture diagram, then detail sections, with the run-by-run history in collapsible blocks. The most important information is in the first screen, and the skills list leads with AI product management.
5. **The case study**, read as a web page (`docs/case-study/index.html` on GitHub Pages, built from `docs/case-study.html` by `tools/case_study_page.py`: one reading column on a phone and two from 860px, the diagram as a drawing that scrolls sideways on a phone, light and dark, and a links row at the end with the PDF as one option) and as a two-page PDF (`docs/case-study.pdf`, US Letter) made from the same file, titled as an AI product management case study. The README links the page, not the PDF. Page 1: header band, five KPI tiles (12 blind graded runs on 6 fictional targets; 96% to 100% Critical and High recall on four held-out targets; 0 unsupported findings; 38 to 13 report pages; 75% to 78% lower cost per deal than a two-analyst first pass), two columns (problem, what was built, key decisions and the two real-filing backtests, limits first, on the left; diagram, conclusion and lessons on the right) and a caveat note. Page 2 is a one-page dashboard, "Cost and time per deal: this system versus a manual first pass by two analysts", for a professional setup and a team doing 20 deals a year, with the one-time setup spread over 3 years: five KPI tiles (cost per deal for each side, 75% to 78% lower, 155 to 164 person-hours saved, 1 to 2 days instead of about 2 weeks), two range bar charts (cost and person-hours per deal; teal for this system, ember for manual, the lighter part running from the low to the high estimate), two line-item tables with bars on one US$0 to US$15,000 scale (this system: data subscriptions with LexisNexis news, Claude Enterprise, connector upkeep, setup, agent runs, PACER, senior review; manual: 160 analyst hours split by task plus the same data, PACER and review), a time table, a per-year table, a "measured and assumed" note, then the footer, which names the author and links the repository. Only the filings-only run cost, its time and the checkpoint minutes are measured; the rest is labeled as list-price assumptions; the per-agent breakdown is not shown. The backtests name no company, and the footer says the fictional targets are invented and the backtests' real companies stay unnamed.
6. **The Project Memory website** (desktop and phone): one tab per planning file (Product Spec, Design Spec, Tech Spec, Plan) with color swatches, diagrams and the plan. The file tabs follow the Clarivi Project Memory site: a "Four files. Choose one to read it:" line above a segmented control, a document icon before each label (hidden on a phone, where the labels shorten), the open file as a raised white pill, the other labels in teal, and a translucent sticky bar. A phase whose status starts with "Roadmap" gets a Roadmap chip and stays out of the progress ring, the current phase and the next task, so optional work never makes v1 look unfinished. One build is served two ways: a static page on GitHub Pages, linked from the README, which anyone can read without a sign-in and which shows the plan as written; and a claude.ai page, for the owner, where finished tasks are ticked live. Each tab's header shows a short status pill and the date, with the latest change in one note below it.
7. **The demo video** (105 seconds, 1920 x 1080, played in the README on GitHub; remade November 3, 2026): nine scenes recreated from a blind run's saved output: title and diagram, the approved plan, the four analysts' finding counts, the Critical red flags, the verifier's re-checks, the report scrolling, the committee dashboard (always shown in its light theme), the graded results for Falcon and every held-out target, and an end card. Dark navy scenes with teal and gold accents, a caption on every scene so it works muted, and the owner's own voice-over. It says on screen that the scenes are recreated, and it shows aggregate scores only.

## Change history

Earlier status notes, moved here on November 4, 2026 so the status line stays short. Nothing was removed.

- **Version 1.16 (November 4, 2026):** the public files describe the project, not its audience.
- **Version 1.15 (November 4, 2026):** the case study becomes a web page, the README's problem statement moves above the demo video, and the website's file tabs follow the Clarivi pattern.
- **Version 1.14 (November 4, 2026):** after a review of the public files as a first-time reader sees them, the case study's page 1 tiles lead with the held-out recall range and the per-deal saving, its footer names the author and the repository, the README opens with the author, one headline result and a links row, and the Project Memory website is also served as a static page on GitHub Pages; earlier notes are in Change history at the end of this file.
- **Version 1.13 (November 3, 2026):** page 2 of the case study becomes a one-page cost and time dashboard per deal, professional setup against two analysts; earlier the same day, the demo video is remade with a committee dashboard scene and every held-out target in its results, in a new voice-over; earlier the same day, the case study grows to two pages; page 2 compares the measured cost and time of a real-company backtest with an illustrative two-analyst first pass; earlier, November 2, 2026: the one-page case study gains a short section on the two real-company backtests, limits first, and still fits one page; earlier the same day, the report cover for a real company is built, in `templates/real-target-rules.md`.

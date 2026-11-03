# Wren target: build notes

**FICTIONAL. Grader and owner use only. Do not show this file to the system under test.**

## What was built

A fifth fictional diligence target. Codename **Wren**. Target **Meridale Lift Services, Inc.** (NYSE: MDLS), the largest independent US elevator and escalator service company (FY2025 revenue US$1,067.7 million). Deal: take-private by **Ostrander Hale Partners Fund IV** at US$41.50 per share, equity value US$1,917.3 million, EV US$2,459.5 million, 14.4x LTM Q2 2026 Adjusted EBITDA of US$171.2 million. Signed September 20, 2026; special meeting December 9, 2026. Data room "as of" date: October 28, 2026.

| Path | Contents |
|---|---|
| `data/deal-brief.md` | Terms, model base, sources and uses, thesis, six IC questions |
| `data/README.md` | Fictional label and file list |
| `data/sec-filings/` | 10-K FY2025, 10-Q Q2 2026, 8-K 2026-02-25 (results), 8-K 2026-09-21 (merger agreement), DEFM14A |
| `data/news/` | 14 articles, including noise (training academy, market study) and one unreliable blog (D4) |
| `data/litigation/` | `docket_index.csv` (8 matters) and 6 case files (LIT-01 to LIT-06) |
| `data/financials/` | `README.md` and the seven CSV files with the reference headers |
| `evaluation/answer-key.md` | P01 to P18, P19 positives, D1 to D4 |
| `checks.json` | 19 planted rows, 4 distractors |
| `build_financials.py` | Generates every CSV and prints the derived figures used in the documents |

## How

- Worked only in `falcon-target-builder/`. I did not open, list or search the project under `~/Documents/Claude/M&A/`. I read only `BRIEF.md`, `reference/` and the sibling hand-over notes in the shared notes folder (layout notes only, no answer keys).
- All financials come from `build_financials.py`. The balance sheet is rolled forward from the cash flow drivers, and cash is the result, so the balance sheet balances and cash ties to the cash flow by construction. The script asserts the balance, the debt carrying-value roll and the quarter sums.
- Percentages and amounts quoted in the filings, news and answer key were taken from the script's derived output or recomputed against the CSVs (segment growth, margins, unit and backlog changes, organic growth on both definitions, EV, multiples, deal costs, retrofit and pension exposure as a share of EV).
- Phase 2 checks were run in a scratch copy (`tests/` from `reference/` plus `targets/wren/`, manifest written there): **12 checks, 0 failed, 1 skipped** (the real-target cutoff check). No `data_manifest.json` is included in `out/wren/`. The owner writes it after copying, with `python3 tests/run_all.py --write-manifest --target wren`.

## The three test items

1. **Known deal costs: P14 (Medium).** Award cash-out US$52.3 million, Brockmere termination fee US$9.5 million, CIC severance US$16.8 million. Total US$78.6 million, 3.2% of EV. The "break fee" is the fee Meridale owes the sellers of Brockmere, because the buyer requires that deal to be terminated. The merger's own termination fees are contingent and are listed as not counted.
2. **Trend with a judgment inside: P01 (Critical trend) and P05 (High judgment).** The judgment is the October 1, 2025 change in commission amortization period from six to ten years, based on a renewal rate that has since fallen.
3. **Controls and auditor: P19 item (a), qualified by P06.** Effective ICFR, a clean opinion, auditor since 2007. P06 is the Q1 2026 out-of-period correction plus the Southwest dismissals and a former employee's allegation. No weakness was reported.

## Caveats

- **Resemblance to avoided types.** P03 (multiemployer withdrawal liability) is a pension issue but not change-of-control pension funding: the merger does not trigger it, the buyer's branch plan does. P07 (collective agreement cost) involves a union but no dispute. P06 involves an accrual error but in cost of revenue, not revenue recognition, and no weakness. P11 is a deal model error on a tax assumption, not a stale model. P10 is a consumer-protection challenge to renewal practices, not sales tax or marketplace economics. P13 is a change-of-control put on notes, not a covenant breach. D3 is a legitimate add-back included so that a report does not flag add-back inflation.
- **P01 headline vs one-offs.** The H1 2026 EBITDA decline of US$15.2 million includes P06 (US$4.1 million) and the P09 loss provision (US$5.2 million). Excluding both, the decline is about 6.6%. The brief asks for the trend to be rated on its headline numbers, so the key says Critical. A grader may see a well-argued High as a near miss.
- **Multi-source share.** 13 of 18 planted rows are marked multi-source, above the brief's "about half". Several of the rows marked "No" are still easier to size with a second folder.
- **Fictional law and agencies.** Illinois' Elevator Door Integrity Act, the New Jersey rule, the New Jersey Service Contract Renewal Act and the Lift Mechanics union and fund are invented, even where real places or real agencies are named.
- **Simplifications.** No noncontrolling interest (the Canada business is a 50% equity-method investment). AOCI is held flat. The FY2023 and H1 2025 cash flow columns are set directly because there is no opening balance sheet for them. Book tax is a flat 24.5% of pretax income.
- The build script sits at the target root, outside `data/`, so it is not covered by the manifest. Delete it after copying if it is not wanted.

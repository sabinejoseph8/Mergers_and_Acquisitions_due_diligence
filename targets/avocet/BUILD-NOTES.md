# Project Avocet: build notes

## What was built

A sixth fictional diligence target. **Brindlewick Cold Chain, Inc. (NYSE: BWCC)**, a temperature-controlled warehousing and refrigerated trucking company in the western United States, is the subject of a hypothetical $34.00-per-share cash acquisition by **Trelliswood Logistics Corp.** Equity value is $1,632.0m, net debt $1,118.0m and enterprise value $2,750.0m (11.0x LTM Q2 2026 Adjusted EBITDA of $250.0m). The deal brief is dated October 28, 2026.

| Folder | Contents |
|---|---|
| `data/deal-brief.md` | Price, equity value, EV bridge, deal model basis, sources and uses, proposed terms, integration plan, six IC questions |
| `data/README.md` | Fictional label and file list |
| `data/sec-filings/` | 10-K FY2025, DEF 14A 2026, 10-Q Q2 2026, 8-K March 20, 2026 (Harbor District), 8-K September 22, 2026 (strategic review and severance plan) |
| `data/news/` | 14 items, December 2025 to October 2026, including two noise items (Q4 results, food bank donation) and one unreliable source (pseudonymous forum post) |
| `data/litigation/` | `docket_index.csv` (8 matters, exact reference headers) and six case files |
| `data/financials/` | `README.md` and the seven CSVs with the exact reference names and headers |
| `evaluation/answer-key.md` | Value-base preamble, the four test items, P01 to P19, D1 to D4 |
| `checks.json` | 19 planted issues, 4 distractors |

## How

- All financial CSVs come from one script, `build/generate_avocet.py`, in the builder folder (not in this target, so the system under test cannot read it). It holds every input as integer tenths of $ millions, derives each total once, builds the balance sheet from an opening balance with full roll-forwards (PP&E, software, intangibles, equity, debt) so it balances by construction, derives the cash flow from balance sheet movements, and asserts that the cash flow ends at balance-sheet cash. It also writes `build/avocet_facts.json` with the deal and test-item figures quoted in the Markdown.
- The deal values were fixed first: LTM Adjusted EBITDA $250.0m × 11.0 = EV $2,750.0m; net debt $1,118.0m from the June 30, 2026 balance sheet; equity $1,632.0m = 48.0m shares × $34.00.
- Every percentage quoted in a filing, the deal brief or the answer key was recomputed against the CSVs. The Phase 2 checks (`test_phase2_data.py`) were run on November 3, 2026 against a scratch copy of this target with a temporary manifest: 12 checks, 0 failed, 1 skipped (the real-target cutoff check). `build/verify_avocet.py` in the builder folder checks the reference headers and file names, and recomputes about 40 quoted figures from the CSVs. All passed. No `data_manifest.json` is included: the owner writes it with `run_all.py --write-manifest --target avocet` after copying.

## Where the four required test items sit

1. **Deal costs on one value base:** P14 (Medium). $46.2m award cash-out + $49.0m termination fee + $16.4m severance = $111.6m: 4.06% of EV, 6.84% of equity. $72.0m of advisory, financing and other fees would push the total to 6.68% of EV if wrongly added (5.06% with the $27.5m advisory fee alone).
2. **Earnings trend:** P01 (Critical). H1 Adjusted EBITDA −$21.0m, annualized $42.0m × 11.0 = $462.0m = 16.8% of EV; LTM decline alone is 8.4% of EV. The dated judgment is P05 (High): the claims accrual rate was cut from 6.5% to 4.8% on January 1, 2026 while accident frequency rose 18%.
3. **Unrecorded liability:** P02 (Critical). Lease-end restoration, full $312.0m = 11.35% of EV; the buyer's plan to exit four leased sites triggers $118.0m = 4.29% of EV.
4. **Unconfirmed denied claim:** D4 (Low, open question). A pseudonymous forum post about altered temperature records at Fresno, denied on the record, with no supporting filing or court record.

## Caveats

- **Resemblance to avoided types.** None of the planted issues repeats an avoided type, but several sit near one, and the differences are deliberate:
  - P02 (lease restoration) is a contractual make-good obligation, not an environmental remediation reserve or building code retrofit.
  - P05 changes the accrual rate going forward for a new accident year. Prior-year reserves are unchanged, so it is not a one-time reserve release, and it is not a warranty reserve.
  - P06 is about insurance limits being too low for a claim, not an insurance exclusion.
  - P10 is an antitrust class action, not a securities class action. P03 is US merger review, not an EU competition case.
  - P11 is a sale-leaseback with an unrelated REIT, not a related-party lease.
  - P13 concerns immigration document compliance, not a labour dispute.
  - P15 is property tax reassessment, not sales tax or transfer pricing.
  - P12 is a failed software rollout, not a network shutdown forcing hardware upgrades.
  - Equity awards and severance appear only because test item 1 requires them; there are no bonuses and no gross-ups.
- **P11 interacts with D2.** If the sale-leaseback failed sale accounting, the $214.0m would become a financing obligation, but rent of about $16m would also leave Adjusted EBITDA, which partly offsets the change in value. The answer key rates P11 High for restatement and controls risk, not for a large change in price. D2 (operating leases are not debt) still holds for the other leases.
- **P12 severity.** P12 could reasonably be graded Medium. It is keyed High because of customer attrition, the cost overrun and a $47.0m capitalized asset that the buyer's own plan makes worthless.
- **P03 and P02 interact.** A divestiture remedy could require selling the four overlap sites the plan would close. That would change the triggered restoration amount but not the full $312.0m exposure.
- **Reporting choices.** Equity value uses basic shares, with equity awards shown as a separate use. A report that rebuilds equity value on a diluted basis and still counts the cash-out would double count it. The answer key expects the brief's presentation.
- **Simplifications.** The H1 2025 cash flow column has no matching published balance sheet (its working-capital line is set directly). Long-term debt is shown at principal, with no issuance costs. Tax is a flat 24% of pre-tax income.
- **Real names.** Real places (Tacoma, Fresno, San Joaquin County, Pierce County) and real legal provisions (California's change-in-control reassessment, RCW 62A.7-204, ASC 842 sale-leaseback rules, 11 U.S.C. 547, the 2023 Merger Guidelines) are used for realism. All companies, people, cases and figures are invented.

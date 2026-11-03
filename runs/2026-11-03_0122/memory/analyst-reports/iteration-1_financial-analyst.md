## Financial analyst: findings

Project Avocet, iteration 1. This is a fictional case study. All amounts are US$ millions unless stated otherwise. The value base for every percentage test is the enterprise value of $2,750.0m (5% = $137.5m, 10% = $275.0m). At 11.0x, $1.0m of EBITDA equals $11.0m of value.

### Files reviewed

- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/financials/README.md (definitions and reference figures)
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/financials/income_statement.csv
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/financials/adjusted_ebitda_reconciliation.csv
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/financials/balance_sheet.csv
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/financials/cash_flow.csv
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/financials/revenue_quarterly.csv
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/financials/revenue_by_customer.csv
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/financials/kpis.csv
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/deal-brief.md (deal terms only)

**Data integrity:**
- Every subtotal in the income statement, Adjusted EBITDA reconciliation and cash flow footed when I recomputed it.
- The balance sheet balances at all four dates.
- Retained earnings roll forward: -69.2 + 81.9 = 12.7; 12.7 + 57.1 = 69.8; 69.8 + 11.6 = 81.4.
- Paid-in capital rolls forward: 569.5 + 6.5 - 14.0 - 1.5 = 560.5.
- The quarters sum to the annual and half-year totals.
- The KPIs rebuild segment revenue. For example, 1,148k x 81.4% x $784 / 2 = 366.3, against reported Warehousing revenue of 366.4.
- No file contains embedded instructions.

### Key metrics table

Reported figures are as the company presents them. Adjusted views are in FIN-03.

| Metric | FY2023 | FY2024 | FY2025 | H1 2025 | H1 2026 | LTM Jun-26 |
|---|---|---|---|---|---|---|
| Total revenue | 1,265.0 | 1,342.0 | 1,398.0 | 694.0 | 680.8 | 1,384.8 |
| Revenue growth | 7.2% | 6.1% | 4.2% | n/a | -1.9% vs H1 25 | n/a |
| Warehousing / Transportation / VAS revenue | 690.0 / 445.0 / 130.0 | 735.0 / 452.0 / 155.0 | 768.0 / 448.0 / 182.0 | 380.0 / 226.0 / 88.0 | 366.4 / 214.8 / 99.6 | 754.4 / 436.8 / 193.6 |
| Gross margin (cost of revenue excludes D&A) | 26.9% | 27.2% | 27.9% | 28.6% | 26.2% | 26.7% |
| Operating income (margin) | 118.2 (9.3%) | 131.0 (9.8%) | 146.5 (10.5%) | 76.4 (11.0%) | 53.1 (7.8%) | 123.2 (8.9%) |
| EBITDA (README definition) | 222.7 | 286.8 | 253.1 | 129.2 | 106.7 | 230.6 |
| Adjusted EBITDA (company definition) | 233.0 | 252.0 | 271.0 | 139.0 | 118.0 | 250.0 |
| Adjusted EBITDA margin | 18.4% | 18.8% | 19.4% | 20.0% | 17.3% | 18.1% |
| Add-backs (SBC + transaction + other non-recurring) / Adj. EBITDA | 10.8 / 4.6% | 12.0 / 4.8% | 18.5 / 6.8% | 10.1 / 7.3% | 10.9 / 9.2% | 19.3 / 7.7% |
| Net income | 42.3 | 81.9 | 57.1 | 30.6 | 11.6 | 38.1 |
| Operating cash flow | 163.5 | 169.2 | 185.1 | 77.5 | 79.5 | 187.1 |
| Total capex incl. capitalized software | 130.0 | 247.3 | 172.9 | 84.0 | 74.6 | 163.5 |
| Maintenance capex (% of revenue) | 52.0 (4.1%) | 44.3 (3.3%) | 34.9 (2.5%) | 18.0 (2.6%) | 15.6 (2.3%) | 32.5 (2.3%) |
| FCF (OCF less total capex) | 33.5 | -78.1 | 12.2 | -6.5 | 4.9 | 23.6 |
| OCF / Adjusted EBITDA | 70.2% | 67.1% | 68.3% | 55.8% | 67.4% | 74.8% |
| DSO (days) | 48.5 | 47.9 | 48.0 | n/a | 48.5 (annualized H1) | 47.7 |
| Net debt (period end) | 1,044.0 | 967.1 | 1,100.9 | n/a | 1,118.0 | 1,118.0 |
| Net debt / Adjusted EBITDA | 4.48x | 3.84x | 4.06x | n/a | n/a | 4.47x |
| Net debt / EBITDA | 4.69x | 3.37x (4.02x ex gain) | 4.35x | n/a | n/a | 4.85x |
| Adjusted EBITDA / interest | 3.70x | 3.60x | 3.76x | 3.81x | 3.15x | 3.42x |
| Revolver drawn (period end) | 41.5 | 4.1 | 70.4 | n/a | 95.0 | 95.0 |
| Warehouse economic occupancy | 87.4% | 87.0% | 85.6% | n/a | 81.4% | n/a |
| Revenue per occupied pallet (US$, annualized) | 776 | 823 | 815 | n/a | 784 | n/a |
| Transportation operating ratio | 92.9% | 93.2% | 94.0% | n/a | 96.4% | n/a |
| DOT accidents per million miles | 0.66 | 0.68 | 0.72 | n/a | 0.84 | n/a |
| Insurance and claims accrual rate | 6.4% | 6.5% | 6.5% | n/a | 4.8% | n/a |
| Top customer / top 10 share | n/a | 5.5% / 33.7% | 5.7% / 34.3% | n/a | n/a | n/a |
| Employees / active customers | 5,980 / 1,240 | 6,050 / 1,265 | 6,610 / 1,310 | n/a | 6,540 / 1,295 | n/a |

**How the LTM column and ratios are built:**
- LTM = FY2025 - H1 2025 + H1 2026. For example, LTM operating cash flow = 185.1 - 77.5 + 79.5 = 187.1, and LTM operating income = 146.5 - 76.4 + 53.1 = 123.2.
- Net debt = revolver + current term loan + non-current term loan + finance leases - cash:
  - FY2023: 41.5 + 15.0 + 985.0 + 64.0 - 61.5 = 1,044.0
  - FY2024: 4.1 + 15.0 + 970.0 + 70.0 - 92.0 = 967.1
  - FY2025: 70.4 + 25.0 + 1,007.5 + 79.0 - 81.0 = 1,100.9
  - June 2026: 95.0 + 25.0 + 995.0 + 77.0 - 74.0 = 1,118.0
- DSO = accounts receivable / revenue x 365:
  - FY2023: 168.0 / 1,265.0 x 365 = 48.5
  - FY2024: 176.0 / 1,342.0 x 365 = 47.9
  - FY2025: 184.0 / 1,398.0 x 365 = 48.0
  - LTM: 181.0 / 1,384.8 x 365 = 47.7

### Findings

#### FIN-01: The $250.0m LTM Adjusted EBITDA rebuilds exactly from the source
- **Finding:** The deal brief's $250.0m base and every component and subtotal of the company's reconciliation recompute without error. The issues are with quality, not arithmetic (FIN-02 to FIN-08).
- **Evidence:**
  - FY2025: EBITDA = 57.1 + 18.0 + 72.0 + 106.0 = 253.1. Adjusted EBITDA = 253.1 - 0.6 + 12.0 + 3.2 + 3.3 = 271.0.
  - H1 2025: EBITDA = 30.6 + 9.6 + 36.5 + 52.5 = 129.2. Adjusted EBITDA = 129.2 - 0.3 + 6.0 + 2.6 + 1.5 = 139.0.
  - H1 2026: EBITDA = 11.6 + 3.6 + 37.5 + 54.0 = 106.7. Adjusted EBITDA = 106.7 + 0.4 + 6.5 + 1.4 + 3.0 = 118.0.
  - LTM = 271.0 - 139.0 + 118.0 = 250.0.
  - Component check: 230.6 + 0.1 + 12.5 + 2.0 + 4.8 = 250.0.
  - Cross-foot from operating income for H1 2026: 53.1 + 54.0 + 6.5 + 1.4 + 3.0 = 118.0.
  - Other non-recurring detail: severance 2.6 + integration 2.2 = 4.8.
- **Source:** `targets/avocet/data/financials/adjusted_ebitda_reconciliation.csv` rows 2 to 13; `income_statement.csv` rows 5 to 15
- **Severity:** Low
- **Confidence:** High. Directly recomputed.
- **Deal impact:** Valuation (none from arithmetic).
- **Cross-check:** The non-GAAP reconciliations in the FY2025 10-K and the Q2 2026 10-Q.

#### FIN-02: H1 2026 Adjusted EBITDA is down 15.1%; the annualized fall of $42.0m is worth $462.0m at 11.0x
- **Finding:** Adjusted EBITDA fell from 139.0 to 118.0 (down 21.0, -15.1%). The margin fell from 20.0% to 17.3% and gross margin from 28.6% to 26.2%. Critical test (more than 10% of value): 42.0 x 11.0 = 462.0, which is 16.8% of $2,750.0m (projection).
- **Evidence:**
  - Bridge from H1 2025 to H1 2026, which reconciles to -21.0:
    - revenue: -13.2 (694.0 to 680.8)
    - cost of revenue: up 6.9 (495.3 to 502.2), even though revenue fell
    - SG&A: up 1.7 (69.8 to 71.5)
    - add-backs: up 0.8 (10.1 to 10.9)
    - total: -13.2 - 6.9 - 1.7 + 0.8 = -21.0
  - Operating income fell from 76.4 to 53.1 (-30.5%). Net income fell from 30.6 to 11.6 (-62.1%).
  - Annualized fall: 21.0 x 2 = 42.0. At 11.0x: 42.0 x 11.0 = 462.0, which is 462.0 / 2,750.0 = 16.8%.
  - Context: the LTM already contains half of this fall. Measured against the deal base:
    - H1 2026 x 2 = 236.0, which is 14.0 below 250.0. That is 154.0 at 11.0x (5.6%).
    - FY2026 at FY2025 seasonality: H1 share 139.0 / 271.0 = 51.3%, so 118.0 / 0.5129 = 230.1. That is 19.9 below the base, or 218.9 at 11.0x (8.0%) (projection).
- **Source:** `income_statement.csv` rows 5 to 10 and 15 (H1_2025, H1_2026); `adjusted_ebitda_reconciliation.csv` rows 11 and 14
- **Severity:** Critical. Test met: changes value by more than 10%, at $462.0m against a $275.0m threshold (projection).
- **Confidence:** Medium. The fall is computed directly from unaudited H1 data. Annualizing and valuing it are projections. H1 has been 48.5% to 49.6% of annual revenue, so annualizing H1 is seasonally conservative.
- **Deal impact:** Valuation.
- **Cross-check:** The Q2 2026 10-Q MD&A. Q3 2026 results, if already published (quarter ended September 30, 2026). Guidance in news. Any customer losses or price cuts reported in news.

#### FIN-03: Normalized LTM and run-rate earnings imply $51.7m to $310.2m less value at 11.0x (projection)
- **Finding:** Normalizing only the items my files support lowers LTM to 245.3. On H1 2026 run-rate earnings, the value at the deal multiple falls 8.9% to 11.3% below $2,750.0m. My files show no separate gain, credit, settlement or one-off contract income inside the LTM. The non-recurring benefit I can identify is the insurance accrual cut (FIN-04). Two other candidates I cannot size from my files are minimum-volume commitment billings, which are included in occupancy (FIN-12), and the flat-price power contract (FIN-17). My files show no probable but unrecorded cost, and the lead gave me none to apply.
- **Evidence:**

| Line | LTM Jun-26 | H1 2026 x 2 | FY2026E (H1 share 51.3%) |
|---|---|---|---|
| Reported Adjusted EBITDA | 250.0 | 236.0 | 230.1 |
| Less: insurance accrual at FY2025 rate of 6.5% (FIN-04) | -3.7 | -7.3 | -7.3 |
| Less: recurring severance, FY2022 to FY2025 average (FIN-05) | -1.0 | -1.0 | -1.0 |
| Normalized | 245.3 | 227.7 | 221.8 |
| Value at 11.0x | 2,698.3 | 2,504.7 | 2,439.8 |
| Shortfall vs $2,750.0m | 51.7 (1.9%) | 245.3 (8.9%) | 310.2 (11.3%) |
| Implied $/share ((value - 1,118.0) / 48.0) | 32.92 | 28.89 | 27.54 |

  - Inputs: insurance 214.8 x (6.5% - 4.8%) = 3.65 per half-year, or 7.30 a year. Severance (1.2 + 0.8 + 1.0 + 0.9) / 4 = 0.975.
  - Sensitivity: an accident-scaled accrual (-6.0) plus full LTM severance (-2.6) gives an LTM of 250.0 - 6.0 - 2.6 = 241.4. At 11.0x that is 2,655.4, or 94.6 below the EV (3.4%).
  - The $2,750.0m EV as a multiple of other earnings bases:
    - reported EBITDA of 230.6: 11.93x
    - normalized LTM of 245.3: 11.21x
    - H1 2026 run-rate of 236.0: 11.65x
    - normalized run-rate of 227.7: 12.08x
    - normalized FY2026E of 221.8: 12.40x
  - The peer trading range is 9.5x to 11.5x (deal brief).
  - Unaffected EV = 26.15 x 48.0 + 1,118.0 = 2,373.2, which is 9.49x LTM.
  - SBC (12.5) is not deducted. Deducting it would remove a further 137.5 of value (5.0%).
- **Source:** `adjusted_ebitda_reconciliation.csv` rows 8, 11 and 12; `kpis.csv` rows 12 and 13; `income_statement.csv` row 3; `targets/avocet/data/deal-brief.md` sections 1 and 2
- **Severity:** High. This is a material price impact. The deepest case crosses 10%, but it stacks two projections, so I use FIN-02 for the Critical test and do not double-count.
- **Confidence:** Medium. It depends on the assumed normal accrual rate and on seasonality.
- **Deal impact:** Valuation.
- **Cross-check:** Ask the lead for any one-off revenue, settlement income, credit or unaccrued cost found in SEC filings or court records. I will apply them to this bridge, including their share of revenue and operating income growth.

#### FIN-04: The insurance and claims accrual rate was cut from 6.5% to 4.8% while the accident rate rose 16.7%
- **Finding:** The current-year accrual rate for auto liability and cargo claims fell 1.7 points in H1 2026. Over the same period, recordable accidents per million miles rose from 0.72 to 0.84, and the claims reserve fell 2.4. This added about 3.7 to H1 2026 Adjusted EBITDA. H1 2026 earnings and the June 30, 2026 reserve, which are already-reported interim figures, are at risk of later correction (inference).
- **Evidence:**
  - Accrual rate: 6.4%, 6.5%, 6.5%, 4.8%. Accidents per million miles: 0.66, 0.68, 0.72, 0.84 (0.84 / 0.72 = +16.7%).
  - H1 2026 accrual recorded: 214.8 x 4.8% = 10.3. At the FY2025 rate: 214.8 x 6.5% = 14.0. Gap: 214.8 x 1.7% = 3.65.
  - Accident-scaled rate: 6.5% x 0.84 / 0.72 = 7.58%. Gap: 214.8 x (7.583% - 4.8%) = 6.0.
  - Accrued claims and insurance reserves fell from 46.5 to 44.1. As a share of transportation revenue: 46.5 / 448.0 = 10.4%, falling to 44.1 / 436.8 (LTM) = 10.1%.
  - At the FY2025 rate, the H1 2026 transportation operating ratio would be (0.964 x 214.8 + 3.65) / 214.8 = 98.1%, not the reported 96.4%.
  - Value at 11.0x:
    - LTM effect: 3.65 x 11.0 = 40.2 (1.5% of EV)
    - annualized: 7.30 x 11.0 = 80.3 (2.9%)
    - accident-scaled and annualized: 11.96 x 11.0 = 131.6 (4.8%)
  - Any reserve shortfall is also a debt-like item.
- **Source:** `kpis.csv` rows 11 to 13 (rate definition in README); `income_statement.csv` row 3; `balance_sheet.csv` row 14
- **Severity:** High. It needs a specific protection: an actuarial review before signing, a reserve true-up in the price, or an indemnity.
- **Confidence:** Medium. The change and the arithmetic are direct. The right normal rate is an assumption, and a change in the insurance program (for example lower retentions, with premiums recorded elsewhere) could explain part of it.
- **Deal impact:** Valuation and post-closing.
- **Cross-check:** The 10-Q note on insurance retentions and actuarial assumptions and on prior-year development. Auto-liability suits in the litigation docket. Crash reports in the news.

#### FIN-05: Severance and restructuring "non-recurring" costs recur every year
- **Finding:** Severance and restructuring have been added back in every period since FY2022. The H1 2026 amount of 2.1 is the highest on record.
- **Evidence:**
  - By period: 1.2, 0.8, 1.0, 0.9, then 2.1 in H1 2026. LTM: 0.9 - 0.4 + 2.1 = 2.6, which is 2.6 / 250.0 = 1.0% of Adjusted EBITDA.
  - Four-year average: 0.975. At 11.0x: 10.7 of value. The full LTM amount is 28.6 (1.0% of EV).
- **Source:** `adjusted_ebitda_reconciliation.csv` row 12
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Valuation (minor).
- **Cross-check:** 10-K restructuring note. Ask management what the H1 2026 program covered.

#### FIN-06: Transaction-related costs of $1.4m in H1 2026 predate the announced strategic review
- **Finding:** H1 2026 includes 1.4 of transaction-related add-backs, but the strategic review was announced on September 22, 2026, after the period. The nature of the cost is not explained.
- **Evidence:**
  - FY2025: 3.2 (H1 2025 2.6, H2 2025 0.6). H1 2026: 1.4. LTM: 3.2 - 2.6 + 1.4 = 2.0.
  - At 11.0x: 22.0 (0.8% of EV).
- **Source:** `adjusted_ebitda_reconciliation.csv` row 9; `deal-brief.md` section 1
- **Severity:** Low
- **Confidence:** Medium. The amount is direct; its nature is unknown.
- **Deal impact:** Valuation (minor).
- **Cross-check:** 10-Q non-GAAP footnote. Whether advisers were engaged before September 2026 (news, proxy background section).

#### FIN-07: The acquisition integration add-back is declining and tied to the 2025 acquisition
- **Finding:** Integration costs relate to the $88.0m acquisition in H1 2025. They are still being added back about a year after the acquisition, but they are falling.
- **Evidence:**
  - FY2025: 2.4 (H1 2025 1.1). H1 2026: 0.9. LTM: 2.2. Acquisition cash outflow: 88.0 in H1 2025.
  - At 11.0x: 2.2 x 11.0 = 24.2 (0.9% of EV).
- **Source:** `adjusted_ebitda_reconciliation.csv` row 13; `cash_flow.csv` row 12
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Valuation (minor).
- **Cross-check:** 10-K acquisition note (closing date, integration program end date).

#### FIN-08: Share-based compensation add-back
- **Finding:** SBC of 12.5 in the LTM is a standard add-back under the company's definition. It is cashed out at closing (FIN-35), but replacement pay for retained staff is not in my files.
- **Evidence:**
  - LTM SBC: 12.0 - 6.0 + 6.5 = 12.5, which is 5.0% of 250.0.
  - Deducting it would lower value by 12.5 x 11.0 = 137.5 (5.0% of EV).
- **Source:** `adjusted_ebitda_reconciliation.csv` row 8
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Valuation (methodology choice).
- **Cross-check:** Peer definitions of Adjusted EBITDA in the 10-K.

#### FIN-09: The November 2024 sale-leaseback gain is correctly excluded from Adjusted EBITDA
- **Finding:** The $46.0m gain is in FY2024 other income. It is removed in the Adjusted EBITDA reconciliation and in operating cash flow, and it is outside the LTM. This risk is neutralized by the accounting treatment.
- **Evidence:**
  - FY2024 other income of 46.8 includes the 46.0 gain. The reconciliation deducts 46.8, so FY2024 Adjusted EBITDA is 252.0.
  - Cash flow: the gain is removed (-46.0) and the proceeds of 214.0 are in investing activities. Book value of the assets sold = 214.0 - 46.0 = 168.0.
- **Source:** `income_statement.csv` row 12; `adjusted_ebitda_reconciliation.csv` row 7; `cash_flow.csv` rows 5 and 13; README
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None.
- **Cross-check:** 10-K sale-leaseback note (sites, lease term). See FIN-24 and FIN-25.

#### FIN-10: Revenue growth turned negative, and Q3 2025 breaks the trend
- **Finding:** Year-over-year quarterly growth slowed from about 6% to 7% to -2.3% by Q2 2026. Q3 2025 was the first quarter that broke the usual seasonal pattern, and it did so while including the 2025 acquisition, so organic growth is weaker than reported (inference, FIN-11).
- **Evidence:**
  - Year-over-year growth by quarter:
    - 2023 quarters: 7.2%, 7.2%, 7.2%, 7.2%
    - 2024 quarters: 6.1%, 6.1%, 6.1%, 6.1%
    - Q1 2025: 341.2 / 319.4 = 6.8%
    - Q2 2025: 352.8 / 331.5 = 6.4%
    - Q3 2025: 351.6 / 342.2 = 2.7%
    - Q4 2025: 352.4 / 348.9 = 1.0%
    - Q1 2026: 336.0 / 341.2 = -1.5%
    - Q2 2026: 344.8 / 352.8 = -2.3%
  - Q2 to Q3 sequential growth was +3.2% in 2022, 2023 and 2024 (for example 342.2 / 331.5), but -0.3% in 2025 (351.6 / 352.8).
  - H1 2026 vs H1 2025: 680.8 vs 694.0 (-13.2, -1.9%). By segment:
    - Warehousing: -13.6 (-3.6%)
    - Transportation: -11.2 (-5.0%)
    - VAS: +11.6 (+13.2%)
  - Annual growth: 7.2%, 6.1%, 4.2%.
- **Source:** `revenue_quarterly.csv` rows 2 to 19; `income_statement.csv` rows 2 to 5
- **Severity:** High
- **Confidence:** High for the trend. Medium for the organic point.
- **Deal impact:** Valuation.
- **Cross-check:** 10-Q MD&A volume and price commentary. Q3 2026 results. Customer loss news.

#### FIN-11: The 2025 acquisition masks organic decline, and acquired revenue is not disclosed in my files
- **Finding:** H1 2026 contains six months of the acquired warehouses and H1 2025 about one month (inference), so the reported -1.9% overstates organic performance. The acquired revenue is not in my files.
- **Evidence:**
  - Acquisition: 88.0 (H1 2025).
  - Balance sheet and KPI changes in 2025:
    - goodwill: 212.0 to 251.0
    - intangibles: 84.0 to 105.0
    - warehouses: 17 to 19
    - pallet positions: 1,032k to 1,148k (+116k)
    - employees: 6,050 to 6,610
  - Average positions of 1,101k imply the added positions were held for (1,101 - 1,032) / 116 = 59% of 2025, which fits an addition around the end of May 2025 (inference).
  - Illustration only: if the 116k positions ran at H1 2026 company averages, they would contribute 116 x 81.4% x 784 / 2 = 37.0 of H1 2026 warehousing revenue (inference, assumes no organic capacity added).
- **Source:** `cash_flow.csv` row 12; `balance_sheet.csv` rows 8 and 9; `kpis.csv` rows 2 to 6 and 23
- **Severity:** Medium
- **Confidence:** Low for size, Medium for direction. The estimate rests on assumptions.
- **Deal impact:** Valuation.
- **Cross-check:** 10-K business combination note (closing date, acquired revenue and earnings since acquisition, pro forma figures).

#### FIN-12: Warehousing occupancy fell 4.2 points and revenue per occupied pallet fell 3.8%
- **Finding:** The core segment is losing both volume and price. Occupied positions fell even after capacity grew. Occupancy counts contractual minimum-volume commitments, so physical use may be lower still.
- **Evidence:**
  - Occupancy: 87.4%, 87.0%, 85.6%, 81.4%. Rate per occupied pallet: $776, $823, $815, $784.
  - Occupied positions: 1,101 x 85.6% = 942.5k in FY2025, against 1,148 x 81.4% = 934.5k in H1 2026.
  - Bridge from FY2025 (768.1) to H1 2026 annualized (732.6), total -35.5:
    - capacity: 47 x 85.6% x 815 = +32.8
    - occupancy: 1,148 x -4.2% x 815 = -39.3
    - rate: 934.5 x -31 = -29.0
  - Throughput: 8.31m pallets in FY2025, against 3.94m in H1 2026 (annualized 7.88m, -5.2%).
  - Turns per average position: 7.55 in FY2025, against 6.86 in H1 2026.
- **Source:** `kpis.csv` rows 3 to 7; README occupancy definition; `income_statement.csv` row 2
- **Severity:** High
- **Confidence:** High for the KPIs. Medium for annualized comparisons, because of seasonality.
- **Deal impact:** Valuation.
- **Cross-check:** Customer exits in the news. Expiring minimum-volume commitments (contracts in SEC exhibits).

#### FIN-13: Transportation volume is falling and its operating ratio is near breakeven
- **Finding:** Loaded miles and tractor use are falling, and the segment margin has narrowed to 3.6% (1.9% before the accrual benefit in FIN-04).
- **Evidence:**
  - Loaded miles: 152.0, 151.0, 146.0, then 69.5 in H1 2026 (annualized 139.0, -4.8%).
  - Revenue per loaded mile: $3.068 to $3.091.
  - Bridge from FY2025 (448.0) to H1 2026 annualized (429.6): miles -21.5, rate +3.2.
  - Operating ratio: 92.9%, 93.2%, 94.0%, 96.4%. Segment operating income: 448.0 x 6.0% = 26.9 in FY2025, against 214.8 x 3.6% = 7.7 in H1 2026 (annualized 15.5).
  - Loaded miles per tractor: 105.8k in FY2025, against 101.3k annualized in H1 2026.
- **Source:** `kpis.csv` rows 9 to 11 and 14; `income_statement.csv` row 3
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation and integration.
- **Cross-check:** 10-Q segment note.

#### FIN-14: DOT recordable accidents per million miles are up 16.7% in six months
- **Finding:** The accident rate rose from 0.72 to 0.84, and is up 27.3% since FY2023 (0.66). This raises liability exposure for a fleet the buyer plans to combine with its own. It also undermines the lower accrual in FIN-04.
- **Evidence:** 0.66, 0.68, 0.72, 0.84. 0.84 / 0.72 = 1.167; 0.84 / 0.66 = 1.273.
- **Source:** `kpis.csv` row 12
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Post-closing.
- **Cross-check:** FMCSA safety data. The auto-liability litigation docket. Crash news.

#### FIN-15: Value-added services are still growing
- **Finding:** VAS is the only segment still growing, although growth is slowing.
- **Evidence:**
  - Revenue: 110.0, 130.0, 155.0, 182.0. H1 2026: 88.0 to 99.6 (+13.2%), down from +17.4%.
  - VAS was 99.6 / 680.8 = 14.6% of H1 2026 revenue.
- **Source:** `income_statement.csv` row 4; `kpis.csv` row 8
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Valuation (positive).
- **Cross-check:** 10-Q MD&A.

#### FIN-16: Most-favored-customer pricing covers a rising share of warehousing revenue while rates fall
- **Finding:** 23% of warehousing revenue sits under most-favored-customer (MFC) clauses. A price cut to one customer could spread to the others, and repricing or moving customers after closing may trigger these clauses (inference).
- **Evidence:**
  - MFC share: 21%, 22%, 22%, 23%. In H1 2026: 366.4 x 23% = 84.3 (annualized 168.5).
  - Each 1% concession costs 1.7 a year, or 18.5 at 11.0x (0.7% of EV).
  - The rate per occupied pallet fell 3.8% (FIN-12).
- **Source:** `kpis.csv` rows 6 and 21
- **Severity:** Medium
- **Confidence:** Medium
- **Deal impact:** Valuation and integration.
- **Cross-check:** Customer contracts and MFC triggers in SEC exhibits or the data room.

#### FIN-17: Electricity is 70% fixed at a flat $61.0/MWh in every period; expiry is not in my files
- **Finding:** A flat fixed price over four periods points to a single long-term agreement. If it reprices, earnings fall.
- **Evidence:**
  - Fixed share: 71%, 70%, 70%, 70%. Price: $61.0/MWh in every period.
  - FY2025 fixed volume: 589 x 70% = 412.3 GWh. Cost: 412.3 x 61 = 25.2.
  - Each +$10/MWh costs 4.1 a year, or 45.4 at 11.0x (1.7% of EV).
  - Break-even rise per MWh: +$30.3 (to $91.3) to cost 5% of EV, and +$60.6 (to $121.6) to cost 10%.
- **Source:** `kpis.csv` rows 18 to 20
- **Severity:** Medium
- **Confidence:** Medium. The contract term and market price are not in my files.
- **Deal impact:** Valuation (from the expiry date).
- **Cross-check:** The supply agreement and its term in the 10-K. Regional power price news.

#### FIN-18: Maintenance capex fell to 2.3% of revenue while refrigeration systems aged
- **Finding:** Maintenance capex is down by more than a third while seven of 19 warehouses run ammonia systems older than 25 years. That suggests deferred spending that a buyer will have to fund (inference).
- **Evidence:**
  - Maintenance capex: 52.0, 44.3, 34.9, then 15.6 in H1 2026 (LTM 32.5). As a share of revenue: 4.1%, 3.3%, 2.5%, 2.3%.
  - Average age of refrigeration systems: 18.2 to 20.4 years.
  - Warehouses with ammonia systems older than 25 years: 4, 5, 7, 7.
  - Maintenance capex covers 50.0%, 40.6%, 32.9% and 28.9% of D&A.
  - H1 2026 PP&E depreciation is about 44.0 (inference): 54.0 - 7.0 intangible amortization (105.0 - 98.0) - 3.0 software amortization (39.0 + 11.0 - 47.0). The PP&E roll-forward ties: 1,498.2 + 15.6 + 48.0 + 6.5 finance lease additions - 44.0 = 1,524.3. Maintenance capex is therefore about 35% of PP&E depreciation.
  - Shortfall against the FY2023 rate of 4.1% (inference): FY2024 10.7 + FY2025 22.4 + H1 2026 12.3 = 45.5 (1.7% of EV), a candidate debt-like item.
  - Ongoing gap: 1,384.8 x 4.1% - 32.5 = 24.3 a year.
- **Source:** `cash_flow.csv` rows 9 to 11; `kpis.csv` rows 15 to 17; `balance_sheet.csv` rows 5, 7, 9 and 18
- **Severity:** Medium
- **Confidence:** Medium. The normal rate is an assumption.
- **Deal impact:** Valuation and post-closing.
- **Cross-check:** EPA risk management program and OSHA process safety records for ammonia. News of leaks. Engineering due diligence.

#### FIN-19: $48.0m of H1 2026 growth capex added no capacity
- **Finding:** Growth capex continued while pallet positions and warehouse count were flat. This raises a question about the company's internal capex classification. If some sustaining spend is labeled as growth, FIN-18 is understated (inference). The spend could also be construction in progress.
- **Evidence:**
  - Growth capex: 68.0, 190.0, 120.0, 48.0. That is 358.0 since FY2024.
  - Positions: +12k in FY2024; +116k in FY2025 (with the acquisition); 0 in H1 2026 (1,148k to 1,148k, 19 warehouses).
- **Source:** `cash_flow.csv` row 10; `kpis.csv` rows 2 and 3; README (internal classification)
- **Severity:** Medium
- **Confidence:** Low to Medium
- **Deal impact:** Valuation.
- **Cross-check:** 10-K capex and construction-in-progress disclosure. Project list from management.

#### FIN-20: $47.0m of capitalized ColdTrack software would be stranded by the integration plan
- **Finding:** The integration plan halts the ColdTrack rollout, which is live at 3 of 19 sites. The asset would have little use to the buyer (inference, non-cash). Capitalizing 21.0 a year of development also supports EBITDA.
- **Evidence:**
  - Capitalized software: 14.0, 24.5, 39.0, 47.0. Annual development spend: 10.0, 13.0, 18.0, 11.0.
  - LTM spend: 21.0, which is 8.4% of LTM Adjusted EBITDA.
  - Sites live: 0, 0, 1, 3.
- **Source:** `balance_sheet.csv` row 7; `cash_flow.csv` row 11; `kpis.csv` row 22; `deal-brief.md` section 5
- **Severity:** Low
- **Confidence:** Medium
- **Deal impact:** Post-closing (non-cash). Future capex of about 21.0 a year would be avoided.
- **Cross-check:** Software capitalization policy in the 10-K.

#### FIN-21: The deal brief's net debt of $1,118.0m ties to the June 30, 2026 balance sheet
- **Finding:** Every component of the brief's net debt matches the balance sheet, and every debt roll-forward ties.
- **Evidence:**
  - 95.0 + 25.0 + 995.0 + 77.0 - 74.0 = 1,118.0.
  - Revolver: 70.4 + 24.6 = 95.0.
  - Term loans: 1,032.5 - 12.5 = 1,020.0.
  - Finance leases: 79.0 - 8.5 + 6.5 implied additions = 77.0.
  - Cash: 81.0 - 7.0 = 74.0.
  - Debt is shown at principal (README).
- **Source:** `balance_sheet.csv` rows 2 and 15 to 18; `cash_flow.csv` rows 15 to 18 and 22 to 24
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None.
- **Cross-check:** 10-Q debt note.

#### FIN-22: Leverage rose to 4.47x in six months, and interest cover is falling
- **Finding:** Leverage on company Adjusted EBITDA rose from 4.06x to 4.47x as earnings fell and the revolver grew. On run-rate earnings it reaches 4.74x to 4.91x. The covenant level, facility size and maturities are not in my files. Repayment at closing would cure a covenant problem, but a breach before closing would be Critical under the calibration rule.
- **Evidence:**
  - Net debt / Adjusted EBITDA: 4.48x, 3.84x, 4.06x, 4.47x. On EBITDA, LTM: 1,118.0 / 230.6 = 4.85x.
  - At constant net debt: 1,118.0 / 236.0 = 4.74x, and 1,118.0 / 227.7 = 4.91x.
  - Adjusted EBITDA / interest: LTM 3.42x; H1 2026 118.0 / 37.5 = 3.15x.
  - Operating income / interest: LTM 123.2 / 73.0 = 1.69x; H1 2026 1.42x.
  - Revolver drawn: 4.1, 70.4, 95.0.
- **Source:** `balance_sheet.csv` rows 2 and 15 to 18; `adjusted_ebitda_reconciliation.csv` rows 4, 6 and 11; `income_statement.csv` rows 10 and 11
- **Severity:** Medium
- **Confidence:** High for the ratios. The covenant is unknown.
- **Deal impact:** Financing and closing risk.
- **Cross-check:** The credit agreement covenant definition and level (10-K exhibit). Please send it and I will compute headroom.

#### FIN-23: Share buybacks continued while the revolver funded the shortfall
- **Finding:** The company bought back shares in H1 2026 while free cash flow after finance leases was negative and it borrowed on the revolver.
- **Evidence:**
  - Buybacks: 35.0 (FY2024), 30.0 (FY2025), 14.0 (H1 2026), so LTM 44.0.
  - H1 2026 FCF after finance lease principal: 4.9 - 8.5 = -3.6. Revolver draw: 24.6.
- **Source:** `cash_flow.csv` rows 15, 18 and 19
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Financing (minor).
- **Cross-check:** Board buyback authorization (10-Q).

#### FIN-24: Operating lease liabilities of $668.0m sit outside net debt, consistent with the EBITDA definition
- **Finding:** Lease cost is deducted in Adjusted EBITDA, so leaving lease liabilities out of net debt is consistent. The liability rose about 185 in FY2024, which coincides with the sale-leaseback (inference), and rose again in H1 2026 while capacity was flat.
- **Evidence:**
  - Lease liabilities: 455.0, 640.0, 652.0, 668.0. Right-of-use assets: 438.0, 618.0, 627.0, 641.0.
  - 668.0 is 24.3% of EV.
- **Source:** `balance_sheet.csv` rows 6 and 19; README
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None on method.
- **Cross-check:** 10-K lease note.

#### FIN-25: The integration budget has no cost for surrendering four leased warehouses
- **Finding:** The $45.0m one-time cost lists product moves, racking, IT migration and severance, with no lease exit cost for Puyallup Junction, Kent Valley, Stockton North and Lodi. The liabilities for each site are not in my files.
- **Evidence:**
  - Total operating lease liabilities: 668.0. The four sites are 4 / 19 = 21% of warehouses.
  - Break-even: remaining obligations of 137.5 (20.6% of 668.0) would cost 5% of EV, and 275.0 (41.2%) would cost 10%.
- **Source:** `balance_sheet.csv` row 19; `deal-brief.md` section 5
- **Severity:** Medium. Raise to High if SEC filings show long remaining terms or no termination right for these sites, for example if they were in the 2024 sale-leaseback.
- **Confidence:** Medium
- **Deal impact:** Valuation and post-closing.
- **Cross-check:** 10-K lease and sale-leaseback notes (sites, term, renewal and termination rights).

#### FIN-26: Other debt-like items outside the deal's net debt
- **Finding:** Several liabilities may be debt-like but are not in the $1,118.0m. The balance sheet also shows no pension, multiemployer withdrawal or asset retirement line.
- **Evidence:**
  - Accrued claims reserves: 44.1 (1.6% of EV).
  - Other non-current liabilities: 25.5, composition unknown.
  - Deferred maintenance: 45.5 (FIN-18).
  - Together, 115.1 (4.2% of EV) (inference).
  - Deferred taxes of 102.5 are normally not debt-like.
  - There are 4,560 hourly warehouse employees, and the integration plan closes four sites. Any multiemployer plan withdrawal liability would sit off the balance sheet.
  - The change-in-control severance plan (September 2026) is not accrued at June 30.
- **Source:** `balance_sheet.csv` rows 14, 20 and 21; `kpis.csv` row 24; `deal-brief.md` section 4
- **Severity:** Medium
- **Confidence:** Medium
- **Deal impact:** Valuation (net debt definition).
- **Cross-check:** 10-K pension and multiemployer note, asset retirement obligations, and collective bargaining.

#### FIN-27: Customer concentration is low and stable
- **Finding:** No customer exceeds 5.7% of revenue, and the top-10 share barely moved. This is a positive point.
- **Evidence:**

| FY2025 rank | Customer | FY2024 | FY2025 | Change |
|---|---|---|---|---|
| 1 | Northwind Harvest Foods | 74.2 (5.5%) | 79.6 (5.7%) | +5.4 (+7.3%) |
| 2 | Bellcrest Dairy Cooperative | 61.0 (4.5%) | 64.8 (4.6%) | +3.8 (+6.2%) |
| 3 | Pacific Tidewater Seafood | 52.3 (3.9%) | 55.1 (3.9%) | +2.8 (+5.4%) |
| 4 | Sunvale Frozen Foods | 49.8 (3.7%) | 51.4 (3.7%) | +1.6 (+3.2%) |
| 5 | Granite Peak Grocers | 43.5 (3.2%) | 46.2 (3.3%) | +2.7 (+6.2%) |
| 6 | Orchard Lane Produce | 38.9 (2.9%) | 41.7 (3.0%) | +2.8 (+7.2%) |
| 7 | Meridale Meats | 37.6 (2.8%) | 39.0 (2.8%) | +1.4 (+3.7%) |
| 8 | Cascadia Bakeries | 33.0 (2.5%) | 35.9 (2.6%) | +2.9 (+8.8%) |
| 9 | Alder BioPharma Distribution | 28.4 (2.1%) | 33.6 (2.4%) | +5.2 (+18.3%) |
| 10 | FreshArc Distributors, Inc. | 34.1 (2.5%) | 31.8 (2.3%) | -2.3 (-6.7%) |
| | Top 10 | 452.8 (33.7%) | 479.1 (34.3%) | +26.3 (+5.8%) |
| | All other (includes acquired customers) | 889.2 | 918.9 | +29.7 (+3.3%) |

  - Top 5 share: 280.8 / 1,342.0 = 20.9%, rising to 297.1 / 1,398.0 = 21.3%.
- **Source:** `revenue_by_customer.csv` rows 2 to 13
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Valuation (positive).
- **Cross-check:** Look up every party named in news and litigation against this list. My files have no customer data for H1 2026.

#### FIN-28: FreshArc Distributors is the only top-10 customer whose revenue fell
- **Finding:** FreshArc's revenue fell 2.3 (-6.7%). By FY2024 revenue it ranked 8th; by FY2025 it ranked 10th.
- **Evidence:** 34.1 to 31.8. In FY2024 it was ahead of Cascadia (33.0) and Alder (28.4).
- **Source:** `revenue_by_customer.csv` row 11
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Valuation (minor).
- **Cross-check:** News and the litigation docket for any dispute, insolvency or contract loss involving FreshArc.

#### FIN-29: Alder BioPharma Distribution grew 18.3%
- **Finding:** Alder is the fastest-growing top-10 customer (pharma cold chain). It moved from 10th to 9th among the listed customers.
- **Evidence:** 28.4 to 33.6 (+5.2).
- **Source:** `revenue_by_customer.csv` row 10
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None.
- **Cross-check:** Contract term and any change-of-control clause.

#### FIN-30: Active customers fell in H1 2026, and there is no retention data
- **Finding:** Active customers fell for the first time in the data. My files have no churn, retention or backlog figures to test growth against.
- **Evidence:** 1,240, 1,265, 1,310, then 1,295 in H1 2026 (-15, -1.1%).
- **Source:** `kpis.csv` row 25
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Valuation.
- **Cross-check:** Management churn data. News of lost accounts.

#### FIN-31: Cash conversion has held steady
- **Finding:** Operating cash flow conversion has been stable at roughly 67% to 75% of Adjusted EBITDA.
- **Evidence:**
  - OCF / Adjusted EBITDA: 70.2%, 67.1%, 68.3%, LTM 74.8%.
  - OCF / EBITDA: 73.4%; 59.0% (70.3% excluding the gain); 73.1%; LTM 187.1 / 230.6 = 81.1%.
  - OCF / net income: 3.87x, 2.07x, 3.24x, and 6.85x in H1 2026 (because net income was low).
- **Source:** `cash_flow.csv` row 8; `adjusted_ebitda_reconciliation.csv` rows 6 and 11
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None (positive).
- **Cross-check:** 10-Q cash flow statement.

#### FIN-32: Free cash flow is thin once all capex and finance leases are paid
- **Finding:** After all capex and finance lease principal, free cash flow has been near zero or negative. Buybacks and the acquisition were funded by the sale-leaseback proceeds and by debt.
- **Evidence:**
  - OCF less total capex: 33.5, -78.1, 12.2, LTM 23.6.
  - Less finance lease principal: 19.5, -93.1, -3.8, LTM 23.6 - 16.5 = 7.1.
  - Uses of cash: buybacks of 44.0 LTM; acquisition of 88.0; sale-leaseback inflow of 214.0 in FY2024.
- **Source:** `cash_flow.csv` rows 8 to 13, 18 and 19
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation and financing.
- **Cross-check:** 10-K liquidity section.

#### FIN-33: A working capital inflow held H1 2026 operating cash flow flat
- **Finding:** Net income fell 19.0, but operating cash flow rose 2.0 (77.5 to 79.5). The difference is an 18.5 swing in working capital (+5.9 against -12.6).
- **Evidence:** Mapping from the balance sheet (inference): receivables +3.0, prepaid -2.0, payables +3.0, accrued +2.3, claims reserve -2.4, lease liability growth net of right-of-use assets +2.0. Total 5.9.
- **Source:** `cash_flow.csv` row 7; `balance_sheet.csv` rows 3, 4, 6 and 12 to 19
- **Severity:** Low
- **Confidence:** Medium
- **Deal impact:** None.
- **Cross-check:** 10-Q cash flow detail.

#### FIN-34: DSO is stable at about 48 days
- **Finding:** Receivable days have been steady for three years. There is no inventory or contract asset line. The allowance for credit losses is not disclosed, because receivables are shown net.
- **Evidence:** 48.5, 47.9, 48.0, and 47.7 on an LTM basis.
- **Source:** `balance_sheet.csv` row 3; `income_statement.csv` row 5
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None.
- **Cross-check:** Allowance roll-forward in the 10-K.

#### FIN-35: The equity award cash-out recomputes to $46.2m
- **Finding:** The brief's cash-out is correct on its own assumptions. It is a known deal cost of 1.7% of EV, a price item. The weighted-average strike method gives a lower bound if any option is out of the money at $34.00. PSUs are counted at target.
- **Evidence:**
  - RSUs: 860,000 x $34.00 = 29.24.
  - PSUs: 210,000 x $34.00 = 7.14. Each 10% of target paid above 100% adds 0.71.
  - Options: 1,180,000 x (34.00 - 25.68) = 1,180,000 x 8.32 = 9.82.
  - Total: 46.20.
  - Known deal cost total from my files: 46.2 (1.7%). The change-in-control severance amount is not in my files.
  - The reverse termination fee of 110.0 (4.0%) is payable only if the deal fails on antitrust grounds. If the lead counts it, the total is 156.2 (5.7%), which crosses the 5% High threshold. Lead to decide.
  - Fees of 72.0 are a use of funds, not part of this total.
- **Source:** `deal-brief.md` section 3 notes and section 4
- **Severity:** Medium (known deal cost)
- **Confidence:** High
- **Deal impact:** Valuation (price).
- **Cross-check:** 10-Q equity award note (option strike distribution, PSU change-of-control payout terms). Severance plan 8-K.

#### FIN-36: Enterprise value and sources and uses arithmetic tie
- **Finding:** Every figure in the deal brief's price, enterprise value and sources and uses tables recomputes.
- **Evidence:**
  - Equity value: 48.0 x 34.00 = 1,632.0. Premium: 34.00 / 26.15 - 1 = 30.0%.
  - EV: 1,632.0 + 1,118.0 = 2,750.0. Multiple: 2,750.0 / 250.0 = 11.0x.
  - Uses: 1,632.0 + 46.2 + 1,115.0 (95.0 + 1,020.0) + 72.0 = 2,865.2.
  - Sources: 1,900.0 + 600.0 + 365.2 = 2,865.2.
  - Fees: 27.5 + 33.0 + 11.5 = 72.0.
- **Source:** `deal-brief.md` sections 1 and 3; `balance_sheet.csv` rows 15 to 17
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None.
- **Cross-check:** None needed.

#### FIN-37: Sources and uses omit some closing items
- **Finding:** The uses table repays debt at June 30, 2026 balances, but closing is in Q2 to Q3 2027 and the revolver keeps rising. It has no line for change-in-control severance, accrued interest or prepayment costs. Brindlewick's cash of 74.0 is not used as a source, which is conservative.
- **Evidence:** Revolver draws over the LTM: 66.3 - 22.5 + 24.6 = 68.4. All nine executive officers are expected to leave within three months of closing.
- **Source:** `cash_flow.csv` row 15; `deal-brief.md` sections 3 and 4
- **Severity:** Medium
- **Confidence:** Medium
- **Deal impact:** Financing.
- **Cross-check:** Severance plan amounts (8-K or proxy). Credit agreement prepayment terms.

#### FIN-38: Termination fee arithmetic ties
- **Finding:** Both termination fees match their stated percentages.
- **Evidence:** 3.0% x 1,632.0 = 48.96, rounded to 49.0. 4.0% x 2,750.0 = 110.0.
- **Source:** `deal-brief.md` section 4
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None.
- **Cross-check:** None needed.

#### FIN-39: Goodwill and intangibles total $349.0m; the impairment test date is not in my files
- **Finding:** Goodwill and intangibles are 54.4% of book equity. At the entity level, the unaffected market value of equity is about twice book. The H1 earnings fall and the 96.4% transportation operating ratio are indicators to test at the reporting-unit level (inference).
- **Evidence:**
  - Goodwill: 251.0 (+39.0 in 2025). Intangibles: 98.0.
  - (251.0 + 98.0) / 641.9 = 54.4%. Tangible equity: 292.9.
  - Unaffected market value of equity: 26.15 x 48.0 = 1,255.2, which is 1.96x book.
- **Source:** `balance_sheet.csv` rows 8, 9 and 25; `deal-brief.md` section 1
- **Severity:** Low
- **Confidence:** Medium
- **Deal impact:** Post-closing (accounting).
- **Cross-check:** The test date and reporting units in the 10-K. Share price path since the test date in news.

#### FIN-40: Headcount is down 1.1%
- **Finding:** Headcount fell roughly in line with occupied positions (-0.8%).
- **Evidence:**
  - Employees: 6,610 to 6,540. Hourly warehouse staff: 4,610 to 4,560.
  - Revenue per employee: 211.5k in FY2025, against 211.7k on an LTM basis.
- **Source:** `kpis.csv` rows 23 and 24
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None.
- **Cross-check:** Union status and the collective bargaining calendar (10-K).

### Positive or mitigating points

- The arithmetic of the base ties exactly (FIN-01), and so does net debt (FIN-21).
- The sale-leaseback gain is correctly excluded from Adjusted EBITDA (FIN-09).
- Operating lease treatment is consistent with the EBITDA definition (FIN-24).
- Value-added services are still growing at 13.2% (FIN-15).
- Customer concentration is low and stable (top customer 5.7%, top 10 34.3%) (FIN-27).
- Cash conversion is steady at 67% to 75% of Adjusted EBITDA (FIN-31), and DSO is stable at about 48 days (FIN-34).
- The term loans were refinanced in H1 2025 (1,045.0 new). Maturities are not in my files, and the sources and uses repay them at closing.

### Gaps and questions for management

1. Q3 2026 results and monthly Adjusted EBITDA for 2026, to test the run-rate in FIN-02 and FIN-03.
2. Revenue and EBITDA of the 2025 acquisition by quarter, the closing date, and organic growth (FIN-11).
3. The insurance program: retentions, the latest actuarial report, the reason for the 4.8% rate, reserves by accident year and prior-year development (FIN-04).
4. Physical versus economic occupancy, revenue from minimum-volume commitments, and when those commitments expire (FIN-12).
5. The electricity supply agreement: expiry, renewal terms, and the cost of the 30% bought at market (FIN-17).
6. The MFC clauses: which customers, and what triggers them (FIN-16).
7. The capex plan: replacement schedule and cost for the seven ammonia systems older than 25 years, the capex classification policy, and what the 48.0 of H1 2026 growth capex is for (FIN-18, FIN-19).
8. The lease schedule by site, including remaining liability, term and termination rights for the four sites to be surrendered, and the list of sale-leaseback sites (FIN-25).
9. The credit agreement: revolver size, covenant definition and level, maturities and prepayment terms (FIN-22). If the lead can obtain the covenant, I will compute headroom.
10. The breakdown of other non-current liabilities (25.5), any multiemployer pension participation, and asset retirement obligations (FIN-26).
11. The allowance for credit losses (FIN-34).
12. Change-in-control severance amounts, PSU payout mechanics on a change of control, and the option strike distribution (FIN-35, FIN-37).
13. Customer revenue for H1 2026, churn data, and the status of FreshArc (FIN-28, FIN-30).
14. The nature of the 1.4 of transaction costs in H1 2026 (FIN-06).
15. The goodwill impairment test date, reporting units and headroom (FIN-39).
16. The drivers of the 6.9 increase in cost of revenue in H1 2026 while revenue fell (FIN-02).

**Not possible from my files:**
- software ARR, backlog and retention metrics (not applicable or not provided)
- the allowance for credit losses
- the impairment test date
- the covenant level
- any one-off income or unaccrued liability disclosed only in SEC filings or court records

If the lead supplies these, I can apply them to the FIN-03 bridge.

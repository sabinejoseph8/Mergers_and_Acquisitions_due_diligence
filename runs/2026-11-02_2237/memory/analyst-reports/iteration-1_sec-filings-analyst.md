## SEC filings analyst: findings

### Files reviewed
I read all five files in full, plus the deal brief for context:
- `targets/wren/data/deal-brief.md` (context only)
- `targets/wren/data/sec-filings/MDLS_10-K_FY2025_excerpts.md` (filed Feb 26, 2026)
- `targets/wren/data/sec-filings/MDLS_8-K_2026-02-25_fy2025-results.md` (FY2025 earnings release)
- `targets/wren/data/sec-filings/MDLS_10-Q_Q2-2026_excerpts.md` (filed Aug 6, 2026)
- `targets/wren/data/sec-filings/MDLS_8-K_2026-09-21_merger-agreement.md`
- `targets/wren/data/sec-filings/MDLS_DEFM14A_2026_excerpts.md` (filed Oct 23, 2026)

None of the files contains text that tries to instruct the agents (see SEC-45).

Value bases used throughout: EV is US$2,459.5m, so 10% = US$246.0m. Equity value is US$1,917.3m, so 10% = US$191.7m. Reported stockholders' equity is not found in SEC filings, so I cannot give percentages of book equity.

### Findings

#### SEC-01: LTM Adjusted EBITDA of US$171.2m recomputes from the filings
- **Finding:** The deal brief's LTM base ties to the filings. The FY2025 reconciliation also adds up.
- **Evidence:** FY2025 186.4 - H1 2025 89.9 + H1 2026 74.7 = 171.2. FY2025: 62.9 + 20.4 + 41.6 + 42.8 = 167.7 EBITDA; plus 12.4 + 0.0 + 3.8 + 2.5 = 186.4. Multiples: 2,459.5 / 171.2 = 14.4x and 2,459.5 / 186.4 = 13.2x. LTM net income: 62.9 - 28.8 + 15.7 = 49.8.
- **Source:** `targets/wren/data/sec-filings/MDLS_8-K_2026-02-25_fy2025-results.md`, reconciliation table; `targets/wren/data/sec-filings/MDLS_10-Q_Q2-2026_excerpts.md`, Item 2 "Results for the six months ended June 30"
- **Severity:** Low
- **Confidence:** High. Figures from primary filings, recomputed.
- **Deal impact:** Valuation. The arithmetic is sound. Whether it is a sound base is covered in SEC-02, SEC-04, SEC-07, SEC-09 and SEC-10.
- **Cross-check:** Financial analyst's quarterly data for H2 2025 and H1 2026.

#### SEC-02: Contract-cost amortization period lengthened from 6 to 10 years on a renewal rate that has since fallen
- **Finding:** Effective October 1, 2025, management lengthened the amortization period for capitalized commissions from six to ten years. It justified the change with the FY2024 renewal rate of 92.3%. The trailing renewal rate was already 90.6% when the 10-K was filed and was 86.9% at June 30, 2026. Using management's own sensitivity, the rate now supports a period well below ten years.
- **Evidence:** 10-K: the change "reflects our analysis of customer relationship duration, including our fiscal 2024 renewal rate of 92.3%". Sensitivity: "A one-percentage-point change in the long-run renewal rate would change the estimated period of benefit by about one year." Expense reduced by US$1.7m in Q4 2025 and US$3.4m in H1 2026, so US$5.1m within the LTM; about US$6.8m expected in FY2026. My calculation (inference): 92.3% - 86.9% = 5.4 pts, which implies roughly 10 - 5.4 = about 4.6 years, below even the original six. Balance: US$92.1m (Dec 2025) and US$98.1m (Jun 2026).
- **Source:** `MDLS_10-K_FY2025_excerpts.md`, Item 7 "Critical accounting estimates", Note 4, and "Key operating metrics"; `MDLS_10-Q_Q2-2026_excerpts.md`, Note 5 and Item 2 "Key operating metrics"
- **Severity:** High
- **Confidence:** Medium. The facts are High. Whether the US$5.1m sits inside Adjusted EBITDA is not certain: the expense is "recorded in SG&A", and the filings do not say whether the D&A add-back (US$42.8m) includes it. If it does, EBITDA is unaffected and only net income benefits.
- **Deal impact:** Valuation. If the benefit is in EBITDA, US$5.1m x 14.4 = US$73.4m of EV (3.0%) (inference). The judgment was made as of a date, and later renewal data puts it in doubt. A shorter period would raise future amortization. A prospective estimate change is not a restatement, but the auditor could question the judgment.
- **Cross-check:** Financial analyst: is contract-cost amortization inside D&A in the EBITDA bridge? What was the trailing renewal rate at October 1, 2025?

#### SEC-03: Organic growth definition shortened from 12 to 6 months, which flattered FY2025 organic growth
- **Finding:** Starting in FY2025, Meridale counts acquired revenue as organic after six months instead of twelve. Under the old definition, FY2025 organic growth would have been about 3.3%, not the reported 5.4%. Excluding Pinecrest from both periods, H1 2026 revenue fell about 3.1%, not the 1.0% reported.
- **Evidence:** The definition was changed "from twelve months to six months". Pinecrest revenue after September 3, 2025 was US$20.6m. Reported basis: (1,067.7 - (51.0 - 20.6)) / 984.0 - 1 = 5.4%. Old basis: (1,067.7 - 51.0) / 984.0 - 1 = 3.3%. H1 like-for-like: (510.8 - 30.6) / (516.0 - 20.4) - 1 = 480.2 / 495.6 - 1 = -3.1%. The 8-K says "Organic growth accelerated" and "Prior-year organic growth has not been restated."
- **Source:** `MDLS_10-K_FY2025_excerpts.md`, Item 7 "Fiscal 2025 overview"; `MDLS_8-K_2026-02-25_fy2025-results.md`, footnote (1) and CEO quote; `MDLS_10-Q_Q2-2026_excerpts.md`, Item 2
- **Severity:** Medium
- **Confidence:** High. Recomputed from the filings. The like-for-like figure is my calculation (inference).
- **Deal impact:** Valuation and disclosure. Underlying growth is weaker than the headline.
- **Cross-check:** Financial analyst's revenue by period and acquisition; analyst or news commentary on the definition change.

#### SEC-04: US$4.1m out-of-period error: FY2025 subcontractor costs not accrued
- **Finding:** Internal audit found US$4.1m of FY2025 Southwest modernization subcontractor costs that had not been accrued at December 31, 2025. The company booked them in Q1 2026 cost of revenue and did not revise FY2025, judging the error immaterial under SAB 99.
- **Evidence:** "had not been accrued at December 31, 2025... We recorded the correction, US$4.1 million, in cost of revenue in the first quarter of 2026." My calculations: corrected FY2025 Adjusted EBITDA 186.4 - 4.1 = 182.3 (2.2% lower). The error equals 3.3% of FY2025 operating income of 123.4.
- **Source:** `MDLS_10-Q_Q2-2026_excerpts.md`, Note 2 "Out-of-period adjustment" and Item 2
- **Severity:** Medium
- **Confidence:** High. Primary source.
- **Deal impact:** Valuation. The FY2025 base and the Q1 2026 comparison are both affected. The LTM effect depends on whether the work was in H1 or H2 2025, which is not disclosed. Modernization uses cost-to-cost revenue recognition, yet the correction is described only in cost of revenue, with no revenue adjustment. Whether revenue progress was also misstated is a question for management (inference).
- **Cross-check:** Financial analyst: quarterly gross margin in the Southwest region. Is the 4.1 added back in the 2026 Adjusted EBITDA?

#### SEC-05: Effective-controls conclusion for FY2025 set against the unaccrued subcontractor costs
- **Finding:** Management and the auditor concluded that internal control over financial reporting was effective at December 31, 2025. In the same period, an accrual control failed to capture US$4.1m of costs (SEC-04). After the fact, the company added a quarter-end purchase-order review and moved Southwest accrual approval to the corporate controller. The 10-Q does not classify the gap as a deficiency, a significant deficiency or a material weakness.
- **Evidence:** 10-K Item 9A: ICFR "effective". 10-Q Item 4: "we added a regional review of open subcontractor purchase orders at each quarter-end and moved accrual approval for the Southwest region to the corporate controller."
- **Source:** `MDLS_10-K_FY2025_excerpts.md`, Item 9A and auditor's report; `MDLS_10-Q_Q2-2026_excerpts.md`, Note 2 and Item 4
- **Severity:** Medium
- **Confidence:** High on the facts. The control assessment is an inference.
- **Deal impact:** Post-closing and valuation. Modernization accruals and estimates at completion are the auditor's critical audit matter. The same area carries the St. Aldric loss contract (SEC-15, SEC-16). Treat FY2025 modernization cost accruals and the St. Aldric estimate as a restatement risk if more items emerge (inference). The planned conversion branches are also in the Southwest (deal brief), the region with the accrual failure.
- **Cross-check:** Ask whether the auditor communicated a significant deficiency to the audit committee, and whether internal audit has found other unaccrued items.

#### SEC-06: Clean audit opinion and effective ICFR; auditor tenure 19 years
- **Finding:** Whitcombe & Ames gave unqualified opinions on both the FY2025 financial statements and ICFR. It has audited the company since 2007. No auditor change or reportable event was found. The critical audit matter is estimated costs at completion on fixed-price modernization contracts.
- **Evidence:** "the Company maintained, in all material respects, effective internal control"; "We have served as the Company's auditor since 2007."
- **Source:** `MDLS_10-K_FY2025_excerpts.md`, Item 9A and "Report of Independent Registered Public Accounting Firm"
- **Severity:** Low (positive)
- **Confidence:** High
- **Deal impact:** Disclosure. A mitigant, qualified by SEC-05.
- **Cross-check:** News for any auditor change or dispute.

#### SEC-07: Adjusted EBITDA definition and 2026 add-backs not disclosed in the SEC files
- **Finding:** Adjusted EBITDA adds back stock-based compensation, debt extinguishment losses, M&A costs and "other non-recurring items". The SEC files contain no 2026 reconciliation. They do not show whether the US$4.1m out-of-period charge, the US$5.2m loss provision or 2026 merger costs were added back. Together the two charges (US$9.3m) equal 61% of the H1 decline in Adjusted EBITDA (89.9 - 74.7 = 15.2), if they were not added back.
- **Evidence:** "It adds stock-based compensation, loss on extinguishment of debt, merger and acquisition-related costs and other non-recurring items to EBITDA." Stock-based compensation add-back: US$12.4m in FY2025, a recurring cost.
- **Source:** `MDLS_8-K_2026-02-25_fy2025-results.md`, footnote (2) and table; `MDLS_10-Q_Q2-2026_excerpts.md`, Item 2
- **Severity:** Medium
- **Confidence:** Medium. A gap in the filings.
- **Deal impact:** Valuation. The direction of normalization depends on the treatment.
- **Cross-check:** Financial analyst's H1 2026 Adjusted EBITDA bridge.

#### SEC-08: Core operating metrics deteriorating in H1 2026
- **Finding:** Units under contract, renewal rate, maintenance margin, backlog and technician retention all worsened in H1 2026. Repair and modernization revenue fell.
- **Evidence:**
  - Units: 176,300 to 168,100 (-4.7%).
  - Renewal rate: 92.8% (2023), 92.3% (2024), 90.6% (2025), 86.9% (Jun 2026).
  - Maintenance gross margin: 37.1% to 34.6%.
  - Backlog: 448.0 to 372.0 (-17.0%).
  - Voluntary technician attrition: 14.6% to 17.1%.
  - Repair revenue: -6.0%. Modernization revenue: -12.0%.
  - Overall gross margin: 33.6% to 31.2%. Adjusted EBITDA margin: 17.4% to 14.6%.
  - Units ex-Pinecrest at Dec 2025: 176,300 - 9,600 = 166,700, up only 1.1% on 164,900.
- **Source:** `MDLS_10-Q_Q2-2026_excerpts.md`, Item 2 "Results" and "Key operating metrics"; `MDLS_10-K_FY2025_excerpts.md`, "Key operating metrics"
- **Severity:** High
- **Confidence:** High
- **Deal impact:** Valuation. This undercuts the "recurring maintenance base" thesis. The deal brief's "about 168,000 units" matches June 30, 2026, but the trend is down.
- **Cross-check:** News on customer losses to manufacturers. Financial analyst's customer churn and retention data.

#### SEC-09: FY2026 outlook cut; August management case below the LTM base
- **Finding:** February guidance was revenue of US$1,095m to US$1,120m and Adjusted EBITDA of US$192m to US$198m. On August 6, 2026 the outlook was lowered. The August case is FY2026E Adjusted EBITDA of US$168m, 13.8% below the February plan of US$195m and below the US$171.2m LTM base. The revised public guidance figures are not found in SEC filings. The projections exclude code compliance costs, withdrawal liability and Brockmere.
- **Evidence:** February: "2025 was a record year... Organic growth accelerated". Proxy: the Company "lowered its fiscal 2026 outlook. The share price fell 21% to US$31.90." My calculations: 168 / 195 - 1 = -13.8%; FY2026E revenue 1,031 is 5.8% below the bottom of guidance; 2,459.5 / 168 = 14.6x FY2026E.
- **Source:** `MDLS_8-K_2026-02-25_fy2025-results.md`, "Fiscal 2026 outlook"; `MDLS_DEFM14A_2026_excerpts.md`, "Background of the merger" and "Certain financial projections"
- **Severity:** High
- **Confidence:** High
- **Deal impact:** Valuation. Earnings are declining, and the deal multiple is applied to a trailing figure.
- **Cross-check:** News on the August 6 earnings call. Financial analyst's forecast.

#### SEC-10: New collective agreement at 6.5% a year against price escalators capped at 4.0%
- **Finding:** A four-year national agreement effective July 1, 2026 raises combined wages and benefits by 6.5% a year, against 3.4% under the prior agreement. 62% of maintenance contracts by revenue cap price escalators at the lesser of CPI and 4.0%. The LTM base contains none of the new rates.
- **Evidence:** Covered wages and benefits were about US$286m in FY2025. My calculations (projection): year-one increase 286 x 6.5% = US$18.6m, against 286 x 3.4% = US$9.7m under the old pace, an incremental US$8.9m. After four years: 286 x (1.065^4 - 1) = US$81.9m, against 286 x (1.04^4 - 1) = US$48.6m at a 4.0% pass-through, a gap of US$33.3m.
- **Source:** `MDLS_10-Q_Q2-2026_excerpts.md`, Item 2 "Collective agreement"; `MDLS_10-K_FY2025_excerpts.md`, Item 1A
- **Severity:** High
- **Confidence:** High on the inputs. The projections are mine.
- **Deal impact:** Valuation. There is a structural margin squeeze. The August case says it reflects the agreement.
- **Cross-check:** Financial analyst's labor cost model. The agreement's terms on converting branches or exiting bargaining units are not found in SEC filings.

#### SEC-11: Lift Mechanics pension fund in critical and declining status; withdrawal liability US$338m, unrecorded
- **Finding:** The fund moved from critical status (2025) to critical and declining status (2026), and its actuary projects insolvency in 2041. Meridale's estimated complete withdrawal liability rose 14.2%, from US$296m to US$338m. No liability is recorded, and the merger projections exclude it.
- **Evidence:** "complete withdrawal liability as of January 1, 2026 is US$338 million (January 1, 2025: US$296 million)". "We have no current intention to withdraw." Contributions were US$41.3m in 2025, about 6.1% of the fund's total, rising 5% a year under the rehabilitation plan through 2029. My calculations: 338 / 2,459.5 = 13.7% of EV; 338 / 1,917.3 = 17.6% of equity value.
- **Source:** `MDLS_10-K_FY2025_excerpts.md`, Note 12 and Item 1A; `MDLS_10-Q_Q2-2026_excerpts.md`, Note 10; `MDLS_DEFM14A_2026_excerpts.md`, "Certain financial projections"
- **Severity:** High. Not Critical, because no source shows a complete withdrawal is planned or triggered.
- **Confidence:** High
- **Deal impact:** Valuation and post-closing. This is a debt-like exposure outside net debt. Insolvency risk and contribution increases also bear on future costs.
- **Cross-check:** The fund's public status notices; news on the fund.

#### SEC-12: Branch conversion would trigger a partial withdrawal liability of roughly US$98m to US$100m that the model omits
- **Finding:** The thesis converts 14 branches (about 1,000 of 3,390 covered technicians) away from the collective agreement. The 10-K says ceasing contributions at some facilities or bargaining units "would trigger a proportional liability". Model savings are US$18.0m a year, net of US$6.0m transition costs, and no withdrawal cost is shown.
- **Evidence:** "A partial withdrawal, including from ceasing contributions at some facilities or bargaining units, would trigger a proportional liability." My calculations (inference): 1,000 / 3,390 = 29.5%, and 29.5% x 338 = US$99.7m. On the 10-K headcount (79% x 4,380 = 3,460), 1,000 / 3,460 = 28.9%, or US$97.7m. That is 4.1% of EV and 5.2% of equity value, about 5.5 years of the US$18.0m saving, undiscounted.
- **Source:** `MDLS_10-K_FY2025_excerpts.md`, Note 12 and Item 1 "Workforce"; `MDLS_10-Q_Q2-2026_excerpts.md`, Note 10; `targets/wren/data/deal-brief.md`, thesis 3
- **Severity:** High
- **Confidence:** Medium. The filing states proportionality, but the statutory calculation and the payment schedule are not found in SEC filings.
- **Deal impact:** Valuation. The conversion saving is overstated unless the model includes the withdrawal cost.
- **Cross-check:** Ask for the fund actuary's partial withdrawal estimate. Check whether the agreement permits conversion during its term.

#### SEC-13: Illinois and New Jersey door-safety codes: unaccrued, unestimated compliance cost on about 22,400 units
- **Finding:** Illinois enacted its law in October 2025 (deadline December 31, 2028), and New Jersey adopted its rule on April 1, 2026 (deadline July 1, 2029). About 22,400 comprehensive-contract units in those two states are on forms that do not exclude code-mandated upgrades. Meridale has no completed cost estimate and no accrual, and it expenses the cost as incurred. Price recovery is limited by escalator caps. The projections and the fairness DCF exclude the cost.
- **Evidence:** "We have not completed our estimate of the cost of compliance. We recognize these costs as incurred and have not recorded a liability." Reported periods covered since enactment: FY2025 (Illinois from October 2025), Q1 2026 and Q2 2026. Break-even (my calculation): 246.0 / 22,400 = about US$10,980 per unit to reach 10% of EV; 191.7 / 22,400 = about US$8,560 per unit for 10% of equity value. Per-unit cost is not found in SEC filings.
- **Source:** `MDLS_10-K_FY2025_excerpts.md`, Note 14 and Item 1A; `MDLS_10-Q_Q2-2026_excerpts.md`, Note 11 "Code compliance"; `MDLS_DEFM14A_2026_excerpts.md`, "Certain financial projections"
- **Severity:** High. Not Critical, because the amount is not computable from SEC sources.
- **Confidence:** High on the facts. The break-even is mine.
- **Deal impact:** Valuation. This is an obligation outside net debt. Expensing as incurred may be acceptable for service contracts, but if a loss-contract or liability view applies, FY2025 and 2026 interim statements could need revision (inference). Other states could follow.
- **Cross-check:** Ask the litigation and financial analysts or news for an industry cost per unit. Ask management for its estimate and the unit count by contract form.

#### SEC-14: 10-K risk factor described the door codes as hypothetical after Illinois had enacted its law
- **Finding:** The FY2025 risk factor says states are "considering" retrofit rules, "If adopted". Note 14 of the same 10-K says Illinois enacted its law in October 2025, and the 10-Q later confirms New Jersey's adoption. The 10-K also says "most of them on contract forms used before 2019". The 10-Q is sharper: "most on contract forms that do not exclude code-mandated upgrades."
- **Evidence:** "Several states are considering new retrofit requirements... If adopted in states where we have many comprehensive contracts". Note 14: "In October 2025, Illinois enacted the Elevator Door Integrity Act".
- **Source:** `MDLS_10-K_FY2025_excerpts.md`, Item 1A and Note 14; `MDLS_10-Q_Q2-2026_excerpts.md`, Note 11
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Disclosure. A possible stockholder-claim theory. It also shows how management framed the issue.
- **Cross-check:** News on when analysts first raised the issue.

#### SEC-15: St. Aldric Health System arbitration seeking US$38.0m
- **Finding:** A US$61.4m fixed-price contract to modernize 46 elevators is about 10 months late: due March 31, 2026, now expected February 2027. The customer filed for arbitration on July 14, 2026, seeking US$38.0m. Liquidated damages are capped at US$15.4m, but the customer alleges gross negligence or willful misconduct, which could lift the consequential-damages exclusion. The 10-Q (August 6) disclosed the filing, so the disclosure was timely.
- **Evidence:** "seeking US$38.0 million, including liquidated damages and delay-related damages". Cap: 25% x 61.4 = 15.35, or US$15.4m. Remedy sought as an upper bound: 38.0 / 2,459.5 = 1.5% of EV.
- **Source:** `MDLS_10-Q_Q2-2026_excerpts.md`, Note 11 "Fixed-price modernization contract" and Note 12
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation and post-closing. The claim is below the Critical threshold.
- **Cross-check:** Litigation analyst for the arbitration docket and the customer's claims. Check St. Aldric's rank in revenue_by_customer.csv.

#### SEC-16: No liquidated-damages accrual on St. Aldric despite a 10-month delay and a recorded loss provision
- **Finding:** Meridale recorded a US$5.2m loss provision for cost overruns but accrued nothing for liquidated damages. Its stated reason is that a loss is neither probable nor estimable, even though the project was already three months past its completion date at June 30. This judgment sits in the auditor's critical audit matter area and in the region-and-process area of the SEC-04 error.
- **Evidence:** "have not accrued any amount for liquidated damages because we do not consider a loss probable and cannot reasonably estimate it."
- **Source:** `MDLS_10-Q_Q2-2026_excerpts.md`, Note 11; `MDLS_10-K_FY2025_excerpts.md`, critical audit matter
- **Severity:** Medium
- **Confidence:** Medium. The judgment is disclosed, and my challenge to it is an inference.
- **Deal impact:** Valuation. Accrued damages up to the US$15.4m cap would reduce earnings in the reported periods (inference).
- **Cross-check:** Litigation analyst on the claimed delay and the customer-caused-delay defense.

#### SEC-17: New Jersey automatic-renewal investigation and class action
- **Finding:** On March 30, 2026, the New Jersey Division of Consumer Affairs issued a civil investigative demand on renewal notices and early termination fees. On May 19, 2026, a putative class action followed, seeking refunds, treble damages and an injunction. The company cannot estimate a loss, and no accrual is recorded. Both events came after the 10-K, so the timing is consistent. The 10-K had a generic risk factor on the topic.
- **Evidence:** The suit seeks "refunds of cancellation fees, treble damages and an injunction." "We cannot estimate a range of possible loss." The cancellation fee income base is not found in SEC filings.
- **Source:** `MDLS_10-Q_Q2-2026_excerpts.md`, Note 11 "Automatic renewal matters"; `MDLS_10-K_FY2025_excerpts.md`, Item 1A
- **Severity:** Medium. It becomes High if the cancellation fee base or New Jersey revenue shows meaningful exposure, or if an injunction would change renewal terms.
- **Confidence:** High on the facts.
- **Deal impact:** Valuation and post-closing. This attacks the evergreen renewal model at the center of the thesis.
- **Cross-check:** Litigation docket. Financial analyst for New Jersey revenue and cancellation fee income.

#### SEC-18: Legacy asbestos claims rising; insurance projected to run out in 2029
- **Finding:** Pending claims went from 29 to 34 to 41. Meridale holds a US$7.2m accrual through 2035 and a US$4.9m insurance receivable. Insurance pays 68% of costs until its limits run out, projected for 2029.
- **Evidence:** "41 asbestos-related personal injury claims were pending (34 at December 31, 2024 and 29 at December 31, 2023)". Net accrual: 7.2 - 4.9 = US$2.3m.
- **Source:** `MDLS_10-K_FY2025_excerpts.md`, Note 14 "Legacy asbestos claims"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Post-closing. The cost after 2029 is uninsured.
- **Cross-check:** Litigation analyst's claim counts in 2026.

#### SEC-19: Harbor Pointe escalator injury suit (US$85.0m) appears insured
- **Finding:** The suit seeks US$85.0m. The US$2.0m self-insured retention is accrued, and US$150.0m of insurance sits above it. The carriers accepted defense without reservation of rights.
- **Evidence:** "The primary and excess carriers have accepted defense of the claim without reservation of rights."
- **Source:** `MDLS_10-K_FY2025_excerpts.md`, Note 14 "Personal injury litigation"
- **Severity:** Low (neutralized by insurance)
- **Confidence:** High
- **Deal impact:** None material.
- **Cross-check:** Litigation analyst for any change in the claim or in carrier position.

#### SEC-20: Vantor Elevator trade secret suit dismissed with prejudice (closed)
- **Finding:** The suit was dismissed on May 12, 2026, and Vantor did not appeal.
- **Evidence:** "dismissed... with prejudice. Vantor did not appeal within the time allowed."
- **Source:** `MDLS_10-Q_Q2-2026_excerpts.md`, Note 11 "Vantor Elevator"; `MDLS_10-K_FY2025_excerpts.md`, Note 14
- **Severity:** Low (closed)
- **Confidence:** High
- **Deal impact:** None.
- **Cross-check:** Litigation docket.

#### SEC-21: 2030 notes change-of-control put at 101% is unfunded, and holders have a price incentive to use it
- **Finding:** The merger is a change of control under the indenture, and no ratings downgrade is needed to trigger the put. Within 30 days after closing, Meridale must offer to repurchase all US$400.0m of notes at 101%. The debt commitment does not fund the repurchase. The notes traded at 97.25% on June 30, so holders gain by putting. The deal brief assumes the notes stay outstanding.
- **Evidence:** "The indenture does not require a ratings downgrade". "The debt commitment does not include financing for any such repurchase." Fair value US$389.0m (97.25%). Full put: 400.0 x 101% = US$404.0m plus accrued interest. That is 16.4% of EV, 21.1% of equity value and 31.0% of the US$1,304.9m Fund IV equity. Rough post-closing liquidity: cash 102.8 - 30.0 = 72.8, plus a US$250.0m revolver = 322.8, below 404.0 (the revolver's survival after a change of control is not found in SEC filings).
- **Source:** `MDLS_10-K_FY2025_excerpts.md`, Note 9 "Change of control"; `MDLS_10-Q_Q2-2026_excerpts.md`, Note 8; `MDLS_DEFM14A_2026_excerpts.md`, "Financing of the merger"; `MDLS_8-K_2026-09-21_merger-agreement.md`, "Financing"
- **Severity:** High. Under the calibration rule the put arises after closing, not before. It would become Critical if no backstop exists and the repurchase would cause a default.
- **Confidence:** High
- **Deal impact:** Closing and financing structure, and post-closing liquidity. Needs committed backstop financing for up to US$404.0m plus accrued interest. The 1% premium is US$4.0m, not in the model.
- **Cross-check:** News on the notes' trading price after the announcement. Financial analyst on liquidity. Ask whether the new term loan's terms allow the repurchase.

#### SEC-22: Existing term loan and revolver; maturities; covenant terms not in the filings
- **Finding:** The term loan B is US$245.0m, due May 2031, and is refinanced at closing in the model. The US$250.0m revolver, due May 2029, was undrawn at June 30, 2026 (US$20.0m drawn at December 2025). There are no near-term maturities. Debt principal of US$645.0m confirms the deal brief. Financial covenant definitions, test dates and lien limits in the indenture are not found in SEC filings.
- **Evidence:** "Our next scheduled debt maturity is the 5.875% senior notes due 2030." 245.0 + 400.0 = 645.0.
- **Source:** `MDLS_10-K_FY2025_excerpts.md`, Note 9 and "Liquidity"; `MDLS_10-Q_Q2-2026_excerpts.md`, Note 8
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None. Maturities are a mitigant. Whether the indenture's lien covenant permits the new US$925.0m secured term loan is an open question.
- **Cross-check:** Credit agreement and indenture.

#### SEC-23: Interest rate swap expires December 31, 2026
- **Finding:** The swap fixes SOFR at 1.92% on US$200.0m of the term loan. Its expiry would add about US$4.2m a year of interest. The term loan is refinanced at closing, so the effect is mainly interim (and standalone if the deal fails).
- **Evidence:** "interest expense on the term loan would rise by about US$4.2 million a year after expiry."
- **Source:** `MDLS_10-Q_Q2-2026_excerpts.md`, Item 2 "Liquidity"; `MDLS_10-K_FY2025_excerpts.md`, Note 9
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Minor interim cost.
- **Cross-check:** None needed.

#### SEC-24: Laurent-Meridale put: about US$53.4m cash at 12.0x EBITDA against a US$9.7m book value in the model
- **Finding:** After a change of control, Groupe Laurent can make Meridale buy its 50% within 180 days. The price is the greater of appraised fair value and 12.0x trailing EBITDA x 50%, paid in cash within 90 days. Groupe Laurent says it is "reviewing its rights." No liability is recorded. The deal brief carries the stake at book and has no funding for the put. No guarantees or funding obligations for the JV are found in SEC filings.
- **Evidence:** 12.0 x 8.9 x 50% = US$53.4m floor, against carrying value US$9.7m: a cash need of US$53.4m and an excess over book of US$43.7m. The floor is 2.2% of EV. JV trailing EBITDA rose from 8.4 to 8.9.
- **Source:** `MDLS_10-K_FY2025_excerpts.md`, Note 6; `MDLS_10-Q_Q2-2026_excerpts.md`, Note 6; `MDLS_DEFM14A_2026_excerpts.md`, "Regulatory approvals and third-party consents"
- **Severity:** Medium. A computable, deal-triggered cash item. Meridale would receive 100% of the JV at 12.0x against the 14.4x deal multiple, so value lost is limited, but the cash is unfunded and the appraisal could exceed the floor.
- **Confidence:** High
- **Deal impact:** Price and funding. Add to uses as a contingent item.
- **Cross-check:** News on Groupe Laurent's intentions.

#### SEC-25: Brockmere termination fee of US$9.5m, not in sources and uses
- **Finding:** The merger agreement requires Meridale to terminate the US$96.0m Brockmere deal at Parent's request and to pay any fee due. The fee is US$9.5m if terminated before December 31, 2026 for any reason other than a seller breach. The fee for termination after that date is not found in SEC filings.
- **Evidence:** "we must pay the sellers a termination fee of US$9.5 million." The 8-K says the Company agreed "to pay any termination fee payable under that agreement."
- **Source:** `MDLS_10-Q_Q2-2026_excerpts.md`, Note 11 "Brockmere acquisition"; `MDLS_8-K_2026-09-21_merger-agreement.md`, "Brockmere"
- **Severity:** Medium (known deal cost)
- **Confidence:** High
- **Deal impact:** Price. Add to uses. If Meridale terminates Brockmere and the merger then fails, Meridale has paid the fee and lost the acquisition.
- **Cross-check:** Ask for the Brockmere agreement and the planned termination timing.

#### SEC-26: Equity-award cash-out of US$52.3m confirmed
- **Finding:** The proxy's award table ties to the deal brief.
- **Evidence:** RSUs 740,000 x 41.50 = 30.7. PSUs 380,000 x 41.50 = 15.8. Options 420,000 x 13.90 = 5.8 (41.50 - 27.60 = 13.90). Total 52.3.
- **Source:** `MDLS_DEFM14A_2026_excerpts.md`, "Treatment of equity awards"; `MDLS_8-K_2026-09-21_merger-agreement.md`, "Equity awards"
- **Severity:** Medium (known deal cost, in the model)
- **Confidence:** High
- **Deal impact:** Price. Already in the deal brief's uses.
- **Cross-check:** Award counts at closing could change through new grants.

#### SEC-27: Unvested awards accelerate at closing (single-trigger), and PSUs vest at target despite weak results
- **Finding:** Unvested RSUs are cashed out at closing, and PSUs vest at target regardless of performance. Adjusted EBITDA fell 16.9% in H1 2026, and the outlook was cut. Severance, by contrast, is double-trigger. No tax gross-ups; 280G best-net cutback.
- **Evidence:** "each performance stock unit will vest at target". "No executive is entitled to a tax gross-up."
- **Source:** `MDLS_8-K_2026-09-21_merger-agreement.md`, "Equity awards"; `MDLS_DEFM14A_2026_excerpts.md`, "Golden parachute compensation"; `MDLS_10-Q_Q2-2026_excerpts.md`, Item 2
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Governance and disclosure. The cost is already in SEC-26.
- **Cross-check:** Proxy advisory or news commentary.

#### SEC-28: Change-in-control severance of US$16.8m is effectively certain and not in the model
- **Finding:** Severance is double-trigger, but Parent intends to replace the executive team other than Mr. Pell within 12 months. Pell has waived his severance, so all US$16.8m goes to executives Parent plans to replace.
- **Evidence:** Parent "expects... to replace the executive team, other than Mr. Pell, within 12 months after closing." 4.2 + 3.9 + 2.6 + 2.3 = 13.0; + 3.8 = 16.8.
- **Source:** `MDLS_DEFM14A_2026_excerpts.md`, "Golden parachute compensation"
- **Severity:** Medium (known deal cost)
- **Confidence:** High
- **Deal impact:** Price. Add to uses.
- **Cross-check:** None needed.

#### SEC-29: Pellham Rowe fee of US$27.0m contingent on closing, not in the buyer's fees line
- **Finding:** The company pays its advisor US$31.5m. US$4.5m was due at the opinion and US$27.0m is due at closing. The deal brief's US$64.0m covers only the buyer's own fees. The company's legal and other transaction costs are not found in SEC filings.
- **Evidence:** "US$27.0 million is contingent on closing."
- **Source:** `MDLS_DEFM14A_2026_excerpts.md`, "Opinion of Pellham Rowe & Co." (Fees and relationships)
- **Severity:** Medium (known deal cost)
- **Confidence:** High
- **Deal impact:** Price. Add to uses or reduce the cash available.
- **Cross-check:** Ask for the company's full transaction expense estimate.

#### SEC-30: Pellham Rowe conflicts: fees from Ostrander Hale and an affiliate arranging the buyer's term loan
- **Finding:** In the two years before its engagement, Pellham Rowe earned about US$14.2m from Ostrander Hale and its portfolio companies. Its affiliate is a joint lead arranger of the US$925.0m term loan, with about US$7.9m of fees expected. The committee was told before engaging the firm. Price US$41.50 is below the midpoint of the DCF range of US$38.10 to US$46.80 (midpoint 42.45). The DCF uses the August case, which excludes code costs and withdrawal liability.
- **Evidence:** "An affiliate, Pellham Rowe Credit Partners, is a joint lead arranger of the US$925.0 million term loan commitment to Parent".
- **Source:** `MDLS_DEFM14A_2026_excerpts.md`, "Opinion of Pellham Rowe & Co."
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Closing risk and litigation. These facts strengthen stockholder-suit, appraisal and vote-against arguments.
- **Cross-check:** News and litigation for merger suits citing the conflict.

#### SEC-31: Known deal costs total, at or because of closing
- **Finding:** Known contractual costs total US$105.6m: awards 52.3, severance 16.8, Brockmere fee 9.5 and Pellham Rowe contingent fee 27.0. That is 4.3% of EV and 5.5% of equity value. Of this, US$53.3m is outside the deal brief's uses. If all noteholders put, the 1% premium adds US$4.0m (total 109.6, or 4.5% of EV). The Laurent put floor of US$53.4m (SEC-24) is a separate cash item.
- **Evidence:** 52.3 + 16.8 + 9.5 + 27.0 = 105.6; 105.6 / 2,459.5 = 4.3%; 105.6 / 1,917.3 = 5.5%. Not in the model: 16.8 + 9.5 + 27.0 = 53.3.
- **Source:** SEC-25, SEC-26, SEC-28, SEC-29 sources
- **Severity:** Medium on an EV basis (below 5%). On an equity-value basis the total exceeds 5%, so the lead may choose High.
- **Confidence:** High
- **Deal impact:** Price.
- **Cross-check:** Financial analyst's sources-and-uses rebuild.

#### SEC-32: Two vote conditions, including a majority of the unaffiliated shares outstanding
- **Finding:** Closing needs a majority of all outstanding shares and a majority of the unaffiliated shares outstanding. Not voting counts as against.
- **Evidence:** Unaffiliated shares: 46.20 - 1.43 = 44.77m, so 22.39m votes are needed. Halsey Rock's 5.267m is 11.8% of unaffiliated shares. "Failing to vote has the same effect as voting against."
- **Source:** `MDLS_DEFM14A_2026_excerpts.md`, "Summary" and "Security ownership"; `MDLS_8-K_2026-09-21_merger-agreement.md`, "Conditions"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Closing risk. Turnout matters.
- **Cross-check:** News on Halsey Rock and proxy advisor positions.

#### SEC-33: Halsey Rock alone holds more than the 10% appraisal-condition threshold
- **Finding:** Parent need not close if holders of more than 10% of outstanding shares demand appraisal. Halsey Rock holds 11.4%, up from about 9% in March 2026, so it alone could fail the condition. The condition benefits Parent, which may waive it.
- **Evidence:** 10% x 46.20m = 4.62m shares, against Halsey Rock's 5,267,000. In March 2026 Halsey Rock "asked for two board seats and urged the board to consider a sale."
- **Source:** `MDLS_DEFM14A_2026_excerpts.md`, "Summary", "Background of the merger" and "Security ownership"; `MDLS_8-K_2026-09-21_merger-agreement.md`, "Conditions"
- **Severity:** High. It would be Critical (block closing) if a source shows Halsey Rock intends to demand appraisal; the SEC files do not state its current stance.
- **Confidence:** High on the numbers.
- **Deal impact:** Closing risk. A waiver means paying appraisal claims at a court-set fair value.
- **Cross-check:** News analyst on Halsey Rock's public position. Litigation analyst for any appraisal demands.

#### SEC-34: Price history supports an appraisal argument
- **Finding:** Ostrander Hale's May indication was US$44.00 to US$46.00. It fell to US$39.00 after the Q2 results and ended at US$41.50. The 25.0% premium is measured against a price already down 21% after the results. The market check (15 parties, three NDAs) produced no proposal.
- **Evidence:** Premium check: 41.50 / 33.20 = 1.25 (confirms the deal brief). Implied price before the results: 31.90 / 0.79 = about US$40.38, so the deal is about 2.8% above it (inference). 41.50 is 5.7% below the US$44.00 low end of the May indication.
- **Source:** `MDLS_DEFM14A_2026_excerpts.md`, "Background of the merger"; `MDLS_8-K_2026-09-21_merger-agreement.md`, Item 8.01
- **Severity:** Medium
- **Confidence:** High on the facts. The pre-results price is derived.
- **Deal impact:** Closing risk and appraisal exposure. The market check is a mitigant.
- **Cross-check:** Share price data from the financial analyst or news.

#### SEC-35: Section 382: the model's NOL assumption is contradicted by the 2023 ownership change
- **Finding:** The model assumes the merger sets a new limit of about US$65.2m a year and that US$66.8m of tax value is fully used in FY2027 to FY2029. The 10-K says a November 2023 ownership change limits pre-change losses to about US$11.2m a year. Those losses "would remain subject to the lower of the limits". The NOLs arose mainly in 2019 to 2021, before that change.
- **Evidence:** "pre-change losses would remain subject to the lower of the limits that apply to them." Effective rate: 66.8 / 318.0 = 21.0%. Three years at 11.2 = US$33.6m of NOL, worth about US$7.1m of tax, against the model's US$66.8m. About US$59.7m of tax value moves beyond FY2029: 2.4% of EV (inference). Using all US$318.0m at 11.2 a year takes about 28 years. US$61.0m expires from 2034 to 2037.
- **Source:** `MDLS_10-K_FY2025_excerpts.md`, Note 11 "Income taxes"; `targets/wren/data/deal-brief.md`, thesis 5
- **Severity:** High
- **Confidence:** High on the limit. The value shift is my calculation.
- **Deal impact:** Valuation. The model overstates near-term tax savings, so the PV is much lower.
- **Cross-check:** Tax diligence on the pre-change share of the US$318.0m and any built-in gains.

#### SEC-36: LiftSense LTE-M network shutdown: about US$5.2m of replacement cost at Meridale's expense
- **Finding:** The carrier shuts its LTE-M network on September 30, 2027. About 9,800 units need new hardware, which Meridale replaces at its own cost, mostly in 2027.
- **Evidence:** 9,800 x 530 = US$5.19m, or about 5.2. "we replace hardware at our cost."
- **Source:** `MDLS_10-Q_Q2-2026_excerpts.md`, Item 2 "Connected services"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Post-closing cost in 2027. Connected growth is confirmed and is a positive (61,900 units, against a 110,000 target by 2029).
- **Cross-check:** Is it in the August case? Not stated.

#### SEC-37: Customer contracts: reverse triangular structure avoids assignment consents
- **Finding:** 34% of maintenance contracts by revenue prohibit assignment without consent. The company knows of no material change-of-control clause, and expects no consents to be needed because Meridale survives the merger.
- **Evidence:** "the Company does not expect it to require the consent of customers under contracts that restrict assignment."
- **Source:** `MDLS_DEFM14A_2026_excerpts.md`, "Regulatory approvals and third-party consents"; `MDLS_10-K_FY2025_excerpts.md`, Item 1A
- **Severity:** Low (positive)
- **Confidence:** High
- **Deal impact:** Closing. Mitigant.
- **Cross-check:** A sample of customer contracts.

#### SEC-38: Termination fees and no financing condition
- **Finding:** The company would pay a US$57.5m termination fee (3.0% of equity value). Parent would pay a US$115.0m reverse fee (6.0%), including on financing failure. There is no financing condition. HSR early termination came on October 14, 2026.
- **Evidence:** "There is no financing condition."
- **Source:** `MDLS_8-K_2026-09-21_merger-agreement.md`, "Termination fees" and "Financing"; `MDLS_DEFM14A_2026_excerpts.md`, "Regulatory approvals"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Closing. The buyer's US$115.0m exposure rises if financing for the notes put (SEC-21) is uncertain.
- **Cross-check:** None needed.

#### SEC-39: No finance leadership departures disclosed
- **Finding:** No CFO, chief accounting officer or audit committee change is found in the SEC filings. The CFO is Marisol Okafor. The 10-Q certifications are by the CEO and CFO.
- **Evidence:** Item 4: "Our Chief Executive Officer and Chief Financial Officer concluded..."
- **Source:** `MDLS_10-Q_Q2-2026_excerpts.md`, Item 4; `MDLS_DEFM14A_2026_excerpts.md`, "Golden parachute compensation"
- **Severity:** Low
- **Confidence:** Medium. These are excerpts.
- **Deal impact:** None.
- **Cross-check:** News for any executive departures.

#### SEC-40: Planned replacement of the CFO and finance team while key judgments are open
- **Finding:** Parent plans to replace the executive team except Mr. Pell, including the CFO, within 12 months and to move corporate functions to its shared-services platform. Several judgments would still be open at that point: St. Aldric, code compliance, pension, the amortization estimate and the newly remediated accrual controls.
- **Evidence:** "combine Meridale's corporate functions with Ostrander Hale's shared-services platform".
- **Source:** `MDLS_DEFM14A_2026_excerpts.md`, "Golden parachute compensation"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Post-closing. Needs a finance transition plan and retention through the first audit.
- **Cross-check:** None.

#### SEC-41: CEO's dual role, rollover and voting agreement
- **Finding:** Dorian Pell is chairman and CEO. He rolls 450,000 of his 1,010,000 shares (US$18.7m, which confirms the deal brief), signed a voting agreement and waived severance. He did not take part in the deliberations, and a four-member special committee led the process. No other related-party transactions are found in SEC filings.
- **Evidence:** 0.45 x 41.50 = 18.7.
- **Source:** `MDLS_8-K_2026-09-21_merger-agreement.md`, "Rollover" and "Special committee"; `MDLS_DEFM14A_2026_excerpts.md`, "Security ownership"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Governance. Pell's shares are excluded from the unaffiliated vote.
- **Cross-check:** News for any objections.

#### SEC-42: Deal brief figures checked against the filings
- **Finding:** Most figures tie. Exceptions are listed below.
- **Evidence:**
  - Confirmed: shares 46.20m (record date); equity value 1,917.3; debt principal 645.0; HSR on Oct 14; dates (Jun 15, Jul 9/16, Sep 20/21, Oct 23, Dec 9); LiftSense growth (35.9 / 26.0 = 38.1%; 22.6 / 16.4 = 37.8%); about 168,000 units; NOL 318.0 / 66.8; Laurent book 9.7.
  - Not found in SEC filings: cash of US$102.8m at June 30, 2026 (so net debt of 542.2 is unconfirmed); 3,390 covered technicians (the 10-K implies about 3,460 at Dec 2025).
  - Contradicted or incomplete: Section 382 limit (SEC-35); notes staying outstanding (SEC-21); Laurent at book (SEC-24); uses missing severance, Brockmere fee and company advisor fee (SEC-31); conversion saving missing withdrawal liability (SEC-12).
- **Source:** All five files; `targets/wren/data/deal-brief.md`
- **Severity:** Low (the individual issues carry their own cards)
- **Confidence:** High
- **Deal impact:** Model hygiene.
- **Cross-check:** Financial analyst for June 30 cash and headcount.

#### SEC-43: Revenue recognition policies
- **Finding:** Maintenance runs on five-year automatically renewing contracts with 90 to 120 day notice periods. Repair is billed as performed. Fixed-price modernization is recognized over time on cost-to-cost, with full loss provisions. No bill-and-hold or unusual arrangements are found in SEC filings. The open question is whether the unaccrued costs in SEC-04 also understated revenue progress.
- **Evidence:** "We recognize revenue over time based on costs incurred relative to total estimated costs."
- **Source:** `MDLS_10-K_FY2025_excerpts.md`, Item 1 and "Critical accounting estimates"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None beyond SEC-04 and SEC-16.
- **Cross-check:** Contract-level margin data.

#### SEC-44: Pinecrest acquisition (March 2025)
- **Finding:** Meridale paid US$152.0m for about 9,600 units, funded by cash and the revolver. Pinecrest contributed US$51.0m of revenue in FY2025 and US$30.6m in H1 2026. Management called it "fully integrated". It drove most of the increase in D&A (34.2 to 42.8, inference).
- **Evidence:** "Pinecrest is fully integrated".
- **Source:** `MDLS_10-K_FY2025_excerpts.md`, Item 1 and Item 7; `MDLS_8-K_2026-02-25_fy2025-results.md`
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Context for SEC-03.
- **Cross-check:** None.

#### SEC-45: No embedded instructions found in the SEC files
- **Finding:** None of the five files contains text that tries to instruct the agents.
- **Evidence:** Each file carries a fictional-data notice only.
- **Source:** All five files
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None.
- **Cross-check:** None.

### Positive or mitigating points
- **Audit and controls:** clean audit and ICFR opinions; auditor since 2007; no auditor change (SEC-06). Qualified by SEC-05.
- **Debt maturities:** none before May 2029 (revolver), May 2030 (notes) and May 2031 (term loan). The revolver was undrawn at June 30, 2026 (SEC-22).
- **Litigation closed or neutralized:** Vantor was dismissed with prejudice and not appealed (SEC-20). Harbor Pointe is insured with defense accepted without reservation (SEC-19).
- **Growing product:** connected services grew 38.1% in FY2025 and 37.8% in H1 2026 (SEC-36, SEC-42).
- **Customer consents:** the reverse triangular structure means no customer consents are needed (SEC-37).
- **Deal terms:** no financing condition, a US$115.0m reverse termination fee and early HSR clearance (SEC-38).
- **Executive pay:** double-trigger severance, no gross-ups, CEO severance waived (SEC-27, SEC-28).
- **Controls remediation:** remediation of the Southwest accrual control has been implemented (SEC-05).
- **Market check:** contacting 15 parties produced no competing proposal (SEC-34).

### Gaps and questions for management
1. Is the amortization of capitalized contract costs inside the D&A add-back in Adjusted EBITDA? What period does the June 2026 renewal rate support (SEC-02)?
2. Please provide the H1 2026 Adjusted EBITDA reconciliation. Were the US$4.1m and US$5.2m charges, and merger costs, added back (SEC-07)?
3. In which quarter of 2025 was the US$4.1m of subcontractor work done? Was revenue progress also misstated? Did the auditor report a deficiency to the audit committee (SEC-04, SEC-05)?
4. What is the estimated per-unit cost and total cost of the Illinois and New Jersey door code compliance, and how many units in other states face proposed rules (SEC-13)?
5. Please provide the fund actuary's partial withdrawal estimate for the 14-branch conversion and the payment schedule. Does the collective agreement permit conversion during its term (SEC-12)?
6. What is the backstop for the US$404.0m notes put? Does the revolver survive a change of control? Does the indenture permit the new secured term loan (SEC-21, SEC-22)?
7. What is Groupe Laurent's position? Is there an appraisal history for Laurent-Meridale? Are there any JV guarantees or funding obligations (SEC-24)?
8. What cancellation fee income and revenue come from New Jersey customers (SEC-17)?
9. What are the company's total transaction expenses beyond the Pellham Rowe fee, and what Brockmere fee applies after December 31, 2026 (SEC-25, SEC-29)?
10. Please provide a Section 382 analysis: the pre-change share of the US$318.0m and whether any built-in gain exceptions apply (SEC-35).
11. Not found in SEC filings: June 30, 2026 cash (US$102.8m), the revised FY2026 public guidance figures, financial covenant definitions, Halsey Rock's current stance on the vote or appraisal, and St. Aldric's revenue rank.
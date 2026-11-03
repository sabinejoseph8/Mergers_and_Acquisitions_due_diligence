## Financial analyst: findings

Target: Project Wren, Meridale Lift Services, Inc. (fictional). All figures are in US$ millions unless stated. "LTM" means LTM Q2 2026, which is FY2025 - H1 2025 + H1 2026, the definition in the README. Every figure the lead agent gave me was checked against the deal brief. I had no facts from other sources (SEC, news, litigation).

### Files reviewed
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/wren/data/deal-brief.md`
- `.../targets/wren/data/financials/README.md`
- `.../targets/wren/data/financials/income_statement.csv`
- `.../targets/wren/data/financials/adjusted_ebitda_reconciliation.csv`
- `.../targets/wren/data/financials/balance_sheet.csv`
- `.../targets/wren/data/financials/cash_flow.csv`
- `.../targets/wren/data/financials/revenue_quarterly.csv`
- `.../targets/wren/data/financials/revenue_by_customer.csv`
- `.../targets/wren/data/financials/kpis.csv`

None of the files contains text that tries to give the agents instructions (FIN-41).

Integrity checks:
- Segment revenue adds up to total revenue in every period.
- Quarterly revenue adds up to the annual and H1 totals.
- The balance sheet balances at June 30, 2026: assets 1,344.5 = liabilities 1,012.9 + equity 331.6.
- H1 2026 balance sheet movements tie to the cash flow lines. AR -5.8, capitalized contract costs +6.0, AP -3.3, accrued compensation -6.1, contract liabilities +2.9 and other liabilities +3.4 all match exactly. Retained earnings move by net income of 15.7. APIC moves by +5.2 (SBC 6.6 + option proceeds 0.8 - net share settlement taxes 2.2).

### Key metrics table

Reported figures, as the company presents them, plus my ratios:

| Metric | FY2023 | FY2024 | FY2025 | H1 2026 (LTM where noted) |
|---|---|---|---|---|
| Total revenue | 905.0 | 984.0 | 1,067.7 | 510.8 (LTM 1,062.5) |
| Revenue growth | 10.4% | 8.7% | 8.5% | H1 -1.0% YoY (LTM vs prior LTM +4.5%) |
| Gross margin | 34.0% | 33.9% | 33.4% | 31.2% (LTM 32.2%) |
| Maintenance services gross margin (KPI) | 38.9% | 38.4% | 37.1% | 34.6% |
| EBITDA (company reconciliation) | 150.5 | 119.8 | 167.7 | 64.7 (LTM 153.1) |
| Adjusted EBITDA (company definition) | 163.1 | 177.0 | 186.4 | 74.7 (LTM 171.2) |
| Adjusted EBITDA margin | 18.0% | 18.0% | 17.5% | 14.6% (LTM 16.1%) |
| Add-backs as % of Adjusted EBITDA | 7.7% | 32.3% (incl. 41.2 debt loss) | 10.0% | 13.4% (LTM 10.6%) |
| Operating income | 116.5 | 125.0 | 123.4 | 41.4 (LTM 106.7) |
| Net income | 61.1 | 35.3 | 62.9 | 15.7 (LTM 49.8) |
| Operating cash flow | 102.1 | 119.5 | 128.4 | 41.0 (LTM 122.2) |
| Capex | 27.9 | 29.8 | 33.5 | 17.4 (LTM 35.3) |
| Free cash flow (OCF - capex) | 74.2 | 89.7 | 94.9 | 23.6 (LTM 86.9) |
| OCF / Adjusted EBITDA | 62.6% | 67.5% | 68.9% | LTM 71.4% |
| Debt principal (derived) | 600.0 | 647.5 | 665.0 | 645.0 |
| Cash | 74.6 | 151.9 | 100.6 | 102.8 |
| Net debt | 525.4 | 495.6 | 564.4 | 542.2 |
| Net debt / Adjusted EBITDA | 3.22x | 2.80x | 3.03x | 3.17x LTM |
| Adjusted EBITDA / interest | 4.43x | 4.55x | 4.48x | 4.06x LTM |
| DSO (net AR / revenue x 365) | 61.0 | 61.0 | 61.0 | 59.3 (LTM revenue) |
| Units under maintenance contract | 158,400 | 164,900 | 176,300 | 168,100 |
| Renewal rate (TTM) | 92.8% | 92.3% | 90.6% | 86.9% |
| Modernization backlog | 412.0 | 455.0 | 448.0 | 372.0 |
| LiftSense connected units | 21,000 | 34,500 | 52,800 | 61,900 |
| Field technicians / voluntary attrition | 3,920 / 11.2% | 4,060 / 12.0% | 4,380 / 14.6% | 4,290 / 17.1% |
| Top customer / top 10 share | n/a | 2.3% / 14.7% | 2.3% / 14.8% | not provided |

My adjusted figures, kept separate from the reported ones (see FIN-10):

| Metric | Value |
|---|---|
| Normalized LTM Adjusted EBITDA, buyer case | 159.2 (range 155.1 to 159.2) |
| Implied EV at 14.4x (projection) | 2,292.5 (range 2,233.4 to 2,292.5) |
| Gap to deal EV | -167.0 (-6.8%), range up to -226.1 (-9.2%) |

### Findings

#### FIN-01: Adjusted EBITDA recomputation ties to the deal brief
- **Finding:** LTM Q2 2026 Adjusted EBITDA of 171.2 and FY2025 Adjusted EBITDA of 186.4 both recompute exactly from the company reconciliation.
- **Evidence:**
  - LTM net income = 62.9 - 28.8 + 15.7 = 49.8.
  - LTM tax = 20.4 - 9.4 + 5.1 = 16.1.
  - LTM interest = 41.6 - 20.6 + 21.2 = 42.2.
  - LTM D&A = 42.8 - 20.5 + 22.7 = 45.0.
  - LTM EBITDA = 49.8 + 16.1 + 42.2 + 45.0 = 153.1.
  - LTM add-backs: SBC 12.4 - 6.1 + 6.6 = 12.9. M&A costs 3.8 - 3.3 + 2.1 = 2.6. Other 2.5 - 1.2 + 1.3 = 2.6.
  - LTM Adjusted EBITDA = 153.1 + 12.9 + 2.6 + 2.6 = 171.2.
  - FY2025 = 167.7 + 12.4 + 3.8 + 2.5 = 186.4.
  - H1 2026 = 64.7 + 6.6 + 2.1 + 1.3 = 74.7.
  - H1 2025 = 79.3 + 6.1 + 3.3 + 1.2 = 89.9.
  - LTM add-backs total 18.1, which is 10.6% of 171.2.
- **Source:** `financials/adjusted_ebitda_reconciliation.csv`, all rows; `financials/income_statement.csv`, rows Net income, Income tax, Interest expense.
- **Severity:** Low
- **Confidence:** High. Recomputed directly.
- **Deal impact:** Valuation (the arithmetic is sound; the quality of the base is a separate matter, see FIN-02 to FIN-10).
- **Cross-check:** Tie to the 10-Q non-GAAP reconciliation and the merger proxy's financial advisor section.

#### FIN-02: H1 2026 Adjusted EBITDA fell 16.9%, so the LTM base still carries a stronger H2 2025
- **Finding:** H1 2026 Adjusted EBITDA was 74.7, against 89.9 in H1 2025. The LTM base of 171.2 is propped up by H2 2025 at 96.5. On the H1 2026 run-rate, the deal multiple is 16.5x, not 14.4x.
- **Evidence:**
  - H1 change = 74.7 - 89.9 = -15.2, or -16.9%.
  - H1 2026 margin = 74.7 / 510.8 = 14.6%, against 89.9 / 516.0 = 17.4% a year earlier.
  - H2 2025 = 186.4 - 89.9 = 96.5, a margin of 96.5 / 551.7 = 17.5%.
  - H1 2026 operating income 41.4 vs 58.1 = -28.7%.
  - Simple run-rate = 74.7 x 2 = 149.4, so EV / run-rate = 2,459.5 / 149.4 = 16.5x (projection).
  - Seasonally adjusted: H1 2025 was 89.9 / 186.4 = 48.2% of the year, so 74.7 / 0.482 = 154.9, which gives 15.9x (projection).
  - LTM is 171.2 / 186.4 - 1 = -8.2% below FY2025.
- **Source:** `financials/adjusted_ebitda_reconciliation.csv`, Adjusted EBITDA row; `financials/income_statement.csv`, Total revenue and Operating income rows.
- **Severity:** High. At the deal multiple, the run-rate implies 149.4 x 14.4 = 2,151.4, which is -12.5% of value. That figure is a projection that annualizes one half-year. The seasonally adjusted figure is 2,230.6, or -9.3%. So the more-than-10% test is not met on reported facts, and I do not rate it Critical.
- **Confidence:** High for the reported decline. Medium for the run-rate, which depends on an annualization assumption.
- **Deal impact:** Valuation, and financing (lender covenants sized on 171.2).
- **Cross-check:** Q3 2026 10-Q (it would be due before the December 9 vote), the proxy's management projections, and any guidance cut in the news.

#### FIN-03: A change in accounting estimate (contract cost amortization moved from 6 to 10 years) inflates EBITDA and is not supported by churn
- **Finding:** In FY2025 the company extended the amortization period for capitalized sales commissions from 6 to 10 years. That amortization sits in SG&A and is not added back, so the longer period lifts EBITDA. Renewal data now implies an average customer life of about 7.6 years, not 10.
- **Evidence:**
  - The net capitalization proxy for the lower amortization is this. Net growth in capitalized contract costs was 5.1 in FY2024. It was 8.6 in FY2025 (2.2 in H1 2025, so 6.4 in H2 2025) and 6.0 in H1 2026. LTM net growth = 8.6 - 2.2 + 6.0 = 12.4. Compared with the FY2024 pace of 5.1, that is about 7.3 of lower amortization in the LTM (estimate, inference).
  - The H2 2025 step-up suggests the change took effect in H2 2025 (inference).
  - 7.3 is 4.3% of 171.2. At 14.4x it is about 105.1 of value.
  - Implied customer life = 1 / (1 - renewal rate). That gives 1 / 0.094 = 10.6 years at FY2025 (90.6% renewal) and 1 / 0.131 = 7.6 years at June 2026 (86.9%).
  - The contracts themselves run five years (deal brief, thesis 1).
  - The balance sheet asset grew from 83.5 to 98.1, up 17.5% in 18 months, while revenue was flat.
- **Source:** `financials/kpis.csv`, rows "Capitalized contract acquisition costs, amortization period" and "Maintenance contract renewal rate"; `financials/cash_flow.csv`, row "Change in capitalized contract acquisition costs"; `financials/balance_sheet.csv`, row Capitalized contract acquisition costs; `financials/README.md` (amortization is in SG&A).
- **Severity:** High. It needs a price adjustment and the deal brief's IC question 1 asks about it directly. On its own it is below 10% of value.
- **Confidence:** Medium. The change is stated, but the EBITDA effect is my proxy. The actual amortization expense is not in the files.
- **Deal impact:** Valuation (earnings base), and a possible future impairment of the 98.1 asset if churn stays high.
- **Cross-check:** The 10-K note on the change in estimate (the stated effect on SG&A and EPS), the 10-Q contract cost note, and the auditor's preferability or critical audit matter discussion.

#### FIN-04: Contract cancellation fees are churn-driven income inside revenue
- **Finding:** Revenue includes cancellation fees, which are paid when customers leave. They rose from 6.1 to 9.8 (FY2023 to FY2025) and were 6.2 in the latest column, as renewal fell. They are one-time by nature and should not be capitalized at 14.4x.
- **Evidence:**
  - Cancellation fees as a share of revenue: 9.8 / 1,067.7 = 0.9% in FY2025.
  - Assuming the fees carry full margin (an inference): 9.8 / 186.4 = 5.3% of FY2025 Adjusted EBITDA, and 6.2 / 171.2 = 3.6% of LTM.
  - 6.2 x 14.4 = 89.3 of value.
  - The KPI column header says TTM for rates, but this row is an amount. If 6.2 is H1 2026 only, the annualized figure is 12.4. That needs clarification.
- **Source:** `financials/kpis.csv`, row "Contract cancellation fees recognized in revenue"; README column definition.
- **Severity:** Medium
- **Confidence:** Medium. The amount is stated, but the margin and the period of the last column are assumptions.
- **Deal impact:** Valuation (normalization).
- **Cross-check:** The 10-Q revenue disaggregation note and the MD&A discussion of cancellations.

#### FIN-05: Branch consolidation and ERP costs recur every year but are added back as "non-recurring"
- **Finding:** Branch consolidation costs have been added back in every year from FY2022 to LTM. ERP costs have been added back for four years running. Both behave like normal operating costs.
- **Evidence:**
  - Branch consolidation: 1.4, 0.9, 1.2, 1.6, LTM 1.6 - 0.7 + 0.9 = 1.8.
  - ERP: 0.0, 1.1, 1.4, 0.9, LTM 0.9 - 0.5 + 0.4 = 0.8.
  - Together 2.6 in the LTM, which is 1.5% of 171.2, or 37.4 at 14.4x.
- **Source:** `financials/adjusted_ebitda_reconciliation.csv`, Detail rows.
- **Severity:** Medium
- **Confidence:** High. Recomputed directly.
- **Deal impact:** Valuation (small).
- **Cross-check:** The non-GAAP definitions in the 10-K and 10-Q. Ask whether the branch conversion plan (thesis 3) will add more add-backs of this kind.

#### FIN-06: M&A-related cost add-back is properly excluded
- **Finding:** M&A costs (1.9 FY2024, 3.8 FY2025, 2.6 LTM) line up with the Pinecrest acquisition (March 2025) and the Brockmere agreement (June 2026). They are shown on their own income statement line and are a reasonable exclusion.
- **Evidence:** The income statement line "Merger and acquisition-related costs" equals the add-back in each period.
- **Source:** `financials/income_statement.csv`, row 11; `financials/adjusted_ebitda_reconciliation.csv`, row 9; README (Pinecrest note); deal brief section 4.
- **Severity:** Low
- **Confidence:** High. Stated in the company financials.
- **Deal impact:** None. Note that H2 2026 will carry the costs of this merger and of the Brockmere termination.
- **Cross-check:** Brockmere termination terms in the 8-K or proxy.

#### FIN-07: The stock-based compensation add-back would become a cash cost under private ownership
- **Finding:** SBC of 12.9 in the LTM (7.5% of Adjusted EBITDA) is added back. Under private ownership it is typically replaced by a cash or equity incentive plan (inference).
- **Evidence:**
  - 12.9 / 171.2 = 7.5% of LTM Adjusted EBITDA.
  - SBC has grown every year: 9.8, 10.6, 11.5, 12.4.
  - 12.9 x 14.4 = 185.8 of value, which is 7.6% of EV.
- **Source:** `financials/adjusted_ebitda_reconciliation.csv`, row 7.
- **Severity:** Medium. This is a sensitivity; adding back SBC is common market practice.
- **Confidence:** Medium. How it is treated after closing is an assumption.
- **Deal impact:** Valuation (sensitivity) and the post-closing cost base.
- **Cross-check:** The post-closing management incentive plan in the merger agreement or the rollover terms.

#### FIN-08: The Q1 2026 out-of-period adjustment of 4.1 means prior periods were misstated
- **Finding:** Cost of revenue in Q1 2026 includes a 4.1 charge that relates to earlier periods. So earlier periods' cost of revenue was understated by that amount. The files do not say which periods.
- **Evidence:**
  - The 4.1 is 0.8% of H1 2026 revenue (4.1 / 510.8) and 5.5% of H1 2026 Adjusted EBITDA (4.1 / 74.7).
  - Restatement risk for the affected prior periods (inference). It is immaterial to FY2025 on its own: 4.1 / 186.4 = 2.2%.
  - If all of it relates to periods before the LTM window, the LTM base is understated by 4.1.
  - If it relates to H2 2025, the LTM effect is nil but FY2025 is overstated by 4.1.
- **Source:** `financials/README.md`, Notes bullet 3; `financials/income_statement.csv`, Cost of revenue H1 2026.
- **Severity:** Medium
- **Confidence:** High that the adjustment exists; Low on which periods it belongs to.
- **Deal impact:** Valuation (base) and the controls representation.
- **Cross-check:** The 10-Q note (the nature of the error and the periods affected), the Q1 2026 10-Q controls section (Item 4) for any deficiency, and the auditor's communications.

#### FIN-09: A loss provision of 5.2 on a fixed-price modernization contract signals execution risk in a shrinking segment
- **Finding:** In Q2 2026 the company booked a 5.2 estimated loss on a fixed-price modernization contract. At the same time, modernization revenue fell 12.0% and contract assets rose.
- **Evidence:**
  - 5.2 / 92.1 = 5.6% of H1 2026 modernization revenue.
  - Excluding both the 4.1 and the 5.2, the H1 2026 gross margin would be (159.4 + 9.3) / 510.8 = 33.0%. That is still below H1 2025 at 33.6%.
  - The company did not add the 5.2 back in its Adjusted EBITDA. I also keep it in, because loss contracts can recur in fixed-price work.
- **Source:** `financials/README.md`, Notes bullet 3; `financials/income_statement.csv`.
- **Severity:** Medium
- **Confidence:** High for the amount; Medium on whether such losses recur.
- **Deal impact:** Valuation and post-closing integration (bidding discipline on modernization).
- **Cross-check:** The 10-Q contract loss disclosure, and news or litigation about a named modernization project.

#### FIN-10: The normalized earnings base is 155.1 to 159.2, which implies 2,233.4 to 2,292.5 at 14.4x (projection)
- **Finding:** After taking out items that will not recur at the same level, the LTM base is 155.1 to 159.2, against 171.2. At the deal's own 14.4x, that implies 6.8% to 9.2% less value. Treating SBC as a cash cost takes the gap to 14.3%.
- **Evidence (all projection, US$m):**

| Step | Amount |
|---|---|
| Reported LTM Adjusted EBITDA | 171.2 |
| Less recurring branch consolidation (FIN-05) | -1.8 |
| Less recurring ERP (FIN-05) | -0.8 |
| Less cancellation fees, one-time income (FIN-04) | -6.2 |
| Less amortization period benefit, proxy (FIN-03) | -7.3 |
| Subtotal (low case) | 155.1 |
| Plus out-of-period charge, if it belongs entirely to pre-LTM periods (FIN-08) | +4.1 |
| Normalized buyer case (high case) | 159.2 |

  - Implied EV at 14.4x: 159.2 x 14.4 = 2,292.5, which is -167.0 or -6.8% against 2,459.5.
  - Low case: 155.1 x 14.4 = 2,233.4, which is -226.1 or -9.2%.
  - Deal EV on the normalized base = 2,459.5 / 159.2 = 15.4x (15.9x on 155.1).
  - Sensitivity with SBC as a cash cost: 159.2 - 12.9 = 146.3, and 146.3 x 14.4 = 2,106.7, which is -352.8 or -14.3%.
  - Break-even for the 10% test: a base reduction of 17.1 (10% of 171.2). The other adjustments net to 4.7 (1.8 + 0.8 + 6.2 - 4.1). So the amortization benefit would have to be at least 12.4 for the high case to cross 10%; for the low case, at least 8.3.
  - I kept the 5.2 contract loss in. Adding it back would give 164.4, or 2,367.4 at 14.4x.
  - No source in my files gives a probable but unrecorded cost. If the lead agent has one (for example a multiemployer withdrawal liability or a code-compliance obligation), it should be deducted on top of this.
- **Source:** `financials/adjusted_ebitda_reconciliation.csv`; `financials/kpis.csv`; `financials/README.md`; deal brief section 2.
- **Severity:** High. The company-definition normalization is below 10% of value. The more-than-10% test is met only in the SBC-as-cash sensitivity, which is a buyer policy choice, so I do not rate it Critical.
- **Confidence:** Medium. It depends on the FIN-03 proxy and the FIN-08 allocation.
- **Deal impact:** Valuation (price), and financing (leverage on the normalized base is 1,325.0 / 159.2 = 8.3x).
- **Cross-check:** A quality-of-earnings report, the actual contract cost amortization expense, and the periods of the out-of-period error.

#### FIN-11: Quarterly revenue broke trend in Q1 2026
- **Finding:** Revenue fell from 277.1 in Q4 2025 to 250.2 in Q1 2026 (-9.7%), and both 2026 quarters are below a year earlier. In earlier years, Q1 was flat to up on the prior Q4.
- **Evidence:**
  - Q1 against the prior Q4: Q1 2023 vs Q4 2022 = 219.3 / 210.4 = +4.2%; Q1 2024 = 238.4 / 232.4 = +2.6%; Q1 2025 = 252.1 / 252.1 = 0.0%; Q1 2026 = 250.2 / 277.1 = -9.7%.
  - Year on year: Q1 2026 = 250.2 / 252.1 = -0.8%; Q2 2026 = 260.6 / 263.9 = -1.3%.
  - Q3 2025 grew +10.5% and Q4 2025 +9.9% year on year, both helped by Pinecrest.
  - This decline comes even though Pinecrest was in the base for the full quarter, against only one month in Q1 2025.
- **Source:** `financials/revenue_quarterly.csv`, rows Q4 2022 to Q2 2026.
- **Severity:** High
- **Confidence:** High. Recomputed directly.
- **Deal impact:** Valuation (the growth thesis).
- **Cross-check:** Q3 2026 revenue, the MD&A explanation, and news about lost contracts or a strike.

#### FIN-12: Segment growth: repair and modernization are contracting and maintenance is slowing
- **Finding:** H1 2026 repair revenue fell 6.0% and modernization fell 12.0%. Maintenance grew only 2.7% while units fell. LiftSense is the only segment still growing fast.
- **Evidence (growth by year):**

| Segment | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---|---|---|---|
| Maintenance | 506.0 / 468.0 = +8.1% | +6.9% | 588.6 / 541.0 = +8.8% | 291.8 / 284.0 = +2.7% |
| Repair | +9.3% | +7.5% | +6.7% | 104.3 / 111.0 = -6.0% |
| Modernization and installation | +15.2% | +11.5% | +5.8% | 92.1 / 104.6 = -12.0% |
| LiftSense | +50.0% | +44.4% | +38.1% | +37.8% |

  - Repair revenue per unit fell from US$1,296 to US$1,241 (-4.2%).
- **Source:** `financials/income_statement.csv`, Revenue rows; `financials/kpis.csv`, Repair revenue per unit row.
- **Severity:** Medium. This is the segment detail behind FIN-11 and FIN-17.
- **Confidence:** High
- **Deal impact:** Valuation
- **Cross-check:** Segment discussion in the 10-Q MD&A.

#### FIN-13: LiftSense growth matches the deal brief and supports the connected-services thesis
- **Finding:** The brief's growth rates recompute (38.1% in FY2025 and 37.8% in H1 2026). Connected units reached 61,900. Revenue per connected unit is easing slightly.
- **Evidence:**
  - Revenue growth: 35.9 / 26.0 = +38.1%, and 22.6 / 16.4 = +37.8%.
  - Units grew 64.3% in FY2024 (34,500 / 21,000), 53.0% in FY2025 (52,800 / 34,500), and 17.2% in H1 2026 (61,900 / 52,800).
  - Revenue per average unit: FY2025 35.9 / 43,650 = US$822; H1 2026 annualized 45.2 / 57,350 = US$788 (-4.1%).
  - The 110,000 target needs +48,100 units in about 3.5 years.
  - LiftSense is 22.6 / 510.8 = 4.4% of revenue.
- **Source:** `financials/income_statement.csv`, LiftSense row; `financials/kpis.csv`, Connected units row; deal brief thesis 2.
- **Severity:** Low (positive)
- **Confidence:** High
- **Deal impact:** Valuation (supports the thesis)
- **Cross-check:** Investor presentation LiftSense disclosures.

#### FIN-14: 9,800 LiftSense units (15.8%) sit on LTE-M modules facing a 2027 network sunset
- **Finding:** 9,800 of 61,900 connected units rely on LTE-M modules that the company itself flags for a 2027 network sunset. Replacing them is a cost, and possibly a churn risk, that the files do not quantify.
- **Evidence:**
  - 9,800 / 61,900 = 15.8% of connected units. That exposure was 0 at FY2023, 4,200 at FY2024 and 8,700 at FY2025.
  - Sensitivity: each US$100 per unit of replacement cost is 0.98. The per-unit cost is not in the sources.
- **Source:** `financials/kpis.csv`, row "Connected units on LTE-M modules subject to 2027 network sunset".
- **Severity:** Medium
- **Confidence:** High for the exposure; Low for the cost.
- **Deal impact:** Post-closing capex or opex
- **Cross-check:** 10-K risk factors, carrier sunset notices in the news, and the module supplier contract (who bears the replacement cost).

#### FIN-15: Units under contract fell 4.7% in H1 2026 and the renewal rate dropped to 86.9%
- **Finding:** The "about 168,000 units" in the thesis is the June 30, 2026 figure, after a loss of 8,200 units in six months. Churn has nearly doubled since FY2023, so the recurring base is shrinking.
- **Evidence:**
  - Units: 176,300 to 168,100 = -8,200, or -4.7%.
  - Pinecrest units: 9,600 to 9,100 (-5.2%).
  - Organic units: 166,700 to 159,000 (-4.6%), and 3.6% below the 164,900 at Dec 2024.
  - Renewal rate: 92.8%, 92.3%, 90.6%, 86.9%, so churn went from 7.2% to 13.1%.
  - Comprehensive-contract units fell from 68,400 to 66,900 (-2.2%).
  - Maintenance gross margin fell from 37.1% to 34.6% (see FIN-18).
- **Source:** `financials/kpis.csv`, rows 2, 3, 4 and 6.
- **Severity:** High
- **Confidence:** High
- **Deal impact:** Valuation (the recurring-base thesis), plus the FIN-03 amortization assumption.
- **Cross-check:** 10-Q MD&A on renewal, news about competitor wins or customer complaints, and any litigation over service quality.

#### FIN-16: FY2025 growth was partly bought (Pinecrest); organic growth is not disclosed
- **Finding:** Pinecrest (acquired March 3, 2025 for 152.0) contributed 9,600 units. Organic unit growth in FY2025 was only 1.1%. The files do not give Pinecrest's revenue, so organic revenue growth cannot be computed.
- **Evidence:**
  - Organic units at FY2025 = 176,300 - 9,600 = 166,700, against 164,900, which is +1.1%.
  - Reported revenue growth was 8.5%.
  - The acquisition added goodwill of 501.0 - 412.6 = 88.4, and intangibles of 105.4 - 68.8 + 15.4 amortization = 52.0.
- **Source:** `financials/kpis.csv`, rows 2 and 3; `financials/README.md`; `financials/balance_sheet.csv`, Goodwill and Intangibles; `financials/income_statement.csv`, amortization row.
- **Severity:** Medium
- **Confidence:** High for units; revenue cannot be determined.
- **Deal impact:** Valuation (quality of growth)
- **Cross-check:** The 10-K business combination note (Pinecrest revenue since acquisition, pro forma revenue).

#### FIN-17: Modernization backlog fell 17.0%, and implied H1 2026 bookings were only 16.1
- **Finding:** Backlog fell from 448.0 to 372.0 in six months. Implied H1 2026 bookings were about 16.1, a book-to-bill of 0.17, against 0.97 in FY2025. This points to further modernization revenue decline (projection).
- **Evidence:**
  - Implied bookings = ending backlog - opening backlog + revenue.
  - H1 2026: 372.0 - 448.0 + 92.1 = 16.1, so book-to-bill = 16.1 / 92.1 = 0.17.
  - FY2025: 448.0 - 455.0 + 214.8 = 207.8, so 0.97.
  - FY2024: 455.0 - 412.0 + 203.0 = 246.0, so 1.21.
  - Caveat: backlog cancellations, or installation revenue that sits outside backlog, would change implied bookings (inference).
- **Source:** `financials/kpis.csv`, Backlog row; `financials/income_statement.csv`, Modernization row.
- **Severity:** High
- **Confidence:** Medium. The bookings figure is derived, and the backlog definition is not given.
- **Deal impact:** Valuation (FY2026 to FY2027 revenue)
- **Cross-check:** 10-Q backlog and remaining performance obligations note, and any cancelled projects in the news.

#### FIN-18: Gross margin and maintenance margin are declining
- **Finding:** Gross margin fell from 34.0% in FY2023 to 31.2% in H1 2026, and is 33.0% excluding the two disclosed H1 charges. Maintenance gross margin fell from 38.9% to 34.6%.
- **Evidence:**
  - Gross margin: FY2022 277.2 / 820.0 = 33.8%; FY2023 34.0%; FY2024 33.9%; FY2025 356.6 / 1,067.7 = 33.4%; H1 2025 33.6%; H1 2026 159.4 / 510.8 = 31.2%. LTM = 342.6 / 1,062.5 = 32.2%.
  - SG&A rose from 20.0% of revenue (214.0 / 1,067.7) to 21.1% (107.6 / 510.8).
- **Source:** `financials/income_statement.csv`, Gross profit and SG&A rows; `financials/kpis.csv`, Maintenance gross margin row.
- **Severity:** High
- **Confidence:** High
- **Deal impact:** Valuation
- **Cross-check:** MD&A on labor cost (the collective agreement wage schedule) and pricing.

#### FIN-19: Technician attrition rose to 17.1% while headcount fell
- **Finding:** Voluntary attrition among field technicians has risen every year, and headcount fell by 90 in H1 2026. That is a service quality and labor cost risk, and it bears on the branch conversion plan (FIN-32).
- **Evidence:**
  - Attrition: 11.2%, 12.0%, 14.6%, 17.1%.
  - Technicians: 4,380 to 4,290 (-2.1%).
  - Units per technician: 176,300 / 4,380 = 40.3, against 168,100 / 4,290 = 39.2.
  - Covered by the collective agreement: 4,290 x 79% = 3,389, which matches the brief's "roughly 3,390".
- **Source:** `financials/kpis.csv`, rows 12 to 14; deal brief thesis 3.
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Post-closing integration and the cost base
- **Cross-check:** News on labor relations and union statements, and NLRB filings.

#### FIN-20: Customer concentration is low and stable
- **Finding:** The top customer is 2.3% of revenue and the top 10 are 14.8% (FY2025), against 14.7% in FY2024. No single customer is material.
- **Evidence:**
  - FY2025 ranking and revenue (FY2024 revenue in brackets):
    1. Harrowgate Residential REIT, 24.6 (22.9)
    2. Commonwealth Office Properties Trust, 21.7 (20.8)
    3. Lanark Hospitality Group, 18.9 (17.3)
    4. Northfield University System, 16.2 (15.1)
    5. Calder Mall Partners, 15.4 (15.6, the only top-10 customer to decline, -1.3%)
    6. St. Aldric Health System, 14.8 (9.8, +51.0%, possibly Pinecrest-related, an inference)
    7. Brightline Senior Living, 13.1 (12.2)
    8. Ferris Park Housing Cooperative, 12.0 (11.6)
    9. Penwick Industrial Logistics, 10.7 (9.4)
    10. Tolland Medical Partners, 10.2 (9.9)
  - Top 10 FY2025 = 157.6, and 157.6 / 1,067.7 = 14.8%.
  - Top 10 FY2024 = 144.6, and 144.6 / 984.0 = 14.7%.
  - Top-10 growth = +9.0%.
  - No H1 2026 customer data is provided.
- **Source:** `financials/revenue_by_customer.csv`, rows 1 to 10 and Total.
- **Severity:** Low (positive)
- **Confidence:** High
- **Deal impact:** None
- **Cross-check:** Check any customer named in news or litigation against this list.

#### FIN-21: DSO is stable at about 61 days; allowance data is missing
- **Finding:** DSO has been flat at 61.0 days, and the inventory days ratio is flat at about 19 days. The files have no gross receivables or allowance, so the allowance percentage cannot be computed.
- **Evidence:**
  - DSO FY2023 = 151.3 / 905.0 x 365 = 61.0.
  - DSO FY2024 = 164.4 / 984.0 x 365 = 61.0.
  - DSO FY2025 = 178.4 / 1,067.7 x 365 = 61.0.
  - DSO June 2026 = 172.6 / 1,062.5 x 365 = 59.3 on LTM revenue, or 61.7 on H1 annualized revenue of 1,021.6.
  - Inventory days on cost of revenue: FY2025 = 36.9 / 711.1 x 365 = 18.9; June 2026 = 37.5 / 719.9 (LTM) x 365 = 19.0.
- **Source:** `financials/balance_sheet.csv`, AR and Inventories rows; `financials/income_statement.csv`.
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None
- **Cross-check:** The 10-K allowance roll-forward.

#### FIN-22: Contract assets are rising while modernization revenue falls
- **Finding:** Contract assets edged up from 44.6 to 45.3 while modernization revenue fell 12.0%. Measured against annualized modernization revenue, contract assets rose from 20.8% to 24.6%. Combined with the FIN-09 loss contract, this points to slower billing or estimate risk.
- **Evidence:** FY2025 44.6 / 214.8 = 20.8%; June 2026 45.3 / (92.1 x 2 = 184.2) = 24.6%.
- **Source:** `financials/balance_sheet.csv`, Contract assets; `financials/income_statement.csv`.
- **Severity:** Medium
- **Confidence:** Medium. Annualized modernization revenue is only a proxy for the revenue that contract assets relate to.
- **Deal impact:** Working capital peg
- **Cross-check:** 10-Q contract balances note.

#### FIN-23: Cash conversion is solid and free cash flow is positive
- **Finding:** Operating cash flow consistently runs above net income and converts about 70% of Adjusted EBITDA. LTM free cash flow is 86.9. H1 2026 operating cash flow was helped by a 5.8 fall in receivables.
- **Evidence:**
  - OCF / net income: FY2023 102.1 / 61.1 = 1.67x; FY2025 128.4 / 62.9 = 2.04x; H1 2026 41.0 / 15.7 = 2.61x.
  - LTM OCF = 128.4 - 47.2 + 41.0 = 122.2. That is 79.8% of EBITDA (153.1) and 71.4% of Adjusted EBITDA (171.2).
  - FCF FY2023 to FY2025: 74.2, 89.7, 94.9.
  - H1 2026 FCF = 41.0 - 17.4 = 23.6, against 31.6 in H1 2025.
  - LTM FCF = 94.9 - 31.6 + 23.6 = 86.9.
- **Source:** `financials/cash_flow.csv`, rows 2, 8, 18 and 19.
- **Severity:** Low (positive)
- **Confidence:** High
- **Deal impact:** Financing (debt service capacity, but see FIN-25)
- **Cross-check:** Q3 2026 cash flow.

#### FIN-24: Net debt and leverage in the deal brief recompute; the revolver is undrawn
- **Finding:** Net debt of 542.2 ties. Leverage is 3.17x net on Adjusted EBITDA and 3.54x net on EBITDA. The revolver was repaid to nil by June 30, 2026.
- **Evidence:**
  - Principal 245.0 + 400.0 = 645.0, less cash 102.8 = 542.2.
  - Carrying amount 2.5 + 637.8 = 640.3, so unamortized costs are 4.7.
  - Gross / Adjusted EBITDA = 645.0 / 171.2 = 3.77x. Net / Adjusted EBITDA = 3.17x. Gross / EBITDA = 645.0 / 153.1 = 4.21x. Net / EBITDA = 3.54x.
  - Revolver: +90.0 drawn in H1 2025 (Pinecrest), net +20.0 for FY2025, -20.0 in H1 2026, so nil.
  - Interest cover (LTM): Adjusted EBITDA 171.2 / 42.2 = 4.06x; EBITDA 3.63x; operating income 106.7 / 42.2 = 2.53x.
  - Operating lease liabilities of 73.8 are excluded from net debt.
- **Source:** `financials/balance_sheet.csv`, debt and cash rows; `financials/cash_flow.csv`, rows 26 and 27; README bullet 4.
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None standing alone
- **Cross-check:** The 10-Q debt note (revolver size, term loan maturity and covenants, none of which are in my files).

#### FIN-25: Pro forma leverage of 7.7x ties, but it is 8.7x on EBITDA and 8.3x on the normalized base, with interest cover near 1.9x (projection)
- **Finding:** Pro forma debt of 1,325.0 / 171.2 = 7.74x ties to the brief. On weaker bases it is 8.65x (EBITDA 153.1), 8.32x (normalized 159.2) and 8.87x (H1 run-rate 149.4).
- **Evidence:**
  - Implied current term loan rate = (42.2 interest - 23.5 notes coupon at 400.0 x 5.875% - 1.4 fee amortization) / 245.0 = 7.1% (inference).
  - Pro forma interest = 23.5 + 925.0 x 7.06% (65.3) = about 88.8 (projection).
  - Adjusted EBITDA / pro forma interest = 171.2 / 88.8 = 1.93x, or 1.79x on 159.2.
  - Pro forma FCF = LTM FCF 86.9 + current cash interest (42.2 - 1.4 = 40.8) - 88.8 = about 38.9 before the tax shield (projection).
  - Cash after closing = 102.8 - 30.0 = 72.8. Pro forma net debt = 1,252.2, or 7.31x.
- **Source:** Deal brief section 2 and sources and uses; `financials/adjusted_ebitda_reconciliation.csv`; `financials/cash_flow.csv`; README bullet 4.
- **Severity:** High
- **Confidence:** Medium. The new loan's pricing is not in the sources; I assumed the current loan's rate.
- **Deal impact:** Financing
- **Cross-check:** Debt commitment letters in the proxy (pricing, flex, covenants, any EBITDA definition that includes add-backs).

#### FIN-26: The model assumes the 2030 notes stay outstanding; a change-of-control put would leave about 404.0 unfunded
- **Finding:** The sources and uses keep the 400.0 notes in place. If the indenture gives holders a put at 101% on a change of control (the standard term, but not confirmed in my files), funding of 404.0 is not provided for. Cash after closing is 72.8.
- **Evidence:**
  - The put would cost 400.0 x 1.01 = 404.0 plus accrued interest, against 72.8 of cash left after closing.
  - The shortfall is about 331.2 before any revolver use (projection).
  - At 7.7x leverage, a 5.875% coupon may sit below market for this credit, which gives holders a reason to put (inference).
- **Source:** Deal brief section 2 and sources and uses; `financials/README.md`, bullet 4.
- **Severity:** High. It is a financing gap that can be cured by committed backstop financing at closing (calibration rule). Rate it Critical only if no backstop exists and the funding gap blocks closing.
- **Confidence:** Medium. The indenture terms are not in my files.
- **Deal impact:** Financing and closing risk
- **Cross-check:** The 2030 notes indenture (8-K, 2024) and the commitment letters (bridge or backstop for a notes put).

#### FIN-27: Sources and uses tie, but the uses leave out several known or likely costs
- **Finding:** Both sides add up to 2,278.6. The equity value includes Pell's 0.45 million rolled shares, which the 18.7 rollover offsets correctly. The uses leave out the target's own transaction costs, any Brockmere termination cost, change-in-control severance, accrued interest and a possible notes put (FIN-26). None of those amounts is in my files.
- **Evidence:**
  - Uses = 1,917.3 + 52.3 + 245.0 + 64.0 = 2,278.6.
  - Sources = 925.0 + 1,304.9 + 18.7 + 30.0 = 2,278.6.
  - Equity value = 46.20 x 41.50 = 1,917.3. Rollover = 0.45 x 41.50 = 18.7.
  - The brief says the 64.0 covers buyer fees only.
- **Source:** Deal brief sections 1 and 2.
- **Severity:** Medium
- **Confidence:** High for the arithmetic; Low for the size of what is omitted.
- **Deal impact:** Price and financing
- **Cross-check:** The proxy (target advisor fees including Pellham Rowe, golden parachute table), and the Brockmere agreement termination fee.

#### FIN-28: The deal EV leaves out the 52.3 equity award cash-out; the fully diluted multiple is 14.7x
- **Finding:** The brief computes EV on basic shares. Adding the award cash-out, which is economically part of the equity price, gives an EV of 2,511.8.
- **Evidence:**
  - 1,917.3 + 52.3 + 542.2 = 2,511.8.
  - 2,511.8 / 171.2 = 14.67x LTM, and 2,511.8 / 186.4 = 13.48x FY2025.
  - On the normalized 159.2 it is 15.78x.
- **Source:** Deal brief sections 1 and 2.
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation (the headline multiple is understated)
- **Cross-check:** The proxy's fully diluted share count and award table.

#### FIN-29: Known deal costs total 116.3, which is 4.7% of EV
- **Finding:** The equity award cash-out (52.3) and the buyer fees and expenses (64.0) are fixed, known deal costs. Together they are 116.3, or 4.7% of EV, which is below the 5% threshold. Severance and any Brockmere termination cost are not quantified in my files and would add to this.
- **Evidence:** 52.3 + 64.0 = 116.3, and 116.3 / 2,459.5 = 4.7%. Headroom to the 5% threshold = 123.0 - 116.3 = 6.7.
- **Source:** Deal brief, sources and uses.
- **Severity:** Medium (price item). It moves to High if severance or termination fees add more than 6.7.
- **Confidence:** High
- **Deal impact:** Price
- **Cross-check:** The proxy's golden parachute table and the Brockmere agreement.

#### FIN-30: The NOL model is inconsistent with its own Section 382 limit and with post-LBO taxable income
- **Finding:** The brief values all 66.8 of tax-effected NOLs as used in FY2027 to FY2029. At its own limit of 65.2 a year, only 195.6 of the 318 gross can be used in three years. After the buyout's interest cost, taxable income looks far below the roughly 106 a year that full use would need (projection).
- **Evidence:**
  - Tax-effected value: 318 x 21% = 66.8, which ties.
  - Implied rate behind the limit: 65.2 / 1,917.3 = 3.40%.
  - Three years x 65.2 = 195.6 gross, worth 41.1 tax-effected. That leaves 25.7 deferred beyond 2029.
  - Full use needs 318 / 3 = 106 a year of taxable income.
  - Pro forma pretax proxy = 171.2 - 45.0 D&A - 12.9 SBC - 88.8 interest (FIN-25) = about 24.5 (projection, which ignores the section 163(j) interest limit and tax-to-book differences).
- **Source:** Deal brief thesis 5; `financials/adjusted_ebitda_reconciliation.csv`.
- **Severity:** Medium
- **Confidence:** High for the arithmetic; Medium for taxable income.
- **Deal impact:** Valuation (the tax model)
- **Cross-check:** The 10-K income tax note (NOL expiry, existing limitations) and the buyer's tax advisors.

#### FIN-31: The slow drawdown of deferred tax assets suggests the NOLs are already limited
- **Finding:** The net deferred tax asset falls by only 2.4 a year, while the company books about 18.0 of current tax on 83.3 of pretax income. That pattern suggests an existing annual limit on NOL use of about 11.4 gross (inference). If such a limit exists, a new ownership change generally cannot raise it, so the model's 65.2 limit would not apply (a question for tax counsel).
- **Evidence:**
  - Deferred tax asset: 71.8 to 69.4 to 67.0 to 65.8. Deferred tax expense in the cash flow is 2.4 a year (1.2 per half).
  - FY2025 current tax = 20.4 - 2.4 = 18.0, an effective rate of 20.4 / 83.3 = 24.5%.
  - Implied gross NOL use = 2.4 / 21% = 11.4 a year (inference; other temporary differences also run through this line).
  - At that pace, use in FY2027 to FY2029 = 3 x 2.4 = 7.2, against 66.8 in the model.
  - Shortfall = 59.6, which is 2.4% of EV and 3.1% of equity value.
  - The net deferred tax asset (65.8) is already smaller than the NOL component (66.8).
- **Source:** `financials/balance_sheet.csv`, Deferred tax assets row; `financials/cash_flow.csv`, Deferred income taxes row; `financials/income_statement.csv`, tax rows; README bullet 5; deal brief thesis 5.
- **Severity:** High. It contradicts a named pillar of the investment thesis and needs a price adjustment. At 2.4% of EV it is not Critical.
- **Confidence:** Medium. The finding is inferred from the movement in deferred taxes; the tax note is not in my files.
- **Deal impact:** Valuation
- **Cross-check:** The 10-K tax note (any existing Section 382 limitation, possibly from a prior ownership change, and the valuation allowance).

#### FIN-32: The collective agreement and branch conversion carry a possible multiemployer withdrawal liability that the model omits
- **Finding:** 79% of technicians are covered by the Lift Mechanics agreement. Converting 14 branches (about 1,000 technicians, 29.5% of the covered group) could trigger a partial withdrawal from a multiemployer plan (inference). My files show no withdrawal liability and no pension line, and the model's 18.0 saving is net only of 6.0 of transition costs.
- **Evidence:**
  - 1,000 / 3,390 = 29.5% of covered technicians, and 1,000 / 4,290 = 23.3% of all technicians.
  - Model saving = 18.0 / 1,000 = US$18,000 per technician a year.
  - Rising attrition (17.1%, FIN-19) adds execution risk.
  - Break-even: a liability of 246.0 would be 10% of EV, and 33.2 would be 10% of reported equity.
- **Source:** `financials/kpis.csv`, rows 12 to 14; `financials/balance_sheet.csv` (no pension line; other long-term liabilities 43.0); deal brief thesis 3.
- **Severity:** Medium on my data alone. Re-rate if the lead agent has a withdrawal liability estimate from the 10-K multiemployer note: above 24.6 (1% of EV) it is material to the saving's value, and above 246.0 the Critical test applies.
- **Confidence:** Low. This is an inference; my files contain no plan data.
- **Deal impact:** Valuation and post-closing
- **Cross-check:** The 10-K multiemployer plan note (plan name, funded zone, estimated withdrawal liability), Form 5500 filings, and union statements in the news.

#### FIN-33: The balance sheet shows no defined benefit pension; AOCI is flat
- **Finding:** There is no separate pension liability line, and accumulated other comprehensive loss is exactly -6.2 at every date. That pattern is unusual if a remeasured defined benefit plan exists (inference).
- **Evidence:** AOCI is -6.2 at FY2023, FY2024, FY2025 and June 2026.
- **Source:** `financials/balance_sheet.csv`, AOCI row and Other long-term liabilities row.
- **Severity:** Low
- **Confidence:** Low. Directional only.
- **Deal impact:** None identified
- **Cross-check:** The 10-K pension and AOCI notes.

#### FIN-34: 22,400 comprehensive-contract units are in Illinois and New Jersey (code-compliance exposure base)
- **Finding:** The company tracks full-coverage units in Illinois and New Jersey separately: 22,400, which is 33.5% of comprehensive units. If a code change makes Meridale bear upgrade costs under full-coverage terms, this is the base. My files give no cost.
- **Evidence:**
  - 22,400 / 66,900 = 33.5% of comprehensive units, and 22,400 / 168,100 = 13.3% of all units.
  - Break-even: US$10,980 per unit equals 10% of EV (246.0 / 22,400), and US$1,480 per unit equals 10% of equity (33.2 / 22,400).
- **Source:** `financials/kpis.csv`, row 5.
- **Severity:** Medium (break-even only). Apply the unrecorded-liability test if another source says the cost is probable.
- **Confidence:** High for the base; there is no cost data.
- **Deal impact:** Valuation and indemnity
- **Cross-check:** 10-K contingencies, and state code rulemaking in the news (Illinois and New Jersey).

#### FIN-35: The Laurent-Meridale JV is carried at 9.7; there is no other data
- **Finding:** The 50% equity-method investment is in other long-term assets at 9.7, the figure the model uses. My files give no equity income, guarantees or JV liabilities.
- **Evidence:** 9.7 of the 16.0 in other long-term assets. 9.7 / 2,459.5 = 0.4% of EV.
- **Source:** `financials/README.md`, bullet 6; `financials/balance_sheet.csv`, Other long-term assets.
- **Severity:** Low (on my data)
- **Confidence:** High for the carrying amount
- **Deal impact:** Valuation (small), unless there are off-balance-sheet guarantees
- **Cross-check:** The 10-K equity-method note, Canadian litigation and news (IC question 2).

#### FIN-36: Goodwill and intangibles are large against equity; the impairment test date is not in my files
- **Finding:** Goodwill (501.0) and intangibles (97.1) total 598.1, which is 180% of book equity. The H1 2026 earnings decline is a possible trigger for an impairment review. Market capitalization at the unaffected price was well above book value.
- **Evidence:**
  - 598.1 / 331.6 = 180%.
  - Market capitalization at the unaffected price = 46.20 x 33.20 = 1,533.8, which is 4.6x book equity. The deal values equity at 1,917.3.
  - My files have no share price history and no test date.
- **Source:** `financials/balance_sheet.csv`, Goodwill and Intangibles rows; deal brief section 1.
- **Severity:** Low
- **Confidence:** Medium. The reporting-unit structure is unknown.
- **Deal impact:** None at the current price
- **Cross-check:** The 10-K goodwill note (annual test date, reporting units, headroom), and the share price since the test.

#### FIN-37: Liquidity is adequate and capex is modest
- **Finding:** Cash is 102.8, the revolver is undrawn, and capex is about 3.3% of revenue. There are no buybacks in H1 2026.
- **Evidence:**
  - Capex as a share of revenue: LTM 35.3 / 1,062.5 = 3.3%; FY2025 33.5 / 1,067.7 = 3.1%.
  - The PP&E roll-forward ties for H1 2026: 111.7 + 17.4 - depreciation 14.4 (22.7 - 8.3) = 114.7.
  - Buybacks were 0.0 in H1 2026, against 10.0 in H1 2025.
- **Source:** `financials/cash_flow.csv`, rows 19 and 28; `financials/balance_sheet.csv`, PP&E row.
- **Severity:** Low (positive)
- **Confidence:** High
- **Deal impact:** None
- **Cross-check:** The revolver size and maturity in the 10-K.

#### FIN-38: Reserves and accruals move in line with history; no detail is available
- **Finding:** Other accrued liabilities (49.9) and other long-term liabilities (43.0) rose 3.4 together in H1 2026. Accrued compensation fell 6.1, a seasonal bonus payout like H1 2025 (-5.6). The files give no breakdown of reserves (warranty, insurance, legal or loss contracts).
- **Evidence:** 47.6 + 41.9 = 89.5, rising to 49.9 + 43.0 = 92.9, a change of +3.4 that matches the cash flow line.
- **Source:** `financials/balance_sheet.csv`, rows 16, 18 and 22; `financials/cash_flow.csv`, rows 14 and 16.
- **Severity:** Low
- **Confidence:** Medium. There is no detail to check against.
- **Deal impact:** None identified
- **Cross-check:** 10-Q accrued liabilities and contingencies notes (is the 5.2 loss accrual in here, and are there any litigation reserves?).

#### FIN-39: Debt maturities: the senior notes run to 2030
- **Finding:** The 400.0 of 5.875% notes are due 2030. The term loan has only 2.5 a year of scheduled amortization. There is no near-term maturity wall before closing.
- **Evidence:** Current portion of long-term debt is 2.5 at every date. There was no term loan repayment in H1 2026, which is consistent with annual timing.
- **Source:** `financials/balance_sheet.csv`, row 19; `financials/README.md`, bullet 4; `financials/cash_flow.csv`, row 26.
- **Severity:** Low (positive)
- **Confidence:** High for the notes; the term loan maturity is not in my files.
- **Deal impact:** Financing (mitigant)
- **Cross-check:** The 10-K debt note.

#### FIN-40: The FY2024 loss on extinguishment of debt (41.2) is correctly excluded
- **Finding:** The 2024 refinancing loss (38.2 premium + 3.0 write-off) is a true one-off. It is properly added back and is not in the LTM base.
- **Evidence:**
  - 38.2 + 3.0 = 41.2. It ties to the add-back and to the cash flow (38.2 premium paid).
  - It explains the FY2024 dip in net income (35.3) and EBITDA (119.8).
- **Source:** `financials/README.md`, bullet 2; `financials/adjusted_ebitda_reconciliation.csv`, row 8; `financials/cash_flow.csv`, rows 7 and 24.
- **Severity:** Low (neutralized, correctly excluded)
- **Confidence:** High
- **Deal impact:** None
- **Cross-check:** The 2024 10-K debt note.

#### FIN-41: No embedded instructions in the source files
- **Finding:** None of the eight financial files or the deal brief contains text trying to instruct the agents.
- **Evidence:** Full read of each file.
- **Source:** All files listed above.
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None
- **Cross-check:** Not applicable.

### Positive or mitigating points
- **Reconciliation:** the Adjusted EBITDA reconciliation, net debt and sources and uses all recompute exactly (FIN-01, FIN-24, FIN-27).
- **Items correctly excluded:** the 2024 debt extinguishment loss (FIN-40) and the M&A costs (FIN-06) are properly kept out of Adjusted EBITDA.
- **Segment still growing:** LiftSense grew 37.8%, with 61,900 connected units (FIN-13). This is qualified by the LTE-M sunset exposure (FIN-14).
- **Concentration:** customer concentration is low, with the top customer at 2.3% and the top 10 at 14.8% (FIN-20).
- **Cash and liquidity:** cash conversion is solid and LTM FCF is 86.9 (FIN-23), but the post-LBO interest burden makes this a qualified positive (FIN-25). Liquidity is adequate, with the revolver undrawn (FIN-37).
- **Maturities:** there is no maturity wall before 2030 (FIN-39). This is qualified by the change-of-control put question (FIN-26).
- **Working capital:** DSO is stable at about 61 days (FIN-21).
- **Customer retention:** I found no retention positive. Renewal is deteriorating (FIN-15).

### Gaps and questions for management
1. The actual amortization of capitalized contract costs by period, and the stated effect of the change from 6 to 10 years on FY2025 and H1 2026 SG&A (FIN-03).
2. Which periods the 4.1 out-of-period adjustment relates to, its root cause, and the controls conclusion (FIN-08).
3. Whether the 6.2 of cancellation fees is TTM or H1 2026 only, and their margin (FIN-04).
4. Pinecrest revenue and EBITDA since acquisition; organic revenue growth (FIN-16).
5. The backlog definition, H1 2026 bookings and cancellations; the loss contract's name and remaining exposure (FIN-17, FIN-09).
6. The 2030 notes indenture change-of-control terms, and whether the commitment papers backstop a put (FIN-26).
7. New term loan pricing and covenants (FIN-25); the existing revolver size and term loan maturity (FIN-24, FIN-39).
8. The 10-K tax note: any existing Section 382 limitation, NOL vintages and expiry, valuation allowance (FIN-30, FIN-31).
9. The multiemployer plan: name, funded status, estimated complete and partial withdrawal liability (FIN-32); any defined benefit plans (FIN-33).
10. Illinois and New Jersey code-compliance obligations under comprehensive contracts, and the cost per unit (FIN-34).
11. The LTE-M replacement cost per unit, and who bears it (FIN-14).
12. Laurent-Meridale JV: equity income, guarantees and liabilities (FIN-35).
13. Goodwill test date, reporting units and headroom (FIN-36).
14. Gross receivables and the allowance for credit losses; a reserves breakdown (FIN-21, FIN-38).
15. Target-side transaction fees, change-in-control severance and any Brockmere termination fee (FIN-27, FIN-29).
16. Customer revenue for H1 2026, and churn by top customer (FIN-20).
17. Q3 2026 results, before the December 9 vote (FIN-02, FIN-11).
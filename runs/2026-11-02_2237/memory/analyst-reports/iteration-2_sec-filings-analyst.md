## SEC filings analyst: findings (iteration 2, narrow follow-up)

### Files reviewed
I read all five files in full. I also ran a Grep across the folder for: goodwill, impairment, reporting unit, dismiss, controller, deficiency, weakness, Halsey, Bramford, St. Aldric, subcontract, withdraw.
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/wren/data/sec-filings/MDLS_10-K_FY2025_excerpts.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/wren/data/sec-filings/MDLS_8-K_2026-02-25_fy2025-results.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/wren/data/sec-filings/MDLS_10-Q_Q2-2026_excerpts.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/wren/data/sec-filings/MDLS_8-K_2026-09-21_merger-agreement.md`
- `/Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/wren/data/sec-filings/MDLS_DEFM14A_2026_excerpts.md`

I did not open the iteration-1 report or anything outside my folder. Some Q8 items below may repeat iteration-1 findings. The lead should de-duplicate them, keeping the earlier ID as parent.

Two limits apply to every card. All the filings are labeled "excerpts", so where I write "not found in SEC filings", that means not found in these excerpts. The files contain no balance sheet, so reported equity is not found in SEC filings. I give percentages against EV (US$2,459.5m) and against equity value at the deal price: 46,200,000 record-date shares x US$41.50 = US$1,917.3m. No source text tried to instruct the agents.

### Short answers to the eight questions
1. The proxy says nothing about the October 6 letter, Halsey Rock's appraisal intention, Bramford's position or any appraisal demands received. The condition text is in the 8-K, and Parent may waive it (SEC-46, SEC-47).
2. No filing mentions the dismissals. No filing calls the accrual gap a deficiency, significant deficiency or material weakness. No filing ties the US$4.1m to any 2025 quarter (SEC-50, SEC-51).
3. Goodwill (test date, reporting units, headroom, interim test) is not found in SEC filings (SEC-52).
4. Not found: cost per unit, unit count by state, names of other states, and any discussion of the probability that Meridale bears the cost. The filings do give the combined Illinois and New Jersey unit count and the contract-form language. The proxy excludes the cost from the projections (SEC-53, SEC-54, SEC-55).
5. The agreement runs four years from July 1, 2026. An end date of June 30, 2030 is my inference; no filing states it. No clause on converting branches, subcontracting or withdrawal is found. The August case includes the new agreement. Whether it includes the LTE-M cost or the Laurent put is not found (SEC-56, SEC-57, SEC-58).
6. No filing says whether contract cost amortization is inside or outside the D&A add-back. Amounts are given for 2024 and 2025 only (SEC-59, SEC-60).
7. The proxy says nothing about St. Aldric and gives no accrual update (SEC-62).
8. Other matters: SEC-61 and SEC-63 to SEC-67.

### Findings

#### SEC-46: Proxy is silent on Halsey Rock's October 6 opposition, its appraisal intention and Bramford's position
- **Finding:** The DEFM14A was filed October 23, 2026, 17 days after the October 6 article. Its Background section mentions Halsey Rock only for March 2026. It does not mention the October 6 letter, Halsey Rock's stated plan to vote against and demand appraisal, Bramford's "leaning against" position, or any appraisal demands received.
- **Evidence:** The only Background entry is "March 2026. Halsey Rock Capital Management, then holding about 9% of the shares, asked for two board seats". The ownership table shows Halsey Rock at 5,267,000 shares (11.4%) and Bramford at 2,680,000 (5.8%), with no comment on how they will vote.
- **Source:** `targets/wren/data/sec-filings/MDLS_DEFM14A_2026_excerpts.md`, sections "Background of the merger (excerpts)" and "Security ownership of certain beneficial owners"
- **Severity:** High. This is a disclosure gap on a fact that bears directly on a closing condition (see SEC-47). It may call for supplemental disclosure before the vote.
- **Confidence:** Medium. The fact that the filing is silent is High. But these are excerpts, so the full proxy may cover the matter elsewhere.
- **Deal impact:** Disclosure and closing risk.
- **Cross-check:** Get the full DEFM14A and any proxy supplement or 8-K filed after October 23. Look for a Halsey Rock 13D amendment carrying the letter. Check news for any demands Halsey Rock has sent.

#### SEC-47: Halsey Rock's stake alone exceeds the 10% dissenting-shares condition, which only Parent may waive
- **Finding:** Parent does not have to close if holders of more than 10% of outstanding shares demand appraisal. Halsey Rock alone holds 11.4%. If it carries out its stated intention, the condition fails unless Parent waives it. The condition is for Parent's benefit only, so the Company cannot waive it.
- **Evidence:** The 8-K text reads: "holders of not more than 10% of the outstanding shares having demanded appraisal (a condition for the benefit of Parent only, which Parent may waive)". The proxy Summary repeats the 10% condition but does not mention the waiver. The Background says Ostrander Hale's US$41.50 best and final offer was "conditioned on ... the 10% appraisal condition". Math: 5,267,000 / 46,200,000 = 11.4%. Adding Bramford gives 7,947,000 / 46,200,000 = 17.2%.
- **Source:** `targets/wren/data/sec-filings/MDLS_8-K_2026-09-21_merger-agreement.md`, section "Item 1.01, Conditions"; `targets/wren/data/sec-filings/MDLS_DEFM14A_2026_excerpts.md`, sections "Summary, Appraisal rights" and "Background of the merger"
- **Severity:** Critical. Test met: it could block closing. Halsey Rock's stated demand on 11.4% of shares exceeds the 10% threshold, and only Parent can waive. The intention comes from news (Capital Markets Wire, October 6, 2026). Demands become relevant only if the vote passes.
- **Confidence:** High on the condition mechanics and holdings (primary filings, recomputed). Medium on whether the demand will happen, since that rests on one news source.
- **Deal impact:** Closing risk. It could also give Parent leverage to renegotiate price after the vote (inference).
- **Cross-check:** Look for a Halsey Rock 13D/A or the letter itself. Check how many Section 262 demands have been received by the meeting date. Ask whether Parent has said if it would waive.

#### SEC-48: Size of the appraisal exposure if Halsey Rock and Bramford dissent
- **Finding:** Cash for Halsey Rock's shares at the deal price is US$218.6m. In an appraisal, the extra cost is the court's fair value above US$41.50, plus statutory interest. No source states that interest. The filings give two reference points above the deal price: the top of Pellham Rowe's DCF range (US$46.80) and Ostrander Hale's May indication (US$44.00 to US$46.00).
- **Evidence:** Halsey Rock: 5,267,000 x US$41.50 = US$218.6m (8.9% of EV). At US$46.80, the uplift is 5,267,000 x 5.30 = US$27.9m (1.1% of EV). Adding Bramford: 7,947,000 x 5.30 = US$42.1m (1.7% of EV) (projection). The DCF range is "US$38.10 to US$46.80 per share". The May indication was "US$44.00 to US$46.00".
- **Source:** `targets/wren/data/sec-filings/MDLS_DEFM14A_2026_excerpts.md`, sections "Opinion of Pellham Rowe & Co.", "Background of the merger" and "Security ownership"
- **Severity:** Medium. On the filing reference points, the uplift is below 2% of EV.
- **Confidence:** Medium. The arithmetic is from primary figures, but the fair-value outcome is a projection.
- **Deal impact:** Valuation and post-closing cash need.
- **Cross-check:** Ask counsel for Delaware statutory interest. Check whether Halsey Rock has published its own valuation in the news.

#### SEC-49: Vote math under the majority-of-unaffiliated condition
- **Finding:** Adoption needs a majority of all outstanding shares and a majority of unaffiliated shares. Failing to vote counts as a vote against. Halsey Rock and Bramford together hold 17.8% of the unaffiliated shares.
- **Evidence:** Unaffiliated base: 46,200,000 - 1,430,000 = 44,770,000. Halsey Rock and Bramford: 7,947,000 / 44,770,000 = 17.8%. The proxy says "Failing to vote has the same effect as voting against." Corbel Index Advisors holds 9.1%.
- **Source:** `targets/wren/data/sec-filings/MDLS_DEFM14A_2026_excerpts.md`, sections "Summary, Required votes" and "Security ownership"
- **Severity:** Medium. The vote is not blocked on these numbers alone. Turnout and Corbel's vote matter.
- **Confidence:** High. Primary figures, recomputed.
- **Deal impact:** Closing risk.
- **Cross-check:** Proxy advisor recommendations, solicitation updates and Corbel's voting policy.

#### SEC-50: The Southwest dismissals are not in any filing, and the accrual gap is not classified as a control deficiency
- **Finding:** No filing mentions the dismissal of the Southwest regional controller or the two Phoenix project managers. No filing uses the words deficiency, significant deficiency or material weakness. The 10-Q says only that disclosure controls were effective and describes two control changes. The news ties the dismissals to the same internal audit review of subcontractor costs. If that points to intentional conduct, it would be a qualitative factor against the SAB 99 conclusion that the error was immaterial (inference).
- **Evidence:** The 10-Q Item 4 says disclosure controls "were effective as of June 30, 2026". It also says "we added a regional review of open subcontractor purchase orders at each quarter-end and moved accrual approval for the Southwest region to the corporate controller." Note 2 says "we did not revise prior periods". The 10-K Item 9A reports internal control over financial reporting as "effective" at December 31, 2025, the same date at which the costs "had not been accrued".
- **Source:** `targets/wren/data/sec-filings/MDLS_10-Q_Q2-2026_excerpts.md`, "Note 2. Out-of-period adjustment" and "Item 4. Controls and Procedures"; `targets/wren/data/sec-filings/MDLS_10-K_FY2025_excerpts.md`, "Item 9A"
- **Severity:** Medium. The amount is small (see SEC-51), and this is a gap in disclosure and possibly in control classification. Raise it to High if the internal audit report shows intent or a wider scope.
- **Confidence:** Medium. The silence in the filings is High. The link to possible misconduct rests on one news source.
- **Deal impact:** Restatement risk for FY2025 (inference). Disclosure. A specific representation on financial statements and internal controls.
- **Cross-check:** Get the internal audit report, the audit committee minutes, and the date in Q1 2026 when the error was found relative to the 10-K filing on February 26, 2026. Get the auditor's deficiency evaluation and the Q1 2026 10-Q, which is not in my files.

#### SEC-51: The US$4.1m is not attributed to any 2025 quarter
- **Finding:** The filings say only that the work was "performed in fiscal 2025" and was not accrued at December 31, 2025. No quarterly split is found in SEC filings. Against FY2025 results the error is modest. No filing says whether Adjusted EBITDA in H1 2026 adds the charge back.
- **Evidence:** 4.1 / 123.4 = 3.3% of FY2025 operating income. 4.1 / 186.4 = 2.2% of FY2025 Adjusted EBITDA. 4.1 / 83.3 (pre-tax income, 62.9 + 20.4) = 4.9%. In H1 2026, 4.1 / 41.4 = 9.9% of operating income.
- **Source:** `targets/wren/data/sec-filings/MDLS_10-Q_Q2-2026_excerpts.md`, "Note 2" and "Item 2, Results for the six months"; `targets/wren/data/sec-filings/MDLS_8-K_2026-02-25_fy2025-results.md`, reconciliation table
- **Severity:** Medium
- **Confidence:** High. Primary figures, recomputed.
- **Deal impact:** Quality of earnings. The FY2025 base and the Q4 2025 "record" results are overstated by up to US$4.1m (inference).
- **Cross-check:** Ask the financial analyst whether the quarterly data show the costs by quarter. Ask management for the subcontractor invoice dates.

#### SEC-52: Goodwill is not found in SEC filings
- **Finding:** No excerpt mentions goodwill, an annual test date, reporting units, headroom or an interim test. The US$152.0m Pinecrest acquisition in March 2025 would normally have created goodwill (inference). On August 6, 2026 the share price fell 21% to US$31.90, the outlook was cut and units fell 4.7%. These are common interim triggers. No interim test is disclosed.
- **Evidence:** Pinecrest cost "US$152.0 million, net of cash acquired". The proxy says "The share price fell 21% to US$31.90". The 10-Q shows units at 168,100 against 176,300.
- **Source:** `targets/wren/data/sec-filings/MDLS_10-K_FY2025_excerpts.md`, "Item 1. Business, Acquisitions"; `targets/wren/data/sec-filings/MDLS_DEFM14A_2026_excerpts.md`, "Background"; `targets/wren/data/sec-filings/MDLS_10-Q_Q2-2026_excerpts.md`, "Key operating metrics"
- **Severity:** Medium. This is a gap. The amount cannot be tested from my files.
- **Confidence:** Low to Medium. The absence of the topic may reflect the excerpting.
- **Deal impact:** A dated accounting judgment and possible impairment. The impairment would be non-cash.
- **Cross-check:** Ask the financial analyst for the goodwill balance and the purchase price allocation. Ask management for the test date, the reporting units and the headroom at the last test.

#### SEC-53: Code compliance cost is not estimated, its probability is not discussed, and an upper bound built from news per-unit costs exceeds 10% of EV
- **Finding:** The filings give no cost per unit and no unit count by state. They give only a combined Illinois and New Jersey count: 22,600 units at December 31, 2025 and 22,400 at June 30, 2026. Most of these units are on forms that do not exclude code-mandated upgrades. No filing, including the proxy, discusses the probability that Meridale bears the cost. The proxy projections exclude it. Meridale expenses these costs as incurred and has recorded no liability. Price recovery is limited by the 4.0% escalator caps.
- **Evidence:** The 10-Q says "most on contract forms that do not exclude code-mandated upgrades". It also says "We have not completed our estimate of the cost of compliance." Deadlines are December 31, 2028 for Illinois and July 1, 2029 for New Jersey. Math using the news range of US$11,000 to US$15,000 per elevator: 22,400 x 11,000 = US$246.4m, which is 10.0% of EV and 12.9% of equity value. 22,400 x 15,000 = US$336.0m, which is 13.7% of EV and 17.5% of equity value. Break-even for 10% of EV (US$246.0m) is 22,359 units at US$11,000 or 16,397 units at US$15,000 (73% of 22,400).
- **Source:** `targets/wren/data/sec-filings/MDLS_10-Q_Q2-2026_excerpts.md`, "Note 11, Code compliance"; `targets/wren/data/sec-filings/MDLS_10-K_FY2025_excerpts.md`, "Item 1A" and "Note 14"; `targets/wren/data/sec-filings/MDLS_DEFM14A_2026_excerpts.md`, "Certain financial projections"
- **Severity:** Critical, as an upper bound. Test met: more than 10% of value. The full-population cost is 10.0% to 13.7% of EV. The low end crosses the threshold only if all 22,400 units are covered. Because "most", not all, units are on old forms, the lead should treat the low end as borderline. Price recovery of the cost is not shown in any source.
- **Confidence:** Medium. Unit counts and contract terms are primary. The per-unit cost is from one secondary source.
- **Deal impact:** Valuation. Cost is likely concentrated in 2027 to 2029, inside the projection period (inference).
- **Cross-check:** Ask management for the units by state and by contract form, and for its internal cost estimate. Ask whether any customer has agreed to pay. Ask the financial analyst for revenue from these contracts.

#### SEC-54: The 10-K's "several states are considering" language was not updated or carried forward
- **Finding:** The 10-K risk factor says several states are considering retrofit rules but names none beyond Illinois and New Jersey. The 10-Q discusses only Illinois and New Jersey. It does not say whether other states are still considering rules. No other state is named in any filing.
- **Evidence:** The 10-K says "Several states are considering new retrofit requirements for door-lock monitoring and car door restrictors."
- **Source:** `targets/wren/data/sec-filings/MDLS_10-K_FY2025_excerpts.md`, "Item 1A"; `targets/wren/data/sec-filings/MDLS_10-Q_Q2-2026_excerpts.md`, "Note 11"
- **Severity:** Low. This is an open question, not a quantified exposure.
- **Confidence:** Medium. The absence may reflect the excerpting.
- **Deal impact:** Valuation upside to SEC-53 if more states adopt rules (inference).
- **Cross-check:** Check news and trade press for other state rulemakings. Ask management for comprehensive-contract units in those states.

#### SEC-55: The fairness opinion's DCF uses a case that excludes code compliance and withdrawal liability
- **Finding:** Pellham Rowe's DCF (US$38.10 to US$46.80) is built on the August case. That case excludes door-safety compliance cost and any withdrawal liability. The proxy does not show how the DCF would change with these costs included.
- **Evidence:** The proxy says "The projections do not include any cost of compliance with the Illinois and New Jersey door-safety requirements, any withdrawal liability, or the Brockmere acquisition." Per share, before tax and discounting (projection): code compliance at US$246.4m to US$336.0m is US$5.33 to US$7.27 per share (divided by 46.2m shares). The low end would put the bottom of the DCF range at US$32.77, below US$41.50. The disclosed complete withdrawal liability of US$338m equals US$7.32 per share.
- **Source:** `targets/wren/data/sec-filings/MDLS_DEFM14A_2026_excerpts.md`, "Certain financial projections" and "Opinion of Pellham Rowe & Co."; `targets/wren/data/sec-filings/MDLS_10-Q_Q2-2026_excerpts.md`, "Note 10"
- **Severity:** High. It bears on how reliable the price support is and on proxy disclosure.
- **Confidence:** Medium. The exclusion is primary. The per-share effects are my projection.
- **Deal impact:** Valuation and disclosure.
- **Cross-check:** Ask for Pellham Rowe's board book and whether any sensitivity case included these costs.

#### SEC-56: Collective agreement term, missing clauses, and cost escalation against capped prices
- **Finding:** The new agreement is four years from July 1, 2026. That implies an end date of June 30, 2030, but no filing states it. No clause on converting branches to non-union work, subcontracting or withdrawal is found in SEC filings. The 10-K warns that ceasing contributions at some facilities or bargaining units triggers a proportional partial withdrawal liability. Parent's stated plan covers corporate functions, not field units.
- **Evidence:** The 10-Q describes "a new four-year national agreement effective July 1, 2026" with increases of "6.5% a year" against 3.4% before. The wage and benefit base is about US$286m (FY2025). Year one cost at 6.5% is 286 x 6.5% = US$18.6m, against 286 x 3.4% = US$9.7m, an increment of US$8.9m. By year four (projection): 286 x (1.065^4 - 1) = US$81.9m against 286 x (1.034^4 - 1) = US$40.9m, an annual gap of about US$41.0m before price recovery. 62% of maintenance contracts by revenue cap escalators at the lesser of CPI and 4.0%.
- **Source:** `targets/wren/data/sec-filings/MDLS_10-Q_Q2-2026_excerpts.md`, "Collective agreement"; `targets/wren/data/sec-filings/MDLS_10-K_FY2025_excerpts.md`, "Item 1" and "Note 12"; `targets/wren/data/sec-filings/MDLS_DEFM14A_2026_excerpts.md`, "Golden parachute compensation"
- **Severity:** Medium
- **Confidence:** High on the stated terms. The end date and cost path are inference and projection.
- **Deal impact:** Margins and an integration plan. Any restructuring of union branches after closing could trigger partial withdrawal (inference).
- **Cross-check:** Get the agreement text: subcontracting, successorship and work-preservation clauses.

#### SEC-57: The August case includes the new agreement, but the filings do not say whether it includes the LTE-M replacement or the Laurent put
- **Finding:** The proxy says the August case "reflects ... the new collective agreement". It does not mention the LTE-M hardware replacement or the Laurent put, either as included or as excluded. Its exclusion list names only code compliance, withdrawal liability and Brockmere.
- **Evidence:** The LTE-M replacement is about 9,800 units x US$530 = US$5.2m, "most of it in 2027". Under the LiftSense terms, Meridale replaces hardware at its own cost. The Laurent put is in SEC-58.
- **Source:** `targets/wren/data/sec-filings/MDLS_DEFM14A_2026_excerpts.md`, "Certain financial projections"; `targets/wren/data/sec-filings/MDLS_10-Q_Q2-2026_excerpts.md`, "Connected services"
- **Severity:** Medium
- **Confidence:** High that the proxy is silent on these two items.
- **Deal impact:** Valuation, a small adjustment to FY2027 cash flow.
- **Cross-check:** Ask management and the financial analyst for the projection model's line items.

#### SEC-58: The floor price on the Laurent put is far above carrying value, and Groupe Laurent is reviewing its rights
- **Finding:** The partnership agreement lets Groupe Laurent make Meridale buy its 50% interest after a change of control. The price is the greater of appraised fair value and 12.0x TTM EBITDA x 50%, paid in cash within 90 days. The proxy says Groupe Laurent "is reviewing its rights". No liability is recorded.
- **Evidence:** Floor: 12.0 x 8.9 x 50% = US$53.4m (2.2% of EV), against a carrying value of US$9.7m. The excess over carrying value is US$43.7m. The 10-K says "We have not recorded a liability for this right because no change of control has occurred."
- **Source:** `targets/wren/data/sec-filings/MDLS_10-K_FY2025_excerpts.md`, "Note 6"; `targets/wren/data/sec-filings/MDLS_10-Q_Q2-2026_excerpts.md`, "Note 6"; `targets/wren/data/sec-filings/MDLS_DEFM14A_2026_excerpts.md`, "Regulatory approvals and third-party consents"
- **Severity:** Medium. It is a computable contractual cash need, and the buyer receives an asset in return.
- **Confidence:** High. Primary figures, recomputed.
- **Deal impact:** A price item and a cash need within 270 days after closing (180 days to exercise plus 90 days to pay).
- **Cross-check:** Check news for Groupe Laurent's intentions. Ask whether the term loan commitment covers this payment.

#### SEC-59: No filing says whether contract cost amortization is inside the Adjusted EBITDA add-back
- **Finding:** The 10-K says the amortization is "recorded in SG&A". The Adjusted EBITDA reconciliation adds back one "Depreciation and amortization" line and has no separate contract-cost line. No filing states whether that line includes contract cost amortization. If it is excluded, which is consistent with the financials README you passed on, the October 2025 change of estimate raises Adjusted EBITDA directly (inference).
- **Evidence:** Amortization was US$16.9m in 2024 and US$15.5m in 2025. The change cut it by US$1.7m in Q4 2025 and by US$3.4m in H1 2026, and is expected to cut it by about US$6.8m in FY2026. The H1 2026 amortization amount is not found in SEC filings. 6.8 / 168 = 4.0% of FY2026E Adjusted EBITDA. At EV / FY2026E Adjusted EBITDA of 2,459.5 / 168 = 14.6x, US$6.8m is worth about US$99.6m (4.0% of EV) (projection). For FY2025, 1.7 / 186.4 = 0.9%.
- **Source:** `targets/wren/data/sec-filings/MDLS_10-K_FY2025_excerpts.md`, "Critical accounting estimates" and "Note 4"; `targets/wren/data/sec-filings/MDLS_10-Q_Q2-2026_excerpts.md`, "Note 5"; `targets/wren/data/sec-filings/MDLS_8-K_2026-02-25_fy2025-results.md`, reconciliation table
- **Severity:** Medium
- **Confidence:** Medium. The add-back treatment is inferred, not stated.
- **Deal impact:** Quality of earnings in the pricing base.
- **Cross-check:** Ask the financial analyst to confirm the treatment in the EBITDA bridge.

#### SEC-60: The ten-year amortization period rests on a renewal rate that has since fallen 5.4 points
- **Finding:** The change from six to ten years, effective October 1, 2025, cites the FY2024 renewal rate of 92.3%. The trailing renewal rate fell to 90.6% at December 31, 2025 and 86.9% at June 30, 2026. The August case assumes "lower expected renewal rates". The 10-Q keeps the ten-year period and reports no reassessment.
- **Evidence:** The 10-K says "A one-percentage-point change in the long-run renewal rate would change the estimated period of benefit by about one year." 92.3 - 86.9 = 5.4 points. Extended linearly, that implies roughly 4.6 years, below the old six years (inference, beyond the stated sensitivity). The asset was US$98.1m at June 30, 2026.
- **Source:** `targets/wren/data/sec-filings/MDLS_10-K_FY2025_excerpts.md`, "Critical accounting estimates" and "Key operating metrics"; `targets/wren/data/sec-filings/MDLS_10-Q_Q2-2026_excerpts.md`, "Note 5" and "Key operating metrics"; `targets/wren/data/sec-filings/MDLS_DEFM14A_2026_excerpts.md`, "Certain financial projections"
- **Severity:** Medium
- **Confidence:** High on the figures. The judgment being in doubt is my inference.
- **Deal impact:** A dated accounting judgment. Reversing the change would add back about US$6.8m a year of amortization expense and could bring an impairment of the US$98.1m asset (inference).
- **Cross-check:** Ask the auditor how it reviewed the estimate. Ask the financial analyst for the renewal trend by quarter.

#### SEC-61: The August case implies a sharp H2 2026 margin recovery
- **Finding:** FY2026E Adjusted EBITDA of US$168m less H1 actual US$74.7m implies H2 of US$93.3m. That is 3.3% below H2 2025, while H1 was 16.9% below H1 2025. It also implies an H2 margin above H1 even though the 6.5% labor increases start July 1.
- **Evidence:** Implied H2 2026 revenue is 1,031 - 510.8 = US$520.2m, against H2 2025 of 1,067.7 - 516.0 = US$551.7m (-5.7%). Implied H2 2026 Adjusted EBITDA is US$93.3m, against H2 2025 of 186.4 - 89.9 = US$96.5m. H2 margins: 93.3 / 520.2 = 17.9% in 2026E against 17.5% in H2 2025 and 14.6% in H1 2026. If the US$9.3m of H1 one-offs (4.1 + 5.2) were not added back, H1 would be (74.7 + 9.3) / 510.8 = 16.4%. Whether they were added back is not found in SEC filings. Part of the H2 margin comes from the amortization change (SEC-59).
- **Source:** `targets/wren/data/sec-filings/MDLS_DEFM14A_2026_excerpts.md`, "Certain financial projections"; `targets/wren/data/sec-filings/MDLS_10-Q_Q2-2026_excerpts.md`, "Results for the six months"; `targets/wren/data/sec-filings/MDLS_10-K_FY2025_excerpts.md`, "Fiscal 2025 overview"
- **Severity:** Medium
- **Confidence:** Medium. The arithmetic is from primary figures. What the case assumes underneath is not disclosed.
- **Deal impact:** Valuation. The pricing base may depend on a recovery not yet shown (inference).
- **Cross-check:** Compare with Q3 2026 actuals (the Q3 10-Q is not in my files). Ask the financial analyst for monthly run-rate data.

#### SEC-62: St. Aldric is absent from the proxy, and the "not probable" position has not been updated since August
- **Finding:** The 10-Q, filed August 6, 2026, recorded a US$5.2m loss provision and nothing for liquidated damages, saying a loss was not probable. The proxy, filed October 23, does not mention St. Aldric. Outside counsel's preliminary view in September (per the litigation file) is that exposure is "likely, at least in part". If so, Q3 2026 may need an accrual (inference). The Q3 10-Q is not in my files.
- **Evidence:** The 10-Q says "have not accrued any amount for liquidated damages because we do not consider a loss probable". The claim is US$38.0m. The liquidated damages cap is US$15.4m (25% x 61.4 = 15.35), and gross negligence is alleged, which could lift the cap. Against EV: 15.4 / 2,459.5 = 0.6%, and 38.0 / 2,459.5 = 1.5%. Reported periods covered: the Q2 2026 10-Q (June 30, 2026, with a subsequent-events note) and Q3 2026, which is not in my files.
- **Source:** `targets/wren/data/sec-filings/MDLS_10-Q_Q2-2026_excerpts.md`, "Note 11, Fixed-price modernization contract" and "Note 12"; `targets/wren/data/sec-filings/MDLS_DEFM14A_2026_excerpts.md` (no mention)
- **Severity:** High. The amount stated by the claimant is below 10% of value, so the finding is not Critical. It needs a specific indemnity or escrow, and the accrual position conflicts with counsel's view.
- **Confidence:** Medium. The filing positions are High. Counsel's view comes from another source.
- **Deal impact:** An unrecorded liability, disclosure, and an indemnity or escrow.
- **Cross-check:** The Q3 2026 10-Q, the arbitration docket, and the counsel letter in the litigation file.

#### SEC-63: The noteholders' change-of-control put is not covered by the debt commitment
- **Finding:** Closing triggers a 101% repurchase offer on the US$400.0m notes within 30 days. The proxy says the debt commitment does not finance it. The notes traded at 97.25% at June 30, 2026, so holders have an economic incentive to tender (inference).
- **Evidence:** 400.0 x 101% = US$404.0m, including a US$4.0m premium. The proxy says "The debt commitment does not include financing for any such repurchase." The 10-K says no ratings downgrade is required for the put.
- **Source:** `targets/wren/data/sec-filings/MDLS_DEFM14A_2026_excerpts.md`, "Financing of the merger"; `targets/wren/data/sec-filings/MDLS_10-K_FY2025_excerpts.md`, "Note 9"; `targets/wren/data/sec-filings/MDLS_10-Q_Q2-2026_excerpts.md`, "Note 8"
- **Severity:** High, under the calibration rule: a problem cured by refinancing at closing. It is not a default before closing.
- **Confidence:** High. Primary figures.
- **Deal impact:** A liquidity need after closing and the financing structure. This may repeat an iteration-1 finding.
- **Cross-check:** Ask Parent's lenders for the backstop plan. Check current note pricing.

#### SEC-64: Parent's plan to replace executives makes the double-trigger severance a near-certain cost
- **Finding:** Severance is double-trigger. But Parent says it expects to replace the executive team other than Mr. Pell within 12 months. That would trigger most of the US$16.8m in cash severance (inference).
- **Evidence:** The proxy says Parent "expects ... to replace the executive team, other than Mr. Pell, within 12 months after closing." Total cash severance is US$16.8m (US$13.0m for named executives plus US$3.8m for others).
- **Source:** `targets/wren/data/sec-filings/MDLS_DEFM14A_2026_excerpts.md`, "Golden parachute compensation"
- **Severity:** Medium (known deal cost)
- **Confidence:** High
- **Deal impact:** A price item. It also leaves a gap in finance oversight after closing: the CFO is to be replaced while the contingencies above remain open.
- **Cross-check:** Ask Parent for its retention plan.

#### SEC-65: Total of known deal costs
- **Finding:** Fixed or computable deal costs in the filings come to about US$114.1m (4.6% of EV). Adding the Laurent put floor brings the total to US$167.5m (6.8%).
- **Evidence:** Equity award cash-out US$52.3m, plus cash severance US$16.8m, plus Pellham Rowe fee US$31.5m (US$27.0m of it contingent on closing), plus Brockmere termination fee US$9.5m, plus note premium US$4.0m, equals US$114.1m. 114.1 / 2,459.5 = 4.6%. With the Laurent floor of US$53.4m, the total is 167.5 / 2,459.5 = 6.8%.
- **Source:** `targets/wren/data/sec-filings/MDLS_DEFM14A_2026_excerpts.md`, "Treatment of equity awards", "Golden parachute compensation" and "Opinion of Pellham Rowe"; `targets/wren/data/sec-filings/MDLS_8-K_2026-09-21_merger-agreement.md`, "Brockmere"; `targets/wren/data/sec-filings/MDLS_10-Q_Q2-2026_excerpts.md`, "Note 11, Brockmere"
- **Severity:** Medium at 4.6%. It becomes High (above 5%) if the lead treats the Laurent put as a deal cost.
- **Confidence:** High. Primary figures, recomputed.
- **Deal impact:** Price
- **Cross-check:** Ask the financial analyst whether the EV already nets any of these amounts.

#### SEC-66: The merger will likely be a new Section 382 ownership change, and the proxy is silent on it
- **Finding:** The 10-K says any later ownership change sets a new limit on using the NOLs. The merger would be such a change (inference). The new limit is not disclosed. NOLs total US$318.0m (US$66.8m tax-effected), and the existing limit is US$11.2m a year.
- **Evidence:** The 10-K says "Any later ownership change would set a new limit". The proxy has no tax-attribute discussion in the excerpts.
- **Source:** `targets/wren/data/sec-filings/MDLS_10-K_FY2025_excerpts.md`, "Note 11. Income taxes"
- **Severity:** Medium
- **Confidence:** Medium. That the merger is an ownership change is my inference.
- **Deal impact:** Valuation of the tax asset.
- **Cross-check:** Ask the buyer's tax advisors to model the post-closing limit.

#### SEC-67: The proxy's statement on change-of-control contracts matches the 10-K
- **Finding:** The proxy repeats that the Company knows of no material customer contract with a change-of-control provision. It says the reverse triangular structure avoids the assignment-consent issue, which covers about 34% of maintenance revenue.
- **Evidence:** The proxy says "The Company is not aware of any material customer contract with a change-of-control provision."
- **Source:** `targets/wren/data/sec-filings/MDLS_DEFM14A_2026_excerpts.md`, "Regulatory approvals and third-party consents"; `targets/wren/data/sec-filings/MDLS_10-K_FY2025_excerpts.md`, "Item 1A"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Closing (mitigant)
- **Cross-check:** Review a sample of large customer contracts.

### Positive or mitigating points
- **Clean controls and audit.** Internal control over financial reporting was effective at December 31, 2025, with a clean auditor attestation. Whitcombe & Ames has been auditor since 2007. Remediation steps for the Southwest gap are described in the 10-Q Item 4. This is qualified by SEC-50 and SEC-51.
- **No customer consents needed.** No customer change-of-control provisions are known, and the reverse triangular structure avoids assignment consents (SEC-67).
- **HSR cleared.** The HSR waiting period ended early on October 14, 2026 (DEFM14A, "Regulatory approvals").
- **Vantor case closed.** The Vantor case was dismissed with prejudice and not appealed (10-Q, Note 11).
- **Harbor Pointe claim insured.** The US$2.0m retention is accrued, and carriers accepted defense without reservation of rights (10-K, Note 14).
- **No tax gross-ups.** No tax gross-ups, and a best-net 280G cutback (DEFM14A).
- **No near-term maturities.** The next maturity is the 2030 notes, and the revolver was undrawn at June 30, 2026.

### Gaps and questions for management
1. Have any Section 262 demands been received? Will Parent waive the 10% condition? Will a proxy supplement disclose Halsey Rock's October 6 letter?
2. Internal audit report on Southwest subcontractor costs: what was the scope, was there intent, and why were the controller and project managers dismissed? On what date in Q1 2026 was the error found, compared with the 10-K filing on February 26, 2026? How did the auditor classify the deficiency? How does the US$4.1m split by quarter?
3. Goodwill balance, reporting units, test date, headroom, and whether an interim test was done after August 6, 2026.
4. Code compliance: units by state and contract form, the internal cost estimate, customer responses, and other states considering rules.
5. Collective agreement text: expiry, subcontracting, successorship and branch-closure clauses.
6. Projection model: whether the August case includes the LTE-M replacement cost, the Laurent put and the amortization change, and the assumptions behind the H2 2026 margin.
7. Is contract cost amortization inside or outside the D&A add-back? What was the amortization amount in H1 2026?
8. Q3 2026 10-Q: the St. Aldric accrual position, given outside counsel's view.
9. Section 382 limit after the merger.
10. Reported equity, which I could not use as a denominator because it is not found in SEC filings.
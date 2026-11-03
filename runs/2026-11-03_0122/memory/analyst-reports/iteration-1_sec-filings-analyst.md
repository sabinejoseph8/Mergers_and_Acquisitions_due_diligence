## SEC filings analyst: findings

### Files reviewed

I read all five SEC files and the deal brief in full.

- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md (filed Feb 26, 2026)
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/sec-filings/BWCC_8-K_2026-03-20_harbor-district-update.md (event Mar 17, 2026; filed Mar 20, 2026)
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/sec-filings/BWCC_DEF14A_2026_excerpts.md (filed Apr 9, 2026)
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md (filed Aug 6, 2026)
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/sec-filings/BWCC_8-K_2026-09-22_strategic-review.md (event Sep 21, 2026; filed Sep 22, 2026)
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/deal-brief.md (context only)

None of the source files contains text that tries to instruct the agents.

**Key dates from the SEC filings:** I-5 fatal accident Feb 3, 2025. Refinancing and Bayfront acquisition Mar 2025. Antitrust class action filed Jun 12, 2025. Holbrook assessment Oct 2025. New insurance accrual rate in force from Jan 1, 2026. FreshArc Chapter 11 Jan 12, 2026. Sandhaven 2 compressor failure Feb 2026. 10-K filed Feb 26, 2026. Terminal 7 plan adopted Mar 17, 2026. Buybacks suspended Apr 2026. I-5 lawsuit Apr 17, 2026. Coastline suit May 27, 2026. Seven-year customer agreement and FreshArc trustee demand Jul 2026. ICE notices Jul 28, 2026. 10-Q filed Aug 6, 2026. Severance Plan adopted Sep 21, 2026. Strategic review announced Sep 22, 2026. Fixed-price power ends Dec 31, 2026. Calder Valley injunction hearing Jan 15, 2027. Sandhaven concession ends Sep 30, 2028.

Value base for every test: enterprise value $2,750.0m (5% = $137.5m, 10% = $275.0m). Deal multiple: 11.0x.

### Findings

#### SEC-01: Adjusted EBITDA definition and the LTM build check out
- **Finding:** The company's Adjusted EBITDA adds back other (income) expense, share-based pay, transaction costs, and severance, restructuring and integration. The 10-Q's LTM figure of $250.0m matches the deal brief, and every line recomputes.
- **Evidence:** 271.0 less 139.0 plus 118.0 = 250.0. LTM: net income 38.1 + tax 12.0 + interest 73.0 + D&A 107.5 = EBITDA 230.6. Add other 0.1, share-based pay 12.5, transaction costs 2.0 and severance 4.8 = 250.0. Add-backs total $19.4m (7.8% of LTM). LTM revenue = 1,398.0 less 694.0 plus 680.8 = 1,384.8, so the LTM margin is 18.1%.
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, section "Reconciliation of Adjusted EBITDA"; `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, section "Reconciliation of Adjusted EBITDA"
- **Severity:** Low
- **Confidence:** High. Primary source, recomputed.
- **Deal impact:** Valuation (checks the earnings base)
- **Cross-check:** The LTM build in the financials folder and the earnings releases.

#### SEC-02: Add-backs labeled non-recurring come back every period
- **Finding:** Severance, restructuring and integration costs are added back every period. Transaction costs of $1.4m were added back in H1 2026, before the company announced any transaction (the strategic review came on Sep 22, 2026). What that transaction was is not found in SEC filings.
- **Evidence:** Severance and related add-backs: 1.0 (FY2024), 3.3 (FY2025), 3.0 (H1 2026), 4.8 (LTM). Transaction costs: 3.2 (FY2025), 1.4 (H1 2026). If the LTM severance and transaction add-backs are treated as recurring, that is $6.8m (2.7% of LTM), or $74.8m at 11.0x (2.7% of EV) (projection).
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, section "Reconciliation of Adjusted EBITDA"; `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, same heading
- **Severity:** Low
- **Confidence:** High on the figures. Medium on whether they recur (inference).
- **Deal impact:** Valuation
- **Cross-check:** Detail of the add-backs in the financials folder. News of any 2026 deal approach before September.

#### SEC-03: The 2024 sale-leaseback gain is correctly kept out of Adjusted EBITDA
- **Finding:** FY2024 net income included a $46.0m pre-tax gain on the Ironbridge sale-leaseback. The reconciliation removes it through other income, so it is not in Adjusted EBITDA or the LTM base. This risk is neutralized by the accounting treatment.
- **Evidence:** "Net income in 2024 included a $46.0 million pre-tax gain on the sale-leaseback of five facilities." FY2024 other (income) expense, net: (46.8).
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, sections "Results of operations" and "Reconciliation of Adjusted EBITDA"
- **Severity:** Low (neutralized)
- **Confidence:** High
- **Deal impact:** Valuation (mitigant)
- **Cross-check:** The financials folder confirms that no FY2024 gain sits in the LTM.

#### SEC-04: A cut in the insurance accrual rate lifts LTM earnings by $3.7m while accidents rose
- **Finding:** From Jan 1, 2026, Brindlewick cut its accrual for current-year auto and cargo claims from 6.5% to 4.8% of Transportation revenue, citing its camera telematics program. In the same half, recordable accidents per million miles rose 18.3% and a fatal-accident suit was filed (SEC-29). Claims reserves fell from $46.5m to $44.1m. Self-insurance reserves are the auditor's critical audit matter.
- **Evidence:** "reduced the rate at which we accrue expected auto liability and cargo claims for the current accident year from 6.5% to 4.8%". "The change reduced insurance and claims expense by approximately $3.7 million". Recomputed: 214.8 × 1.7% = 3.65. Accidents per million miles went from 0.71 to 0.84. Annualized on LTM Transportation revenue of $436.8m, the benefit is $7.4m. Value at 11.0x: $40.7m on the LTM effect (1.5% of EV) and $81.7m annualized (3.0%) (projection). Without the change, the H1 2026 Transportation operating ratio would be about 98.1%, not 96.4% (inference).
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, sections "Note 5. Change in accounting estimate" and "Key operating metrics"; `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, sections "Critical accounting estimates" and "Item 9A"
- **Severity:** Medium
- **Confidence:** High on the figures. Medium on whether the new rate is adequate (inference).
- **Deal impact:** Valuation (normalize the earnings base) and post-closing reserve adequacy
- **Cross-check:** Actuarial reports and telematics data, DOT/FMCSA safety data in the news, and claims data in the financials folder.

#### SEC-05: First-half 2026 results weakened in almost every segment and metric
- **Finding:** H1 2026 revenue, margins, occupancy, pricing, throughput and the Transportation operating ratio all weakened against H1 2025. Revenue fell faster in Q2 than in Q1. The LTM base of $250.0m captures only half a year of this decline.
- **Evidence:**
  - Revenue: 680.8 vs 694.0 (down 1.9%). Q1: 336.0 vs 341.2 (down 1.5%). Q2: 344.8 vs 352.8 (down 2.3%).
  - Gross margin: 26.2% vs 28.6%.
  - Adjusted EBITDA: 118.0 vs 139.0 (down 21.0, or 15.1%). Excluding the SEC-04 benefit it would be 114.3 (down 17.8%).
  - Occupancy: 81.4% vs 86.1%. Revenue per occupied pallet: $784 vs $819 (down 4.3%). Throughput: down 5.7%. Transportation operating ratio: 96.4% vs 93.8%.
  - Projections: if H2 2026 falls by the same $21.0m against H2 2025 ($132.0m), FY2026 is $229.0m. That is $21.0m below the deal base, or $231.0m at 11.0x (8.4% of EV). Doubling H1 gives $236.0m, $14.0m below the base ($154.0m, 5.6%). The full annualized fall from FY2025 is $42.0m ($462.0m at 11.0x, 16.8%), but half of that fall is already in the LTM base (projection).
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, sections "Overview of the six months ended June 30, 2026" and "Key operating metrics"
- **Severity:** High. Not Critical: the incremental fall below the deal base that I can project is $231.0m, under the $275.0m line. The lead should test it together with SEC-04, SEC-15 and SEC-16.
- **Confidence:** High on the reported figures. Medium on the projections.
- **Deal impact:** Valuation
- **Cross-check:** Q3 2026 results or earnings releases, monthly data in the financials folder, and news on frozen-food inventory and new Central Valley capacity.

#### SEC-06: ColdTrack service credits of $4.6m reduced H1 2026 revenue
- **Finding:** Warehousing revenue is net of $4.6m of service credits issued after failed ColdTrack go-lives, and two customers moved part of their volume elsewhere. The credits could be added back if they do not recur. Remediation is still under way, and the lost volume continues.
- **Evidence:** "Warehousing revenue is also net of $4.6 million of service credits". If treated as one-off: +$4.6m LTM, or $50.6m at 11.0x (1.8% of EV) (projection).
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, sections "Warehousing" and "ColdTrack warehouse management system"
- **Severity:** Low
- **Confidence:** High on the amount. Low on whether it recurs.
- **Deal impact:** Valuation (possible upward normalization)
- **Cross-check:** Customer data in the financials folder (who received credits and who left) and news about ColdTrack.

#### SEC-07: ColdTrack is over budget and paused, with $47.0m capitalized and no impairment; the buyer will halt it
- **Finding:** ColdTrack's cost estimate rose from $38.0m to $61.0m, and deployments are paused. Capitalized software (mainly ColdTrack) was $47.0m at June 30, 2026, and management "concluded that no impairment was required." The buyer plans to halt the rollout, so the asset is likely to be written off after closing (inference). That write-off is non-cash and does not touch EBITDA.
- **Evidence:** Overrun of $23.0m (60.5%). "We have paused further deployments while we remediate the system." $47.0m is 1.7% of EV. Reported equity is not found in SEC filings.
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, section "ColdTrack warehouse management system"; `targets/avocet/data/deal-brief.md`, section 5
- **Severity:** Medium
- **Confidence:** High on the facts. Medium on the write-off (inference).
- **Deal impact:** Post-closing (purchase accounting) and the timing of a dated impairment judgment
- **Cross-check:** News on ColdTrack problems, and the impairment memo and remaining spend from management.

#### SEC-08: FY2025 growth includes acquired and new capacity
- **Finding:** FY2025 revenue grew 4.2% and Adjusted EBITDA 7.5%. That growth includes the Bayfront acquisition (Mar 2025, $88.0m) and the new Calder Valley site (Jun 2025). Organic growth and Bayfront's revenue are not found in SEC filings.
- **Evidence:** "In March 2025 we acquired Bayfront Cold Storage (Oakland, California) for $88.0 million in cash."
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, sections "Item 1. Business" and "Results of operations"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Valuation (quality of growth)
- **Cross-check:** Facility-level revenue in the financials folder.

#### SEC-09: No FY2026 guidance in the SEC filings
- **Finding:** No guidance for FY2026, and no revision of guidance, is found in SEC filings.
- **Evidence:** Not found in SEC filings.
- **Source:** All five SEC files
- **Severity:** Low
- **Confidence:** High on its absence from these excerpts
- **Deal impact:** Disclosure
- **Cross-check:** Earnings releases and call coverage in the news.

#### SEC-10: Share buybacks in Q1 2026, then suspended in April
- **Finding:** Brindlewick bought back 515,000 shares for $14.0m in Q1 2026 and suspended buybacks in April 2026. Over the same half, the revolver draw rose $24.6m and cash fell $7.0m.
- **Evidence:** Average price $27.18 (14.0 / 0.515), above the $26.15 unaffected price. "suspended repurchases in April 2026". Revolver 70.4 to 95.0; cash 81.0 to 74.0.
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, section "Liquidity and capital resources"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Disclosure (signal about liquidity or outlook, inference)
- **Cross-check:** The reason for the suspension, from news or management.

#### SEC-11: The Sandhaven concession ends Sep 30, 2028, and the Harbor District plans other use from 2029
- **Finding:** Sandhaven 1 and 2 earn about $31.0m, or 12.4%, of LTM Adjusted EBITDA. They sit on a port concession that ends Sep 30, 2028, with no renewal option, and the improvements revert to the District. On Mar 17, 2026 the District designated the site for container yard and rail use from 2029. The deal multiple capitalizes this income as if it continues indefinitely.
- **Evidence:** "contributed approximately $31.0 million, or approximately 12%, of our Adjusted EBITDA" (31.0 / 250.0 = 12.4%; 118k of 1,148k pallets = 10.3% of capacity). The 8-K: "for container yard and on-dock rail use beginning in 2029, subject to environmental review and funding." The 10-Q: "We have not reached agreement, and there can be no assurance that we will."
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, section "Sandhaven"; `targets/avocet/data/sec-filings/BWCC_8-K_2026-03-20_harbor-district-update.md`, Item 8.01; `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, Item 1A and Item 2
- **Severity:** Critical. Test met: more than 10% of value. 31.0 × 11.0 = $341.0m, or 12.4% of EV, above the $275.0m line. Crediting the 12 to 18 months of income left after a Q2 to Q3 2027 closing ($31.0m to $46.5m) still leaves $294.5m to $310.0m (10.7% to 11.3%) (projection). Relocation cost is not found in SEC filings.
- **Confidence:** High. Primary sources, recomputed.
- **Deal impact:** Valuation. Possible price cut, a contingent value structure, or an extension as a condition.
- **Cross-check:** District board minutes and the environmental review and funding status, news on the talks, Sandhaven customers (Coastline is one, see SEC-30), and the carrying value and depreciation period of the improvements.

#### SEC-12: Sandhaven wording changed between filings
- **Finding:** The 10-K, filed 19 days before the Terminal 7 plan was adopted, said management expected to negotiate an extension. The 8-K and 10-Q dropped that expectation. The 10-Q added talks about an alternative site and gave the EBITDA figure for the first time. No source says the plan was known when the 10-K was filed, so the timing alone carries a Low rating.
- **Evidence:** 10-K: "expect to negotiate one, but the District is evaluating long-term plans". 8-K: "Brindlewick cannot predict the outcome of these discussions." The 8-K was filed 3 days after the event.
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, Item 1A; `targets/avocet/data/sec-filings/BWCC_8-K_2026-03-20_harbor-district-update.md`; `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, section "Sandhaven"
- **Severity:** Low (timing alone)
- **Confidence:** High on the wording. Low on what was known when.
- **Deal impact:** Disclosure
- **Cross-check:** District agendas before Feb 26, 2026, and news.

#### SEC-13: $312.0m of lease-end restoration is unrecorded, and the buyer's plan triggers $118.0m of it
- **Finding:** Eleven leases require Brindlewick to demolish or strip its improvements when it leaves. Holbrook (Oct 2025) put the cost at $312.0m, undiscounted and at 2025 prices. None of it is recorded as a liability. By the company's own policy, a liability is recognized once it decides to exit, and the buyer's plan to surrender four leases would trigger $118.0m. That $118.0m is not in the deal brief's $45.0m of integration costs. Three of the four leases would be surrendered before their current terms end: Puyallup Junction (2031), Stockton North (2033) and Lodi (2030). Kent Valley's term ends in 2029. The remaining rent on each lease is not found in SEC filings.
- **Evidence:** "aggregate undiscounted cost of satisfying these restoration provisions at all eleven facilities at approximately $312.0 million". "A restoration obligation is recognized when we decide to exit a facility". Triggered amount: 41.5 + 14.0 + 38.0 + 24.5 = 118.0. The periods with no liability recorded are FY2025 and its comparative year in the 10-K and H1 2026 in the 10-Q (the 10-Q excerpts do not mention the provisions), so there is a restatement risk (inference). It would take 88.1% of the base to reach 10% of value. Reported equity is not found in SEC filings, so I cannot give the share of equity.
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, Item 2, "Critical accounting estimates" and "Note 12"; `targets/avocet/data/deal-brief.md`, section 5
- **Severity:** Critical. Test met: more than 10% of value under the full-amount rule. $312.0m / $2,750.0m = 11.3%. The near-term cash cost from the buyer's plan is $118.0m (4.3% of EV).
- **Confidence:** High on the amounts. Medium on the restatement risk (inference).
- **Deal impact:** Valuation, post-closing cash, and integration plan economics ($21.0m of yearly network synergies against $118.0m of restoration)
- **Cross-check:** The Holbrook report, lease documents for exit and early-termination terms, and remaining rent by lease.

#### SEC-14: The effective-controls conclusion sits alongside the unrecorded restoration obligations
- **Finding:** Management found internal control over financial reporting effective at Dec 31, 2025, and disclosure controls effective at Jun 30, 2026. In the same periods it recorded no liability for SEC-13's contractual restoration duties. Its reason was that settlement dates are "indeterminate" and fair value "cannot be reasonably estimated". Yet each lease has a final expiry date (2039 to 2084), and a facility-by-facility cost estimate existed from Oct 2025. That estimate puts the stated reason in doubt, and the affected balance sheets carry a restatement risk (inference). The auditor's critical audit matter covers self-insurance, not restoration.
- **Evidence:** "we have concluded that settlement dates are indeterminate, and fair value cannot be reasonably estimated". "Management concluded that ... our internal control over financial reporting were effective as of December 31, 2025." This links SEC-13 and SEC-36. Another open judgment in the same period is SEC-04.
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, "Critical accounting estimates", "Note 12" and "Item 9A"; `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, "Item 4"
- **Severity:** Medium. The economic exposure is in SEC-13.
- **Confidence:** Medium (inference about the accounting)
- **Deal impact:** Disclosure, restatement risk, and representations on the financial statements
- **Cross-check:** Accounting diligence and the auditor's work papers on the ARO conclusion.

#### SEC-15: Fixed-price power ends Dec 31, 2026, before closing, and 2027 forward prices are "substantially above"
- **Finding:** About 70% of power was bought at about $61/MWh under contracts that end Dec 31, 2026. The LTM base includes that price, but the buyer will never pay it. The 10-K said 2027 supply was not yet contracted. The 10-Q says procurement has begun and forward prices are "substantially above" the current price.
- **Evidence:** "expire on December 31, 2026". "Forward prices for 2027 delivery in our markets are substantially above the price under our current agreements." Recomputed: 589 GWh × 70% = 412.3 GWh at $61 = $25.15m, consistent with the $25.2m 2026 commitment. The other 176.7 GWh cost $14.35m, about $81.2/MWh.
  - Illustration: repricing the contracted share at $81.2 adds $8.3m a year, or $91.6m at 11.0x (3.3% of EV) (projection).
  - Break-even: a rise of $30.3/MWh (to about $91/MWh) reaches 5% of EV; a rise of $60.6/MWh (to about $122/MWh) reaches 10%.
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, sections "Energy", Item 1A and "Note 12"; `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, section "Energy"
- **Severity:** High. The repricing is certain and happens before closing, but its size is not stated.
- **Confidence:** High on the facts. Medium on the illustration.
- **Deal impact:** Valuation (normalize run-rate EBITDA)
- **Cross-check:** Power contracts signed for 2027, forward price curves in the news or financials, and any energy line in the forecast.

#### SEC-16: The change of control itself raises California property tax by about $4.7m a year
- **Finding:** The merger would trigger reassessment of the Fresno facility and of Brindlewick-owned improvements at Stockton North and Modesto East, adding about $4.7m a year of operating cost. The split by facility is not found in SEC filings. Surrendering Stockton North could remove part of the increase (inference).
- **Evidence:** "a reassessment following a change in control would increase our annual property tax expense by approximately $4.7 million". At 11.0x that is $51.7m (1.9% of EV).
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, Item 1A
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation (a cost of the deal itself)
- **Cross-check:** Assessor records and an estimate from a tax adviser.

#### SEC-17: Maintenance capex was deferred, and $96m of priority replacements fall due in 2027 to 2029
- **Finding:** Maintenance capex fell to 2.5% of revenue in 2025 (3.3% in 2024, 4.1% in 2023) and to 2.3% in H1 2026, while projects were deferred. Holbrook found about $96m of priority 1 and 2 replacements for 2027 to 2029, mostly at seven sites with ammonia systems more than 25 years old. All of it falls in the buyer's ownership.
- **Evidence:** "Pending the assessment, we deferred certain non-critical projects". $96m is 3.5% of EV, about $32.0m a year. Compared with the 2023 rate, the shortfall was about $22.4m in 2025 and $12.3m in H1 2026 (inference). The Sandhaven 2 compressor failure (SEC-30) fits this pattern (inference).
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, sections "Capital expenditures" and Item 1A; `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, section "Liquidity and capital resources"
- **Severity:** Medium
- **Confidence:** High on the figures. Medium on the deferral estimate.
- **Deal impact:** Valuation (catch-up capex) and post-closing
- **Cross-check:** The Holbrook report, capex plan in the financials folder, and incident news.

#### SEC-18: The Ironbridge sale-leaseback depends on a contestable "sale" judgment
- **Finding:** Five facilities were sold for $214.0m and leased back for 20 years, plus four five-year options. Brindlewick keeps a right of first offer and an option to buy back the sites in lease years 10 to 15 at fair value. Sale treatment rests on management's view that comparable assets are "readily available". If that view failed, the $214.0m would be a financing obligation and the $46.0m gain would be reversed (inference). The company lists this as a critical estimate, and the auditor billed $350,000 for consultations on it.
- **Evidence:** "We concluded that the transfer qualified as a sale because the repurchase price is fair value at the time of exercise". Initial rent is $15.6m, rising 2.75% a year. $214.0m is 7.8% of EV.
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, "Note 7. Leases"; `targets/avocet/data/sec-filings/BWCC_DEF14A_2026_excerpts.md`, "Proposal 3"
- **Severity:** Medium
- **Confidence:** Medium (inference about the accounting)
- **Deal impact:** Debt-like item outside net debt and a restatement risk
- **Cross-check:** The master lease's change-of-control or assignment terms and the auditor consultation memo.

#### SEC-19: Most-favored-customer clauses cover about $169.0m of revenue, and two customers have asked for repricing
- **Finding:** Agreements worth about 22% of 2025 warehousing revenue carry most-favored-customer clauses. In H1 2026 Brindlewick granted rate concessions. In July 2026 it signed a seven-year agreement with a new Central Valley customer, after which two existing customers asked for pricing reviews. Management argues the new deal is not comparable. Its terms are not found in SEC filings.
- **Evidence:** 0.22 × 768.0 = $169.0m. "Two existing customers have since requested pricing reviews under the most-favored-customer provisions". To reach 5% of EV, rates on that base would have to fall 7.4% ($12.5m of EBITDA); to reach 10%, 14.8% ($25.0m).
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, sections "Pricing" and "Warehousing"; `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, "Customers and contracts" and Item 1A
- **Severity:** High. The repricing has no stated cap, and the seven-year contract fixes the comparison point. A specific representation and a contract review are needed.
- **Confidence:** Medium. The amount is not stated.
- **Deal impact:** Valuation and contracts that change after 2026
- **Cross-check:** Customer contracts and the July 2026 agreement. Ask whether the clauses would capture Trelliswood's rates after the merger, and rank the two requesting customers in revenue_by_customer.csv.

#### SEC-20: Customer concentration is low
- **Finding:** About 1,310 customers in 2025. None was above 6% of revenue, and the top ten made up 34.3%. Contracts run one to five years, many with minimum volumes.
- **Evidence:** "No customer accounted for more than 6% of revenue, and our ten largest customers accounted for 34.3%."
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, "Customers and contracts"
- **Severity:** Low (positive, qualified by SEC-06, SEC-19 and SEC-31)
- **Confidence:** High
- **Deal impact:** Mitigant
- **Cross-check:** revenue_by_customer.csv

#### SEC-21: Change-of-control and assignment terms of leases and contracts are not disclosed
- **Finding:** The excerpts do not show whether the ground leases, building leases, the Ironbridge master lease, the Sandhaven concession, or customer and power contracts need consent on a change of control, or allow termination because of one. Early-termination and surrender terms for the four leases the buyer plans to exit are also not found in SEC filings.
- **Evidence:** Not found in SEC filings.
- **Source:** All SEC files; `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, Item 2 and Note 7
- **Severity:** Medium (follow-up)
- **Confidence:** High on the absence
- **Deal impact:** Closing risk (consents) and integration costs
- **Cross-check:** Lease documents in the data room and the litigation and news sources.

#### SEC-22: No pension or multiemployer plan disclosed, and the workforce is non-union
- **Finding:** No pension, multiemployer plan or withdrawal liability is found in SEC filings. The workforce is not unionized.
- **Evidence:** "None of our employees is represented by a union."
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, "Employees"
- **Severity:** Low
- **Confidence:** Medium. These are excerpts.
- **Deal impact:** Mitigant
- **Cross-check:** Benefit plan documents and Form 5500 filings.

#### SEC-23: No debt matures before 2030, and all debt can be repaid at par
- **Finding:** The facilities are a $300.0m revolver and a $325.0m Term Loan A, both due March 2030, and a $720.0m Term Loan B due March 2032. Term Loan A amortizes $25.0m a year. Everything is prepayable at par, so the $1,115.0m repayment at closing (95.0 + 300.0 + 720.0) carries no premium.
- **Evidence:** "All facilities are prepayable at par." "We have no debt maturities before March 2030."
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, "Liquidity and capital resources" and "Note 9"; `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, "Liquidity and capital resources"
- **Severity:** Low (positive)
- **Confidence:** High
- **Deal impact:** Mitigant
- **Cross-check:** The credit agreement.

#### SEC-24: Covenant terms and change-of-control default are not disclosed, and leverage is rising
- **Finding:** The filings say only that the company "was in compliance with all covenants". Covenant definitions, levels, test dates and any change-of-control default are not found in SEC filings. Net debt to LTM Adjusted EBITDA rose from 4.06x at Dec 31, 2025 to 4.47x at Jun 30, 2026. On SEC-05's $229.0m projection it would be 4.88x (projection).
- **Evidence:** 1,100.9 / 271.0 = 4.06x. 1,118.0 / 250.0 = 4.47x. Revolver availability is $205.0m before letters of credit, which are not found in SEC filings.
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, "Liquidity and capital resources"; `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, same heading
- **Severity:** Medium. Repayment at closing cures any change-of-control default. A breach before closing would be Critical, but none is shown.
- **Confidence:** High on the figures
- **Deal impact:** Closing risk if earnings keep falling before Q2 to Q3 2027
- **Cross-check:** The credit agreement and covenant compliance certificates.

#### SEC-25: Antitrust class action seeks treble damages, with no accrual
- **Finding:** *In re Refrigerated Warehousing Services Antitrust Litigation* (N.D. Cal. No. 3:25-cv-04417, filed Jun 12, 2025) alleges that Brindlewick, six other operators and Coldmetric exchanged current rates. Plaintiffs seek treble damages and an injunction. The motion to dismiss is still pending. Nothing is accrued because the loss "cannot reasonably" be estimated. The 10-Q excerpt no longer repeats the 10-K's statement that the claims are without merit.
- **Evidence:** 10-K: "We believe the claims are without merit." 10-Q: "remains under submission. We have not accrued a loss." Break-even: trebled damages reach 10% of EV at $91.7m of single damages, which is 11.9% of 2025 warehousing revenue.
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, Item 3; `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, Note 11
- **Severity:** High. The exposure has no cap or estimate and may need a specific protection.
- **Confidence:** High on the facts. The amount is unknown.
- **Deal impact:** Valuation, specific protection, and spillover into merger antitrust review
- **Cross-check:** The docket (motion status, class period, co-defendants; is Trelliswood one?).

#### SEC-26: The merger overlaps in two markets where Brindlewick holds about 19% and 18%
- **Finding:** Brindlewick estimates its share of public refrigerated capacity at about 19% in Puget Sound and 18% in the Northern Central Valley, and names Trelliswood as a principal competitor in both. The deal brief caps divestitures at $15.0m of LTM EBITDA. Sandhaven alone, in Puget Sound, earns $31.0m. Trelliswood's own shares are not found in SEC filings.
- **Evidence:** "Trelliswood Logistics Corp. and several privately held operators are our principal competitors in both markets." Brindlewick pallets: Puget Sound 304k (Puyallup 78, Kent 38, Sandhaven 1 66, Sandhaven 2 52, Fife 70); Northern Central Valley 176k (Stockton North 72, Modesto East 58, Lodi 46).
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, "Markets and competition" and Item 2; `targets/avocet/data/deal-brief.md`, sections 4 and 5
- **Severity:** High. This is a closing risk, but my files cannot show that it would block closing.
- **Confidence:** Medium. The combined share is not in SEC filings.
- **Deal impact:** Closing risk (divestiture cap, outside date, the $110.0m reverse termination fee)
- **Cross-check:** Trelliswood's capacity data, news on the review, and antitrust counsel.

#### SEC-27: ICE is inspecting six warehouses, with known eligibility gaps for about 410 workers
- **Finding:** On Jul 28, 2026, ICE served Notices of Inspection on six warehouses. A self-audit begun in 2025 found unresolved eligibility discrepancies for about 410 employees. The company cannot estimate penalties or the effect on its workforce. The 10-Q disclosed this 9 days later as a subsequent event.
- **Evidence:** "unresolved discrepancies in employment eligibility documentation for approximately 410 employees". That is 8.9% of 4,610 hourly warehouse staff and 6.2% of 6,610 total staff (Dec 31, 2025 headcounts).
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, Note 14
- **Severity:** High. An active federal inspection, a workforce disruption risk, and an amount that cannot be estimated; it needs a specific covenant or representation and work before signing.
- **Confidence:** High on the facts. Low on the amount.
- **Deal impact:** Post-closing operations, specific protection
- **Cross-check:** News on ICE actions and staffing at the six sites.

#### SEC-28: The 10-K's I-9 risk factor was written as hypothetical while a self-audit was under way
- **Finding:** The 10-K risk factor describes eligibility failures as something that "could" happen. The 10-Q shows a self-audit begun in 2025 had found discrepancies. When they were found is not stated.
- **Evidence:** "Failures in employment eligibility verification could lead to civil penalties and loss of workers."
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, Item 1A; `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, Note 14
- **Severity:** Low (timing alone)
- **Confidence:** Low on what was known when
- **Deal impact:** Disclosure
- **Cross-check:** Ask management for the self-audit timeline.

#### SEC-29: Fatal I-5 accident suit is reserved only to the $5.0m retention
- **Finding:** On Apr 17, 2026, the estates and families of three people killed in the Feb 3, 2025 accident sued. Brindlewick reserved its $5.0m retention and tendered the claim to its excess insurers. Their response is not found. Excess cover is $50.0m per occurrence and in the aggregate, and anything above $55.0m is uninsured. The 10-K called it only a "multi-vehicle accident" and did not mention the deaths.
- **Evidence:** "the estates and families of three people killed". The 10-K risk factor: "A claim above our $55.0 million combined retention and excess coverage would be paid from our own resources." The damages sought are not found in SEC filings.
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, Note 11; `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, "Insurance", Item 1A and Note 12
- **Severity:** Medium. It would rise to High if the claim exceeds $55.0m or insurers reserve their rights.
- **Confidence:** High on the facts
- **Deal impact:** Valuation and specific protection if the claim exceeds cover
- **Cross-check:** The San Joaquin County docket (amount sought) and insurer correspondence.

#### SEC-30: Coastline seeks $41.2m for spoiled product; $1.2m is accrued under a contractual cap
- **Finding:** Coastline Seafood sued for $41.2m after a compressor failure at Sandhaven 2 in Feb 2026. Brindlewick accrued $1.2m under its warehouse-receipt limit of $0.50 per pound. Coastline did not declare a higher value. The limit is a contract term shown in the source, so it counts as a mitigant if it is enforceable.
- **Evidence:** "sued us for $41.2 million". "We have accrued $1.2 million, our estimate of liability under that limit." The full remedy is 1.5% of EV, below the 10% line, and the unaccrued gap is $40.0m (1.5%). Cargo insurance above the $1.0m retention is not described.
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, Note 11; `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, "Insurance"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation (minor) and the Sandhaven customer relationship
- **Cross-check:** The docket (challenges to the cap) and Coastline's rank in revenue_by_customer.csv.

#### SEC-31: FreshArc's trustee demands $14.6m of preferences, and the customer is liquidating
- **Finding:** FreshArc, a customer, filed for Chapter 11 on Jan 12, 2026. In July 2026 its liquidating trustee demanded $14.6m of payments made in the 90 days before the filing. Nothing is accrued; Brindlewick cites ordinary-course and new-value defenses. Because the trust is a liquidating one, FreshArc's revenue is likely lost (inference).
- **Evidence:** "demanded the return of $14.6 million of payments". That is 0.5% of EV. Annualized, $14.6m over 90 days is about $59.2m, or 4.2% of 2025 revenue, if the payments were regular (inference).
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, Note 11
- **Severity:** Medium
- **Confidence:** High on the claim. Low on the revenue inference.
- **Deal impact:** Valuation (lost revenue) and a minor liability
- **Cross-check:** FreshArc's rank and revenue trend in revenue_by_customer.csv, and the bankruptcy docket.

#### SEC-32: Calder Valley suit seeks a ban on night truck traffic, with a hearing on Jan 15, 2027
- **Finding:** A neighborhood group seeks an injunction against truck movements from 10 p.m. to 6 a.m. at Calder Valley. The site is the newest (opened Jun 2025, 64k pallets) and was the main use of $120.0m of 2025 growth capex. Nothing is accrued. The hearing comes before the expected closing.
- **Evidence:** "A hearing on the plaintiffs' motion for a preliminary injunction ... is scheduled for January 15, 2027." The share of revenue from night operations is not found in SEC filings.
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, Note 11; `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, Item 3 and Note 12
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Operations at a new site; bring-down before closing
- **Cross-check:** The Riverside County docket and local news.

#### SEC-33: Polar Ridge suit is indemnified, and the defense tender was accepted
- **Finding:** Westmark Grocers sued Polar Ridge and named Brindlewick as its former parent. Arcturus, the buyer of Polar Ridge, assumed the liabilities and accepted the defense. The 10-Q excerpts do not mention the matter.
- **Evidence:** "Arcturus has accepted our tender of defense."
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, Item 3
- **Severity:** Low (mitigated by contract and accepted tender)
- **Confidence:** High
- **Deal impact:** Mitigant
- **Cross-check:** The docket and Arcturus's ability to pay.

#### SEC-34: Greenfield Produce case dismissed with prejudice, no appeal
- **Finding:** The case is closed.
- **Evidence:** "dismissed with prejudice ... No appeal was filed."
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, Item 3
- **Severity:** Low (closed)
- **Confidence:** High
- **Deal impact:** Mitigant
- **Cross-check:** The E.D. Cal. docket.

#### SEC-35: The 10-K does not mention several events from early 2026
- **Finding:** The 10-K, filed Feb 26, 2026, does not mention three earlier events. FreshArc filed for Chapter 11 on Jan 12, 2026. The new insurance accrual rate took effect Jan 1, 2026, yet the 10-K says only that the rate "was 6.5% ... in 2025 and 2024". The Sandhaven 2 compressor failure happened in Feb 2026 (exact date not given). These are excerpts, and timing alone carries a Low rating.
- **Evidence:** Dates as above.
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`; `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, Notes 5 and 11
- **Severity:** Low (timing alone)
- **Confidence:** Medium. These are excerpts.
- **Deal impact:** Disclosure
- **Cross-check:** The full 10-K text, including subsequent events.

#### SEC-36: Controls effective, clean audit opinions, long-tenured auditor
- **Finding:** Internal control over financial reporting was effective at Dec 31, 2025, with unqualified opinions on both the financial statements and the controls. Disclosure controls were effective at Jun 30, 2026, with no control changes in Q2. Pemberton & Hale has audited the company since 2009, and the lead partner rotated in 2024. The only critical audit matter is self-insurance reserves. No auditor change and no material weakness are disclosed. The audit committee has three members, all financial experts, chaired by a former audit partner. SEC-14 sets this conclusion against the restoration practice.
- **Evidence:** "independent registered public accounting firm since 2009". "The lead engagement partner rotated in 2024, as required."
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, Item 9A; `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, Item 4; `targets/avocet/data/sec-filings/BWCC_DEF14A_2026_excerpts.md`, "Board of directors" and "Proposal 3"
- **Severity:** Low (positive, qualified by SEC-14)
- **Confidence:** High
- **Deal impact:** Mitigant
- **Cross-check:** None needed beyond SEC-14.

#### SEC-37: Known deal costs total $62.6m (2.3% of EV)
- **Finding:** The equity award cash-out ($46.2m) plus severance under the change-in-control plan ($16.4m) comes to $62.6m. Severance is payable because the buyer expects all nine officers to leave within the plan's 24-month window. Advisory and financing fees of $72.0m (2.6%) are uses of funds, not part of this total. The $110.0m reverse termination fee is paid only if the deal fails on antitrust grounds, so it cannot be paid alongside the closing costs. Counted with them it would make $172.6m (6.3%), above the 5% line. The $49.0m termination fee is payable by Brindlewick, not the buyer.
- **Evidence:** Severance recomputed:
  - CEO: (900 + 1,080) × 2.5 = $4.95m.
  - Other four named officers: 972, 936, 782 and 693 (thousands), each × 2.0 = $6.766m.
  - Named officers total $11.716m; the 8-K says about $11.7m.
  - Four other officers: 1,950 × 1.6 × 1.5 = $4.68m.
  - Total $16.396m; the 8-K says about $16.4m.
- **Source:** `targets/avocet/data/sec-filings/BWCC_8-K_2026-09-22_strategic-review.md`, Item 5.02; `targets/avocet/data/sec-filings/BWCC_DEF14A_2026_excerpts.md`, CD&A; `targets/avocet/data/deal-brief.md`, sections 3 and 4
- **Severity:** Medium (price item). Supporting: SEC-39 and SEC-40.
- **Confidence:** High
- **Deal impact:** Price
- **Cross-check:** Exhibit 10.1 (definition of good reason) and the final merger agreement.

#### SEC-38: The deal brief leaves the $16.4m severance out of sources and uses, and computes EV on basic shares
- **Finding:** Sources and uses has no line for change-in-control severance, so the funding is short by $16.4m (Trelliswood's cash would need to rise to $381.6m). The $2,750.0m EV and 11.0x multiple use basic shares only, which leaves out the $46.2m award cash-out. Including both, the EV is $2,812.6m, or 11.25x.
- **Evidence:** Deal brief uses total $2,865.2m with no severance line. 2,750.0 + 46.2 + 16.4 = 2,812.6, and 2,812.6 / 250.0 = 11.25x.
- **Source:** `targets/avocet/data/deal-brief.md`, sections 1 and 3; `targets/avocet/data/sec-filings/BWCC_8-K_2026-09-22_strategic-review.md`, Item 5.02
- **Severity:** Medium (a gap in how costs are presented)
- **Confidence:** High
- **Deal impact:** Presentation to the IC and funding
- **Cross-check:** The financial analyst's model.

#### SEC-39: PSUs vest at target under the plan, and the $46.2m cash-out recomputes
- **Finding:** Under the 2020 Omnibus Plan, awards that are not assumed vest in full, with PSUs at target. The 8-K confirms that this plan still governs. The deal brief's figure matches: RSUs $29.24m, PSUs $7.14m (at the 200% maximum they would be $14.28m) and options $9.82m, totaling $46.20m.
  - The option figure is a floor: if any tranche is underwater, the true spread payment is higher (inference).
  - Not assuming the awards makes vesting single-trigger for every holder. Assumed awards would vest only on a qualifying termination within 24 months.
  - 2,410,000 shares remained available for grants at Dec 31, 2025, so new awards could raise the cash-out (interim covenant needed).
- **Evidence:** "performance share units vest at target". 1,180,000 × (34.00 less 25.68) = $9.82m.
- **Source:** `targets/avocet/data/sec-filings/BWCC_DEF14A_2026_excerpts.md`, "Equity compensation plan information"; `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, Note 8; `targets/avocet/data/sec-filings/BWCC_8-K_2026-09-22_strategic-review.md`
- **Severity:** Low (consistent with the deal brief)
- **Confidence:** High
- **Deal impact:** Price (no change) and deal structure
- **Cross-check:** The option tranche schedule.

#### SEC-40: The severance plan was adopted the day before the sale review and raised multiples
- **Finding:** The board adopted the plan on Sep 21, 2026 and announced the strategic review the next day. Multiples rose from 1.5x to 2.5x for the CEO and from 1.0x to 2.0x for the other named officers. The plan covers terminations from 3 months before to 24 months after a change in control, has no excise tax gross-up, and cuts back payments where that leaves the executive better off. The four other officers' previous terms are not found in SEC filings.
- **Evidence:** Named-officer severance rose from $6.353m to $11.716m, up $5.363m (84.4%).
- **Source:** `targets/avocet/data/sec-filings/BWCC_8-K_2026-09-22_strategic-review.md`; `targets/avocet/data/sec-filings/BWCC_DEF14A_2026_excerpts.md`, "Potential payments upon termination or change in control"
- **Severity:** Low (governance note; the cost is in SEC-37)
- **Confidence:** High
- **Deal impact:** Price (included in SEC-37)
- **Cross-check:** Compensation committee minutes and news.

#### SEC-41: Basic and fully diluted share counts
- **Finding:** Basic shares were 48,512,330 at Feb 13, 2026 and 48,000,412 at Jul 31, 2026, a drop of 511,918 after the 515,000 buyback. Fully diluted shares are 49,359,165 by the treasury method (options add 288,753 net shares) and 50,250,412 gross.
- **Evidence:** At $34.00, equity value is $1,632.0m on basic shares and $1,678.2m including awards.
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md` and `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, covers and Note 8
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Price check
- **Cross-check:** Transfer agent count at signing.

#### SEC-42: No management departures disclosed, but the buyer's plan removes the CFO and CAO while judgments are open
- **Finding:** No officer departures are disclosed in the SEC files. The buyer expects all nine officers, including CFO Priya Venkataraman and the Chief Accounting Officer, to leave within three months of closing. Several accounting judgments would still be open: SEC-04, SEC-07, SEC-11, SEC-13 and SEC-14.
- **Evidence:** Deal brief: "we expect all nine Brindlewick executive officers to leave within three months of closing". The proxy lists the CFO and CAO among the nine.
- **Source:** `targets/avocet/data/sec-filings/BWCC_DEF14A_2026_excerpts.md`, "Executive officers"; `targets/avocet/data/deal-brief.md`, section 4
- **Severity:** Medium (gap in finance oversight; standard retention through the first audit and purchase accounting should cover it)
- **Confidence:** High
- **Deal impact:** Post-closing
- **Cross-check:** News on executive changes.

#### SEC-43: No related person transactions, and Section 16 reports were on time
- **Finding:** Both governance disclosures are clean.
- **Evidence:** "There were no related person transactions in 2025 requiring disclosure."
- **Source:** `targets/avocet/data/sec-filings/BWCC_DEF14A_2026_excerpts.md`, "Related person transactions" and "Delinquent Section 16(a) reports"
- **Severity:** Low (positive)
- **Confidence:** High
- **Deal impact:** Mitigant
- **Cross-check:** News.

#### SEC-44: 2025 bonuses paid at 104% on an Adjusted EBITDA target
- **Finding:** 2025 bonuses paid at 104% of target. Adjusted EBITDA was $271.0m against a $266.0m target (101.9%). The SEC-04 accrual change raises 2026 Adjusted EBITDA, a pay metric (inference). The 2026 target is not found in SEC filings.
- **Evidence:** "2025 annual bonuses paid at 104% of target".
- **Source:** `targets/avocet/data/sec-filings/BWCC_DEF14A_2026_excerpts.md`, CD&A
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Governance
- **Cross-check:** The 2026 bonus plan.

#### SEC-45: Value-added services is still growing
- **Finding:** Value-added services revenue grew 17.4% in FY2025 and 13.2% in H1 2026, driven by kitting and case-picking for grocery and life-sciences customers.
- **Evidence:** 182.0 vs 155.0, and 99.6 vs 88.0.
- **Source:** `targets/avocet/data/sec-filings/BWCC_10-Q_Q2-2026_excerpts.md`, "Value-added services"; `targets/avocet/data/sec-filings/BWCC_10-K_FY2025_excerpts.md`, "Results of operations"
- **Severity:** Low (positive)
- **Confidence:** High
- **Deal impact:** Mitigant
- **Cross-check:** Segment data in the financials folder.

**Earnings-base items from SEC filings (for the lead).** Each item keeps its own finding. Values are at 11.0x.

| Item | ID | $m a year | Value at 11.0x | Share of EV |
|---|---|---|---|---|
| Insurance accrual benefit in the LTM | SEC-04 | (3.7) | (40.7) | 1.5% |
| The same benefit, annualized | SEC-04 | (7.4) | (81.7) | 3.0% |
| Power repricing, illustration (projection) | SEC-15 | (8.3) | (91.6) | 3.3% |
| Property tax reassessment | SEC-16 | (4.7) | (51.7) | 1.9% |
| Sandhaven, after Sep 2028 unless extended | SEC-11 | (31.0) | (341.0) | 12.4% |
| H2 2026 repeats the H1 fall (projection) | SEC-05 | (21.0) | (231.0) | 8.4% |
| Service credits, if they do not recur | SEC-06 | +4.6 | +50.6 | 1.8% |

### Positive or mitigating points

- **Debt:** no maturities before March 2030, and all debt is prepayable at par (SEC-23).
- **Controls and auditor:** controls effective, unqualified opinions, auditor since 2009 with partner rotation in 2024, no weakness and no auditor change (SEC-36). Qualified by SEC-14.
- **Customers:** spread across about 1,310 accounts, none above 6% (SEC-20). Qualified by SEC-06, SEC-19 and SEC-31.
- **Growth:** value-added services still growing (SEC-45).
- **Adjusted EBITDA:** the 2024 $46.0m gain is correctly excluded (SEC-03).
- **Closed or covered litigation:** Greenfield was dismissed with prejudice (SEC-34). Polar Ridge is indemnified and the tender was accepted (SEC-33).
- **Price and liability protections:**
  - Warehouse-receipt cap of $0.50 per pound (SEC-30).
  - $50.0m of excess auto cover (SEC-29).
  - Fixed-price power through Dec 31, 2026, but it ends before closing (SEC-15).
- **Pay and governance:**
  - PSUs fixed at target, and no excise tax gross-up (SEC-39, SEC-40).
  - No related person transactions (SEC-43).
  - Non-union workforce, and no pension disclosed (SEC-22).
- **Sandhaven restoration:** the improvements revert to the District, so the site carries no restoration cost (SEC-13, Item 2).

### Gaps and questions for management

1. **Credit agreement:** covenant definitions, levels and test dates, change-of-control default, and letters of credit.
2. **Leases and the concession:**
   - Remaining rent and early-termination terms for Puyallup Junction, Kent Valley, Stockton North and Lodi.
   - Change-of-control and assignment clauses in all leases, the Ironbridge master lease and the Sandhaven concession.
3. **Sandhaven:** status of the talks, the carrying value and depreciation period of the improvements, and the cost of moving to an alternative site.
4. **Customer pricing:** terms of the July 2026 seven-year agreement, who the two customers requesting reviews are, and the exact wording of the most-favored-customer clauses (do they cover affiliates' rates?).
5. **Power:** 2027 contracts signed since August 2026, and their prices.
6. **Insurance and the I-5 suit:** the actuarial basis for the 4.8% accrual rate, the excess insurers' response to the I-5 tender, and the amount sought.
7. **ColdTrack:** the impairment analysis at Jun 30, 2026, and the remaining spend.
8. **FreshArc:** revenue in 2025 and 2026, the receivable at the petition date, and the preference defense analysis.
9. **ICE:** the self-audit timeline (when were the discrepancies found?), remediation, and staffing plans.
10. **Antitrust class action:** class period, co-defendants (is Trelliswood one?) and the damages theory.
11. **Severance plan:** the definition of good reason, the four other officers' previous terms, and any retention or pro-rata bonuses.
12. **Restoration:** the Holbrook report and the accounting memo on the indeterminate-settlement conclusion.
13. **Reported shareholders' equity:** not found in SEC filings, so I could not compute shares of equity.
14. **Earnings:** what the $1.4m of H1 2026 transaction costs relate to, Bayfront's revenue and organic growth, any FY2026 guidance, and Q3 2026 results.
15. **Not found in SEC filings:** guarantees, purchase obligations other than power, pension plans, and the status of Polar Ridge, which is absent from the 10-Q excerpts.
16. **Property tax:** the $4.7m reassessment split by facility.

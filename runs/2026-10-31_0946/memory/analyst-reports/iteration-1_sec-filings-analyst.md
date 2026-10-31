<!-- Iteration 1. sec-filings-analyst. Full report saved unedited by the lead agent on 2026-10-31. -->

## SEC filings analyst: findings

### Files reviewed

I read all five files in full, plus the deal brief for context:

- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/plover/data/deal-brief.md (context only)
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/plover/data/sec-filings/QTRL_10-K_FY2025_excerpts.md (filed February 26, 2026)
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/plover/data/sec-filings/QTRL_10-Q_Q2-2026_excerpts.md (filed August 6, 2026)
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/plover/data/sec-filings/QTRL_8-K_2026-07-22_borealis-vendor-agreement.md
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/plover/data/sec-filings/QTRL_8-K_2026-09-14_merger-agreement.md
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/plover/data/sec-filings/QTRL_DEF14A_2026_excerpts.md (filed April 24, 2026)

None of the files contains text that tries to instruct the agents. Valuation reference points used below come from the deal brief: EV US$1,561.0m, equity value US$1,326.0m, LTM Adjusted EBITDA US$141.0m, 11.1x, 52.0m shares. The topping premium is (25.50 - 24.00) x 52.0 = US$78.0m. Ridgeline's equity value is 24.00 x 52.0 = US$1,248.0m.

---

### Findings

#### Revenue, channels and Borealis

#### SEC-001: Revenue recognition policy for wholesale and Borealis
- **Finding:** Quillmark records wholesale revenue, including Borealis, on delivery, when control passes. It estimates returns, including stock rotation returns, as variable consideration from historical rates. No bill-and-hold, consignment or sell-through recognition is disclosed.
- **Evidence:** "We recognize wholesale revenue, including sales to Borealis, when control passes to the customer on delivery." Borealis "takes title on delivery to its fulfillment centers, and sets retail prices."
- **Source:** `targets/plover/data/sec-filings/QTRL_10-K_FY2025_excerpts.md`, sections "Note 2. Revenue recognition" and "Channels"
- **Severity:** Low
- **Confidence:** High. Stated directly in the 10-K.
- **Deal impact:** Disclosure
- **Cross-check:** Financial data pack: monthly Borealis shipments, especially late-June 2026 shipment timing.

#### SEC-002: Borealis concentration is rising
- **Finding:** Borealis's share of revenue rose from 31.3% in FY2024 to 34.8% in FY2025, 39.3% in H1 2026 and 42.5% in Q2 2026. Q2 2026 Borealis net sales rose 39.7% from Q1 2026.
- **Evidence:** FY2024: 236.0 / 1.204 = 196.0, and 196.0 / 626.0 = 31.3%. FY2025: 236.0 / 678.0 = 34.8%. H1 2026: (53.4 + 74.6) = 128.0, and 128.0 / 326.0 = 39.3%. Q2 2026: 74.6 / 175.5 = 42.5% (Q2 2025: 61.7 / 161.0 = 38.3%). Q2 over Q1: 74.6 / 53.4 = +39.7%. Risk factor: "We depend on Borealis Market for a large share of our revenue."
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "Channels", "Item 7" and "Item 1A"; `QTRL_10-Q_Q2-2026_excerpts.md`, "Part I, Item 2", "Revenue"
- **Severity:** High. This is the largest customer, its terms worsen from 2027 (SEC-004, SEC-005), and its purchase minimum is being removed.
- **Confidence:** High. Figures are stated and recomputed. Q1 2025 Borealis sales are not disclosed, so seasonality cannot be tested.
- **Deal impact:** Valuation, post-closing
- **Cross-check:** `revenue_by_customer.csv` for Borealis's rank and amount; Borealis sell-through versus sell-in data; news on Borealis fee changes for other brands.

#### SEC-003: Growth outside Borealis was about 1.6% in Q2 2026
- **Finding:** Borealis supplied 89.0% of Q2 2026 revenue growth. Revenue from all other customers and channels grew 1.6%. Q1 2026 total revenue grew only 3.8%.
- **Evidence:** Q2 total growth 175.5 - 161.0 = 14.5. Borealis growth 74.6 - 61.7 = 12.9, and 12.9 / 14.5 = 89.0%. Non-Borealis 100.9 vs 99.3 = +1.6%. Q1 2026: 326.0 - 175.5 = 150.5, vs Q1 2025: 306.0 - 161.0 = 145.0, so +3.8%.
- **Source:** `QTRL_10-Q_Q2-2026_excerpts.md`, "Results" and "Revenue"
- **Severity:** Medium
- **Confidence:** High for the arithmetic. Interpretation: Footwear grew 14.6% in H1, so the other non-Borealis parts of the business were likely flat or down. H1 Apparel growth and the H1 channel split are not disclosed.
- **Deal impact:** Valuation
- **Cross-check:** Financial data for quarterly segment and channel revenue (DTC, stores, wholesale); news on the dealer channel after the 2025 terminations.

#### SEC-004: Amended Borealis agreement cuts prices 6.0% and raises co-op fees to 10.5% from 2027
- **Finding:** From January 1, 2027, wholesale prices to Borealis fall 6.0% and the co-op fee rises from 6.0% to 10.5% of gross purchases. At FY2025 volumes this would cut annual EBITDA by about US$23.3m (projection). The CFO frames the terms as something volume must "offset ... over time."
- **Evidence:** "wholesale prices to Borealis will be reduced by 6.0% across all products"; co-op fee "will increase from 6.0% to 10.5%". Math at FY2025 volume: price cut 236.0 x 6.0% = 14.2. New co-op 10.5% x (236.0 - 14.2 = 221.8) = 23.3, against 14.2 today, so +9.1. Total 14.2 + 9.1 = 23.3. That is 23.3 / 141.0 = 16.5% of LTM Adjusted EBITDA. At 11.1x, 23.3 x 11.1 = 258.6, or 16.6% of EV. Break-even volume growth is about +28.9% (inference, assuming a 50.0% gross margin on Borealis sales: old contribution 0.44 per $ vs new 0.341). CFO: "We are not changing our outlook for 2026." The new terms start in 2027, so the 2026 outlook is unaffected by design. The 10-Q (Note 12) only cross-refers to the 8-K and does not quantify the effect.
- **Source:** `QTRL_8-K_2026-07-22_borealis-vendor-agreement.md`, "Item 1.01" and "Item 7.01"; `QTRL_10-K_FY2025_excerpts.md`, "Channels" and "Note 5"; `QTRL_10-Q_Q2-2026_excerpts.md`, "Note 12. Subsequent event"
- **Severity:** Critical. Test: more than 10% of value. At constant volume the run-rate EBITDA loss of US$23.3m is worth US$258.6m at the deal multiple, 16.6% of EV (projection).
- **Confidence:** High for the terms, which the 8-K states. The EBITDA effect is a constant-volume projection.
- **Deal impact:** Valuation
- **Cross-check:** The 2027 Borealis assumptions in the financial data pack. Compare the deal brief's ~12% Borealis growth with the ~29% volume growth needed to break even. Check news on whether "Featured Brand" status has lifted volumes for other brands.

#### SEC-005: Borealis's US$150.0m purchase minimum is removed and its return right rises to 30%
- **Finding:** From 2027, Borealis has no minimum purchase commitment, and it may return up to 30% (now 20%) of its last two quarters' purchases. Volume and return risk shift to Quillmark.
- **Evidence:** "Borealis's minimum annual purchase commitment of $150.0 million will be removed." The return right will "increase from 20% to 30%". The minimum equaled 150.0 / 678.0 = 22.1% of FY2025 revenue and 63.6% of FY2025 Borealis sales. Return capacity at H1 2026 purchase levels: 20% x 128.0 = 25.6 today; 30% x 128.0 = 38.4 from 2027.
- **Source:** `QTRL_8-K_2026-07-22_borealis-vendor-agreement.md`, "Item 1.01"; `QTRL_10-K_FY2025_excerpts.md`, "Channels"
- **Severity:** High
- **Confidence:** High. Stated directly.
- **Deal impact:** Valuation, post-closing
- **Cross-check:** The amended agreement text (not in the excerpts): does the 30% right apply to 2026 purchases, and at what credit price? Check financial data for return history.

#### SEC-006: Borealis agreement extended to December 31, 2029, with Featured Brand status
- **Finding:** The amendment removes the December 31, 2026 expiry risk flagged in the 10-K and runs to December 31, 2029.
- **Evidence:** "It takes effect on January 1, 2027 and runs to December 31, 2029." Featured Brand status gives "priority placement in search results and seasonal campaigns."
- **Source:** `QTRL_8-K_2026-07-22_borealis-vendor-agreement.md`, "Item 1.01"; `QTRL_10-K_FY2025_excerpts.md`, "Channels"
- **Severity:** Low (mitigant for retention of the largest customer; the economics are covered in SEC-004)
- **Confidence:** High
- **Deal impact:** Post-closing
- **Cross-check:** Termination and change-of-control rights in the amended agreement (not described in the filings).

#### SEC-007: Borealis returns reserve is small against the contractual return right
- **Finding:** At June 30, 2026 the Borealis returns reserve of US$3.1m was 2.4% of the two most recent quarters' Borealis sales. That is below the 3.1% historical return rate, and well below the 20% contractual maximum. The reserve was set before the July 22 amendment raised the right to 30%.
- **Evidence:** Reserve 3.1 (December 31, 2025: 2.6). 3.1 / 128.0 = 2.4%. 3.1% x 128.0 = 4.0 (inference: the reserve's base is not disclosed). Maximum 20% x 128.0 = 25.6. "Historical Borealis returns have averaged 3.1% of purchases."
- **Source:** `QTRL_10-Q_Q2-2026_excerpts.md`, "Note 2. Revenue"; `QTRL_10-K_FY2025_excerpts.md`, "Note 2. Revenue recognition"
- **Severity:** Medium
- **Confidence:** Medium. Reserve amounts are stated, but the base used to set the reserve is not disclosed.
- **Deal impact:** Valuation
- **Cross-check:** Financial data for Borealis returns by quarter and Q3 2026 returns; Borealis sell-through data.

#### SEC-008: Borealis co-op fees are booked as selling expense, not as a reduction of revenue
- **Finding:** Co-op fees paid to Borealis, a customer, are classified in SG&A. If they were treated as a reduction of the transaction price, FY2025 revenue would be US$663.8m and gross margin 48.9% instead of 50.0%. EBITDA is unaffected. The classification becomes larger from 2027 (about US$23.3m at constant volume).
- **Evidence:** "which we classify as selling expense because they fund advertising on the Borealis platform." FY2025 co-op 14.2. Gross profit 50.0% x 678.0 = 339.0, less 14.2 = 324.8, divided by (678.0 - 14.2 = 663.8) = 48.9%. Interpretation: payments to a customer normally reduce revenue unless they buy a distinct service; the filing does not describe that test. The company's own accounting treats co-op as a marketing cost, while its arbitration defense (SEC-021) implies co-op can be deducted from Net Sales.
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "Note 5. Selling, general and administrative expense" and "Channels"
- **Severity:** Medium
- **Confidence:** Medium. The facts are stated; the reclassification is an accounting judgment.
- **Deal impact:** Valuation (gross margin optics), disclosure
- **Cross-check:** Gross margin by channel in the financial data pack; auditor support for treating the co-op service as distinct.

#### SEC-009: Alder & Pine growth slowed
- **Finding:** Alder & Pine revenue growth slowed from 9.3% in FY2025 to 4.7% in H1 2026. It is the highest-margin segment.
- **Evidence:** FY2025: 164.0 vs 150.0 = +9.3%. H1 2026: "Alder & Pine revenue grew 4.7%." Contribution margins in FY2025: Alder & Pine 46.5 / 164.0 = 28.4%, Apparel 72.6 / 354.0 = 20.5%, Footwear 36.9 / 160.0 = 23.1%.
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "Segments" and "Note 12. Segment information"; `QTRL_10-Q_Q2-2026_excerpts.md`, "Revenue"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation
- **Cross-check:** Quarterly Alder & Pine revenue in the financial data; news on the Fennimore relationship.

#### SEC-010: Footwear is still growing strongly
- **Finding:** Footwear grew 13.9% in FY2025 and 14.6% in H1 2026. Its contribution rose 22.2% in FY2025.
- **Evidence:** 160.0 / 140.5 = +13.9%. Contribution 36.9 / 30.2 = +22.2%. "Footwear revenue grew 14.6% in H1 2026."
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "Segments" and "Note 12"; `QTRL_10-Q_Q2-2026_excerpts.md`, "Revenue"
- **Severity:** Low (mitigant: a growing segment; see SEC-031 for the customs-broker change affecting footwear imports)
- **Confidence:** High
- **Deal impact:** Valuation
- **Cross-check:** Quarterly footwear data; any H2 2026 shipping delays.

#### Adjusted EBITDA and outlook

#### SEC-011: A US$15.4m inventory reserve release inflates H1 2026 and LTM Adjusted EBITDA
- **Finding:** In Q2 2026 Quillmark changed how it estimates its excess and obsolete reserve. The change cut cost of revenue by US$15.4m, and the gain stays in Adjusted EBITDA, while new one-off costs are added back. Without it, H1 2026 Adjusted EBITDA fell 4.4% and gross margin fell 1.2 points. The deal brief's "highest in history" 53.0% margin depends on this release.
- **Evidence:** "This change in estimate reduced the reserve and cost of revenue by $15.4 million in Q2 2026." Gross margin rise "primarily reflects a $15.4 million reduction in cost of revenue from a change in estimate". Math: LTM 128.0 - 54.0 + 67.0 = 141.0; excluding the release, 125.6. H1 2026 excluding the release: 67.0 - 15.4 = 51.6 vs 54.0, so -4.4% (reported +24.1%). H1 gross margin excluding the release: (0.530 x 326.0 - 15.4) / 326.0 = 48.3%, vs 49.5% in H1 2025. Reserve as a share of gross inventory fell from 8.7% (22.6 / 260.6) to 2.7% (7.9 / 291.9). Value: 15.4 x 11.1 = 170.9, which is 11.0% of EV and 12.9% of equity value. EV / adjusted LTM = 1,561.0 / 125.6 = 12.4x. Fact: H1 2026 also included US$3.1m of strategic review costs, so the change came during a strategic review.
- **Source:** `QTRL_10-Q_Q2-2026_excerpts.md`, "Gross margin", "Adjusted EBITDA" and "Note 4. Inventories"; `QTRL_10-K_FY2025_excerpts.md`, "Item 7" and "Note 12"
- **Severity:** Critical. Test: more than 10% of value. Capitalizing a one-off US$15.4m at 11.1x adds US$170.9m, 11.0% of EV.
- **Confidence:** High. Stated in the 10-Q and recomputed.
- **Deal impact:** Valuation
- **Cross-check:** The financial data pack's Adjusted EBITDA bridge (does its LTM 141.0 include the 15.4?); whether the auditor reviewed the change; the Q3 2026 reserve level.

#### SEC-012: Special investigation costs of US$4.2m added back to Adjusted EBITDA
- **Finding:** H1 2026 Adjusted EBITDA adds back US$4.2m of costs for the Meridian/FCPA investigation, a new category. These costs may recur until the DOJ and SEC resolve the matter, and longer if a monitor is appointed (inference).
- **Evidence:** "Adjusted EBITDA adds back share-based compensation, special investigation costs of $4.2 million and strategic review costs of $3.1 million." "Investigation costs were $4.2 million in H1 2026."
- **Source:** `QTRL_10-Q_Q2-2026_excerpts.md`, "Adjusted EBITDA" and "Note 9", "Internal investigation"
- **Severity:** Medium
- **Confidence:** High for the amount. Recurrence is an inference.
- **Deal impact:** Valuation
- **Cross-check:** Investigation cost run-rate by month in the financial data; news on DOJ/SEC progress.

#### SEC-013: Strategic review costs of US$3.1m added back
- **Finding:** H1 2026 adds back US$3.1m of strategic review costs. These are transaction costs and are reasonably excluded.
- **Evidence:** "strategic review costs of $3.1 million."
- **Source:** `QTRL_10-Q_Q2-2026_excerpts.md`, "Adjusted EBITDA"
- **Severity:** Low (an item reasonably excluded from an adjusted metric)
- **Confidence:** High
- **Deal impact:** Valuation (minor)
- **Cross-check:** Financial data: confirm these are adviser and deal fees only.

#### SEC-014: FY2025 store closure costs of US$2.4m added back
- **Finding:** The only FY2025 non-recurring add-back was US$2.4m for closing two stores, or US$1.2m per store, a useful benchmark for the store-closure thesis.
- **Evidence:** "which in FY2025 were $2.4 million of store closure costs for two stores." 2.4 / 2 = 1.2.
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "Item 7"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Valuation (minor)
- **Cross-check:** Store-level P&L in the financial data.

#### SEC-015: FY2026 outlook reaffirmed on July 22, 2026, with no breakdown
- **Finding:** Management reaffirmed its FY2026 outlook on the same day it signed the Borealis amendment. The SEC excerpts do not state the outlook figures or whether they include the US$15.4m reserve release. They say nothing about 2027.
- **Evidence:** "We are not changing our outlook for 2026." Using the deal brief's outlook (about 720.0 revenue and 152.0 Adjusted EBITDA), the implied H2 2026 figures are revenue 394.0 vs H2 2025 372.0 (+5.9%) and Adjusted EBITDA 85.0 vs H2 2025 74.0 (+14.9%). If the outlook includes the release, underlying FY2026 is 136.6 (projection).
- **Source:** `QTRL_8-K_2026-07-22_borealis-vendor-agreement.md`, "Item 7.01"; `targets/plover/data/deal-brief.md`, section 4 (the outlook figures are not found in the SEC filings)
- **Severity:** Medium
- **Confidence:** Medium. The outlook figures come from the deal brief, not from a filing.
- **Deal impact:** Valuation
- **Cross-check:** Guidance history in the news and financial data; whether the outlook was set before Q2 2026.

#### Inventory, leases and liquidity

#### SEC-016: Inventory reserve looks thin against aged stock and rapid inventory growth
- **Finding:** At June 30, 2026, inventory more than 12 months old was US$109.0m (37.3% of gross inventory), against a reserve of only US$7.9m (7.2% of the aged stock). Inventory has grown about three times as fast as revenue. The new estimate was made as of June 30, 2026, before the July 22 Borealis amendment and while the PFAS assessment was still open.
- **Evidence:** "Inventory more than 12 months old was $109.0 million at cost at June 30, 2026." 109.0 / 291.9 = 37.3%; 7.9 / 109.0 = 7.2%. Under the old method ("25% for items 12 to 24 months old, and 60% for items over 24 months old"), a reserve of at least 25% x 109.0 = 27.3 would apply before clearance adjustments (inference). Net inventory grew 21.4% in FY2025 and 19.3% in H1 2026, against revenue growth of 8.3% and 6.5%. Of the H1 net increase of 46.0, 14.7 (32.0%) came from the lower reserve (22.6 - 7.9). The new method uses "improved sell-through data from our Borealis channel."
- **Source:** `QTRL_10-Q_Q2-2026_excerpts.md`, "Note 4. Inventories" and "Inventories"; `QTRL_10-K_FY2025_excerpts.md`, "Note 4. Inventories" and "Item 7"
- **Severity:** High
- **Confidence:** High for the numbers. Medium for the adequacy judgment, since the aging split is not disclosed.
- **Deal impact:** Valuation, post-closing (write-down risk)
- **Cross-check:** Aging schedule and PFAS-finished inventory in the financial data; Q3 2026 markdowns; Borealis sell-through.

#### SEC-017: State PFAS bans start January 1, 2027, two years before Quillmark's PFAS-free target
- **Finding:** About 31% of FY2025 apparel units used a PFAS water-repellent finish. Several states ban sales of such textiles from January 1, 2027. Quillmark's PFAS-free target is the end of FY2028. In the 10-K, management said its transition plan "addresses" the restrictions; in the 10-Q it says it is "evaluating" how they apply to products and inventory.
- **Evidence:** 10-K: "We monitor these developments and believe our transition plan addresses them." 10-Q: "we are evaluating how these laws apply to our products and inventory." Rough exposure: 31% x 354.0 = 109.7 of apparel revenue (inference: applies the unit share to revenue; only sales in the banning states are directly at risk, and that share is not disclosed).
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "Materials and product claims" and "Item 1A"; `QTRL_10-Q_Q2-2026_excerpts.md`, "Part II, Item 1A. Risk factors (update)"
- **Severity:** High
- **Confidence:** High for the facts. Medium for the exposure estimate.
- **Deal impact:** Valuation, post-closing
- **Cross-check:** News on which states ban PFAS and when; sales by state and PFAS inventory in the financial data; any PFAS claims in the litigation docket.

#### SEC-018: Store leases of US$150.0m sit outside net debt; few impairments recorded
- **Finding:** Operating lease liabilities were US$150.0m, with 7.8 years of weighted average remaining term. They are not in the deal brief's US$235.0m net debt. Only the two closed stores were impaired. The thesis of closing underperforming stores implies lease exit costs.
- **Evidence:** "Operating lease liabilities were $150.0 million at December 31, 2025, with a weighted average remaining term of 7.8 years." "Apart from the two stores closed in FY2025, we recorded no impairment." 150.0 / 1,561.0 = 9.6% of EV. Average store revenue 101.0 / 46 = 2.2. Interpretation: if some stores are underperforming, impairment indicators may have existed at December 31, 2025.
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "Note 7. Leases" and "Channels"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation, post-closing
- **Cross-check:** Store-level P&L and lease schedule in the financial data.

#### SEC-019: Negative operating cash flow and higher revolver use in H1 2026
- **Finding:** H1 2026 operating cash flow was negative US$2.5m against US$67.0m of Adjusted EBITDA. Revolver drawings rose from US$30.0m to US$55.0m.
- **Evidence:** "Net cash used in operating activities was $2.5 million in H1 2026, mainly because of the increase in inventories." Cash 64.0 to 60.0. Revolver headroom 100.0 - 55.0 = 45.0 (letters of credit not disclosed). Net debt 216.0 (250.0 + 30.0 - 64.0) to 235.0, using the deal brief's 240.0 term loan, a figure not in the 10-Q excerpt.
- **Source:** `QTRL_10-Q_Q2-2026_excerpts.md`, "Liquidity"; `QTRL_10-K_FY2025_excerpts.md`, "Liquidity"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Post-closing (working capital), valuation
- **Cross-check:** Cash flow statement and debt schedule in the financial data.

#### Alder & Pine licence

#### SEC-020: Westbrook Lane's management plan triggers Fennimore's key-person termination right
- **Finding:** Fennimore may end the Alder & Pine licence on 90 days' notice if Ms. Achterberg stops serving as CEO or Chief Creative Officer, unless it approves her successor in writing. The deal team's plan (non-executive Chair, new CEO) triggers this, and so does Ridgeline's (she resigns from both roles). Fennimore is currently arbitrating against the company (SEC-021).
- **Evidence:** Fennimore "may terminate the agreement on 90 days' written notice if Marisol Achterberg ceases ... to serve as Chief Executive Officer or Chief Creative Officer of the licensee", "unless Fennimore has approved her successor in writing." Alder & Pine FY2025: revenue 164.0 (24.2% of 678.0); contribution 46.5 (36.3% of Adjusted EBITDA of 128.0). At 11.1x, 46.5 x 11.1 = 516.2, or 33.1% of EV. The change-of-control clause (SEC-023) covers assignment only, not this trigger.
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "The Alder & Pine licence" and "Note 12"; `QTRL_8-K_2026-09-14_merger-agreement.md`, "Consulting Agreement"; plan from `targets/plover/data/deal-brief.md`, section 3
- **Severity:** Critical. Test: more than 10% of value. The right puts at risk a segment worth about US$516.2m at the deal multiple, 33.1% of EV.
- **Confidence:** High. The contract terms are summarized in the 10-K and the plan is stated in the deal brief.
- **Deal impact:** Valuation, closing risk (if a Fennimore approval is made a condition), post-closing
- **Cross-check:** News on Fennimore's stance; whether Ridgeline has a Fennimore approval or side agreement; legal reading of "CEO or CCO" (would keeping her as executive CCO avoid the trigger?).

#### SEC-021: Fennimore arbitration over US$11.6m of royalties plus a material-breach declaration
- **Finding:** Fennimore claims royalty underpayments of US$11.6m plus interest for 2021 to 2025. It says Quillmark wrongly deducted co-op fees, chargebacks and markdown allowances, and it seeks a declaration of material breach. The licence's Net Sales definition expressly bars those deductions. No accrual or loss range is disclosed.
- **Evidence:** Licence: "No deduction shall be made for advertising, co-operative marketing, promotional allowances, chargebacks, uncollectible accounts or costs of collection." Company: "We believe our royalty calculations are consistent with industry practice." "Fennimore also seeks a declaration that the underpayment is a material breach." Royalty check: 13.1 / 8.0% = 163.8 vs Alder & Pine revenue of 164.0; 12.0 / 8.0% = 150.0 vs 150.0. This suggests royalties were paid on reported net revenue, which is after allowances (inference). Implied unreported base: 11.6 / 8.0% = 145.0 over five years. The claim is 11.6 / 1,561.0 = 0.7% of EV. Hearing March 2027.
- **Source:** `QTRL_10-Q_Q2-2026_excerpts.md`, "Note 9", "Fennimore arbitration"; `QTRL_10-K_FY2025_excerpts.md`, "The Alder & Pine licence"
- **Severity:** High. The monetary remedy sought is 0.7% of EV. A breach finding would create a termination right under Section 14.1, but that section gives a 60-day cure period.
- **Confidence:** High
- **Deal impact:** Valuation, post-closing
- **Cross-check:** The arbitration demand in the litigation docket; royalty workings and any 2026 continuation in the financial data; news on the dispute.

#### SEC-022: Alder & Pine licence ends December 31, 2029 and renewal needs Fennimore's agreement
- **Finding:** The licence behind 36.3% of FY2025 Adjusted EBITDA runs only to December 31, 2029. Renewal needs mutual agreement, and the licensor is adverse.
- **Evidence:** "Term: to December 31, 2029. Renewal for a further five years requires mutual agreement." About three years would remain after a late-2026 closing (inference).
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "The Alder & Pine licence"
- **Severity:** High
- **Confidence:** High
- **Deal impact:** Valuation (terminal and exit value)
- **Cross-check:** News on Fennimore's plans for the brand; the financial forecast's assumption beyond 2029.

#### SEC-023: Licence can be assigned on a merger without Fennimore's consent
- **Finding:** A change of control by itself needs no Fennimore consent.
- **Evidence:** "the licence may be assigned in connection with a merger or sale of the licensee without Fennimore's consent, provided the licensee remains bound by all terms."
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "The Alder & Pine licence"
- **Severity:** Low (mitigant; does not cure SEC-020)
- **Confidence:** High
- **Deal impact:** Closing risk (reduced)
- **Cross-check:** The full Exhibit 10.4 text.

#### SEC-024: Royalty rate and minimum royalty
- **Finding:** The royalty is 8.0% of Net Sales, with a US$10.0m annual minimum. The FY2025 royalty of US$13.1m was 31% above the minimum.
- **Evidence:** "8.0% of Net Sales, with a minimum annual royalty of $10.0 million." 13.1 / 10.0 = 1.31.
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "The Alder & Pine licence"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Valuation (minor)
- **Cross-check:** None needed beyond SEC-021.

#### Debt

#### SEC-025: A change of control is an event of default under the credit agreement
- **Finding:** Any acquisition defaults the credit agreement, so about US$295.0m of debt must be repaid at closing. The deal brief plans this. Prepayment premiums are not found in the SEC filings.
- **Evidence:** "A change of control is an event of default under the credit agreement." December 31, 2025: term loan 250.0 (matures September 2030), revolver 30.0 drawn of 100.0 (matures September 2029). June 30, 2026: revolver 55.0. The term loan balance at June 30, 2026 is not in the 10-Q excerpt; the deal brief gives 240.0.
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "Liquidity"; `QTRL_10-Q_Q2-2026_excerpts.md`, "Liquidity"
- **Severity:** High, under the calibration rule (cured by refinancing at closing). No default before closing is indicated.
- **Confidence:** High
- **Deal impact:** Closing risk (financing certainty)
- **Cross-check:** Credit agreement (Exhibit 10.9) for prepayment terms; debt schedule in the financial data.

#### SEC-026: Wide covenant headroom
- **Finding:** Net leverage of about 1.7x is far below the 3.75x maximum, even without the reserve release.
- **Evidence:** "maximum net leverage ratio of 3.75x". December 31, 2025: 216.0 / 128.0 = 1.7x. June 30, 2026: 235.0 / 141.0 = 1.7x, and 235.0 / 125.6 = 1.9x without the release. EBITDA could fall to 235.0 / 3.75 = 62.7 before a breach. The covenant EBITDA definition, step-downs and test dates are not found in the SEC filings.
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "Liquidity"
- **Severity:** Low (mitigant)
- **Confidence:** High for the ratio. Medium for the June figure, which uses the deal brief's term loan.
- **Deal impact:** Closing risk (low)
- **Cross-check:** Compliance certificates in the financial data.

#### SEC-027: No debt maturities before 2029
- **Finding:** The revolver matures in September 2029 and the term loan in September 2030.
- **Evidence:** "a term loan of $250.0 million maturing in September 2030 ... revolving credit facility, which matures in September 2029."
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "Liquidity"
- **Severity:** Low (mitigant)
- **Confidence:** High
- **Deal impact:** Post-closing
- **Cross-check:** Financial data debt schedule.

#### Legal, regulatory and compliance

#### SEC-028: FTC lawsuit over EverTrail environmental claims
- **Finding:** The FTC investigation (civil investigative demand, November 2025) became a federal lawsuit on June 18, 2026. The FTC seeks an injunction and monetary relief for consumers, with no amount stated. No accrual is recorded. The company stopped using the "Carbon-Neutral" label on new production in January 2026.
- **Evidence:** "The complaint seeks a permanent injunction and monetary relief for consumers. The complaint does not specify an amount." "We cannot estimate a range of possible loss and have not recorded an accrual." In the 10-K the company said "We are cooperating"; in the 10-Q it says "we intend to defend ourselves vigorously." The claims are "Carbon-Neutral" (backed by Rio Verde Forest Carbon Project credits) and "Made with 100% Recycled Nylon."
- **Source:** `QTRL_10-Q_Q2-2026_excerpts.md`, "Note 9", "FTC litigation"; `QTRL_10-K_FY2025_excerpts.md`, "Item 3" and "Materials and product claims"
- **Severity:** High. The remedy sought cannot be costed: EverTrail revenue is not in the SEC filings.
- **Confidence:** High
- **Deal impact:** Valuation, post-closing
- **Cross-check:** The complaint in the litigation docket (does it seek refunds of EverTrail sales, and does it cover the recycled-nylon claim?); EverTrail sales in the financial data; news on the Rio Verde credits. If a refund remedy and EverTrail sales are found, the lead should re-test for Critical.

#### SEC-029: Dealer lawsuit survived dismissal; plaintiffs seek US$33.5m and reinstatement
- **Finding:** 38 dealers terminated in March 2025 are suing. The court denied Quillmark's motion to dismiss on April 2, 2026, and the plaintiffs seek US$33.5m plus reinstatement. The 10-Q drops the 10-K's "without merit" language and states no accrual or range.
- **Evidence:** "The plaintiffs seek damages of $33.5 million and reinstatement. Discovery is under way." The 10-K said "We believe the claims are without merit." 33.5 / 1,561.0 = 2.1% of EV, or US$0.64 per share. The claim is 1.16x the FY2024 purchases (29.0) of all 141 terminated dealers.
- **Source:** `QTRL_10-Q_Q2-2026_excerpts.md`, "Note 9", "Dealer litigation"; `QTRL_10-K_FY2025_excerpts.md`, "Item 3" and "Specialty dealers"
- **Severity:** High. The stated damages claim of US$33.5m is below 10% of value, so it is not Critical, but it is 43% of the US$78.0m topping premium.
- **Confidence:** High
- **Deal impact:** Valuation
- **Cross-check:** Court docket (W.D. Wis.) for the damages theory and schedule.

#### SEC-030: Voluntary FCPA disclosure over US$2.9m of payments to customs broker Meridian
- **Finding:** Internal audit found about US$2.9m of poorly documented "expedited processing fees" paid to Meridian from 2021 to 2025. The company self-reported to the DOJ and SEC in May 2026. Outcomes could include fines, disgorgement and a monitor. The amount is not estimable, and the exposure would pass to a buyer.
- **Evidence:** Payments "recorded as "expedited processing fees," for which supporting documentation was inadequate." "Possible consequences include fines, disgorgement and the appointment of a compliance monitor." "We cannot predict the outcome."
- **Source:** `QTRL_10-Q_Q2-2026_excerpts.md`, "Note 9", "Internal investigation"
- **Severity:** High
- **Confidence:** High
- **Deal impact:** Valuation, post-closing (successor liability, compliance cost)
- **Cross-check:** News and the docket for DOJ/SEC activity or any allegations about Port Selang officials; investigation scope in the data room.

#### SEC-031: Replacing Meridian, which cleared 41% of footwear imports, before peak season
- **Finding:** Meridian handled 41% of FY2025 footwear import volume and was dropped for new shipments from July 1, 2026, ahead of the October to December peak. Footwear is the fastest-growing segment.
- **Evidence:** "Meridian cleared 41% of our footwear import volume in FY2025." "We stopped using Meridian for new shipments from July 1, 2026 and are moving that volume to other brokers." Risk of clearance delays and higher costs (inference).
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "Sourcing and distribution"; `QTRL_10-Q_Q2-2026_excerpts.md`, "Note 9"
- **Severity:** Medium
- **Confidence:** High for the facts. The operational impact is an inference.
- **Deal impact:** Post-closing
- **Cross-check:** News on Port Selang delays; Q3 2026 footwear shipments in the financial data.

#### SEC-032: Delaware unclaimed property audit of gift cards, with US$9m to US$31m reasonably possible and not accrued
- **Finding:** Quillmark has recognized US$34.8m of gift card breakage since 2011 on the view that its gift card LLC is not subject to unclaimed property laws. Delaware opened an audit in April 2026 covering 2011 to 2025 and may estimate amounts where records are incomplete. Delaware's position also puts future breakage revenue in question.
- **Evidence:** 10-K: "We believe unredeemed balances of Quillmark Gift Card LLC are not subject to unclaimed property laws, and we have not remitted unredeemed balances to any state." 10-Q: "we believe a loss is reasonably possible in a range of $9 million to $31 million, including interest. We have not recorded an accrual." The upper end is 2.0% of EV, US$0.60 per share, 89.1% of cumulative breakage (31.0 / 34.8) and 40% of the topping premium.
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "Note 2", "Gift cards"; `QTRL_10-Q_Q2-2026_excerpts.md`, "Note 9", "Unclaimed property audit"
- **Severity:** High
- **Confidence:** High
- **Deal impact:** Valuation (liability outside net debt)
- **Cross-check:** Annual breakage and unredeemed balances in the financial data; the litigation/regulatory docket for audit status.

#### SEC-033: Cedar Hollow permit renewal is opposed; the permit expires December 31, 2026
- **Finding:** Cedar Hollow shipped 72% of FY2025 units. Its 24-hour peak-season operation depends on a county permit that expires December 31, 2026. A neighborhood group opposes the renewal, and a decision is expected in Q4 2026.
- **Evidence:** "shipped 72% of our units in FY2025." "A neighborhood group has opposed the renewal. We expect a decision in the fourth quarter of 2026." The 10-K said "We expect to apply for renewal in 2026"; the application was filed in March 2026.
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "Sourcing and distribution"; `QTRL_10-Q_Q2-2026_excerpts.md`, "Note 9", "Cedar Hollow permit"
- **Severity:** Medium on SEC evidence. Interpretation: denial would limit capacity from peak 2027 rather than close the site. Raise the severity if other sources show an adverse ruling or added conditions.
- **Confidence:** High
- **Deal impact:** Post-closing, closing risk (timing of decision)
- **Cross-check:** Linwood County hearing records in the litigation folder; local news.

#### SEC-034: Down supplier certificate suspended and reinstated (closed)
- **Finding:** A down supplier's Responsible Down Standard certificate was suspended in March 2026 and reinstated in May 2026. No product claims changed.
- **Evidence:** "It was reinstated in May 2026 after a re-audit. We did not change any product claims."
- **Source:** `QTRL_10-Q_Q2-2026_excerpts.md`, "Note 9", "Down certification"
- **Severity:** Low (closed)
- **Confidence:** High
- **Deal impact:** Disclosure
- **Cross-check:** News for any consumer or NGO claims about the lapse.

#### SEC-035: US$95.0m trademark claim dismissed with prejudice; no appeal (closed)
- **Finding:** The Quilmarque SAS trademark claim was dismissed with prejudice on January 14, 2026. The appeal period lapsed.
- **Evidence:** "The time to appeal expired on February 13, 2026 and no appeal was filed."
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "Item 3"
- **Severity:** Low (closed; mitigant)
- **Confidence:** High
- **Deal impact:** None remaining
- **Cross-check:** Court docket (S.D.N.Y.) to confirm the case is closed.

#### SEC-036: Sunvale's US$38.0m claim against the former Kids subsidiary is indemnified by the buyer
- **Finding:** Sunvale sued Quillmark Kids LLC, the former subsidiary, not Quillmark itself as stated. The buyer, Bramblecrest Kids, assumed the defense under an indemnity backed by an escrow and a parent guarantee.
- **Evidence:** "Bramblecrest Kids LLC has assumed the defense under the sale agreement indemnity." "The indemnity is supported by a $15.0 million escrow that runs to August 2027 and by a guarantee from Bramblecrest Holdings, Inc." The escrow covers 15.0 / 38.0 = 39.5% of the claim; the rest relies on the guarantee.
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "Divestiture" and "Item 3"
- **Severity:** Low (neutralized by contract)
- **Confidence:** High
- **Deal impact:** Post-closing (residual credit risk on the guarantor)
- **Cross-check:** Court docket: is Quillmark Trail Co. named? Check Bramblecrest Holdings' financial health in the news.

#### SEC-037: 2023 sale of Quillmark Kids at a US$11.8m loss (historical)
- **Finding:** The Kids business was sold in August 2023 for US$18.0m, with an US$11.8m loss recorded in other income (expense).
- **Evidence:** "sold our Quillmark Kids business to Bramblecrest Kids LLC for $18.0 million and recognized a loss on sale of $11.8 million"
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "Divestiture"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None
- **Cross-check:** None needed.

#### SEC-038: Nylon prices fixed through 2027 for about 70% of volume
- **Finding:** A supply agreement fixes prices for about 70% of expected nylon volume through December 31, 2027.
- **Evidence:** "fixes prices through December 31, 2027 for about 70% of our expected nylon volume."
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "Sourcing and distribution"
- **Severity:** Low (mitigant: supply and price protection)
- **Confidence:** High
- **Deal impact:** Valuation (cost protection)
- **Cross-check:** Mill concentration and terms in the data room.

#### Merger agreement and deal execution

#### SEC-039: The founder controls the outcome and gets US$32.0m from Ridgeline alone
- **Finding:** Ms. Achterberg holds 71.8% of the voting power and has agreed to tender to Ridgeline. Ridgeline will also pay her US$8.0m a year for four years, "whether or not services are requested." That is money other shareholders do not get. On these numbers she is better off under Ridgeline at US$24.00 than under Westbrook Lane at US$25.50 without a side arrangement (inference). A Westbrook offer cannot meet a majority-of-voting-power condition without her shares.
- **Evidence:** She "has agreed to tender her shares into the offer. The support agreement terminates if the Merger Agreement is terminated." Ridgeline "will pay her a consulting fee of $8.0 million a year for four years ($32.0 million in total), payable whether or not services are requested." Her services are "up to 10 hours a month," or about US$66,700 per hour at full use. Her 2025 total pay was US$4.9m. She "is not entitled to change-in-control severance." Math (inference, pre-tax): Ridgeline 11.0m shares x 24.00 = 264.0, plus 32.0, = 296.0 (US$26.91 per share); Westbrook 11.0 x 25.50 = 280.5. Gap 15.5 in Ridgeline's favor. Voting: (104.0 + 0.6) / 145.6 = 71.8%. Interpretation: extra pay to a controlling holder can draw shareholder challenges to the Ridgeline deal.
- **Source:** `QTRL_8-K_2026-09-14_merger-agreement.md`, "Tender and Support Agreement" and "Consulting Agreement"; `QTRL_DEF14A_2026_excerpts.md`, "Security ownership", "Employment agreement with our founder" and "Executive compensation (summary)"
- **Severity:** Critical. Test: could stop the deal. She controls 71.8% of the votes, and her personal economics favor Ridgeline by about US$15.5m (inference).
- **Confidence:** High for the facts. The incentive comparison is an inference.
- **Deal impact:** Closing risk
- **Cross-check:** News on her intentions; any shareholder suits over the consulting agreement in the litigation docket; what role and pay the Westbrook plan would offer her.

#### SEC-040: Ridgeline's offer expires one minute after the go-shop ends
- **Finding:** The go-shop and the tender offer end at the same moment. Her tender alone meets the voting-power condition. If the HSR waiting period has expired, Ridgeline could accept shares at expiry (inference). Westbrook would need its superior proposal accepted, and the Ridgeline agreement terminated, before 11:59 p.m. on November 13, 2026, 13 days after October 31.
- **Evidence:** "The offer is scheduled to expire at one minute after 11:59 p.m. Eastern on November 13, 2026, unless extended." Go-shop: "Until 11:59 p.m. Eastern on November 13, 2026". Conditions include "a majority of the voting power of the outstanding shares" and "expiration of the HSR Act waiting period". HSR status and matching rights are not found in the SEC filings.
- **Source:** `QTRL_8-K_2026-09-14_merger-agreement.md`, "Merger Agreement"
- **Severity:** High
- **Confidence:** High for the dates. Inference on HSR status.
- **Deal impact:** Closing risk
- **Cross-check:** News for HSR early termination or second request; full merger agreement for matching rights and notice periods.

#### SEC-041: Break fees of US$18.7m in the go-shop and US$43.7m after
- **Finding:** Quillmark owes US$18.7m if it takes a superior proposal from a party that bid during the go-shop, and US$43.7m in other cases. A winning Westbrook bid would in effect bear the fee.
- **Evidence:** The US$18.7m applies to "a superior proposal from a party that submitted a proposal during the go-shop period". 18.7 / 1,248.0 = 1.5% and 43.7 / 1,248.0 = 3.5% of Ridgeline's equity value. 18.7 / 52.0 = US$0.36 per share, or 24.0% of the topping premium.
- **Source:** `QTRL_8-K_2026-09-14_merger-agreement.md`, "Termination fees"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Valuation, closing risk (Westbrook must submit before the deadline)
- **Cross-check:** Full merger agreement for the "superior proposal" definition and any expense reimbursement.

#### SEC-042: Ridgeline's offer has no financing or third-party consent condition
- **Finding:** Ridgeline's offer is not conditioned on financing or on any third-party consent, including Fennimore's. A Westbrook bid that adds a Fennimore approval or financing condition may be judged less certain, and so not superior (inference).
- **Evidence:** "The offer is not conditioned on financing or on any third-party consent."
- **Source:** `QTRL_8-K_2026-09-14_merger-agreement.md`, "Conditions"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Closing risk
- **Cross-check:** News on Ridgeline's financing and any arrangement with Fennimore.

#### SEC-043: Board independence and special committee process
- **Finding:** Seven of nine directors are independent and there is a Lead Independent Director. A special committee of independent directors recommended the deal and was told about the consulting agreement beforehand. The filings do not disclose a majority-of-the-minority condition.
- **Evidence:** "The special committee was informed of the Consulting Agreement before approving the Merger Agreement." Board: "nine directors, seven of whom are independent."
- **Source:** `QTRL_8-K_2026-09-14_merger-agreement.md`, "Merger Agreement" and "Consulting Agreement"; `QTRL_DEF14A_2026_excerpts.md`, "Corporate governance"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** Closing risk (process)
- **Cross-check:** The Schedule 14D-9 (not in the files) for the committee's reasoning.

#### SEC-044: Single-trigger RSU vesting costs about US$40.8m, likely outside the deal brief's equity value
- **Finding:** About 1.6m unvested RSUs vest in full at closing and are paid in cash. At US$25.50 that is US$40.8m. The deal brief's US$1,326.0m uses 52.0m outstanding shares, which appear to exclude the RSUs (inference).
- **Evidence:** "All unvested restricted stock units (about 1.6 million) will vest in full at the effective time and be paid out at the offer price." Proxy: RSUs vest "on a change in control ("single trigger"), whether or not employment ends." 1.6 x 25.50 = 40.8, which is 3.1% of equity value and 52% of the topping premium. On a fully diluted basis: 53.6 x 25.50 = 1,366.8, plus 235.0 = 1,601.8 EV, or 11.4x.
- **Source:** `QTRL_8-K_2026-09-14_merger-agreement.md`, "Equity awards"; `QTRL_DEF14A_2026_excerpts.md`, "Potential payments on a change in control" and "Security ownership"
- **Severity:** High
- **Confidence:** High for the RSU count and terms. Medium on whether they sit outside the 52.0m.
- **Deal impact:** Valuation
- **Cross-check:** Fully diluted share count in the financial data.

#### SEC-045: Double-trigger cash severance of US$11.4m for four executives
- **Finding:** The CFO, COO, CMO and GC get two times salary plus target bonus if they are terminated, or leave for good reason, within 24 months of a change of control. Bringing in a new CEO could prompt good-reason claims (inference).
- **Evidence:** "It equals two times base salary plus target bonus." Cash total 11.4. Their RSUs, valued at US$19.40 (10.2), would be worth 10.2 x 25.50 / 19.40 = 13.4 at US$25.50. That amount is already inside SEC-044's 40.8.
- **Source:** `QTRL_DEF14A_2026_excerpts.md`, "Potential payments on a change in control"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Post-closing
- **Cross-check:** Integration plan and retention needs.

#### Founder, governance and pay

#### SEC-046: The founder has no post-employment non-compete in the Westbrook scenario
- **Finding:** Ms. Achterberg's employment agreement has no post-employment non-compete. The only non-compete is in Ridgeline's consulting agreement, which applies only if Ridgeline closes. Under the Westbrook plan she would receive about US$280.5m in cash and be free to compete once she leaves.
- **Evidence:** "The agreement does not contain a post-employment non-compete covenant." Risk factor: she "leads our product design and our relationships with key partners. We do not have key-person insurance." Ridgeline's consulting agreement: "She agrees not to compete with Ridgeline or the Company for four years."
- **Source:** `QTRL_DEF14A_2026_excerpts.md`, "Employment agreement with our founder"; `QTRL_10-K_FY2025_excerpts.md`, "Item 1A"; `QTRL_8-K_2026-09-14_merger-agreement.md`, "Consulting Agreement"
- **Severity:** High. Needs a specific protection: a restrictive covenant agreement signed with the bid.
- **Confidence:** High
- **Deal impact:** Post-closing, valuation
- **Cross-check:** News on her plans after a sale.

#### SEC-047: Founder employment agreement ends March 31, 2027; no formal succession plan
- **Finding:** Her agreement as CEO and CCO runs only to March 31, 2027, and the board has no formal succession plan. If the agreement is not extended, the Fennimore key-person trigger (SEC-020) could arise even without a deal.
- **Evidence:** It "was extended in 2024 and runs to March 31, 2027." "has not adopted a formal succession plan for these roles."
- **Source:** `QTRL_DEF14A_2026_excerpts.md`, "Employment agreement with our founder" and "Corporate governance"
- **Severity:** Medium
- **Confidence:** High
- **Deal impact:** Post-closing
- **Cross-check:** News on renewal talks.

#### SEC-048: Executive bonuses weight Adjusted EBITDA at 40%
- **Finding:** 2025 bonuses were based 40% on revenue, 40% on Adjusted EBITDA and 20% on individual goals. If the 2026 plan is similar (not found), the Q2 2026 reserve release and the new add-backs raise the metric that drives pay (inference).
- **Evidence:** "Annual bonuses for 2025 were based on revenue (40%), Adjusted EBITDA (40%) and individual goals (20%)."
- **Source:** `QTRL_DEF14A_2026_excerpts.md`, "Executive compensation (summary)"
- **Severity:** Medium
- **Confidence:** Medium. The 2026 metrics are not found in the SEC filings.
- **Deal impact:** Disclosure, valuation (earnings quality)
- **Cross-check:** 2026 bonus plan and accruals in the data room.

#### SEC-049: Dual-class structure gives the founder 71.8% of votes on a 21.2% economic stake
- **Finding:** Class B shares carry 10 votes each and convert to Class A on transfer, so an acquirer ends up with ordinary one-vote shares.
- **Evidence:** "Class B shares convert to Class A shares on transfer, other than to permitted transferees." Economic interest 11.0 / 52.0 = 21.2%; voting 104.6 / 145.6 = 71.8%.
- **Source:** `QTRL_DEF14A_2026_excerpts.md`, "Security ownership"
- **Severity:** Low (the deal effect is covered in SEC-039)
- **Confidence:** High
- **Deal impact:** Closing risk (context)
- **Cross-check:** None needed.

#### SEC-050: No pledged shares
- **Finding:** No director or officer has pledged company shares.
- **Evidence:** "None of our directors or executive officers has pledged Company shares."
- **Source:** `QTRL_DEF14A_2026_excerpts.md`, "Security ownership"
- **Severity:** Low (mitigant)
- **Confidence:** High
- **Deal impact:** None
- **Cross-check:** None needed.

#### Internal controls and auditor

#### SEC-051: ICFR was concluded effective for a year in which undocumented payments were made
- **Finding:** Management concluded internal control over financial reporting was effective at December 31, 2025. In March 2026, internal audit found payments from 2021 to 2025 recorded without adequate support. The 10-Q excerpt contains no reassessment or material weakness disclosure (Item 4 is not excerpted).
- **Evidence:** "Management concluded that our internal control over financial reporting was effective at December 31, 2025." Payments "for which supporting documentation was inadequate."
- **Source:** `QTRL_10-K_FY2025_excerpts.md`, "Item 9A. Controls and procedures"; `QTRL_10-Q_Q2-2026_excerpts.md`, "Note 9", "Internal investigation"
- **Severity:** Medium
- **Confidence:** Medium. The conclusion and the payments are stated; whether a material weakness exists is not disclosed.
- **Deal impact:** Disclosure, post-closing (remediation)
- **Cross-check:** Auditor communications and the 10-Q Item 4 in the data room.

#### SEC-052: Long-standing auditor; clean opinion; no auditor change
- **Finding:** Brackenridge & Stowe has audited Quillmark since 2014, gave an unqualified opinion for FY2025 and is reappointed for 2026. Audit fees were US$2.1m. No auditor change or reportable events are disclosed.
- **Evidence:** "Brackenridge & Stowe has audited our financial statements since 2014. Audit fees were $2.1 million in 2025."
- **Source:** `QTRL_DEF14A_2026_excerpts.md`, "Proposal 3: Ratification of auditor"; `QTRL_10-K_FY2025_excerpts.md`, "Item 9A"
- **Severity:** Low
- **Confidence:** High
- **Deal impact:** None
- **Cross-check:** None needed.

#### SEC-053: Proxy refers vaguely to an "internal review" in "2025 and early 2026"
- **Finding:** The April 2026 proxy says the Audit Committee held special meetings about an "internal review," without dates. The 10-Q dates the discovery to March 2026, and the February 2026 10-K mentions no review.
- **Evidence:** "met eleven times in 2025 and early 2026, including special meetings about an internal review."
- **Source:** `QTRL_DEF14A_2026_excerpts.md`, "Corporate governance"
- **Severity:** Low (rests on timing only)
- **Confidence:** Medium. The wording is ambiguous.
- **Deal impact:** Disclosure
- **Cross-check:** Audit Committee minutes: did the review start before the 10-K was filed?

#### Note for the lead: changes between filings

| Topic | 10-K (Feb 26, 2026) | Later filing | Card |
|---|---|---|---|
| FTC | CID; "We are cooperating" | Complaint filed June 18, 2026; "defend ourselves vigorously"; no accrual | SEC-028 |
| Dealers | "without merit" | Motion to dismiss denied; US$33.5m and reinstatement sought; "without merit" not repeated | SEC-029 |
| Fennimore | Licence described, no dispute | Arbitration filed May 11, 2026 | SEC-021 |
| Meridian | Licensed broker, 41% of footwear | FCPA self-disclosure; dropped July 1, 2026 | SEC-030, SEC-031 |
| Gift cards | Not subject to unclaimed property laws | Delaware audit; US$9m to US$31m reasonably possible | SEC-032 |
| Cedar Hollow | "expect to apply" | Applied March 2026; opposed | SEC-033 |
| PFAS | Plan "addresses them" | Bans from January 1, 2027; "evaluating" | SEC-017 |
| Inventory reserve | Fixed percentages by age | Sell-through method; US$15.4m release | SEC-011 |
| Adjusted EBITDA | Add-back of US$2.4m store closures | Add-backs of US$4.2m and US$3.1m; release kept in | SEC-011 to SEC-013 |
| Borealis | US$150.0m minimum; 20% returns; 6.0% co-op; ends 2026 | Minimum removed; 30%; 10.5%; prices -6.0%; to 2029 | SEC-004 to SEC-006 |
| Founder | CEO and CCO | Resigns at Ridgeline closing; US$32.0m consulting fee | SEC-039 |

Quantified items not in the deal brief's net debt or equity value: RSU payout US$40.8m (SEC-044), go-shop fee US$18.7m (SEC-041), lease liabilities US$150.0m (SEC-018), dealer claim US$33.5m (SEC-029), unclaimed property US$9.0m to US$31.0m (SEC-032), Fennimore US$11.6m plus interest (SEC-021). The three quantified contingencies total 33.5 + 31.0 + 11.6 = US$76.1m at the top of the ranges, about equal to the US$78.0m topping premium. The FTC and FCPA matters are not quantified.

---

### Positive or mitigating points

- **Debt maturities:** none before September 2029 (SEC-027). Covenant headroom is wide at about 1.7x against a 3.75x maximum (SEC-026).
- **Customer retention:** Borealis is renewed to December 31, 2029 with Featured Brand status, which removes the 2026 expiry risk (SEC-006). This comes with weaker economics (SEC-004).
- **Segments still growing:** Footwear +14.6% in H1 2026 (SEC-010). Borealis sales +20.9% in Q2 2026 (SEC-002). Alder & Pine is still growing, at +4.7% (SEC-009).
- **Items correctly excluded from adjusted metrics:** strategic review costs of US$3.1m (SEC-013) and FY2025 store closure costs of US$2.4m (SEC-014) are reasonable add-backs.
- **Closed or neutralized litigation:** the US$95.0m Quilmarque claim was dismissed with prejudice and not appealed (SEC-035). The US$38.0m Sunvale claim is indemnified by Bramblecrest, backed by a US$15.0m escrow and a parent guarantee (SEC-036). The down certificate was reinstated (SEC-034).
- **Supply and price protection:** nylon prices are fixed through 2027 for about 70% of volume (SEC-038).
- **Contract protections:** the Alder & Pine licence can be assigned on a merger without consent (SEC-023). The founder's support agreement ends if the Ridgeline agreement is terminated (SEC-039). A reduced US$18.7m fee applies to go-shop bidders (SEC-041).
- **Remediation steps:** the company self-reported to the DOJ and SEC and stopped using Meridian (SEC-030).
- **Governance:** no pledged shares (SEC-050); cash severance is double trigger (SEC-045); the auditor's opinion was clean and there was no auditor change (SEC-052).
- **Relative point:** Ridgeline's plan triggers the same Fennimore key-person clause (SEC-020), so this risk is not unique to Westbrook Lane.

### Gaps and questions for management

**Not found in the SEC filings:**
- Term loan balance at June 30, 2026 (the deal brief's US$240.0m figure).
- The covenant EBITDA definition, step-downs and test dates; prepayment premiums; letters of credit.
- Matching rights, the superior-proposal definition, HSR filing status, and any no-shop terms after the go-shop.
- The amended Borealis agreement text (the 8-K said it would be filed with the next 10-Q; it is not in the excerpts). Key questions: termination rights, change of control, and whether the 30% return right covers 2026 purchases and at what credit price.
- Q1 2025 Borealis sales; Borealis sell-through data; H1 2026 segment and channel revenue (including Apparel growth).
- The aging split of the US$109.0m of old inventory (12 to 24 months versus over 24 months); PFAS-finished inventory at cost; whether the auditor reviewed the change in estimate.
- EverTrail revenue; whether the FTC complaint also challenges the recycled-nylon claim.
- Accrual or loss range for the Fennimore and dealer matters.
- Share-based compensation amount; 2026 bonus metrics; related-party transactions; insider trading (10b5-1) plans; goodwill and intangibles; annual gift card breakage and unredeemed balances.
- Whether the 1.6m RSUs are included in the 52.0m share count; Ms. Achterberg's own unvested RSUs.
- The 2026 outlook figures themselves, and whether they include the US$15.4m release.

**Questions for management:**
1. Has Fennimore approved, or been asked to approve, any CEO or CCO successor? Does Ridgeline have an arrangement with Fennimore?
2. Would Ms. Achterberg back a Westbrook Lane bid without a Ridgeline-style consulting agreement? What role and pay would she accept?
3. Why was the reserve method changed in Q2 2026, and what would the old method give at June 30, 2026?
4. What is the expected 2027 effect of the Borealis amendment, and what volume growth does management assume to offset it?
5. Did the Audit Committee's "internal review" start before the 10-K was filed on February 26, 2026? Has ICFR been reassessed?
6. What is the contingency plan if Cedar Hollow's permit is not renewed?

**Accounting judgments made as of a date (for the lead to test against later evidence):**
- Inventory reserve: set June 30, 2026, before the July 22 Borealis amendment and before the PFAS assessment was finished (SEC-011, SEC-016).
- Borealis returns reserve: June 30, 2026, based on the 20% right (SEC-007).
- Gift card position: as of the February 2026 10-K, before the April 2026 Delaware audit (SEC-032).
- Store impairment: December 31, 2025 (SEC-018).
- ICFR effectiveness: December 31, 2025 (SEC-051).
- PFAS "addresses them" statement: February 2026 (SEC-017).

**Critical findings (four):** SEC-004, SEC-011 and SEC-020 meet the more-than-10%-of-value test. SEC-039 meets the could-stop-the-deal test.

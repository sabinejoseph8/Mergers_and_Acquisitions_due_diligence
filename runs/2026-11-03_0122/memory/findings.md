# Findings register

Status: Verification complete (2026-11-03). 136 findings: 93 Verified, 28 Partially verified, 0 Rejected, 15 Low findings Open (not verified). Awaiting Checkpoint 3.

The Status cell holds exactly one of: Open, Verified, Partially verified, Rejected, with nothing added. A Low finding that is not sent to the verifier stays Open; "not verified" is written only in the report appendix list.

Value base for every percentage test: enterprise value $2,750.0m (5% = $137.5m, 10% = $275.0m). Deal multiple 11.0x.

Each row's Source(s) cell names the source files and links to the full finding card in the saved analyst report. LIT-01 to LIT-08 match the case IDs in `litigation/docket_index.csv`.

## Cross-source findings (lead agent)

| ID | Finding | Workstream | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|---|
| X-01 | Normalized LTM earnings base is $217.5m to $222.5m, not $250.0m (project rule: the unaccrued FreshArc loss of $6.0m to $11.0m deducted from the base; change-of-control property tax included); at 11.0x, value is $302.5m to $357.5m (11.0% to 13.0% of EV) below EV, before the run-rate fall and Sandhaven (projection) | Cross-source | Critical | Medium | Built from X-03, X-04, SEC-06, X-13, SEC-16; draws on X-02 and X-05 (separate parents); supporting: FIN-03; [card](#x-01) | Partially verified |
| X-02 | Operating trend: revenue, occupancy, price, throughput, transport margin and guidance weakened; annualized H1 2026 fall of $42.0m is $462.0m (16.8% of EV) at 11.0x (projection) | Cross-source | Critical | Medium | Separate parents cited: X-04, X-03, X-12, SEC-06; supporting: FIN-02, SEC-05, NEWS-01, FIN-10, FIN-12, FIN-13, NEWS-02, NEWS-03, FIN-30, FIN-11, SEC-08; [card](#x-02) | Verified |
| X-03 | 2021 fixed-price power contracts (70% of use at $61/MWh) end Dec 31, 2026; at 2027 to 2029 offers of about $104/MWh, cost rises $17.7m a year, $195.0m (7.1% of EV) at 11.0x (projection) | Cross-source | High | Medium | Supporting: SEC-15, NEWS-11, FIN-17; [card](#x-03) | Verified |
| X-04 | Insurance accrual rate cut from 6.5% to 4.8% (dated Jan 1, 2026) is put in doubt by later accident data and the I-5 suit; it adds $3.7m to the LTM and $7.3m a year (projection) | Cross-source | High | Medium | Supporting: SEC-04, FIN-04, NEWS-04; cites FIN-14, X-14, LIT-10; [card](#x-04) | Partially verified |
| X-05 | Sandhaven 1 and 2 earn $31.0m (12.4%) of LTM Adjusted EBITDA on a concession ending Sep 30, 2028 with no renewal option; the District's executive director says there will be no extension past 2028; $341.0m (12.4% of EV) at 11.0x; the deal brief does not address it | Cross-source | Critical | High | Supporting: SEC-11, NEWS-21; cites X-06, X-07; [card](#x-05) | Partially verified |
| X-06 | Sandhaven disclosure gap: the 10-K said Brindlewick expected to negotiate an extension while the Harbor District says it had told Brindlewick for more than a year there would be none | Cross-source | Medium | Medium | Supporting: SEC-12, NEWS-22; [card](#x-06) | Verified |
| X-07 | Merger review: combined capacity shares of about 43% (Puget Sound) and 39% (Northern Central Valley), the buyer's stated plan to close acquired capacity, and a $15.0m divestiture cap could block closing | Cross-source | Critical | Medium | Supporting: SEC-26, NEWS-12, NEWS-13, NEWS-14, LIT-09; cites X-05, X-08, X-11; [card](#x-07) | Partially verified |
| X-08 | Antitrust class action: treble damages with joint and several liability give a $1,800.0m upper bound (65.5% of EV); no accrual; the 10-Q omits the July 2026 co-defendant settlement | Cross-source | Critical | Medium | Supporting: LIT-01, NEWS-15, SEC-25; cites X-07; [card](#x-08) | Verified |
| X-09 | Unrecorded lease-end restoration of $312.0m (11.3% of EV, 48.6% of equity); the buyer's plan to surrender four leases triggers $118.0m, which is not in the $45.0m integration budget | Cross-source | Critical | High | Supporting: SEC-13, FIN-25; cites X-10, NEWS-09; [card](#x-09) | Verified |
| X-10 | Effective-controls conclusions for FY2025 (ICFR, unqualified opinion) and H1 2026 (disclosure controls) sit against unrecorded restoration (FY2025, H1 2026), the insurance accrual cut (H1 2026) and the unaccrued FreshArc loss (H1 2026); restatement risk for those periods (inference) | Cross-source | High | Medium | Supporting: SEC-14; cites SEC-36, X-09, X-04, X-13, SEC-42; [card](#x-10) | Partially verified |
| X-11 | Known deal costs: award cash-out $46.2m plus CIC severance $16.4m plus the $110.0m reverse termination fee total $172.6m (6.3% of EV); closing-case cost is $62.6m (2.3%) | Cross-source | High | High | Supporting: SEC-37, SEC-39, SEC-40, FIN-35, FIN-38; cites SEC-38, X-07; [card](#x-11) | Verified |
| X-12 | Harvest Peak seven-year contract at about 9% below rate card has triggered most-favored-customer reviews; upper bound $15.2m a year on $169.0m of MFN revenue, $167.3m (6.1% of EV) (projection) | Cross-source | High | Medium | Supporting: SEC-19, FIN-16, NEWS-08; cites NEWS-09; [card](#x-12) | Verified |
| X-13 | FreshArc (10th-largest customer, $31.8m) ceased operations; the preference loss Brindlewick's counsel calls likely ($6.0m to $11.0m, if the case is not settled) is not accrued | Cross-source | Medium | High | Supporting: LIT-04, SEC-31, LIT-11, FIN-28; [card](#x-13) | Partially verified |
| X-14 | I-5 fatal crash suit: $150.0m demand against $55.0m of combined retention and excess cover leaves $95.0m uninsured; the 10-K omitted the deaths and the 10-Q omits the demand | Cross-source | High | Medium | Supporting: LIT-02, NEWS-16, SEC-29; cites X-04, LIT-10; [card](#x-14) | Verified |
| X-15 | ColdTrack: no impairment of $47.0m capitalized software at Jun 30, 2026, although deployments were paused before that date and the August 6 10-Q reports a 60.5% cost overrun; the buyer's plan halts it (inference: write-off) | Cross-source | Medium | Medium | Supporting: SEC-07, FIN-20, NEWS-10; [card](#x-15) | Partially verified |
| X-16 | Deferred maintenance: capex fell from 4.1% to 2.3% of revenue, $96.0m of priority replacements fall in 2027 to 2029, and a compressor and its standby failed at Sandhaven 2 | Cross-source | Medium | High | Supporting: SEC-17, FIN-18, LIT-12; cites LIT-05; [card](#x-16) | Partially verified |

## Analyst findings

| ID | Finding | Workstream | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|---|
| SEC-01 | Adjusted EBITDA definition and the LTM build check out | SEC filings | Low | High | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-01-adjusted-ebitda-definition-and-the-ltm-build-check-out) | Verified |
| SEC-02 | Add-backs labeled non-recurring come back every period | SEC filings | Low | High | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`; supporting: FIN-05, FIN-06; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-02-add-backs-labeled-non-recurring-come-back-every-period) | Verified |
| SEC-03 | The 2024 sale-leaseback gain is correctly kept out of Adjusted EBITDA | SEC filings | Low | High | `BWCC_10-K_FY2025_excerpts.md`; supporting: FIN-09, NEWS-06; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-03-the-2024-sale-leaseback-gain-is-correctly-kept-out-of-adjusted-ebitda) | Verified |
| SEC-04 | A cut in the insurance accrual rate lifts LTM earnings by $3.7m while accidents rose | SEC filings | Medium | High | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-04-a-cut-in-the-insurance-accrual-rate-lifts-ltm-earnings-by-37m-while-accidents-rose) | Verified |
| SEC-05 | First-half 2026 results weakened in almost every segment and metric | SEC filings | High | High | `BWCC_10-Q_Q2-2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-05-first-half-2026-results-weakened-in-almost-every-segment-and-metric) | Verified |
| SEC-06 | ColdTrack service credits of $4.6m reduced H1 2026 revenue; two customers moved part of their volume to other providers (10-Q does not say whether it returned); one anonymous customer says it moved about a third and has not moved it back (single anonymous source) | SEC filings | Low | High | `BWCC_10-Q_Q2-2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-06-coldtrack-service-credits-of-46m-reduced-h1-2026-revenue) | Partially verified |
| SEC-07 | ColdTrack is over budget and paused, with $47.0m capitalized and no impairment; the buyer will halt it | SEC filings | Medium | High | `BWCC_10-Q_Q2-2026_excerpts.md`, `deal-brief.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-07-coldtrack-is-over-budget-and-paused-with-470m-capitalized-and-no-impairment-the-buyer-will-halt-it) | Verified |
| SEC-08 | FY2025 growth includes acquired and new capacity | SEC filings | Low | High | `BWCC_10-K_FY2025_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-08-fy2025-growth-includes-acquired-and-new-capacity) | Verified |
| SEC-09 | No FY2026 guidance in the SEC filings | SEC filings | Low | High | ?; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-09-no-fy2026-guidance-in-the-sec-filings) | Open |
| SEC-10 | Share buybacks in Q1 2026, then suspended in April | SEC filings | Low | High | `BWCC_10-Q_Q2-2026_excerpts.md`; supporting: FIN-23; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-10-share-buybacks-in-q1-2026-then-suspended-in-april) | Open |
| SEC-11 | The Sandhaven concession ends Sep 30, 2028, and the Harbor District plans other use from 2029 | SEC filings | Critical | High | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`, `BWCC_8-K_2026-03-20_harbor-district-update.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-11-the-sandhaven-concession-ends-sep-30-2028-and-the-harbor-district-plans-other-use-from-2029) | Verified |
| SEC-12 | The 10-K said management expected to negotiate a Sandhaven extension; the District says it had told Brindlewick for more than a year that there would be no extension (news, single named source); alternative sites first appear in the 8-K; not timing alone | SEC filings | Medium | High | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`, `BWCC_8-K_2026-03-20_harbor-district-update.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-12-sandhaven-wording-changed-between-filings) | Partially verified |
| SEC-13 | $312.0m of lease-end restoration is unrecorded, and the buyer's plan triggers $118.0m of it | SEC filings | Critical | High | `BWCC_10-K_FY2025_excerpts.md`, `deal-brief.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-13-3120m-of-lease-end-restoration-is-unrecorded-and-the-buyers-plan-triggers-1180m-of-it) | Verified |
| SEC-14 | The effective-controls conclusion sits alongside the unrecorded restoration obligations | SEC filings | Medium | Medium | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-14-the-effective-controls-conclusion-sits-alongside-the-unrecorded-restoration-obligations) | Verified |
| SEC-15 | Fixed-price power ends Dec 31, 2026, before closing, and 2027 forward prices are "substantially above" | SEC filings | High | High | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-15-fixed-price-power-ends-dec-31-2026-before-closing-and-2027-forward-prices-are-substantially-above) | Verified |
| SEC-16 | The change of control itself raises California property tax by about $4.7m a year | SEC filings | Medium | High | `BWCC_10-K_FY2025_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-16-the-change-of-control-itself-raises-california-property-tax-by-about-47m-a-year) | Verified |
| SEC-17 | Maintenance capex was deferred (2.5% of revenue in 2025, 2.3% in H1 2026, against 4.1% in 2023), and $96m of priority replacements fall due in 2027 to 2029, most of it after a Q2 to Q3 2027 closing | SEC filings | Medium | High | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-17-maintenance-capex-was-deferred-and-96m-of-priority-replacements-fall-due-in-2027-to-2029) | Partially verified |
| SEC-18 | The Ironbridge sale-leaseback depends on a contestable "sale" judgment | SEC filings | Medium | Medium | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_DEF14A_2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-18-the-ironbridge-sale-leaseback-depends-on-a-contestable-sale-judgment) | Verified |
| SEC-19 | Most-favored-customer clauses cover about $169.0m of revenue, and two customers have asked for repricing | SEC filings | High | Medium | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-19-most-favored-customer-clauses-cover-about-1690m-of-revenue-and-two-customers-have-asked-for-repricing) | Verified |
| SEC-20 | Customer concentration is low | SEC filings | Low | High | `BWCC_10-K_FY2025_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-20-customer-concentration-is-low) | Verified |
| SEC-21 | Change-of-control and assignment terms of leases and contracts are not disclosed | SEC filings | Medium | High | `BWCC_10-K_FY2025_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-21-change-of-control-and-assignment-terms-of-leases-and-contracts-are-not-disclosed) | Verified |
| SEC-22 | No pension or multiemployer plan disclosed, and the workforce is non-union | SEC filings | Low | Medium | `BWCC_10-K_FY2025_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-22-no-pension-or-multiemployer-plan-disclosed-and-the-workforce-is-non-union) | Verified |
| SEC-23 | No debt matures before 2030, and all debt can be repaid at par | SEC filings | Low | High | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-23-no-debt-matures-before-2030-and-all-debt-can-be-repaid-at-par) | Verified |
| SEC-24 | Covenant terms and change-of-control default are not disclosed, and leverage is rising | SEC filings | Medium | High | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-24-covenant-terms-and-change-of-control-default-are-not-disclosed-and-leverage-is-rising) | Verified |
| SEC-25 | Antitrust class action survived the motion to dismiss (Aug 14, 2026) and seeks treble damages on at least $600m of alleged class-wide overcharges, with joint and several liability ($1,800.0m upper bound, 65.5% of EV); nothing is accrued | SEC filings | Critical | High | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-25-antitrust-class-action-seeks-treble-damages-with-no-accrual) | Partially verified |
| SEC-26 | The merger overlaps in two markets where Brindlewick holds about 19% and 18% | SEC filings | High | Medium | `BWCC_10-K_FY2025_excerpts.md`, `deal-brief.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-26-the-merger-overlaps-in-two-markets-where-brindlewick-holds-about-19-and-18) | Verified |
| SEC-27 | ICE is inspecting six warehouses; a self-audit found unresolved eligibility documentation discrepancies for about 410 employees (6.2% of all staff); no penalty or workforce estimate | SEC filings | High | High | `BWCC_10-Q_Q2-2026_excerpts.md`; supporting: NEWS-20; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-27-ice-is-inspecting-six-warehouses-with-known-eligibility-gaps-for-about-410-workers) | Partially verified |
| SEC-28 | The 10-K's I-9 risk factor was written as hypothetical while a self-audit was under way | SEC filings | Low | Low | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-28-the-10-ks-i-9-risk-factor-was-written-as-hypothetical-while-a-self-audit-was-under-way) | Verified |
| SEC-29 | Fatal I-5 accident suit is reserved only to the $5.0m retention | SEC filings | Medium | High | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-29-fatal-i-5-accident-suit-is-reserved-only-to-the-50m-retention) | Verified |
| SEC-30 | Coastline seeks $41.2m for spoiled product; $1.2m is accrued under a contractual cap | SEC filings | Medium | High | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-30-coastline-seeks-412m-for-spoiled-product-12m-is-accrued-under-a-contractual-cap) | Verified |
| SEC-31 | FreshArc (No. 10 customer, $31.8m FY2025 revenue) has liquidated; its trustee seeks $14.6m of preferences; counsel expects a recovery of $6m to $11m, none accrued (H1 2026 interim statements, and Q3 2026 if unaccrued: restatement risk, inference) | SEC filings | Medium | High | `BWCC_10-Q_Q2-2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-31-fresharcs-trustee-demands-146m-of-preferences-and-the-customer-is-liquidating) | Partially verified |
| SEC-32 | Calder Valley suit seeks a ban on night truck traffic, with a hearing on Jan 15, 2027 | SEC filings | Medium | High | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-32-calder-valley-suit-seeks-a-ban-on-night-truck-traffic-with-a-hearing-on-jan-15-2027) | Verified |
| SEC-33 | Polar Ridge suit is indemnified, and the defense tender was accepted | SEC filings | Low | High | `BWCC_10-K_FY2025_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-33-polar-ridge-suit-is-indemnified-and-the-defense-tender-was-accepted) | Verified |
| SEC-34 | Greenfield Produce case dismissed with prejudice, no appeal | SEC filings | Low | High | `BWCC_10-K_FY2025_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-34-greenfield-produce-case-dismissed-with-prejudice-no-appeal) | Verified |
| SEC-35 | The 10-K does not mention several events from early 2026 | SEC filings | Low | Medium | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-35-the-10-k-does-not-mention-several-events-from-early-2026) | Verified |
| SEC-36 | Controls effective, clean audit opinions, long-tenured auditor | SEC filings | Low | High | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`, `BWCC_DEF14A_2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-36-controls-effective-clean-audit-opinions-long-tenured-auditor) | Verified |
| SEC-37 | Known deal costs total $62.6m (2.3% of EV) | SEC filings | Medium | High | `BWCC_8-K_2026-09-22_strategic-review.md`, `BWCC_DEF14A_2026_excerpts.md`, `deal-brief.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-37-known-deal-costs-total-626m-23-of-ev) | Verified |
| SEC-38 | Neither the sources and uses nor the $45.0m integration budget includes the $16.4m change-in-control severance, an unbudgeted cash cost after closing; fully diluted EV is $2,796.2m (11.18x), all-in cost with severance $2,812.6m (11.25x); all value tests stay on $2,750.0m | SEC filings | Medium | High | `BWCC_8-K_2026-09-22_strategic-review.md`, `deal-brief.md`; supporting: FIN-37; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-38-the-deal-brief-leaves-the-164m-severance-out-of-sources-and-uses-and-computes-ev-on-basic-shares) | Partially verified |
| SEC-39 | PSUs vest at target under the plan, and the $46.2m cash-out recomputes | SEC filings | Low | High | `BWCC_10-Q_Q2-2026_excerpts.md`, `BWCC_8-K_2026-09-22_strategic-review.md`, `BWCC_DEF14A_2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-39-psus-vest-at-target-under-the-plan-and-the-462m-cash-out-recomputes) | Verified |
| SEC-40 | The severance plan was adopted the day before the sale review and raised multiples | SEC filings | Low | High | `BWCC_8-K_2026-09-22_strategic-review.md`, `BWCC_DEF14A_2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-40-the-severance-plan-was-adopted-the-day-before-the-sale-review-and-raised-multiples) | Verified |
| SEC-41 | Basic and fully diluted share counts | SEC filings | Low | High | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-41-basic-and-fully-diluted-share-counts) | Open |
| SEC-42 | No management departures disclosed, but the buyer's plan removes the CFO and CAO while judgments are open | SEC filings | Medium | High | `BWCC_DEF14A_2026_excerpts.md`, `deal-brief.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-42-no-management-departures-disclosed-but-the-buyers-plan-removes-the-cfo-and-cao-while-judgments-are-open) | Verified |
| SEC-43 | No related person transactions, and Section 16 reports were on time | SEC filings | Low | High | `BWCC_DEF14A_2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-43-no-related-person-transactions-and-section-16-reports-were-on-time) | Open |
| SEC-44 | 2025 bonuses paid at 104% on an Adjusted EBITDA target | SEC filings | Low | High | `BWCC_DEF14A_2026_excerpts.md`; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-44-2025-bonuses-paid-at-104-on-an-adjusted-ebitda-target) | Open |
| SEC-45 | Value-added services is still growing | SEC filings | Low | High | `BWCC_10-K_FY2025_excerpts.md`, `BWCC_10-Q_Q2-2026_excerpts.md`; supporting: NEWS-05, FIN-15; [card](analyst-reports/iteration-1_sec-filings-analyst.md#sec-45-value-added-services-is-still-growing) | Verified |
| NEWS-01 | 2026 guidance cut; H1 2026 Adjusted EBITDA down 15.1% | News and media | High | High | `2026-02-26_capital-markets-wire_brindlewick-q4-results.md`, `2026-08-07_capital-markets-wire_q2-results-guidance-cut.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-01-2026-guidance-cut-h1-2026-adjusted-ebitda-down-151) | Verified |
| NEWS-02 | Occupancy decline, rate cuts and new Central Valley capacity | News and media | Medium | High | `2026-02-26_capital-markets-wire_brindlewick-q4-results.md`, `2026-06-16_supply-chain-insider_trelliswood-investor-day.md`, `2026-07-08_supply-chain-insider_harvest-peak-contract.md`, `2026-08-07_capital-markets-wire_q2-results-guidance-cut.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-02-occupancy-decline-rate-cuts-and-new-central-valley-capacity) | Verified |
| NEWS-03 | Transportation operating ratio worsened to 96.4% | News and media | Medium | High | `2026-08-07_capital-markets-wire_q2-results-guidance-cut.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-03-transportation-operating-ratio-worsened-to-964) | Verified |
| NEWS-04 | Lower insurance and claims accrual rate added about $3.7m to H1 2026 | News and media | Medium | Medium | `2026-04-22_freight-safety-monitor_i5-crash-lawsuit.md`, `2026-08-07_capital-markets-wire_q2-results-guidance-cut.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-04-lower-insurance-and-claims-accrual-rate-added-about-37m-to-h1-2026) | Verified |
| NEWS-05 | Value-added services still growing (positive) | News and media | Low | High | `2026-02-26_capital-markets-wire_brindlewick-q4-results.md`, `2026-08-07_capital-markets-wire_q2-results-guidance-cut.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-05-value-added-services-still-growing-positive) | Verified |
| NEWS-06 | 2024 sale-leaseback gain of $46.0m (one-off, outside the LTM) | News and media | Low | High | `2026-02-26_capital-markets-wire_brindlewick-q4-results.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-06-2024-sale-leaseback-gain-of-460m-one-off-outside-the-ltm) | Verified |
| NEWS-07 | Market reaction and takeover speculation | News and media | Low | High | `2026-02-26_capital-markets-wire_brindlewick-q4-results.md`, `2026-08-07_capital-markets-wire_q2-results-guidance-cut.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-07-market-reaction-and-takeover-speculation) | Open |
| NEWS-08 | Harvest Peak seven-year contract priced about 9% below rate card | News and media | Medium | Medium | `2026-07-08_supply-chain-insider_harvest-peak-contract.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-08-harvest-peak-seven-year-contract-priced-about-9-below-rate-card) | Verified |
| NEWS-09 | Harvest Peak volume sits at two of the four sites Trelliswood plans to close | News and media | Medium | Medium | `2026-07-08_supply-chain-insider_harvest-peak-contract.md`, `deal-brief.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-09-harvest-peak-volume-sits-at-two-of-the-four-sites-trelliswood-plans-to-close) | Verified |
| NEWS-10 | ColdTrack rollout failures, customer credits and deployment pause | News and media | Medium | Medium | `2026-06-02_supply-chain-insider_coldtrack-rollout-glitches.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-10-coldtrack-rollout-failures-customer-credits-and-deployment-pause) | Verified |
| NEWS-11 | 2027 to 2029 power forward prices near record | News and media | Medium | Medium | `2026-09-30_grid-and-power-report_northwest-power-forwards.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-11-2027-to-2029-power-forward-prices-near-record) | Verified |
| NEWS-12 | Antitrust: Trelliswood's stated shares in both overlap markets | News and media | High | Medium | `2026-06-16_supply-chain-insider_trelliswood-investor-day.md`, `deal-brief.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-12-antitrust-trelliswoods-stated-shares-in-both-overlap-markets) | Verified |
| NEWS-13 | Trelliswood investor-day statements a reviewer could use | News and media | High | High | `2026-06-16_supply-chain-insider_trelliswood-investor-day.md`, `deal-brief.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-13-trelliswood-investor-day-statements-a-reviewer-could-use) | Verified |
| NEWS-14 | Coldmetric information-exchange ruling as a merger-review signal | News and media | Medium | Low | `2026-06-16_supply-chain-insider_trelliswood-investor-day.md`, `2026-08-19_courtroom-wire_cold-storage-antitrust-ruling.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-14-coldmetric-information-exchange-ruling-as-a-merger-review-signal) | Verified |
| NEWS-15 | Cold storage price-sharing class action against Brindlewick: damages are trebled and defendants can be held jointly liable for the whole amount, so $1,800.0m is the upper bound; only Northern Frost agreed to cooperate with plaintiffs (Coldmetric cooperates with the court) | News and media | Critical | Medium | `2026-08-19_courtroom-wire_cold-storage-antitrust-ruling.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-15-cold-storage-price-sharing-class-action-against-brindlewick) | Partially verified |
| NEWS-16 | I-5 fatal crash wrongful death suit, $150m demand | News and media | High | Medium | `2026-04-22_freight-safety-monitor_i5-crash-lawsuit.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-16-i-5-fatal-crash-wrongful-death-suit-150m-demand) | Verified |
| NEWS-17 | Rising fleet crash rate | News and media | Medium | Medium | `2026-04-22_freight-safety-monitor_i5-crash-lawsuit.md`, `2026-08-07_capital-markets-wire_q2-results-guidance-cut.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-17-rising-fleet-crash-rate) | Verified |
| NEWS-18 | Calder Valley noise suit seeks overnight truck ban | News and media | Medium | Medium | `2025-12-09_central-valley-business-journal_calder-valley-noise-suit.md`, `2026-02-26_capital-markets-wire_brindlewick-q4-results.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-18-calder-valley-noise-suit-seeks-overnight-truck-ban) | Verified |
| NEWS-19 | Fresno temperature-log rumor, denied by the company | News and media | Low | Low | `2026-05-11_coldchaintalk-forum_fresno-temperature-logs.md`, `2026-05-14_central-valley-business-journal_brindlewick-denies-forum-claims.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-19-fresno-temperature-log-rumor-denied-by-the-company) | Open |
| NEWS-20 | ICE I-9 inspections at six sites and about 410 unresolved eligibility discrepancies (company disclosure); reported night-shift staffing losses and temporary labor at about 35% above payroll (unconfirmed: unnamed workers and agency) | News and media | Medium | Medium | `2026-08-26_central-valley-business-journal_ice-inspections.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-20-ice-i-9-inspections-and-staffing-losses) | Partially verified |
| NEWS-21 | Sandhaven concession ends September 30, 2028, with no extension | News and media | High | High | `2026-03-18_sandhaven-harbor-ledger_terminal-7-plan-vote.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-21-sandhaven-concession-ends-september-30-2028-with-no-extension) | Verified |
| NEWS-22 | CEO's extension expectation contradicted by the Harbor District | News and media | Medium | Medium | `2026-02-26_capital-markets-wire_brindlewick-q4-results.md`, `2026-03-18_sandhaven-harbor-ledger_terminal-7-plan-vote.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-22-ceos-extension-expectation-contradicted-by-the-harbor-district) | Verified |
| NEWS-23 | Food bank donation | News and media | Low | High | `2026-10-14_sandhaven-harbor-ledger_food-bank-donation.md`; [card](analyst-reports/iteration-1_news-media-analyst.md#news-23-food-bank-donation) | Open |
| LIT-01 | Antitrust class action: $1,800.0m upper bound under trebled, joint and several damages, no accrual; Brindlewick subscribed to Coldmetric for the whole period the alleged exchange operated (2019 until reports were suspended in March 2025); the class covers purchases from 2019 to present | Litigation | Critical | Medium | `LIT-01_refrigerated-warehousing-antitrust.md`, `docket_index.csv`; [card](analyst-reports/iteration-1_litigation-analyst.md#lit-01-antitrust-class-action-damages-exposure-joint-and-several-liability-no-accrual) | Partially verified |
| LIT-09 | Antitrust class action: effect on the merger review, injunction, and Trelliswood's own status | Litigation | Medium | Medium | `LIT-01_refrigerated-warehousing-antitrust.md`; [card](analyst-reports/iteration-1_litigation-analyst.md#lit-09-antitrust-class-action-effect-on-the-merger-review-injunction-and-trelliswoods-own-status) | Verified |
| LIT-02 | Okafor wrongful death: $150.0m demand, defense counsel's adverse view on liability, insurance unconfirmed | Litigation | High | Medium | `LIT-02_okafor-wrongful-death.md`, `docket_index.csv`; [card](analyst-reports/iteration-1_litigation-analyst.md#lit-02-okafor-wrongful-death-1500m-demand-defense-counsels-adverse-view-on-liability-insurance-unconfirmed) | Verified |
| LIT-10 | Okafor fleet safety allegations: 15.5 hours on duty against a 14-hour limit, 11 unreviewed camera fatigue events and a post-crash ELD edit; Brindlewick admits the edit but says it corrected a duty-status error, and says the alerts were reviewed; the alleged yearly rise in accident frequency since 2023 matches Brindlewick's KPI data | Litigation | Medium | Low | `LIT-02_okafor-wrongful-death.md`; [card](analyst-reports/iteration-1_litigation-analyst.md#lit-10-fleet-safety-and-record-keeping-allegations-from-okafor) | Partially verified |
| LIT-03 | Calder Valley nuisance: risk of an injunction on night operations | Litigation | Medium | Medium | `LIT-03_calder-valley-nuisance.md`; supporting: NEWS-18, SEC-32; [card](analyst-reports/iteration-1_litigation-analyst.md#lit-03-calder-valley-nuisance-risk-of-an-injunction-on-night-operations) | Verified |
| LIT-04 | FreshArc preference claim: $14.6m claimed, counsel's "likely" $6.0m to $11.0m if not settled, no accrual; the Q2 2026 10-Q relies on defenses that counsel's estimate puts in doubt, and the Q1 and Q2 2026 interim statements may lack an accrual of at least $6.0m (inference) | Litigation | Medium | High | `LIT-04_freshArc-preference.md`, `docket_index.csv`; [card](analyst-reports/iteration-1_litigation-analyst.md#lit-04-fresharc-preference-claim-146m-claimed-counsels-likely-60m-to-110m-no-accrual) | Partially verified |
| LIT-11 | FreshArc: loss of the tenth-largest customer and $3.9m of unpaid services | Litigation | Medium | High | `LIT-04_freshArc-preference.md`; [card](analyst-reports/iteration-1_litigation-analyst.md#lit-11-fresharc-loss-of-the-tenth-largest-customer-and-39m-of-unpaid-services) | Verified |
| LIT-05 | Coastline Seafood spoilage: $41.2m claimed against an about $1.24m contractual limit; summary judgment hearing December 11, 2026 | Litigation | Medium | High | `LIT-05_coastline-seafood-spoilage.md`, `docket_index.csv`; supporting: SEC-30; [card](analyst-reports/iteration-1_litigation-analyst.md#lit-05-coastline-seafood-spoilage-412m-claimed-against-an-about-124m-contractual-limit-summary-judgment-hearing-december-11-2026) | Verified |
| LIT-12 | Sandhaven 2 freezer failure: both the main and the standby compressor failed | Litigation | Medium | Medium | `LIT-05_coastline-seafood-spoilage.md`; [card](analyst-reports/iteration-1_litigation-analyst.md#lit-12-sandhaven-2-freezer-failure-both-the-main-and-the-standby-compressor-failed) | Verified |
| LIT-06 | Westmark / Polar Ridge alter ego claim: neutralized by an uncapped, accepted indemnity (mitigant) | Litigation | Low | Medium | `LIT-06_westmark-polar-ridge.md`; supporting: SEC-33; [card](analyst-reports/iteration-1_litigation-analyst.md#lit-06-westmark--polar-ridge-alter-ego-claim-neutralized-by-an-uncapped-accepted-indemnity-mitigant) | Verified |
| LIT-07 | Greenfield Produce breach of contract: dismissed with prejudice, closed (mitigant) | Litigation | Low | High | `docket_index.csv`; supporting: SEC-34; [card](analyst-reports/iteration-1_litigation-analyst.md#lit-07-greenfield-produce-breach-of-contract-dismissed-with-prejudice-closed-mitigant) | Verified |
| LIT-08 | Canadian trademark opposition by Brindlewick Papeterie | Litigation | Low | High | `docket_index.csv`; [card](analyst-reports/iteration-1_litigation-analyst.md#lit-08-canadian-trademark-opposition-by-brindlewick-papeterie) | Open |
| FIN-01 | The $250.0m LTM Adjusted EBITDA rebuilds exactly from the source | Financial analysis | Low | High | `adjusted_ebitda_reconciliation.csv`, `income_statement.csv`; supporting: SEC-01; [card](analyst-reports/iteration-1_financial-analyst.md#fin-01-the-2500m-ltm-adjusted-ebitda-rebuilds-exactly-from-the-source) | Verified |
| FIN-02 | H1 2026 Adjusted EBITDA is down 15.1%; the annualized fall of $42.0m is worth $462.0m at 11.0x | Financial analysis | Critical | Medium | `income_statement.csv`, `adjusted_ebitda_reconciliation.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-02-h1-2026-adjusted-ebitda-is-down-151-the-annualized-fall-of-420m-is-worth-4620m-at-110x) | Verified |
| FIN-03 | Adjusting only for the insurance accrual change (FIN-04) and recurring severance (FIN-05), normalized LTM and run-rate earnings imply $51.7m to $310.2m less value at 11.0x (projection); the bridge excludes items in the SEC filings and news (power, property tax, ColdTrack credits, FreshArc), which X-01 adds | Financial analysis | High | Medium | `adjusted_ebitda_reconciliation.csv`, `kpis.csv`, `income_statement.csv`, `deal-brief.md`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-03-normalized-ltm-and-run-rate-earnings-imply-517m-to-3102m-less-value-at-110x-projection) | Partially verified |
| FIN-04 | The insurance and claims accrual rate was cut from 6.5% to 4.8% while the accident rate rose 16.7% | Financial analysis | High | Medium | `kpis.csv`, `income_statement.csv`, `balance_sheet.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-04-the-insurance-and-claims-accrual-rate-was-cut-from-65-to-48-while-the-accident-rate-rose-167) | Verified |
| FIN-05 | Severance and restructuring "non-recurring" costs recur every year | Financial analysis | Low | High | `adjusted_ebitda_reconciliation.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-05-severance-and-restructuring-non-recurring-costs-recur-every-year) | Verified |
| FIN-06 | Transaction-related costs of $1.4m in H1 2026 predate the announced strategic review | Financial analysis | Low | Medium | `adjusted_ebitda_reconciliation.csv`, `deal-brief.md`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-06-transaction-related-costs-of-14m-in-h1-2026-predate-the-announced-strategic-review) | Verified |
| FIN-07 | The acquisition integration add-back is declining and tied to the 2025 acquisition | Financial analysis | Low | High | `adjusted_ebitda_reconciliation.csv`, `cash_flow.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-07-the-acquisition-integration-add-back-is-declining-and-tied-to-the-2025-acquisition) | Open |
| FIN-08 | Share-based compensation add-back | Financial analysis | Low | High | `adjusted_ebitda_reconciliation.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-08-share-based-compensation-add-back) | Open |
| FIN-09 | The November 2024 sale-leaseback gain is correctly excluded from Adjusted EBITDA | Financial analysis | Low | High | `income_statement.csv`, `adjusted_ebitda_reconciliation.csv`, `cash_flow.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-09-the-november-2024-sale-leaseback-gain-is-correctly-excluded-from-adjusted-ebitda) | Verified |
| FIN-10 | Revenue growth turned negative, and Q3 2025 breaks the trend | Financial analysis | High | High | `revenue_quarterly.csv`, `income_statement.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-10-revenue-growth-turned-negative-and-q3-2025-breaks-the-trend) | Verified |
| FIN-11 | Two 2025 additions flatter H1 2026 against H1 2025: Bayfront Cold Storage, acquired March 2025 for $88.0m (42k positions), and Calder Valley, opened June 2025 (64k positions); like-for-like decline is worse than the reported -1.9% (inference); revenue from the two sites is not disclosed | Financial analysis | Medium | Low | `cash_flow.csv`, `balance_sheet.csv`, `kpis.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-11-the-2025-acquisition-masks-organic-decline-and-acquired-revenue-is-not-disclosed-in-my-files) | Partially verified |
| FIN-12 | Warehousing occupancy fell 4.2 points and revenue per occupied pallet fell 3.8% | Financial analysis | High | High | `kpis.csv`, `income_statement.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-12-warehousing-occupancy-fell-42-points-and-revenue-per-occupied-pallet-fell-38) | Verified |
| FIN-13 | Transportation volume is falling and its operating ratio is near breakeven | Financial analysis | Medium | High | `kpis.csv`, `income_statement.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-13-transportation-volume-is-falling-and-its-operating-ratio-is-near-breakeven) | Verified |
| FIN-14 | DOT recordable accidents per million miles are up 16.7% in six months | Financial analysis | Medium | High | `kpis.csv`; supporting: NEWS-17; [card](analyst-reports/iteration-1_financial-analyst.md#fin-14-dot-recordable-accidents-per-million-miles-are-up-167-in-six-months) | Verified |
| FIN-15 | Value-added services are still growing | Financial analysis | Low | High | `income_statement.csv`, `kpis.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-15-value-added-services-are-still-growing) | Verified |
| FIN-16 | Most-favored-customer pricing covers a rising share of warehousing revenue while rates fall | Financial analysis | Medium | Medium | `kpis.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-16-most-favored-customer-pricing-covers-a-rising-share-of-warehousing-revenue-while-rates-fall) | Verified |
| FIN-17 | About 70% of electricity is bought at $61.0/MWh under 2021 fixed-price agreements that expire Dec 31, 2026; at the about $104/MWh 2027 to 2029 offers, the fixed volume costs about $17.7m more a year, $195.0m at 11.0x (7.1% of EV); range $14.8m to $20.6m a year (5.9% to 8.2%) (projection) | Financial analysis | High | Medium | `kpis.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-17-electricity-is-70-fixed-at-a-flat-610mwh-in-every-period-expiry-is-not-in-my-files) | Partially verified |
| FIN-18 | Maintenance capex fell to 2.3% of revenue while refrigeration systems aged | Financial analysis | Medium | Medium | `cash_flow.csv`, `kpis.csv`, `balance_sheet.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-18-maintenance-capex-fell-to-23-of-revenue-while-refrigeration-systems-aged) | Verified |
| FIN-19 | No pallet positions or warehouses were added in H1 2026 despite $48.0m of growth capex; no source says what it funded (construction in progress or new services, inference); if some of it is sustaining spend, FIN-18 understates the maintenance gap (inference) | Financial analysis | Medium | Low | `cash_flow.csv`, `kpis.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-19-480m-of-h1-2026-growth-capex-added-no-capacity) | Partially verified |
| FIN-20 | Capitalized software of $47.0m at Jun 30, 2026, principally ColdTrack, would have little use to the buyer once the plan halts ColdTrack (inference, non-cash); the 10-Q concluded no impairment was required although deployments were paused and the program estimate rose from $38.0m to $61.0m | Financial analysis | Low | Medium | `balance_sheet.csv`, `cash_flow.csv`, `kpis.csv`, `deal-brief.md`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-20-470m-of-capitalized-coldtrack-software-would-be-stranded-by-the-integration-plan) | Partially verified |
| FIN-21 | The deal brief's net debt of $1,118.0m ties to the June 30, 2026 balance sheet | Financial analysis | Low | High | `balance_sheet.csv`, `cash_flow.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-21-the-deal-briefs-net-debt-of-11180m-ties-to-the-june-30-2026-balance-sheet) | Verified |
| FIN-22 | Leverage rose to 4.47x in six months, and interest cover is falling | Financial analysis | Medium | High | `balance_sheet.csv`, `adjusted_ebitda_reconciliation.csv`, `income_statement.csv`; supporting: SEC-24; [card](analyst-reports/iteration-1_financial-analyst.md#fin-22-leverage-rose-to-447x-in-six-months-and-interest-cover-is-falling) | Verified |
| FIN-23 | Share buybacks continued while the revolver funded the shortfall | Financial analysis | Low | High | `cash_flow.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-23-share-buybacks-continued-while-the-revolver-funded-the-shortfall) | Open |
| FIN-24 | Operating lease liabilities of $668.0m sit outside net debt, consistent with the EBITDA definition | Financial analysis | Low | High | `balance_sheet.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-24-operating-lease-liabilities-of-6680m-sit-outside-net-debt-consistent-with-the-ebitda-definition) | Verified |
| FIN-25 | The $45.0m integration budget has no cost for surrendering the four leased warehouses; the 10-K puts their lease-end restoration at $118.0m (undiscounted, 2025 prices), which an exit decision brings onto the balance sheet; remaining rent is not disclosed (current terms end 2029 to 2033); X-09 holds the $312.0m liability | Financial analysis | High | Medium | `balance_sheet.csv`, `deal-brief.md`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-25-the-integration-budget-has-no-cost-for-surrendering-four-leased-warehouses) | Partially verified |
| FIN-26 | Possible debt-like items outside the $1,118.0m: accrued claims reserves of $44.1m and other non-current liabilities of $25.5m (composition unknown), together $69.6m (2.5% of EV); deferred refrigeration projects (FIN-18) and restoration (X-09) are separate issues; CIC severance of about $16.4m is not accrued; no source supports a multiemployer exposure (no union employees) | Financial analysis | Medium | Medium | `balance_sheet.csv`, `kpis.csv`, `deal-brief.md`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-26-other-debt-like-items-outside-the-deals-net-debt) | Partially verified |
| FIN-27 | Customer concentration is low and stable | Financial analysis | Low | High | `revenue_by_customer.csv`; supporting: SEC-20; [card](analyst-reports/iteration-1_financial-analyst.md#fin-27-customer-concentration-is-low-and-stable) | Verified |
| FIN-28 | FreshArc Distributors (rank 10 in FY2025, $31.8m, 2.3% of revenue) was the only listed top-10 customer whose revenue fell ($34.1m to $31.8m, -6.7%); it filed Chapter 11 on Jan 12, 2026 and ceased operations in March 2026, so its revenue will not recur; part of it sits in the LTM base (inference) | Financial analysis | Medium | High | `revenue_by_customer.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-28-fresharc-distributors-is-the-only-top-10-customer-whose-revenue-fell) | Partially verified |
| FIN-29 | Alder BioPharma Distribution grew 18.3% | Financial analysis | Low | High | `revenue_by_customer.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-29-alder-biopharma-distribution-grew-183) | Open |
| FIN-30 | Active customers fell in H1 2026, and there is no retention data | Financial analysis | Low | High | `kpis.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-30-active-customers-fell-in-h1-2026-and-there-is-no-retention-data) | Verified |
| FIN-31 | Cash conversion has held steady | Financial analysis | Low | High | `cash_flow.csv`, `adjusted_ebitda_reconciliation.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-31-cash-conversion-has-held-steady) | Verified |
| FIN-32 | Free cash flow is thin once all capex and finance leases are paid | Financial analysis | Medium | High | `cash_flow.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-32-free-cash-flow-is-thin-once-all-capex-and-finance-leases-are-paid) | Verified |
| FIN-33 | A working capital inflow held H1 2026 operating cash flow flat | Financial analysis | Low | Medium | `cash_flow.csv`, `balance_sheet.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-33-a-working-capital-inflow-held-h1-2026-operating-cash-flow-flat) | Open |
| FIN-34 | DSO is stable at about 48 days | Financial analysis | Low | High | `balance_sheet.csv`, `income_statement.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-34-dso-is-stable-at-about-48-days) | Verified |
| FIN-35 | The equity award cash-out recomputes to $46.2m | Financial analysis | Medium | High | `deal-brief.md`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-35-the-equity-award-cash-out-recomputes-to-462m) | Verified |
| FIN-36 | Enterprise value and sources and uses arithmetic tie | Financial analysis | Low | High | `balance_sheet.csv`, `deal-brief.md`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-36-enterprise-value-and-sources-and-uses-arithmetic-tie) | Verified |
| FIN-37 | Sources and uses omit some closing items | Financial analysis | Medium | Medium | `cash_flow.csv`, `deal-brief.md`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-37-sources-and-uses-omit-some-closing-items) | Verified |
| FIN-38 | Termination fee arithmetic ties | Financial analysis | Low | High | `deal-brief.md`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-38-termination-fee-arithmetic-ties) | Verified |
| FIN-39 | Goodwill and intangibles total $349.0m; the impairment test date is not in my files | Financial analysis | Low | Medium | `balance_sheet.csv`, `deal-brief.md`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-39-goodwill-and-intangibles-total-3490m-the-impairment-test-date-is-not-in-my-files) | Verified |
| FIN-40 | Headcount is down 1.1% | Financial analysis | Low | High | `kpis.csv`; [card](analyst-reports/iteration-1_financial-analyst.md#fin-40-headcount-is-down-11) | Open |

## Finding cards

Full cards for analyst findings are in `memory/analyst-reports/` (linked from each row). Cards for `X-` findings are below.

<a id="x-01"></a>
### X-01: Normalized LTM earnings base is $217.5m to $222.5m, not $250.0m (projection)

- **Finding:** The deal prices Brindlewick at 11.0x LTM Adjusted EBITDA of $250.0m. Three items in that base will not recur at the same level:
  - It includes a $3.7m benefit from cutting the insurance accrual rate (X-04).
  - It is net of $4.6m of ColdTrack service credits that may be one-off (SEC-06).
  - It prices about 70% of power at $61/MWh under contracts that end December 31, 2026, before closing (X-03).
- **Bridge (projection):**

  | Line | $m |
  |---|---|
  | LTM Adjusted EBITDA, deal base | 250.0 |
  | Less: insurance accrual benefit in the LTM (X-04) | (3.7) |
  | Add: ColdTrack service credits, if one-off (SEC-06) | 4.6 |
  | Less: power repricing of 412.3 GWh from $61 to $104/MWh (X-03) | (17.7) |
  | Normalized LTM before buyer costs and probable losses | 233.2 |
  | Less: California property tax reassessment on the change of control (SEC-16) | (4.7) |
  | Less: FreshArc preference loss, called likely by Brindlewick's counsel, not accrued (X-13), $6.0m to $11.0m | (6.0) to (11.0) |
  | **Normalized LTM (project rule)** | **222.5 to 217.5** |
  | Value at 11.0x | 2,447.5 to 2,392.5 |
  | Shortfall against EV of $2,750.0m | 302.5 to 357.5 (11.0% to 13.0% of EV) |
  | Implied value per share ((value - 1,118.0) / 48.0) | $27.70 to $26.55 |

- **Basis (stated, as the verifier asked):** the project rule for normalizing the earnings the deal is priced on deducts costs a source calls probable but the company has not recorded. I apply it here, so the FreshArc loss is deducted from the base and the 11.0x multiple is applied to the result.
  - **Without property tax:** the base is $227.2m to $222.2m, a shortfall of $250.8m to $305.8m (9.1% to 11.1%).
  - **FreshArc as a one-off deducted once:** the shortfall is $242.5m to $247.5m with property tax (8.8% to 9.0%), or $190.8m to $195.8m without it (6.9% to 7.1%).
  - **Before property tax and FreshArc:** the base is $233.2m, worth $2,565.2m, a shortfall of $184.8m (6.7%), or $30.15 per share.

- **Not in this bridge (separate parents):**
  - **Run-rate fall (X-02).** On H1 2026 run-rate, before property tax and FreshArc, forward earnings are (118.0 - 3.7 + 4.6) x 2 - 17.7 = $220.1m. That is worth $2,421.1m at 11.0x, which is $328.9m (12.0% of EV) below the deal EV, or $27.15 per share (projection).
  - **Sandhaven (X-05).** Removing its $31.0m from the normalized LTM gives $202.2m (projection).
- **Not quantified:** FreshArc's lost contribution (FY2025 revenue $31.8m; operations ceased March 2026; its EBITDA is not in the sources) and most-favored-customer repricing (X-12).
- **Growth link:** Calder Valley and Bayfront, which drove FY2025 growth (SEC-08), carry $61.5m of the unrecorded restoration (Calder Valley $44.0m, Bayfront $17.5m; X-09). Their share of FY2025 revenue growth ($56.0m) and operating income growth ($15.5m) is not in the sources. The deal multiple is applied to earnings that include them (inference).
- **Severity:** Critical. Test met: more than 10% of value. On the project rule, the shortfall is $302.5m to $357.5m (11.0% to 13.0% of EV) (projection). This is set by X-01's own combined evidence. Its components (X-03, X-04, X-13, SEC-16, SEC-06) keep their own severities, and the value effects are not additive across rows.
- **Confidence:** Medium. The inputs are source figures. The power price, whether the credits recur and the size of the FreshArc loss are assumptions.
- **Verification:** Partially verified (batch D). Corrections applied: FreshArc shown at both ends of counsel's range, basis stated, growth link corrected.
- **Sources:** `adjusted_ebitda_reconciliation.csv`; `income_statement.csv`; `BWCC_10-Q_Q2-2026_excerpts.md` (Note 5, Warehousing, Energy); `BWCC_10-K_FY2025_excerpts.md` (Energy, Item 1A, Item 2); `2026-09-30_grid-and-power-report_northwest-power-forwards.md`; `LIT-04_freshArc-preference.md`; `deal-brief.md` section 2.

<a id="x-02"></a>
### X-02: Revenue, occupancy, price, throughput and margins weakened; annualized fall is $462.0m at 11.0x (projection)

- **Finding:** These measures weakened together through H1 2026:
  - **Revenue growth:** year-over-year growth went from +6.8% (Q1 2025) to -2.3% (Q2 2026). H1 2026 revenue fell 1.9% (Warehousing -3.6%, Transportation -5.0%).
  - **Occupancy:** 86.1% to 81.4% (H1 2025 to H1 2026).
  - **Revenue per occupied pallet:** $815 (FY2025) to $784 (-3.8%).
  - **Throughput:** -5.2% annualized.
  - **Transportation operating ratio:** 93.8% to 96.4%.
  - **Active customers:** 1,310 to 1,295.
  - **H1 Adjusted EBITDA:** $139.0m to $118.0m (-15.1%).
  - **FY2026 guidance:** cut on August 6, 2026 from $268m to $276m to $236m to $244m. The midpoint fell $32.0m (11.8%).
  - **Outlook:** the CFO said "We don't see the second half looking very different from the first."
- **Counterpoint:** value-added services grew 13.2% (SEC-45).
- **Test (projection):** annualized fall 21.0 x 2 = $42.0m. At 11.0x that is $462.0m, 16.8% of EV, above the $275.0m threshold.
- **Second showing (verifier, batch C):** on the company's own FY2026 guidance of $236m to $244m, the fall against FY2025 is $27.0m to $35.0m, or $297.0m to $385.0m at 11.0x (10.8% to 14.0% of EV) (projection).
- **Not a price cut:** the $462.0m is the Critical test number. The gap to the $250.0m deal base is $154.0m to $231.0m (projection).
- **Context (projection):** half of the fall is already in the LTM. The H1 2026 run-rate of $236.0m (the low end of guidance) is $14.0m below the deal base, which is $154.0m (5.6% of EV). The guidance midpoint of $240.0m is $10.0m below the base ($110.0m, 4.0%).
- **Separate parents this trend draws on, each with its own severity:**
  - X-04: the insurance accrual cut flatters H1 2026.
  - SEC-06: service credits depress H1 2026.
  - X-12: most-favored-customer repricing.
  - X-03: power cost from 2027.
- **Organic growth:** FY2025 growth also includes the Bayfront acquisition, so organic performance is weaker than reported (FIN-11, inference).
- **Like-for-like note (verifier):** on an H1 basis the 10-Q gives revenue per pallet -4.3% ($819 to $784) and throughput -5.7%, so the FY2025-based figures above understate the fall.
- **Severity:** Critical. Test met: changes value by more than 10% ($462.0m, projection).
- **Confidence:** Medium. The reported figures have High confidence. The annualization is a projection.
- **Verification:** Verified (batch D).
- **Sources:** `revenue_quarterly.csv`; `income_statement.csv`; `kpis.csv`; `BWCC_10-Q_Q2-2026_excerpts.md` (Overview, Key operating metrics); `2026-08-07_capital-markets-wire_q2-results-guidance-cut.md`; `2026-02-26_capital-markets-wire_brindlewick-q4-results.md`.

<a id="x-03"></a>
### X-03: Power repricing from January 1, 2027 (projection)

- **Finding:** In 2025 Brindlewick consumed 589 GWh. About 70% (412.3 GWh) came under fixed-price agreements signed in 2021 at about $61/MWh, which expire December 31, 2026.
  - **10-K:** 2027 supply was not yet contracted.
  - **10-Q:** procurement has begun, and 2027 forward prices are "substantially above" the current price.
  - **Market data (September 30, 2026):** calendar-2027 forwards were about $97/MWh (Mid-C) and $111/MWh (NorCal). Fixed-price offers for 2027 to 2029 averaged about $104/MWh in Washington and California. An adviser said "Anyone rolling off a contract signed in 2021 is looking at a step-up of 60% or more."
- **Arithmetic (projection):**
  - At $104: 412.3 x ($104 - $61) = $17.7m a year, which is $195.0m at 11.0x (7.1% of EV).
  - Range: $14.8m (at $97) to $20.6m (at $111), or $163.3m to $226.8m (5.9% to 8.2% of EV).
  - The 30% bought at tariff or index rates is not included.
  - The $97 and $111 figures are wholesale baseload forwards. The $104 offers include transmission and shaping, so the low end understates delivered cost.
- **Pass-through:** No source shows that customer contracts pass power costs through to customers.
- **Severity:** High. The cost rises before closing and is not in the LTM. At $104 it exceeds 5% of EV but not 10%.
- **Confidence:** Medium. The contract facts have High confidence. Brindlewick's 2027 price is not in the sources, and the market article does not name Brindlewick.
- **Verification:** Verified (batch D).
- **Sources:** `BWCC_10-K_FY2025_excerpts.md` (Energy, Item 1A, Note 12); `BWCC_10-Q_Q2-2026_excerpts.md` (Energy); `2026-09-30_grid-and-power-report_northwest-power-forwards.md` paras 1 to 3; `kpis.csv` rows 18 to 20.

<a id="x-04"></a>
### X-04: Insurance accrual rate cut is a dated judgment that later data put in doubt

- **Finding:** From January 1, 2026, Brindlewick cut its current-year auto liability and cargo accrual rate from 6.5% to 4.8% of Transportation revenue. It cited its camera program. The cut reduced H1 2026 expense by about $3.7m (10-Q Note 5).
- **What happened after the rate was set:**
  - Recordable accidents per million miles were 0.84 in H1 2026, against 0.72 in FY2025 (+16.7%) and 0.71 in H1 2025 (+18.3%) (FIN-14).
  - The I-5 suit was filed April 17, 2026, and a $150.0m demand was served April 20, 2026 (X-14).
  - The complaint alleges the driver-facing camera flagged the driver 11 times in two weeks with no action (LIT-10, allegation).
  - Accrued claims reserves fell from $46.5m to $44.1m.
  - On the August 6 call an analyst said "Accident frequency is going up and the accrual rate is going down."
- **Context:** Self-insurance reserves are a critical audit matter. Adjusted EBITDA is a bonus and PSU metric (SEC-44), so the cut also raises a pay metric (inference).
- **Value (projection):**

  | Measure | $m | Value at 11.0x | % of EV |
  |---|---|---|---|
  | LTM benefit | 3.7 | 40.7 | 1.5% |
  | Annualized | 7.3 | 80.3 | 2.9% |
  | At an accident-scaled rate of 7.58% | 12.0 | 131.5 | 4.8% |

- **Restatement risk (inference):** H1 2026 earnings and the June 30, 2026 reserve are at risk of later correction.
- **Severity:** High. It needs a specific protection: an actuarial review before signing and a reserve true-up in price.
- **Confidence:** Medium. The figures are stated; the adequacy of the new rate is an inference.
- **Verification:** Partially verified (batch D). Corrections applied: critical audit matter wording, bonus metric wording, demand date, confidence line.
- **Sources:** `BWCC_10-Q_Q2-2026_excerpts.md` (Note 5, Key operating metrics); `kpis.csv` rows 11 to 13; `balance_sheet.csv` row 14; `2026-08-07_capital-markets-wire_q2-results-guidance-cut.md` para 5; `LIT-02_okafor-wrongful-death.md`.

<a id="x-05"></a>
### X-05: Sandhaven earnings end September 30, 2028

- **Finding:** Sandhaven 1 and 2 hold 118k pallets and earned about $31.0m (12.4%) of LTM Adjusted EBITDA (10-Q). They sit on a Harbor District concession that expires September 30, 2028, with no renewal option. The improvements revert to the District (10-K).
  - **District vote:** on March 17, 2026 the District designated the site for container yard and rail use from 2029, "subject to environmental review and funding" (8-K, March 20, 2026). The vote was 4 to 1.
  - **No extension:** the District's executive director said "there will be no extension past 2028." She said the District would demolish the warehouses as part of the terminal construction.
  - **Replacement:** a District staff report estimates a similar facility at $180m to $220m, with about three years to permit and build.
  - **10-Q:** discussions "about an extension or an alternative site continue. We have not reached agreement, and there can be no assurance that we will."
  - **Deal brief:** neither the deal model nor the integration plan mentions Sandhaven.
- **Test:** more than 10% of value. 31.0 x 11.0 = $341.0m, which is 12.4% of EV.
  - Crediting the income left after a Q2 to Q3 2027 closing ($31.0m to $46.5m) still leaves $294.5m to $310.0m (10.7% to 11.3%) (projection).
  - The alternative is replacement capex of $180m to $220m (6.5% to 8.0% of EV). A build of about three years that starts after closing would finish after September 30, 2028, leaving a gap (inference).
- **Antitrust link:** Sandhaven is 118k of Brindlewick's 304k Puget Sound pallets (38.8%) (X-07).
- **Severity:** Critical. Test met: more than 10% of value.
- **Confidence:** High.
- **Verification:** Partially verified (batch D). Corrections applied: demolition attributed, register wording, environmental review condition.
- **Sources:** `BWCC_10-Q_Q2-2026_excerpts.md` (Sandhaven); `BWCC_8-K_2026-03-20_harbor-district-update.md`; `BWCC_10-K_FY2025_excerpts.md` (Item 1A, Item 2); `2026-03-18_sandhaven-harbor-ledger_terminal-7-plan-vote.md` paras 1 to 7; `deal-brief.md` sections 2 and 5.

<a id="x-06"></a>
### X-06: Sandhaven disclosure gap

- **Finding:** The FY2025 10-K, filed February 26, 2026, said: "We are in discussions with the Harbor District about an extension and expect to negotiate one." On the same day the CEO said Brindlewick expected to reach an extension. Nineteen days later the District's executive director said: "We have been clear with Brindlewick for more than a year: Terminal 7 is our growth project, and there will be no extension past 2028."
  - Later filings dropped the expectation. The 8-K says Brindlewick "cannot predict the outcome." The 10-Q says "no assurance."
  - For balance, the same 10-K risk factor said "the District is evaluating long-term plans for the Terminal 7 uplands."
- **Why this is not timing alone:** a named, on-record source (the District) says Brindlewick had been told. On the District's account, the 10-K's expectation conflicted with what management had been told (inference).
- **Deal impact:** disclosure and securities claim risk, and management credibility (inference). The value exposure is in X-05.
- **Severity:** Medium.
- **Confidence:** Medium. This is one party's account, and the District's correspondence is not in the data room.
- **Verification:** Verified (batch D).
- **Sources:** `BWCC_10-K_FY2025_excerpts.md` Item 1A; `2026-02-26_capital-markets-wire_brindlewick-q4-results.md` para 5; `2026-03-18_sandhaven-harbor-ledger_terminal-7-plan-vote.md` para 3; `BWCC_8-K_2026-03-20_harbor-district-update.md`; `BWCC_10-Q_Q2-2026_excerpts.md` (Sandhaven).

<a id="x-07"></a>
### X-07: Merger antitrust review could block closing within the proposed terms

- **Finding:** The two companies overlap in two markets.

  | Market | Brindlewick (10-K) | Trelliswood (investor day) | Combined | Change in HHI |
  |---|---|---|---|---|
  | Puget Sound | about 19% | about 24% | about 43% | 912 |
  | Northern Central Valley | about 18% | about 21% | about 39% | 756 |

  - The 10-K names Trelliswood as a principal competitor in both markets.
  - **What the buyer said in public (June 15, 2026):** "Where we buy, we consolidate. We move the customers into our automated buildings and hand back the older leased boxes." Acquired leased warehouses in overlapping markets would "typically be exited within 24 months of closing."
  - **The deal brief's plan does this:** it surrenders four Brindlewick leased sites in exactly these markets within 24 months. Puyallup Junction (78k) and Kent Valley (38k) are in Puget Sound; Stockton North (72k) and Lodi (46k) are in the Northern Central Valley. Together that is 234k pallets, 20.4% of Brindlewick's capacity.
- **The divestiture cap is small against the overlap:**
  - The cap covers facilities with up to $15.0m of LTM Adjusted EBITDA (6.0% of $250.0m).
  - Brindlewick's capacity in the two markets is 480k of 1,148k pallets (41.8%).
  - At the company average of $217.8 of LTM Adjusted EBITDA per pallet position, the cap equals about 69k pallets (inference).
  - Sandhaven alone earns $31.0m (2.1x the cap).
  - If a reviewer requires more, Trelliswood has no obligation to divest more. The deal could then fail; if it fails for antitrust reasons, Trelliswood owes the $110.0m reverse termination fee (deal brief).
- **Related facts:**
  - The pending class action (X-08) alleges that operators exchanged rates "by market" through Coldmetric. Trelliswood cites Coldmetric data for its own shares.
  - Whether Trelliswood subscribed to Coldmetric or is one of the six unnamed operator defendants is not found in the sources.
- **Possible arguments the other way (inference):**
  - About 140,000 new speculative positions in Stockton and Patterson since 2024 (NEWS-02).
  - The buyer's CFO argued customers can build their own.
  - Sandhaven's exit in 2028 would cut Brindlewick's Puget Sound capacity by 38.8% (X-05).
- **Not in the sources:** no reviewer's position, no market definition by an agency, no facility-level EBITDA, and no review timeline against the 12-month (plus 3) outside date.
- **Severity:** Critical. Test met: could block closing. The facts are the combined shares of about 43% and 39%, the buyer's stated plan to remove acquired capacity in the overlap markets, and a cap that covers about 6% of Brindlewick's EBITDA against 41.8% of its capacity in those markets.
- **Confidence:** Medium. The shares are company estimates from different data sets, so 43% and 39% are approximate. The effect on the review is an inference for antitrust counsel.
- **Verification:** Partially verified (batch D). Corrections applied: predictive wording softened, shares marked approximate.
- **Sources:** `BWCC_10-K_FY2025_excerpts.md` (Markets and competition, Item 2); `2026-06-16_supply-chain-insider_trelliswood-investor-day.md` paras 1 to 5; `LIT-01_refrigerated-warehousing-antitrust.md`; `deal-brief.md` sections 4 and 5.

<a id="x-08"></a>
### X-08: Antitrust class action: Critical under the remedy-sought rule, and disclosure lags events

- **Finding:** In *In re Refrigerated Warehousing Services Antitrust Litigation* (N.D. Cal., filed June 12, 2025), direct purchasers seek treble damages and an injunction from Brindlewick, six other operators and Coldmetric.
  - **Damages claimed:** plaintiffs' economist puts class-wide overcharges at "at least $600 million before trebling." The complaint attributes about 8% of class purchases to Brindlewick.
  - **Joint and several liability:** the case file says defendants are jointly and severally liable for the full trebled amount, with no right of contribution.
  - **Ruling:** the motion to dismiss was denied on August 14, 2026.
  - **Co-defendant settlement:** Northern Frost, with about a 2% share, settled in July 2026 for $9.5m plus cooperation, subject to court approval.
  - **Counsel's view:** Brindlewick's counsel now calls the theory "viable." It has given no loss estimate, and nothing is accrued.
- **Disclosure:**
  - **10-K (February 26, 2026):** "We believe the claims are without merit."
  - **10-Q (filed August 6, 2026):** drops that sentence. It says the motion "remains under submission" and does not mention the July 2026 Northern Frost settlement, which came before the filing.
  - **After the 10-Q:** the denial came eight days later. No later filing in the data room mentions it. The September 22, 2026 8-K covers only the review and the severance plan.
  - **Deal brief:** does not mention the case.
- **Test:** more than 10% of value, under the remedy-sought rule. Class-wide single damages of $600.0m x 3 = $1,800.0m, which is 65.5% of EV. This is an upper bound. Untrebled, it is $600.0m (21.8%).
  - Narrower reference points: Brindlewick's own 8% share is $48.0m single and $144.0m trebled (5.2%). Scaling the Northern Frost settlement to an 8% share gives about $38.0m (projection).
  - No source shows the remedy is unlikely.
- **Next date:** the class certification motion is due February 26, 2027, between signing and closing.
- **Severity:** Critical. Test met: more than 10% of value (upper bound).
- **Confidence:** Medium. The damages figures are plaintiffs' allegations.
- **Verification:** Verified (batch D).
- **Sources:** `LIT-01_refrigerated-warehousing-antitrust.md`; `docket_index.csv` row LIT-01; `2026-08-19_courtroom-wire_cold-storage-antitrust-ruling.md`; `BWCC_10-K_FY2025_excerpts.md` Item 3; `BWCC_10-Q_Q2-2026_excerpts.md` Note 11; `BWCC_8-K_2026-09-22_strategic-review.md`.

<a id="x-09"></a>
### X-09: Unrecorded lease-end restoration; the integration plan triggers $118.0m of it

- **Finding:** Eleven leases require Brindlewick to remove or restore its improvements at lease end.
  - Holbrook (October 2025) puts the cost at $312.0m, undiscounted and at 2025 prices.
  - None of it is recorded. The 10-K says settlement dates are "indeterminate" and that "A restoration obligation is recognized when we decide to exit a facility."
- **The buyer's plan triggers part of it:** surrendering the four leases triggers $118.0m.

  | Lease | Restoration estimate | Current term ends |
  |---|---|---|
  | Puyallup Junction | $41.5m | 2031 |
  | Kent Valley | $14.0m | 2029 |
  | Stockton North | $38.0m | 2033 |
  | Lodi | $24.5m | 2030 |
  | **Total** | **$118.0m** | |

  - The $118.0m is not in the deal brief's $45.0m of one-time integration costs, which list product moves, racking, IT migration and severance. It is 2.6 times that budget, and 5.6 years of the $21.0m a year of network synergies.
  - Three of the leases would be surrendered before their current terms end. Remaining rent and termination rights are not found in the sources.
  - The July 2026 Harvest Peak contract runs seven years at Stockton North, Modesto East and Lodi (NEWS-09).
- **Test (full-amount rule):** $312.0m is 11.3% of EV and 48.6% of reported equity of $641.9m. The near-term cash cost from the buyer's plan is $118.0m (4.3% of EV, 18.4% of equity). A recorded liability would be at present value, below the undiscounted $312.0m (inference).
- **Restatement risk (inference):** the FY2025 balance sheet, its FY2024 comparative and the June 30, 2026 interim balance sheet.
- **Severity:** Critical. Test met: more than 10% of value, on the full amount.
- **Confidence:** High on the amounts. Medium on the accounting.
- **Verification:** Verified (batch D).
- **Sources:** `BWCC_10-K_FY2025_excerpts.md` (Item 2 table, Critical accounting estimates, Note 12); `balance_sheet.csv` row 25; `deal-brief.md` section 5.

<a id="x-10"></a>
### X-10: Effective-controls conclusions against three practices

- **Finding:** Management concluded that internal control over financial reporting was effective at December 31, 2025. The auditor, which has audited the company since 2009, gave unqualified opinions. Disclosure controls were found effective at June 30, 2026 (SEC-36).
- **Three practices in those same periods are called into question:**
  - **Restoration obligations (X-09, SEC-14):** $312.0m is unrecorded on the ground that settlement dates are "indeterminate." Yet each lease has a stated expiry, and a facility-by-facility estimate existed from October 2025.
  - **Insurance accrual (X-04):** the rate was cut to 4.8% while accidents rose. Self-insurance reserves are a critical audit matter.
  - **FreshArc (X-13):** a preference loss that counsel calls likely, $6.0m to $11.0m, is not accrued.
- **Restatement risk (inference), by practice and period:**
  - **Restoration:** lease-related liabilities and equity for FY2025 (with its FY2024 comparative) and at June 30, 2026.
  - **Insurance accrual cut:** claims reserves and insurance expense for H1 2026 only. The FY2025 rate was 6.5%.
  - **FreshArc:** loss contingencies in the H1 2026 interim statements. The FY2025 10-K excerpts do not mention the January 12, 2026 petition (SEC-35).
- **Oversight gap:** the CFO and the Chief Accounting Officer are among the nine officers expected to leave within three months of closing (SEC-42).
- **Severity:** High. It needs accounting diligence before signing, and a response in price or structure.
- **Confidence:** Medium (inference about the accounting).
- **Verification:** Partially verified (batch D). Corrections applied: periods mapped to each practice, critical audit matter wording.
- **Sources:** `BWCC_10-K_FY2025_excerpts.md` (Item 9A, Critical accounting estimates, Note 12); `BWCC_10-Q_Q2-2026_excerpts.md` (Item 4, Notes 5 and 11); `LIT-04_freshArc-preference.md`; `BWCC_DEF14A_2026_excerpts.md`.

<a id="x-11"></a>
### X-11: Known deal costs total $172.6m (6.3% of EV) under the rule; $62.6m if the deal closes

- **Finding:**
  - **Equity award cash-out: $46.2m.**
    - RSUs: 860,000 x $34.00 = $29.24m.
    - PSUs at target, as the 2020 Omnibus Plan provides: 210,000 x $34.00 = $7.14m.
    - Options: 1,180,000 x ($34.00 - $25.68) = $9.82m.
  - **Change-in-control severance for the nine executive officers: about $16.4m** (8-K).
    - The plan was adopted September 21, 2026, the day before the strategic review was announced.
    - It raised the CEO's multiple from 1.5x to 2.5x and the other named officers' from 1.0x to 2.0x.
    - The deal brief expects all nine officers to leave within three months of closing.
  - **Reverse termination fee: $110.0m**, payable by Trelliswood if the merger fails on antitrust grounds.
- **Totals:** the three categories add to $172.6m (6.3% of EV), above the 5% line.
  - The reverse fee cannot be paid together with the closing costs. If the deal closes, the cost is $62.6m (2.3%). If it fails on antitrust grounds, the cost is $110.0m plus fees already spent.
  - Given X-07, the reverse fee is a live exposure.
  - Advisory, financing and other fees of $72.0m (2.6%) are a use of funds, not part of the test.
- **How to present it:** fully diluted EV (awards included) is $2,796.2m, or 11.18x LTM. The all-in cost including severance is $2,812.6m, or 11.25x, not 11.0x. All value tests stay on the $2,750.0m base. Severance is paid after closing as officers leave (SEC-38).
  - The sources and uses omit the severance; that gap is a separate finding (SEC-38).
  - Other cash costs the deal itself triggers: the $118.0m restoration (X-09), the $45.0m integration budget, and $4.7m a year of property tax (SEC-16).
- **Interim covenants needed:**
  - The option figure is a floor if any tranche is out of the money.
  - 2,410,000 shares remained available for new grants at December 31, 2025.
- **Severity:** High. Test: known deal costs above 5% of value ($172.6m).
- **Confidence:** High.
- **Verification:** Verified (batch D).
- **Sources:** `deal-brief.md` sections 3 and 4; `BWCC_8-K_2026-09-22_strategic-review.md` Item 5.02; `BWCC_DEF14A_2026_excerpts.md` (CD&A, Equity compensation plan information); `BWCC_10-Q_Q2-2026_excerpts.md` Note 8.

<a id="x-12"></a>
### X-12: Harvest Peak pricing and most-favored-customer repricing (projection)

- **Finding:** Two sources describe the same contract.
  - **10-Q:** Brindlewick signed a seven-year agreement "with a new customer for frozen storage at our Central Valley facilities" in July 2026. "Two existing customers have since requested pricing reviews under the most-favored-customer provisions."
  - **News (July 8, 2026):** names the customer as Harvest Peak Foods. The agreement covers about 30,000 positions at Stockton North, Modesto East and Lodi, priced about 9% below the Central Valley rate card, according to two people familiar with the bidding. The SVP of Sales did not dispute the figure.
  - **10-K:** agreements carrying most-favored-customer clauses were about 22% of 2025 warehousing revenue, or $169.0m. The clauses require "any lower storage rate ... for comparable services and volumes in the same market." The share was 23% in H1 2026 (FIN-16).
  - **Management's position:** the new agreement is not comparable.
  - Harvest Peak is not a listed top-10 customer.
- **Upper bound (projection):** 9% x $169.0m = $15.2m a year, which is $167.3m at 11.0x (6.1% of EV). The clauses apply only to the same market, and the Central Valley share of the base is not in the sources. The clauses cover storage rates, while the $169.0m includes handling revenue, a further reason this is an upper bound.
- **Severity:** High. The upper bound is above 5% of EV. It needs a specific protection: an interim covenant requiring Trelliswood's consent for pricing concessions and most-favored-customer settlements before closing, plus a price adjustment for the claims already made.
- **Confidence:** Medium.
- **Verification:** Verified (batch D).
- **Sources:** `BWCC_10-Q_Q2-2026_excerpts.md` (Pricing, Warehousing); `BWCC_10-K_FY2025_excerpts.md` (Customers and contracts, Item 1A); `2026-07-08_supply-chain-insider_harvest-peak-contract.md` paras 1 to 5; `kpis.csv` row 21; `revenue_by_customer.csv`.

<a id="x-13"></a>
### X-13: FreshArc: lost customer and an unaccrued probable loss

- **Finding:** FreshArc Distributors was Brindlewick's 10th-largest customer in FY2025, with $31.8m of revenue (2.3% of revenue). Its FY2024 revenue was $34.1m (2.5%).
  - **January 12, 2026:** it filed for Chapter 11, before the 10-K was filed on February 26, 2026. The 10-K excerpts do not mention it (SEC-35).
  - **March 2026:** it ceased operations.
  - **July 2026:** its liquidating trustee demanded $14.6m of preference payments. The 10-Q (August 6) cites ordinary-course and new-value defenses and accrues nothing.
  - **September 8, 2026:** the adversary proceeding was filed.
  - **Counsel's estimate:** Brindlewick's counsel estimates "a likely recovery by the trustee of $6 million to $11 million if the case is not settled". Nothing is accrued.
  - **Ordinary-course defense (trustee's argument):** payment timing moved to 58 to 71 days, from 32 to 40 days, after an October 2025 credit hold.
  - **Unpaid services:** about $3.9m of services were not paid for.
- **Unrecorded liability (inference):** "likely" plus a range suggests a probable, estimable loss. The H1 2026 interim statements (10-Q filed after the July demand), and Q3 2026 if still unaccrued, may be missing a liability of at least $6.0m and carry a restatement risk. The date of counsel's estimate is not found. The FY2025 10-K excerpts do not mention the petition (SEC-35).
- **Size:** $6.0m to $11.0m is 0.2% to 0.4% of EV and 0.9% to 1.7% of equity. The full $14.6m claim is 0.5% of EV. The LTM includes part of FreshArc's revenue, but its EBITDA contribution is not in the sources.
- **Severity:** Medium. The amount is stated and below 10% of value.
- **Confidence:** High on the facts. Medium on the accounting conclusion.
- **Verification:** Partially verified (batch D). Corrections applied: FY2024 rank removed, trustee's argument labeled, settlement condition, periods named.
- **Sources:** `LIT-04_freshArc-preference.md`; `BWCC_10-Q_Q2-2026_excerpts.md` Note 11; `revenue_by_customer.csv` row 11; `balance_sheet.csv` row 25.

<a id="x-14"></a>
### X-14: I-5 fatal crash: uninsured exposure and disclosure gaps

- **Finding:** A Brindlewick Transport tractor-trailer was in a February 3, 2025 crash on I-5 that killed three people.
  - **The suit:** the families sued on April 17, 2026. On April 20, 2026 they served a $150.0m statutory offer to compromise, which was not accepted. That is 5.5% of EV.
  - **Insurance:** Brindlewick retains $5.0m and carries $50.0m of excess cover, $55.0m combined. The 10-K says "A claim above our $55.0 million combined retention and excess coverage would be paid from our own resources."
  - **Reserve:** Brindlewick has reserved only the $5.0m retention. The excess insurers' response is not found in the sources.
  - **Defense counsel's view:** liability "will be difficult to contest if the log edit is admitted." Counsel puts comparable verdicts at about $40m to $180m.
- **Uninsured exposure (projection):** at the demand, $95.0m (3.5% of EV). At the top of counsel's range, $125.0m (4.5%).
- **Disclosure:**
  - **10-K (February 26, 2026):** described "a February 3, 2025 multi-vehicle accident" without mentioning the three deaths.
  - **10-Q (August 6, 2026):** discloses the suit but not the $150.0m demand. The demand was served more than three months earlier and exceeds the cover.
- **Allegations (LIT-10):** hours over the limit, 11 camera alerts and a log edit the day after the crash.
- **Trial:** set for September 13, 2027, which may fall after a Q2 to Q3 2027 closing.
- **Severity:** High. It is below the 10% test even at $180m, and it needs specific protection: confirmation of the insurance tower, a price adjustment for the uninsured amount, and consent rights over settlement.
- **Confidence:** Medium. The liability facts are allegations.
- **Verification:** Verified (batch D).
- **Sources:** `LIT-02_okafor-wrongful-death.md`; `BWCC_10-K_FY2025_excerpts.md` (Insurance, Item 1A, Note 12); `BWCC_10-Q_Q2-2026_excerpts.md` Note 11; `2026-04-22_freight-safety-monitor_i5-crash-lawsuit.md`.

<a id="x-15"></a>
### X-15: ColdTrack impairment judgment at June 30, 2026

- **Finding:** At June 30, 2026, capitalized software was $47.0m, mainly ColdTrack, and management "concluded that no impairment was required" (10-Q).
- **What was known by then, and what came later:**
  - Before the test date: deployments were paused with no new timetable (the COO said so on June 2, 2026).
  - Reported in the August 6 10-Q, with no earlier date given: the cost estimate rose from $38.0m to $61.0m (+60.5%).
  - Service credits of $4.6m had been issued, and two customers had moved part of their volume (10-Q).
  - The system was live at 3 of 19 sites.
- **What happened afterwards:** the share price fell 12.0% to $24.20 after the August 6, 2026 guidance cut (reported August 7), down 11.1% from $27.22 on February 26.
- **The buyer's plan:** the deal brief halts the rollout, so the asset would have little use to Trelliswood (inference, non-cash).
- **Size:** $47.0m is 1.7% of EV and 7.3% of equity.
- **Why the judgment is in doubt (inference):** the pause came before the test date, and the overrun was reported with the same 10-Q. Restatement risk for the June 30, 2026 balance sheet and H1 2026 (inference).
- **Severity:** Medium.
- **Confidence:** Medium.
- **Verification:** Partially verified (batch D). Corrections applied: overrun date, share-fall date, restatement flag.
- **Sources:** `BWCC_10-Q_Q2-2026_excerpts.md` (ColdTrack, Warehousing); `2026-06-02_supply-chain-insider_coldtrack-rollout-glitches.md`; `2026-08-07_capital-markets-wire_q2-results-guidance-cut.md`; `balance_sheet.csv`; `kpis.csv` row 22; `deal-brief.md` section 5.

<a id="x-16"></a>
### X-16: Deferred maintenance and the Sandhaven 2 compressor failure

- **Finding:** Maintenance capex fell from 4.1% of revenue in 2023 to 3.3% in 2024, 2.5% in 2025 and 2.3% in H1 2026. The 10-K says the company deferred certain non-critical projects pending an engineering assessment.
  - **Holbrook (October 2025):** found about $96.0m of priority 1 and 2 replacements for 2027 to 2029. They are mainly compressors, condensers and controls at the seven facilities with ammonia systems more than 25 years old.
  - **Sandhaven 2 (February 2026):** a compressor and its standby unit both failed during a power disturbance. The room warmed from -10°F to about 28°F over 19 hours. Coastline's surveyor declared the 2.48m pounds of product in the room unfit for sale. The resulting claim is $41.2m (LIT-05).
  - The failure is consistent with the deferral pattern (inference). Against that, the standby unit was serviced in December 2025, and the failure came during a power disturbance. Whether Sandhaven 2 is one of the seven facilities is not stated.
- **Size:**
  - $96.0m is 3.5% of EV. The work runs 2027 to 2029, so most of it falls after a Q2 to Q3 2027 closing.
  - The shortfall against the 2023 maintenance rate was about $45.5m from FY2024 to H1 2026 (inference).
- **Severity:** Medium. It needs engineering diligence and a capex plan, and the catch-up spend belongs in price.
- **Confidence:** High on the figures.
- **Verification:** Partially verified (batch D). Corrections applied: timing of spend, power disturbance and service record, attribution of product loss.
- **Sources:** `BWCC_10-K_FY2025_excerpts.md` (Capital expenditures, Item 1A); `cash_flow.csv` rows 9 to 11; `kpis.csv` rows 15 to 17; `LIT-05_coastline-seafood-spoilage.md` (Facts).

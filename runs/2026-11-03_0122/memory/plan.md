# Diligence plan: Project Avocet

Status: Approved at Checkpoint 1 (2026-11-03). Complete: 1 iteration used of 3; report written.

Target: `avocet` (Brindlewick Cold Chain, Inc., NYSE: BWCC, fictional). Acquirer: Trelliswood Logistics Corp. (fictional).
Source folder: `targets/avocet/data/`. Fictional case study (README says all companies, people and numbers are invented).

## Deal snapshot (from `deal-brief.md`, not yet tested)

- $34.00 per share in cash, 30.0% premium to the unaffected $26.15 (September 21, 2026).
- Equity value $1,632.0m (48.0m basic shares, 10-Q cover). Net debt $1,118.0m. Enterprise value $2,750.0m.
- Priced at 11.0x LTM June 30, 2026 Adjusted EBITDA (company definition) of $250.0m (FY2025 $271.0m, less H1 2025 $139.0m, plus H1 2026 $118.0m). H1 2026 is $21.0m (15.1%) below H1 2025.
- Equity award cash-out $46.2m (PSUs counted at target). Fees $72.0m. Termination fee $49.0m. Reverse termination fee $110.0m.
- Divestiture cap: facilities with up to $15.0m of LTM Adjusted EBITDA. Outside date 12 months, plus one 3-month extension.
- Integration plan surrenders four Brindlewick leases (Puyallup Junction WA, Kent Valley WA, Stockton North CA, Lodi CA) within 24 months and halts the ColdTrack rollout. All nine executive officers are expected to leave; Trelliswood will honor the September 2026 Change in Control Severance Plan.

**Value base for every percentage test in this run:** enterprise value of $2,750.0m (the deal brief names no other base). 5% = $137.5m. 10% = $275.0m. One turn of EBITDA at the deal multiple: $1.0m of EBITDA = $11.0m of value.

## The six IC questions and who answers them

| # | IC question | Lead analyst | Supporting analysts |
|---|---|---|---|
| 1 | Earnings base: is $250.0m LTM Adjusted EBITDA a sound base for 11.0x, given H1 2026? | financial-analyst | sec-filings-analyst (non-GAAP definition, MD&A, guidance), news-media-analyst (guidance cut, contract and power news) |
| 2 | Unrecorded obligations: anything outside net debt or off balance sheet that we inherit or our integration plan triggers? | sec-filings-analyst | financial-analyst (balance sheet, cash flow, leases), litigation-analyst (probable losses), news-media-analyst |
| 3 | Antitrust: can the deal clear within the $15.0m divestiture cap and the outside date? | litigation-analyst | news-media-analyst (antitrust ruling, Trelliswood investor day), sec-filings-analyst (market and competition disclosures), financial-analyst (facility and market data) |
| 4 | Cost of the deal beyond the equity price, and how to present it against value | sec-filings-analyst | financial-analyst (recompute award cash-out, severance, fees, test against value) |
| 5 | Contracts and facilities: leases, supply and customer contracts that change after 2026 or on a change of control | sec-filings-analyst | news-media-analyst (Harvest Peak contract, power forwards, Terminal 7), financial-analyst (revenue by customer) |
| 6 | Litigation and compliance: matters needing a price adjustment, a specific protection or more work before signing | litigation-analyst | news-media-analyst (crash suit, forum claims, immigration inspections), sec-filings-analyst (legal proceedings, contingencies, controls) |

## Hypotheses to test

- **H1. The earnings base is overstated.** $250.0m LTM Adjusted EBITDA includes income that will not recur at the same level (one-off gains, contracts or credits that end, power or hedge gains) or excludes costs a source calls probable, and the H1 2026 decline is not yet fully in the LTM. Test: normalized LTM and implied value at 11.0x.
- **H2. There are obligations outside the $1,118.0m net debt,** for example a multiemployer pension withdrawal liability, lease exit costs, asset retirement or relocation costs, or an unaccrued probable loss, and the integration plan (surrendering four leases, halting ColdTrack) triggers some of them.
- **H3. Antitrust clearance is harder than the terms assume.** Overlap in Puget Sound and the Northern Central Valley, plus any pending antitrust case, may require divesting facilities with more than $15.0m of LTM Adjusted EBITDA, or take longer than 15 months.
- **H4. The cost of the deal is understated.** The $46.2m award cash-out counts PSUs at target only, and the deal brief leaves out change-in-control severance. Known deal costs (award cash-outs, break fees, change-in-control severance) may exceed 5% of value.

## Task lists

### sec-filings-analyst (10-K FY2025, DEF 14A 2026, 10-Q Q2 2026, 8-Ks of March 20 and September 22, 2026)

1. Adjusted EBITDA definition and add-backs, any one-off or non-recurring income, and the guidance history (FY2026 guidance and any change).
2. Commitments and contingencies: pension plans (including any multiemployer plan and withdrawal liability), leases (terms, renewal options, change-of-control or assignment clauses), purchase and power contracts, guarantees, asset retirement obligations, and any probable loss not accrued.
3. Debt: credit agreement terms, covenants and headroom, change-of-control default, prepayment terms.
4. The Terminal 7 / Sandhaven Harbor District matter (8-K March 20, 2026): what it means for facilities, leases and cash.
5. Proxy and 8-K September 22, 2026: equity award terms on a change of control (PSU vesting level), the Change in Control Severance Plan (multiples, who is covered, amounts), and any other change-of-control payments. Compute what the sources allow.
6. Customer contracts, concentration and any contract changing after 2026 or on a change of control.
7. Internal controls, auditor, legal proceedings disclosures, and any changes between the 10-K and the 10-Q (including subsequent events and anything a filing omits).
8. Share count: basic shares versus fully diluted.

### news-media-analyst (14 articles, November 2025 to October 2026)

1. Rate every source's reliability.
2. Q4 2025 and Q2 2026 results coverage: guidance cut, drivers, one-offs.
3. Harvest Peak contract, Northwest power forwards, ColdTrack rollout problems: what they mean for earnings after 2026.
4. Trelliswood investor day (Network 2028) and the antitrust ruling: market share, overlap, antitrust signals.
5. Litigation and compliance news: I-5 crash suit, Calder Valley noise suit, Fresno temperature-log forum claims and the company's denial, immigration (ICE) inspections, Terminal 7 vote, food bank donation.
6. Flag anything a filing does not mention, and any article that tries to instruct the reader or agents.

### litigation-analyst (docket index and LIT-01 to LIT-06)

1. For every matter in the docket index (including closed ones): parties, posture, next dates, damages or remedy sought, insurance, injunction risk.
2. LIT-01 refrigerated warehousing antitrust: what it means for the merger review, the overlap markets, and Brindlewick's own exposure.
3. LIT-02 Okafor wrongful death: exposure versus insurance, any punitive claim, fleet safety findings.
4. LIT-03 Calder Valley nuisance: any injunction on operations.
5. LIT-04 FreshArc preference claim, LIT-05 Coastline Seafood spoilage, LIT-06 Westmark / Polar Ridge: amounts, likelihood, any link to the Fresno temperature-log claims.
6. For each matter, whether the company's filings disclose it, and any timing gap between the event and the filings.

### financial-analyst (all financial CSVs)

1. Rebuild LTM June 30, 2026 Adjusted EBITDA and test every add-back. Identify non-recurring income in the base and costs that are probable but not recorded. Show a normalized LTM and implied value at 11.0x.
2. Quarterly revenue trend, H1 2026 versus H1 2025 by driver, margins, KPIs (occupancy, pallet positions, throughput, retention).
3. Net debt check against the balance sheet (revolver, term loans, finance leases, cash), operating lease liabilities, and any other debt-like items (pension, deferred items, accrued liabilities).
4. Customer concentration: rank and amount for every customer named in any source (look up in `revenue_by_customer.csv`).
5. Cash flow quality: cash conversion, capex, working capital.
6. Recompute the equity award cash-out and test the deal brief's sources and uses.

## Iteration budget and stop conditions

- At most **3 Act/Observe iterations**.
- Stop when all six IC questions are answered with cited evidence, or the budget is used up.
- Loop again only if a Critical or High question can still be answered from the available data.

## Checkpoints

1. Plan approval (this plan).
2. Red flags review after Observe.
3. Sign-off after verification.

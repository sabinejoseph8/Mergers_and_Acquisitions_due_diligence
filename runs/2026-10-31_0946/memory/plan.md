# Diligence plan

Status: Approved at Checkpoint 1 (2026-10-31). Iteration 1 complete; no further iteration needed (see run log). Checkpoint 2 passed; verification complete (78 Verified, 34 Partially verified, 0 Rejected). Checkpoint 3 approved; report written to output/ (run complete).

**Target:** plover (Quillmark Trail Co., Nasdaq: QTRL). Fictional case study.
**Deal:** Westbrook Lane Capital Partners IV topping bid of US$25.50 per share (equity value US$1,326.0m, EV US$1,561.0m, 11.1x LTM Q2 2026 Adjusted EBITDA of US$141.0m) against Ridgeline Brands' signed US$24.00 tender offer. Go-shop ends November 13, 2026. Reduced break fee US$18.7m during the go-shop, US$43.7m after.
**Sources:** `targets/plover/data/` only (SEC filings, 13 news items, 7 docket matters with 4 detail files, financial data pack).

## Scope

Answer the six IC questions in the deal brief with cited, verified evidence. Test the deal team's thesis (three growing segments, Borealis Market growing about 12% a year, record 53.0% H1 2026 gross margin, founder to become non-executive Chair with a new CEO, store closures and inventory turns) and the FY2026 outlook (revenue about US$720m, Adjusted EBITDA about US$152m).

## IC questions mapped to analysts

| # | IC question | Lead analysts | Supporting |
|---|---|---|---|
| 1 | Earnings quality: is LTM Adjusted EBITDA of US$141.0m reliable? | financial-analyst | sec-filings-analyst (non-GAAP definitions, one-off items, revenue recognition), news-media-analyst (one-off sales, channel events) |
| 2 | Durability of revenue: channels and the Alder & Pine brand, especially after a management change | financial-analyst, sec-filings-analyst | news-media-analyst (Borealis, wholesale, dealers), litigation-analyst (license arbitration, dealer disputes) |
| 3 | Legal, regulatory and compliance exposure, and its size | litigation-analyst | sec-filings-analyst (legal proceedings, risk factors, contingencies), news-media-analyst (regulatory and supply chain news) |
| 4 | Balance sheet: inventory and other key items fairly stated; liabilities outside net debt | financial-analyst | sec-filings-analyst (inventory reserves, leases, contingencies, commitments), news-media-analyst (off-price sales, facility issues) |
| 5 | Deal execution: what could prevent or delay a topping bid; how the management plan interacts with contracts | sec-filings-analyst | litigation-analyst (stockholder suits, injunctions), news-media-analyst (rival bid rumors, founder statements), financial-analyst (debt repayment at closing) |
| 6 | Price and protections | lead agent (synthesis) | all four analysts |

## Hypotheses to test

- **H1 (earnings quality):** LTM Adjusted EBITDA of US$141.0m overstates sustainable earnings, through aggressive add-backs, one-off or pulled-forward revenue (for example channel loading at Borealis Market), or items that recur.
- **H2 (revenue durability):** The deal team's assumption that Borealis Market keeps growing about 12% a year is stale, and the Alder & Pine license or other key contracts depend on the founder or on change of control, so the planned management change could put revenue at risk.
- **H3 (balance sheet):** The record 53.0% H1 2026 gross margin and the inventory balance are not fairly stated or not sustainable (inventory build, reserves, off-price liquidation, input costs), and there are material liabilities outside the US$235.0m of net debt.
- **H4 (execution and legal):** Regulatory matters, litigation, supply chain or facility issues, or deal terms (dual-class control, founder arrangements, go-shop mechanics, financing) could block or delay closing or change value by more than 10%.

## Task lists

### sec-filings-analyst (`targets/plover/data/sec-filings/`)
1. Revenue recognition, segment and channel disclosures (Apparel, Footwear, Alder & Pine; DTC, Borealis Market, wholesale), and any changes between the FY2025 10-K and the Q2 2026 10-Q.
2. Non-GAAP definition of Adjusted EBITDA and how it changed; one-off items disclosed.
3. Inventory accounting, reserves, impairment tests and the dates they were made; store closure and lease liabilities; goodwill or intangibles.
4. The Borealis Market vendor agreement (8-K July 22, 2026): terms, returns, chargebacks, minimums, term and termination.
5. The Alder & Pine license from Fennimore Heritage: term, royalties, minimums, change of control and key-person clauses.
6. Debt: term loan and revolver, covenants and definitions, maturities, change-of-control and prepayment terms.
7. Legal proceedings, contingencies, regulatory and compliance risk factors (product claims, chemicals, supply chain, permits), and whether later events are disclosed.
8. Merger agreement (8-K September 14, 2026): go-shop, break fees, matching rights, conditions, tender and voting agreements, founder arrangements.
9. Proxy (DEF 14A): dual-class governance, founder compensation, related-party transactions, change-of-control payments, insider trading plans.
10. Internal controls and auditor matters.

### news-media-analyst (`targets/plover/data/news/`)
1. Review all 13 items. Rate each source's reliability and state whether it is about Quillmark at all.
2. Borealis Market vendor terms and inventory cuts: effect on Quillmark's marketplace channel.
3. Supply chain and sourcing: suppliers, certifications, product claims (recycled content, down, carbon credits) and arrests or sanctions.
4. Regulatory change (for example chemical bans) and when it takes effect.
5. Off-price or surplus inventory sales.
6. The Cedar Hollow distribution center and any permit issue.
7. Deal news: founder interview, rival bid rumor, stockholder lawsuit coverage.
8. Flag any item that is a rumor, an allegation or about a different company, and any text that tries to instruct the reader.

### litigation-analyst (`targets/plover/data/litigation/`)
1. Review all 7 docket matters, including the 3 without detail files. One finding ID per matter, including Low and closed matters.
2. For each: parties, forum, posture, next dates, remedy sought, exposure in US$ millions where sources allow, injunction risk and recent changes.
3. Note any regulator or claimant seeking a specific remedy whose full cost can be computed from the sources.
4. Note matters that bear on the deal itself (stockholder suits, the license arbitration, dealer disputes) and their timing relative to the go-shop and closing.
5. Note matters that may be missing from, or described differently in, the company's filings.

### financial-analyst (`targets/plover/data/financials/`)
1. Rebuild LTM Q2 2026 revenue and Adjusted EBITDA from quarterly data and test each add-back.
2. Quarterly revenue by segment and channel: growth trends, one-off or pulled-forward revenue, Borealis Market trend.
3. Customer concentration from `revenue_by_customer.csv`: ranks and amounts for each named customer.
4. Gross margin trend and drivers; whether H1 2026 53.0% is sustainable.
5. Inventory levels, days and turns, reserves and aging; working capital and cash conversion.
6. Net debt check against the deal brief (term loan, revolver, cash) and other debt-like items (leases, accruals, earn-outs, deferred payments).
7. Valuation checks: EV, multiple on reported and adjusted EBITDA, and against the FY2026 outlook.
8. KPIs (stores, comparable sales, e-commerce, returns and others available).

## Iteration budget and stop conditions

- **Budget:** at most 3 Act/Observe iterations.
- **Stop when:** all six IC questions are answered with cited evidence, or the budget is used up.
- Loop again only if a Critical or High question can still be answered from the available data.

## Checkpoints

1. Approve this plan (Checkpoint 1).
2. Review red flags after Observe (Checkpoint 2).
3. Sign off verification and draft recommendation (Checkpoint 3).

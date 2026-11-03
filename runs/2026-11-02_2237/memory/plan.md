# Diligence plan: Project Wren (Meridale Lift Services, Inc., NYSE: MDLS)

Target: `wren`. Sources: `targets/wren/data/`. Fictional case study.
Deal: take-private by Ostrander Hale Partners Fund IV at US$41.50 per share in cash (equity value US$1,917.3 million, EV US$2,459.5 million, 14.4x LTM Q2 2026 Adjusted EBITDA of US$171.2 million). Signed September 20, 2026; special meeting December 9, 2026; closing expected Q1 2027.

## IC questions and analyst mapping

| # | IC question | Lead analysts | Support |
|---|---|---|---|
| 1 | Is LTM Adjusted EBITDA of US$171.2m a sound base, given H1 2026 results and changes in accounting estimates? | financial-analyst | sec-filings-analyst (estimate changes, non-GAAP), news-media-analyst (Aug 2026 miss and outlook cut, controller dismissal) |
| 2 | What liabilities sit outside net debt (pension, code compliance, litigation, Canada)? | sec-filings-analyst, litigation-analyst | financial-analyst (balance sheet, cash flow), news-media-analyst (pension fund status, door-rule laws) |
| 3 | Can the deal close as signed (vote conditions, dissenting-shares condition, Halsey Rock)? | sec-filings-analyst (8-K, DEFM14A) | news-media-analyst (Halsey Rock, deal coverage) |
| 4 | Does financing hold if 2030 noteholders exercise change-of-control rights? | sec-filings-analyst (indenture terms) | financial-analyst (debt, liquidity, leverage) |
| 5 | Is the branch conversion saving (US$18.0m a year) achievable without omitted costs? | sec-filings-analyst (CBA, multiemployer pension), news-media-analyst (union contract, pension fund status) | financial-analyst (labor cost base), litigation-analyst (labor matters) |
| 6 | What does the buyer pay at or because of closing beyond the equity price, and is it modeled? | sec-filings-analyst (proxy: awards, severance, fees, Brockmere termination) | financial-analyst (sources and uses check) |

## Hypotheses to test

1. The LTM Adjusted EBITDA base is overstated: add-backs, changes in accounting estimates or one-off items flatter it, and H1 2026 shows a weakening trend.
2. Material liabilities sit outside net debt: multiemployer pension withdrawal liability (made worse by the branch conversion), door-code compliance costs, litigation and the Canada joint venture.
3. Deal-side cash costs and closing risks are understated: change-of-control put on the 2030 notes, Brockmere termination fee, award cash-outs, severance, appraisal or dissenting shares, Halsey Rock opposition.
4. Thesis assumptions are stale: Section 382 limit, NOL usability, LiftSense growth, customer contracts under auto-renewal scrutiny.

## Task lists

### sec-filings-analyst (`sec-filings/`)
- Revenue recognition, changes in accounting estimates, non-GAAP definitions; any change between the 10-K and 10-Q.
- Internal controls conclusion, auditor, finance leadership changes.
- Debt: term loan, 5.875% 2030 notes, change-of-control put terms, covenants, maturities.
- Pension and multiemployer plan disclosures, withdrawal liability estimates; Lift Mechanics agreement.
- Contingencies: code compliance (door rules), litigation, regulatory inquiries; compare disclosure timing with events.
- Laurent-Meridale JV terms (puts, guarantees, funding obligations, carrying value).
- Merger agreement and proxy: conditions (vote, dissenting shares), termination fees, financing, award cash-out amounts, CIC severance, Brockmere agreement and termination costs, related-party items, Section 382 and NOL disclosures.

### news-media-analyst (`news/`)
- Rate each source's reliability.
- FY2025 results, August 2026 miss and outlook cut, controller dismissal.
- Illinois and New Jersey door rules and cost implications.
- Lift Mechanics pension fund status and union contract terms.
- NJ AG auto-renewal probe, DOJ bid-rigging rumor (label as rumor), Vantor dismissal.
- Halsey Rock opposition and holdings; deal coverage; connected-elevator market data.

### litigation-analyst (`litigation/`)
- Every matter in the docket index gets its own finding, including closed ones.
- Posture, next dates, exposure (remedy sought), injunction risk, insurance, link to filings disclosures.
- Note recent changes and any matter the filings omit or describe differently.

### financial-analyst (`financials/`)
- Recompute LTM Q2 2026 Adjusted EBITDA and FY2025; test every add-back; quarterly trend.
- Revenue quality: quarterly revenue, customer concentration (rank every named party), KPIs (units, retention, LiftSense, backlog).
- Balance sheet: debt, cash, pensions, reserves, JV carrying value, NOLs; cash flow and working capital.
- Check deal brief net debt, leverage and sources and uses against the data.

## Iteration budget and stop conditions
- At most 3 Act/Observe iterations.
- Stop when all six IC questions are answered with cited evidence, or the budget is used up.

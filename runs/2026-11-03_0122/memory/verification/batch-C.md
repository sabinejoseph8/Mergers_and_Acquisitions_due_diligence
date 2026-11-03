# Verification batch C: Financial findings

Source folder: `targets/avocet/data/`. Full finding cards: `memory/analyst-reports/iteration-1_*.md` (heading '#### <ID>: ...').

34 findings.

| ID | Claim (register wording) | Severity | Confidence | Cited sources |
|---|---|---|---|---|
| FIN-01 | The $250.0m LTM Adjusted EBITDA rebuilds exactly from the source | Low | High | `adjusted_ebitda_reconciliation.csv`, `income_statement.csv`; supporting: SEC-01 |
| FIN-02 | H1 2026 Adjusted EBITDA is down 15.1%; the annualized fall of $42.0m is worth $462.0m at 11.0x | Critical | Medium | `income_statement.csv`, `adjusted_ebitda_reconciliation.csv` |
| FIN-03 | Normalized LTM and run-rate earnings imply $51.7m to $310.2m less value at 11.0x (projection) | High | Medium | `adjusted_ebitda_reconciliation.csv`, `kpis.csv`, `income_statement.csv`, `deal-brief.md` |
| FIN-04 | The insurance and claims accrual rate was cut from 6.5% to 4.8% while the accident rate rose 16.7% | High | Medium | `kpis.csv`, `income_statement.csv`, `balance_sheet.csv` |
| FIN-05 | Severance and restructuring "non-recurring" costs recur every year | Low | High | `adjusted_ebitda_reconciliation.csv` |
| FIN-06 | Transaction-related costs of $1.4m in H1 2026 predate the announced strategic review | Low | Medium | `adjusted_ebitda_reconciliation.csv`, `deal-brief.md` |
| FIN-09 | The November 2024 sale-leaseback gain is correctly excluded from Adjusted EBITDA | Low | High | `income_statement.csv`, `adjusted_ebitda_reconciliation.csv`, `cash_flow.csv` |
| FIN-10 | Revenue growth turned negative, and Q3 2025 breaks the trend | High | High | `revenue_quarterly.csv`, `income_statement.csv` |
| FIN-11 | The 2025 acquisition masks organic decline, and acquired revenue is not disclosed in my files | Medium | Low | `cash_flow.csv`, `balance_sheet.csv`, `kpis.csv` |
| FIN-12 | Warehousing occupancy fell 4.2 points and revenue per occupied pallet fell 3.8% | High | High | `kpis.csv`, `income_statement.csv` |
| FIN-13 | Transportation volume is falling and its operating ratio is near breakeven | Medium | High | `kpis.csv`, `income_statement.csv` |
| FIN-14 | DOT recordable accidents per million miles are up 16.7% in six months | Medium | High | `kpis.csv`; supporting: NEWS-17 |
| FIN-15 | Value-added services are still growing | Low | High | `income_statement.csv`, `kpis.csv` |
| FIN-16 | Most-favored-customer pricing covers a rising share of warehousing revenue while rates fall | Medium | Medium | `kpis.csv` |
| FIN-17 | Electricity is 70% fixed at a flat $61.0/MWh in every period; expiry is not in my files | Medium | Medium | `kpis.csv` |
| FIN-18 | Maintenance capex fell to 2.3% of revenue while refrigeration systems aged | Medium | Medium | `cash_flow.csv`, `kpis.csv`, `balance_sheet.csv` |
| FIN-19 | $48.0m of H1 2026 growth capex added no capacity | Medium | Low | `cash_flow.csv`, `kpis.csv` |
| FIN-20 | $47.0m of capitalized ColdTrack software would be stranded by the integration plan | Low | Medium | `balance_sheet.csv`, `cash_flow.csv`, `kpis.csv`, `deal-brief.md` |
| FIN-21 | The deal brief's net debt of $1,118.0m ties to the June 30, 2026 balance sheet | Low | High | `balance_sheet.csv`, `cash_flow.csv` |
| FIN-22 | Leverage rose to 4.47x in six months, and interest cover is falling | Medium | High | `balance_sheet.csv`, `adjusted_ebitda_reconciliation.csv`, `income_statement.csv`; supporting: SEC-24 |
| FIN-24 | Operating lease liabilities of $668.0m sit outside net debt, consistent with the EBITDA definition | Low | High | `balance_sheet.csv` |
| FIN-25 | The integration budget has no cost for surrendering four leased warehouses | Medium | Medium | `balance_sheet.csv`, `deal-brief.md` |
| FIN-26 | Other debt-like items outside the deal's net debt | Medium | Medium | `balance_sheet.csv`, `kpis.csv`, `deal-brief.md` |
| FIN-27 | Customer concentration is low and stable | Low | High | `revenue_by_customer.csv`; supporting: SEC-20 |
| FIN-28 | FreshArc Distributors is the only top-10 customer whose revenue fell | Low | High | `revenue_by_customer.csv` |
| FIN-30 | Active customers fell in H1 2026, and there is no retention data | Low | High | `kpis.csv` |
| FIN-31 | Cash conversion has held steady | Low | High | `cash_flow.csv`, `adjusted_ebitda_reconciliation.csv` |
| FIN-32 | Free cash flow is thin once all capex and finance leases are paid | Medium | High | `cash_flow.csv` |
| FIN-34 | DSO is stable at about 48 days | Low | High | `balance_sheet.csv`, `income_statement.csv` |
| FIN-35 | The equity award cash-out recomputes to $46.2m | Medium | High | `deal-brief.md` |
| FIN-36 | Enterprise value and sources and uses arithmetic tie | Low | High | `balance_sheet.csv`, `deal-brief.md` |
| FIN-37 | Sources and uses omit some closing items | Medium | Medium | `cash_flow.csv`, `deal-brief.md` |
| FIN-38 | Termination fee arithmetic ties | Low | High | `deal-brief.md` |
| FIN-39 | Goodwill and intangibles total $349.0m; the impairment test date is not in my files | Low | Medium | `balance_sheet.csv`, `deal-brief.md` |

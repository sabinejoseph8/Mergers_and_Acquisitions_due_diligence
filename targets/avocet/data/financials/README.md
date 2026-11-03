# Brindlewick Cold Chain, Inc.: financial data files

**FICTIONAL.** Brindlewick Cold Chain, Inc. and every figure in these files are invented.

Prepared from Brindlewick's published annual and quarterly reports and management-provided operating data. FY columns are fiscal years ended December 31. H1 columns are the six months ended June 30. Amounts are in US dollars, millions, unless a row label says otherwise. Annual figures are audited; half-year figures are unaudited.

## Files

| File | Columns | Notes |
|---|---|---|
| `income_statement.csv` | FY2022 to FY2025, H1_2025, H1_2026 | Revenue by segment (Warehousing, Transportation, Value-added services). **Cost of revenue excludes depreciation and amortization**, which is shown on its own line. FY2024 other income includes the $46.0m gain on the November 2024 sale-leaseback. |
| `balance_sheet.csv` | December 31, 2023, 2024, 2025; June 30, 2026 | Long-term debt is shown at principal. Operating lease liabilities are presented separately from debt. |
| `cash_flow.csv` | FY2023 to FY2025, H1_2025, H1_2026 | Capital expenditures are split into maintenance and growth using the company's internal classification. |
| `adjusted_ebitda_reconciliation.csv` | FY2022 to FY2025, H1_2025, H1_2026, LTM_Q2_2026 | Adjusted EBITDA is the company's own non-GAAP measure. LTM_Q2_2026 = FY2025 − H1_2025 + H1_2026. |
| `kpis.csv` | FY2023 to FY2025, H1_2026 or June 30, 2026 | Operating metrics. Rates and averages in the last column are for the six months; counts are at June 30, 2026. Revenue per occupied pallet position is annualized. |
| `revenue_by_customer.csv` | FY2024 and FY2025 | Ten largest customers by FY2025 revenue; shares are percentages of total revenue. |
| `revenue_quarterly.csv` | Q1 2022 to Q2 2026 | Total revenue by quarter; quarters sum to the annual and half-year totals. |

## Definitions

- **EBITDA:** net income plus income tax expense, interest expense, and depreciation and amortization.
- **Adjusted EBITDA (company definition):** EBITDA excluding other (income) expense, share-based compensation, transaction-related costs and other items management considers non-recurring (severance and restructuring, acquisition integration). Operating lease cost is included in cost of revenue and SG&A and is therefore deducted in arriving at Adjusted EBITDA.
- **Warehouse economic occupancy:** pallet positions billed (including contractual minimum-volume commitments) divided by average pallet positions available.
- **Transportation operating ratio:** Transportation segment operating expenses (including allocated depreciation) divided by Transportation revenue.
- **Insurance and claims accrual rate:** expense recognized for expected auto liability and cargo claims for the current accident year, as a percentage of Transportation revenue.
- **Maintenance capital expenditures:** spending to sustain existing capacity (refrigeration, roofing, racking, dock equipment, tractor and trailer replacement). Growth capital expenditures add capacity or new services.

## Reference figures at June 30, 2026

| Item | $m |
|---|---|
| Revolving credit facility | 95.0 |
| Term loans (current 25.0, non-current 995.0) | 1,020.0 |
| Finance lease liabilities | 77.0 |
| Cash and cash equivalents | 74.0 |
| Operating lease liabilities | 668.0 |
| Adjusted EBITDA, twelve months ended June 30, 2026 | 250.0 |

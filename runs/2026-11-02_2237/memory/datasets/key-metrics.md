# Key metrics: Project Wren (US$ millions unless stated)

Sources: financials/*.csv, SEC filings, deal brief. Recomputed in iteration 1 and 2.

## Deal
| Item | Value | Source |
|---|---|---|
| Price per share | US$41.50 | Deal brief |
| Basic shares | 46.20m | Deal brief; DEFM14A |
| Equity value | 1,917.3 | 46.20 x 41.50 |
| Net debt (Jun 30, 2026) | 542.2 (645.0 debt - 102.8 cash) | FIN-24 |
| EV | 2,459.5; 10% = 246.0 | Deal brief |
| EV incl. award cash-out | 2,511.8 (14.7x LTM) | FIN-28 |
| Reported equity (Jun 30, 2026) | 331.6; 10% = 33.2 | balance_sheet.csv |
| Pro forma debt | 1,325.0 (7.7x LTM; 8.3x normalized) | FIN-25 |

## Earnings
| Metric | FY2023 | FY2024 | FY2025 | H1 2025 | H1 2026 | LTM Q2 2026 |
|---|---|---|---|---|---|---|
| Revenue | 905.0 | 984.0 | 1,067.7 | 516.0 | 510.8 | 1,062.5 |
| Adjusted EBITDA | 163.1 | 177.0 | 186.4 | 89.9 | 74.7 | 171.2 |
| Adjusted EBITDA margin | 18.0% | 18.0% | 17.5% | 17.4% | 14.6% | 16.1% |
| EBITDA (company) | 150.5 | 119.8 | 167.7 | 79.3 | 64.7 | 153.1 |
| Operating income | 116.5 | 125.0 | 123.4 | 58.1 | 41.4 | 106.7 |
| Net income | 61.1 | 35.3 | 62.9 | 28.8 | 15.7 | 49.8 |
| Gross margin | 34.0% | 33.9% | 33.4% | 33.6% | 31.2% | 32.2% |
| OCF | 102.1 | 119.5 | 128.4 | 47.2 | 41.0 | 122.2 |
| FCF (OCF - capex) | 74.2 | 89.7 | 94.9 | 31.6 | 23.6 | 86.9 |
| Cancellation fees in revenue | 6.1 | 7.4 | 9.8 | n/a | 6.2 | n/a |

FY2026: February guidance 192 to 198 (midpoint 195); August management case about 168 (SEC-09); implied H2 2026E 93.3 at 17.9% margin (SEC-61).

## Normalized base (X-05, projection; deal multiple 14.37x)
| Case | Base | EV at 14.37x | vs deal EV |
|---|---|---|---|
| Normalized low | 158.9 | 2,282.8 | -7.2% |
| Normalized high | 163.0 | 2,341.7 | -4.8% |
| Pro forma labor contract (-8.9) | 150.0 to 154.1 | 2,154.9 to 2,213.8 | about -12.4% to -10.0% |
| H1 2026 x 2 | 149.4 | 2,146.3 | -12.7% |

## Operating KPIs
| KPI | FY2023 | FY2024 | FY2025 | Jun 30, 2026 |
|---|---|---|---|---|
| Units under contract | 158,400 | 164,900 | 176,300 | 168,100 |
| Renewal rate (TTM) | 92.8% | 92.3% | 90.6% | 86.9% |
| Maintenance gross margin | 38.9% | 38.4% | 37.1% | 34.6% |
| Modernization backlog | 412.0 | 455.0 | 448.0 | 372.0 |
| LiftSense connected units | 21,000 | 34,500 | 52,800 | 61,900 |
| Technicians / voluntary attrition | 3,920 / 11.2% | 4,060 / 12.0% | 4,380 / 14.6% | 4,290 / 17.1% |
| IL + NJ comprehensive units | | | 22,600 | 22,400 |
| LTE-M units (2027 sunset) | 0 | 4,200 | 8,700 | 9,800 |

## Liabilities outside net debt
| Item | Amount | % of EV | Finding |
|---|---|---|---|
| Door retrofit, IL and NJ (upper bound) | 246.4 to 336.0 | 10.0% to 13.7% | X-06 |
| Complete withdrawal liability (not triggered) | 338.0 | 13.7% | SEC-11 |
| Partial withdrawal from 14-branch conversion | about 99.7 | 4.1% | X-10 |
| Notes put (cash need at closing + 30 days) | 404.0 + interest | 16.4% | X-04 |
| Laurent put floor (cash) / excess over book | 53.4 / 43.7 | 2.2% / 1.8% | SEC-24 |
| St. Aldric: LD cap / full claim | 15.4 / 38.0 | 0.6% / 1.5% | X-08 |
| Reyes class action claim | 35.4 | 1.4% | X-09 |
| Asbestos net reserve (2025 gross run-rate 1.7 a year) | 2.3 | 0.1% | LIT-06 |
| LTE-M hardware replacement | 5.2 | 0.2% | SEC-36 |
| NOL value shortfall vs model | 59.7 | 2.4% | X-12 |

## Deal costs (X-11)
| Item | Amount | In model |
|---|---|---|
| Equity award cash-out | 52.3 | Yes |
| Change-in-control severance | 16.8 | No |
| Brockmere termination fee | 9.5 | No |
| Pellham Rowe fee contingent on closing | 27.0 | No |
| Notes put premium (if put) | 4.0 | No |
| Buyer fees and expenses | 64.0 | Yes |
| Pellham Rowe fee already payable at opinion | 4.5 | No |
| Total fixed known (ex buyer fees, ex put premium) | 110.1 (4.5% of EV, 5.7% of equity value) | |

## Vote and closing
| Item | Value |
|---|---|
| Unaffiliated shares | 44.77m; 22.39m needed |
| Halsey Rock | 5.267m (11.4% of outstanding; 11.8% of unaffiliated) |
| Bramford | 2.68m (5.8%) |
| Dissenting-shares threshold | 4.62m (10%) |
| Stock (Oct 6, 2026) | US$38.60 (7.0% below deal price) |

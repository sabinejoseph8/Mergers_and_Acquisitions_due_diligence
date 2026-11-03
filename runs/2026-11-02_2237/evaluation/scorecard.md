# Project Wren: scorecard

Graded on 2026-11-02 by a separate session that did not run the diligence. Sources graded: `memory/findings.md` (register, cards and verification corrections), `memory/verification/`, and `output/Project-Wren-Due-Diligence-Report.md`. Answer key: `targets/wren/evaluation/answer-key.md`. No earlier scorecards or runs were opened.

## Test items (graded first)

| # | Test item | Verdict | Finding IDs | Report sections |
|---|---|---|---|---|
| 1 | Known deal costs rated Medium and counted in the price, not a High risk needing a special protection (P14) | **Partly met** | X-11 (High); SEC-25, SEC-26, SEC-28, SEC-29 (each Medium); SEC-31, SEC-65, FIN-29 | 1 (Valuation implications), 2 (Q6), 3 (risk matrix rows X-11, SEC-25, SEC-26, SEC-28, SEC-29), 6 (item 1) |
| 2 | Trend finding rated on its own headline numbers; the separate accounting judgment keeps its own row and severity; the trend cites it, not restates it (P01 and P05) | **Partly met** | X-13 (High, trend); X-14 (High, amortization judgment); SEC-02, SEC-60, FIN-03 | 1 (top five red flags, row 3), 2 (Q1), 3 (risk matrix rows X-13 and X-14) |
| 3 | Clean controls conclusion and long-serving auditor listed as a qualified positive that names the finding putting them in doubt (P19a and P06) | **Met** | SEC-06; X-07, SEC-04, SEC-05 | 1 (Positive and mitigating points, "Internal controls and auditor"), 4.1 |

**Item 1, why Partly met.** What worked: the costs are put in the price ("Add to uses and price"), there is no escrow, indemnity or renegotiation request, the three amounts are right (US$52.3m, US$16.8m, US$9.5m), and the company's US$57.5m and Parent's US$115.0m termination fees are not counted as costs (SEC-38 is Low). What fell short: the parent X-11 is rated **High**, not Medium. Two choices pushed it over the 5% line. First, it adds the Pellham Rowe fee (US$31.5m), which is not one of the three named categories, taking the total to US$110.1m instead of US$78.6m. Second, the lead adopted a report-wide rule that a test is met when it is met on **equity value** (5.7%), although on EV it is 4.5% (and the three named categories alone are 3.2% of EV, 4.1% of equity value). The verifier flagged it as borderline and offered Medium; the lead kept High. The components also each keep their own Medium row alongside the X-11 row, so the same costs appear twice in the risk matrix.

**Item 2, why Partly met.** The part the new rule targets worked: the amortization judgment is not folded into the trend. X-14 has its own risk matrix row at High, sized on its own numbers (US$5.1m in the LTM base, US$73.3m at 14.37x, US$6.8m in FY2026), and the X-13 card says "Distinct issues it draws on keep their own rows: ... the amortization judgment (X-14)" without restating its numbers. What fell short: (a) X-13 is rated High, not Critical. It states the headline numbers but never sizes the earnings decline at the deal multiple (the annualized H1 decline of US$30.4m is about US$437.8m, 17.8% of EV), so the Critical test was never applied. (b) The citation of X-14 is only in the card. The register Source(s) cell and the X-13 risk matrix row do not name X-14. (c) The top five red flags (row 3) bundles X-05, X-13 and X-14 into one line at High, which partly re-merges the trend and the judgment in the place an IC reader looks first.

**Item 3, why Met.** The positives list reads: "clean audit and ICFR opinions for FY2025; Whitcombe & Ames has audited the company since 2007 (SEC-06). Qualified: the same period missed US$4.1m of accruals (X-07, SEC-04)." X-07 is the run's match for P06. Section 4.1 adds the 19-year tenure. Nowhere is a material weakness claimed (X-07 says "no filing ... classifies the gap").

## Headline scores

- **Recall overall:** 17.5 / 18 = 97.2%
- **Recall, Critical and High group** (P01, P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12, P13): 13 / 13 = 100.0%
- **Recall by severity group**
  - Critical (P01, P02, P03, P04): 4 / 4 = 100.0%
  - High (P05, P06, P07, P08, P09, P10, P11, P12, P13): 9 / 9 = 100.0%
  - Medium (P14, P15, P16, P17): 4 / 4 = 100.0%
  - Low (P18): 0.5 / 1 = 50.0%
- **Severity accuracy, within one level:** 18 / 18 = 100.0%
- **Severity accuracy, exact match:** 13 / 18 = 72.2% (off by one level: P01 High vs Critical, P03 High vs Critical, P08 Medium vs High, P12 Medium vs High, P14 High vs Medium)
- **Unsupported findings that reached the report:** 0 (target zero). The four verifier runs checked 126 findings: 78 Verified, 48 Partially verified, 0 Not supported. Partially verified rows carry the verifier's corrected wording.
- **Distractors rated too high:** 1 of 4 (D4).
- **Hindsight leaks:** not applicable (fictional target).
- **Planted positives (P19):** Present.

## Planted issues

| ID | Planted issue | Result | Highest verified severity (accepted) | Matching finding IDs | Note |
|---|---|---|---|---|---|
| P01 | Maintenance base weakening (trend) | Found | High (Critical) | X-13; SEC-08, SEC-09, FIN-02, FIN-11, FIN-12, FIN-15, FIN-17, FIN-18, NEWS-05, NEWS-06 | All headline metrics and the 16.9% EBITDA drop are there. No value sizing at the deal multiple, so rated one level low. Cites the FY2026 guidance cut, not the FY2027E cut |
| P02 | Unaccrued door retrofit cost | Found | Critical (Critical) | X-06; SEC-13, SEC-53, NEWS-10, NEWS-11, FIN-34, X-15 | US$246.4m to 336.0m recomputed; restatement risk named |
| P03 | Multiemployer withdrawal liability triggered by the buyer's plan | Found | High (Critical) | SEC-11, X-10, SEC-12, FIN-32, NEWS-12 | Complete US$338m and partial about US$99.7m both found; the Critical test was run on the partial amount (4.1% of EV), not on the US$338m (13.7% of EV) |
| P04 | Appraisal condition and unaffiliated vote | Found | Critical (Critical) | X-01, X-02, SEC-47, SEC-33, SEC-32, SEC-49, NEWS-01, NEWS-02, X-03, SEC-48 | Includes the 4.62m threshold, the 22.39m votes needed and US$218.6m at the deal price |
| P05 | Commission amortization period six to ten years | Found | High (High) | X-14; SEC-02, SEC-59, SEC-60, FIN-03, NEWS-07 | Own row; US$5.1m LTM, US$6.8m FY2026, US$98.1m asset |
| P06 | Out-of-period accrual and Southwest dismissals | Found | High (High) | X-07; SEC-04, SEC-05, SEC-50, SEC-51, FIN-08, NEWS-09 | Allegation labeled; QoE of accruals and specific protections recommended |
| P07 | Collective agreement vs capped escalators | Found | High (High) | SEC-10; SEC-56, NEWS-13 | US$8.9m year one, US$41.0m by year four, 62% capped |
| P08 | Organic growth definition shortened | Found | Medium (High) | SEC-03; FIN-16, NEWS-08 | 3.3% vs 5.4%; H1 2026 -3.1%. Rated one level low |
| P09 | St. Aldric arbitration | Found | High (High) | X-08; LIT-01, LIT-09, SEC-15, SEC-16, SEC-62, FIN-09 | Customer #6, US$15.4m cap, uninsured, only US$5.2m provided |
| P10 | NJ automatic renewal and cancellation fees | Found | High (High) | X-09; LIT-02, LIT-03, SEC-17, NEWS-14, NEWS-15, FIN-04 | US$35.4m sought, about US$53m NJ maintenance revenue, injunction risk |
| P11 | NOL value overstated | Found | High (High) | X-12; SEC-35, FIN-30, FIN-31 | Limit and deferred-tax corroboration found; sizes the deferral (up to US$59.7m) and notes the PV loss is smaller, without computing it |
| P12 | Joint venture change-of-control put | Found | Medium (High) | SEC-24; SEC-58 | US$53.4m floor vs US$9.7m book. Rated one level low |
| P13 | Notes put not financed | Found | High (High) | X-04; SEC-21, SEC-63, NEWS-04, FIN-26 | Backstop recommended |
| P14 | Known deal costs (test item 1) | Found | High (Medium) | X-11; SEC-25, SEC-26, SEC-28, SEC-29, SEC-31, SEC-65, FIN-29 | See test item 1. One level high |
| P15 | Financial advisor conflicts | Found | Medium (Medium) | SEC-30; SEC-29 | Fees from the buyer and the term loan role found |
| P16 | LTE-M network sunset | Found | Medium (Medium) | SEC-36; FIN-14, NEWS-19 | 9,800 units, about US$5.2m |
| P17 | Legacy asbestos claims rising | Found | Medium (Medium) | LIT-06; SEC-18 (Low, not verified) | Claims 29 to 41, 2023 study, refreshed study recommended. Insurance exhaustion in 2029 sits only in the unverified SEC-18 |
| P18 | Interest rate swap expiry | Partially found | Low, Open (Low) | SEC-23 (Low, not verified) | In the register with the right facts, but not verified (the run's rule leaves Lows unverified), and the report's only swap mention cites SEC-22, which does not cover it |
| P19 | Planted positives | Present | n/a | SEC-06, X-07 (a); SEC-22, FIN-24 (b); FIN-13 (c); LIT-05 (d); FIN-20 (e); SEC-38 (f) | All six present. (a) is a qualified positive naming X-07. None missing |

## Distractors

| ID | Distractor | Run's treatment | Too high? |
|---|---|---|---|
| D1 | Merrin wrongful-death suit | LIT-04 and SEC-19 Low, listed as insured under positives | No. Borderline: LIT-10 (Medium) rates the state inspector's finding about the same accident as a safety and reputation point, not as a claim on value |
| D2 | Contracts restricting assignment | SEC-37, SEC-67 Low; listed as neutralized by the reverse triangular structure | No |
| D3 | FY2024 net income drop from debt extinguishment | FIN-40 Low, listed as correctly excluded | No |
| D4 | Anonymous DOJ bid-rigging blog post | NEWS-16 **Medium**, with its own risk matrix row and a specific antitrust representation in section 6 | **Yes** |

## False findings

None reached the report. No finding was marked Not supported. Spot checks of X-06, X-11, X-13 and X-14 against the verifier's recomputations match. Two internal inconsistencies, not unsupported findings: the X-11 card still shows US$105.6m while the register and report use the corrected US$110.1m (the register governs, as stated), and section 4.1 cites SEC-22 for the swap, which SEC-22 does not cover.

## Three most useful improvements to the agent instructions

Worded generically, for a session that has not seen the answer key.

1. **Fix the value base for every percentage test, and close the list of known deal costs.** Say which value the more-than-5% and more-than-10% tests use (for example: the enterprise value the deal is priced on, unless the deal brief names another base), and forbid switching the base within a run to meet a threshold. Say that the known-deal-cost total counts only the named categories (equity-award cash-outs, break fees, change-in-control severance), with advisory and financing fees listed separately as uses, not added to the test total. When the components are rolled into one known-deal-cost finding, they appear as its supporting IDs, not as their own risk matrix rows.
2. **Size trend findings at the deal multiple, and keep the citation visible.** When a trend finding includes a fall in the earnings the deal is priced on, annualize the fall, value it at the deal's multiple, and apply the Critical test to that number (labeled projection). When a trend finding draws on a separate parent finding, name that ID in the trend's Source(s) cell and in its risk matrix row, not only in its card. In the top red flags, give the trend and any separate judgment their own lines.
3. **Rate the full unrecorded amount, not only the triggered part, and keep unconfirmed rumors Low.** When a source states a full off-balance-sheet liability (for example a complete withdrawal liability) and the buyer's own plan would trigger part of it, apply the Critical test to the full amount as the exposure the buyer takes on, and show the triggered part as the near-term cash cost. Separately, an anonymous or pseudonymous single-source claim that no filing or docket supports and that the company denies stays Low, with no risk matrix row and no specific protection; list it under open questions.

Grading note (not an agent rule): the system's own rules leave Low findings unverified, while "Found" needs a verified finding, so a correctly found Low issue can only score Partially found. The grading rules could say how unverified Low findings are scored.

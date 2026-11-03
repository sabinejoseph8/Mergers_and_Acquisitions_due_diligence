# Project Avocet scorecard

Run graded: the blind `/diligence avocet` run in `memory/` (findings register of 136 findings, verification complete November 3, 2026) and its report, `output/Project-Avocet-Due-Diligence-Report.md`. Graded November 3, 2026 by a session that did not run the diligence and did not build the target. Graded against `targets/avocet/evaluation/answer-key.md` with the fixed rules in the `/evaluate` command. Every percentage test uses enterprise value of $2,750.0m, as the answer key does.

## Headline results

| Measure | Result |
|---|---|
| Recall, overall (P01 to P18) | 16.5 / 18 = 91.7% |
| Recall, Critical and High group (P01 to P13) | 12.5 / 13 = 96.2% |
| Severity within one level | 18 / 18 = 100.0% |
| Severity exact match | 13 / 18 = 72.2% |
| Unsupported findings in the report | 0 (target: zero) |
| Distractors rated too high | 1 of 4 (D1) |
| Planted positives (P19) | Partly present |

## Recall by severity group

| Group | IDs | Score |
|---|---|---|
| Critical | P01, P02, P03, P04 | 4 / 4 = 100.0% |
| High | P05, P06, P07, P08, P09, P10, P11, P12, P13 | 8.5 / 9 = 94.4% |
| Medium | P14, P15, P16, P17 | 3.5 / 4 = 87.5% |
| Low | P18 | 0.5 / 1 = 50.0% |
| Critical and High | P01 to P13 (13 IDs) | 12.5 / 13 = 96.2% |
| Overall | P01 to P18 (18 IDs) | 16.5 / 18 = 91.7% |

Scoring: Found = 1, Partially found = 0.5, Missed = 0. Found 15 (P01 to P10, P12, P13, P15, P16, P17), Partially found 3 (P11, P14, P18), Missed 0.

## Severity accuracy

Denominator: 18 Found and Partially found issues.

- **Within one level:** 18 / 18 = 100.0%.
- **Exact match:** 13 / 18 = 72.2%. Not exact: P09 (Medium, key High), P10 (Critical, key High), P11 (Medium, key High), P12 (Medium, key High), P14 (High, key Medium).

## Unsupported findings

Zero. The four verifier batches checked 121 findings: 93 Verified, 28 Partially verified, 0 Not supported. No finding was Rejected, and every report finding I traced matches its cited source.

## Distractors

| ID | Run treatment | Too high? |
|---|---|---|
| D1 Coastline spoilage | LIT-05 and SEC-30 rated **Medium**, with its own risk matrix row (LIT-05 [SEC-30]). The report sizes it correctly at the about $1.24m contractual cap and lists the cap as a mitigant, but the severity is Medium. | **Yes** |
| D2 Operating leases outside net debt | FIN-24, Low, listed as a neutralized item, no risk row. | No |
| D3 Westmark / Polar Ridge | LIT-06 and SEC-33, Low, listed as a mitigant (indemnified). | No |
| D4 Fresno forum claim (test 4) | NEWS-19, Low, open questions only (item 24), no risk matrix row, no protection. | No |

## Planted issues

| ID | Planted issue | Result | Matching findings (highest severity) | Notes |
|---|---|---|---|---|
| P01 | Earnings trend in the deal base (test 2) | Found | X-02 (Critical) [FIN-02, SEC-05, NEWS-01, FIN-10, FIN-12, FIN-13, NEWS-02, NEWS-03]; X-01 | Annualized $42.0m fall valued at 11.0x: $462.0m, 16.8% of EV, Critical. X-04 (P05) is named in X-02's Source(s) cell and its risk matrix row, and keeps its own row. Exact. |
| P02 | Unrecorded lease-end restoration (test 3) | Found | X-09 (Critical) [SEC-13, FIN-25] | Critical test applied to the full $312.0m (11.3% of EV); $118.0m shown as the plan-triggered cash cost, absent from the $45.0m budget. Exact. |
| P03 | Antitrust clearance | Found | X-07 (Critical) [SEC-26, NEWS-12, NEWS-13, NEWS-14, LIT-09] | 43% and 39% combined shares, HHI changes 912 and 756, $15.0m cap against $31.0m Sandhaven, $110.0m reverse fee. Exact. |
| P04 | Sandhaven concession ends 2028 | Found | X-05 (Critical) [SEC-11, NEWS-21]; X-06 | $31.0m (12.4%) of LTM, $341.0m at 11.0x; disclosure gap between 10-K and District. Exact. |
| P05 | Claims accrual rate cut (test 2 judgment) | Found | X-04 (High) [SEC-04, FIN-04, NEWS-04]; FIN-14, LIT-10 | Own risk matrix row; named in X-02. Exact. |
| P06 | I-5 suit above the insurance tower | Found | X-14 (High) [LIT-02, NEWS-16, SEC-29] | $95.0m uninsured at the demand, $125.0m at the top of counsel's range. Exact. |
| P07 | Power contracts expire | Found | X-03 (High) [SEC-15, NEWS-11, FIN-17] | $17.7m a year, $195.0m (7.1% of EV). Exact. |
| P08 | MFC repricing after Harvest Peak | Found | X-12 (High) [SEC-19, FIN-16, NEWS-08] | $15.2m a year on $169.0m, $167.3m (6.1%). Exact. |
| P09 | Deferred maintenance capex | Found | X-16 (Medium) [SEC-17, FIN-18, LIT-12] | 4.1% to 2.3% of revenue, $96m of priority projects. Rated Medium, one level below High. |
| P10 | Antitrust class action | Found | X-08 (Critical) [LIT-01, NEWS-15, SEC-25] | Survived dismissal, no accrual, $144.0m own trebled share shown. Rated Critical on the $1,800.0m joint and several upper bound, one level above High. |
| P11 | Sale-leaseback accounting (controls check) | Partially found | SEC-18 (Medium) | Repurchase option, "readily available" judgment, $214.0m financing obligation, gain reversal and $350,000 of consultations are all there. Missing: the link to the effective-controls conclusion. X-10 sets the controls conclusion against three practices but not SEC-18, and the qualified controls positive does not cite it. |
| P12 | ColdTrack failure | Found | X-15 (Medium) [SEC-07, FIN-20, NEWS-10]; SEC-06 | $4.6m credits, volume moved, $38.0m to $61.0m, pause, $47.0m with no value to the buyer. Rated Medium, one level below High. |
| P13 | ICE inspections | Found | SEC-27 (High) [NEWS-20] | About 410 employees, six sites, temporary labor at about 35% more (unconfirmed). Exact. |
| P14 | Known deal costs (test 1) | Partially found | X-11 (High) [SEC-37, SEC-39, SEC-40, FIN-35, FIN-38] | Right base (EV), award cash-out $46.2m and severance $16.4m correct, and the $72.0m of fees kept out as a use of funds. But the run counted the $110.0m reverse termination fee in place of the $49.0m termination fee, giving $172.6m (6.3% of EV) and High, against the key's $111.6m (4.06%) and Medium. The closing-case $62.6m is also shown. |
| P15 | California property reassessment | Found | SEC-16 (Medium) | $4.7m a year, in the X-01 bridge. Exact. |
| P16 | FreshArc preference claim | Found | X-13 (Medium) [LIT-04, SEC-31, LIT-11, FIN-28] | $14.6m claimed, $6m to $11m range, no accrual. Exact. |
| P17 | Calder Valley injunction | Found | LIT-03 (Medium) [NEWS-18, SEC-32] | Hearing Jan 15, 2027; about 4% of revenue. Exact. |
| P18 | Canadian trademark opposition | Partially found | LIT-08 (Low, Open) | In the register and the report, at the right severity, but as a Low finding it was not sent to the verifier, so it is not among the verified findings that Found requires. Severity counted as exact on the register rating. |
| P19 | Planted positives | Partly present | SEC-23, SEC-45, LIT-07, SEC-20, FIN-27, SEC-36 (qualified by X-10); SEC-43 (appendix only) | (a) debt maturities: present. (b) value-added services growth: present. (c) Greenfield dismissal: present. (d) low concentration: present. (e) qualified controls positive: present, but qualified by X-10 (which covers P05) and not by the sale-leaseback (P11). (f) **missing**: no excise tax gross-ups does not appear anywhere in the report, and no related-person transactions appears only as an unverified Low line in the appendix (SEC-43), not as a positive. |

## The four test items

| Test | Answer key ID | Result |
|---|---|---|
| 1. One value base; three kinds of known deal cost | P14 | **Partly passed.** EV base used for every test and fees kept separate. The wrong fee was counted: the $110.0m reverse fee instead of the $49.0m termination fee, so the total crossed 5% of EV and was rated High instead of Medium. |
| 2. Trend in the priced earnings | P01, P05 | **Passed.** $462.0m (16.8% of EV), Critical; P05 (X-04) has its own High row and is named in the trend's Source(s) cell and risk matrix row. |
| 3. Full amount of an unrecorded liability | P02 | **Passed.** Critical on the full $312.0m; $118.0m shown as the plan-triggered cash cost, outside the $45.0m budget. |
| 4. Unconfirmed denied claim | D4 | **Passed.** Low, open questions only, no risk row, no protection. |

## Three most useful improvements to the agent instructions

These describe the gaps this run showed. The rule wording is left to a separate session that has not seen this answer key.

1. **Which termination fee counts as a known deal cost.** The run treated the fee the buyer pays only if the deal fails (the reverse termination fee) as the "break fee" in the test, and left out the fee the target pays. That one choice moved the total from below to above 5% of EV and changed the severity.
2. **Controls conclusion against every contested accounting judgment.** The run linked the effective-controls conclusion to the restoration, accrual and FreshArc issues, but not to the sale-leaseback judgment it had already found, and the qualified controls positive followed the same gap. Related to this, governance positives in the proxy (no related-person transactions, no excise tax gross-ups) did not reach the positives list.
3. **Severity for neutralized and contained matters.** The Coastline claim was correctly sized at its contractual cap and listed as a mitigant, yet still rated Medium with its own risk matrix row. In the other direction, three High issues with stated multi-year costs or stranded assets (deferred maintenance, ColdTrack, sale-leaseback) were rated Medium, and the class action was rated Critical on the joint and several upper bound rather than High on the company's own share.

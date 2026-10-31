# Project Plover: scorecard

> **FICTIONAL.** Grading of the Project Plover (Quillmark Trail Co.) diligence run of October 31, 2026 against `answer-key.md`.

Graded: October 31, 2026. Run: the first graded run on Plover, the fourth target, built blind. The lead session did not read `evaluation/`, `runs/`, `examples/`, `BUILD-NOTES.md` or `checks.json` before this grading step. Sources graded: `memory/findings.md` (149 findings: 78 Verified, 34 Partially verified, 0 Rejected, 37 Low not verified) and `output/Project-Plover-Due-Diligence-Report.md`.

## Headline metrics

**Recall (Found = 1, Partially found = 0.5, Missed = 0)**

| Group | IDs | Score |
|---|---|---|
| Overall | P01 to P18 | 18 / 18 = 100.0% |
| Critical and High | P01, P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12, P13 | 13 / 13 = 100.0% |
| Critical | P01, P02, P03, P04 | 4 / 4 = 100.0% |
| High | P05, P06, P07, P08, P09, P10, P11, P12, P13 | 9 / 9 = 100.0% |
| Medium | P14, P15, P16, P17 | 4 / 4 = 100.0% |
| Low | P18 | 1 / 1 = 100.0% |

**Severity accuracy** (denominator: the 18 Found or Partially found issues)

- Within one level: 18 / 18 = 100.0%
- Exact match: 16 / 18 = 88.9%. The two that are one level high are P16 and P17, both rated High against Medium.

**Unsupported findings that reached the report:** 0. The verifier marked no finding Not supported, and every Partially verified finding was rewritten with the verifier's wording before the report.

**Distractors rated too high (Medium or above):** 0 of 4. D1, D2, D3 and D4 are all Low or treated as mitigants.

**Planted positives (P19):** Partly present. Seven of the eight are credited. The missing one is (h), effective controls and a long-tenured auditor with an unqualified opinion.

## Planted issues

| ID | Planted issue | Result | Matching finding IDs | Highest matched severity | Accepted | Notes |
|---|---|---|---|---|---|---|
| P01 | Reserve release inflates LTM Adjusted EBITDA | Found | X-001, SEC-011, FIN-001, FIN-008, X-002 | Critical | Critical | Exact. All figures match: 15.4, 125.6, 51.6 (-4.4%), 48.3% against 49.5%, 10.9% of EV. X-002 makes the Borealis sell-through link at 15.6 weeks. |
| P02 | Amended Borealis terms from 2027 | Found | X-004, SEC-004, SEC-005, NEWS-001 | Critical | Critical | Exact. The run sizes the cost at 23.3, against the key's 24.2 to 24.8. The run applies the 10.5% co-op to purchases after the 6.0% price cut, which the key does not. Every term, the stale 12% assumption and the November 2025 foreshadowing are found. |
| P03 | Fennimore key-person right triggered by our management plan | Found | X-010, SEC-020, LIT-009, NEWS-014, NEWS-013, SEC-046, SEC-047 | Critical | Critical | Exact. The run has the reservation of rights, the "won't be designing collections" quote, 46.5 = 36.3% of Adjusted EBITDA, and the employment end date with no non-compete. |
| P04 | FTC refund remedy of 212.5 | Found | X-008, LIT-001, SEC-028, NEWS-003, NEWS-004, X-009 | Critical | Critical | Exact. The run sized the remedy from `kpis.csv` (52.4 + 71.8 + 88.3) and labeled it an upper bound. The 10-Q "no amount" gap is recorded as X-009. |
| P05 | Inventory overstated against net realizable value | Found | X-002, SEC-016, FIN-002, NEWS-009, X-019, FIN-003, FIN-004 | High | High | Exact. 109.0 aged stock, 31% recovery, about 28% in the rumored sale, 75.2 implied loss and a 67.3 shortfall. |
| P06 | Q2 Borealis jump with channel stock and return rights | Found | X-005, FIN-005, NEWS-010, FIN-007, X-006, SEC-007, SEC-002, SEC-005 | High | High | Exact. 15.6 weeks against 8.9, the 8-week cap, a 25.6 return right against a 3.1 reserve, and 30% from 2027. |
| P07 | FCPA voluntary disclosure on payments to Meridian | Found | X-016, SEC-030, NEWS-007, SEC-031, SEC-012 | High | High | Exact. The run links the news detention to the company's own disclosure. |
| P08 | Fennimore royalty arbitration | Found | X-011, SEC-021, LIT-002, LIT-010 | High | High | Exact. The run has 11.6 plus 9%, the material-breach termination route, and the company's own Section 1.12 summary weakening its defense. |
| P09 | Stockholder suit over the founder's 32.0 fee | Found | X-013, LIT-004, NEWS-017, NEWS-019 | High | High | Exact on the suit findings. The founder's 71.8% vote, which the key folds into P09, is also a separate Critical finding in the run (X-012, "could stop the deal"). Counting X-012 as a P09 match would make this one level high (see caveats). |
| P10 | PFAS bans applied nationwide by the largest customers | Found | X-003, SEC-017, NEWS-005, NEWS-006, FIN-010 | High | High | Exact. 71.0 PFAS inventory, 31% of units, Borealis rank 1 and Summitline rank 2 (43.5% of revenue), and the 10-Q's "evaluating" wording. |
| P11 | Cedar Hollow permit | Found | X-015, NEWS-011, LIT-007, SEC-033, FIN-022, X-014 | High | High | Exact. All facts match: 7 a.m. to 7 p.m., 180 trucks against about 420, 72% of units, about 45.0 for a second site, hearing Nov 18. |
| P12 | Delaware unclaimed property audit | Found | X-018, SEC-032 | High | High | Exact. 9 to 31, no accrual, the non-escheatable position, 34.8 of breakage. |
| P13 | Dealer termination suit | Found | LIT-003, SEC-029, FIN-039, X-021 | High | High, Medium | Exact. 33.5, the motion to dismiss denied, 103 non-parties to March 2027, Summit & Spoke rank 7 (6.2 to 0.9). |
| P14 | Co-op fees booked in SG&A, not against revenue | Found | SEC-008, FIN-011 | Medium | Medium | Exact. 663.8 and 48.9%. The royalty-deduction inconsistency appears in the SEC-008 card and in open questions. The rise to 10.5% is in X-004. |
| P15 | Store fleet and leases | Found | X-020, SEC-018, FIN-019 | Medium | Medium | Exact. 13 of 46 stores, leases of 150.0 to 152.0 outside net debt, 7.8 years, and no impairment beyond two stores (framed as a dated judgment). |
| P16 | Deal costs outside the headline price | Found | X-017, SEC-044, SEC-045, SEC-041, FIN-021 | High | Medium | Within one level, not exact. RSUs of 40.8 outside the 52.0m shares, severance of 11.4 and the 18.7 break fee are all found. X-017 and SEC-044 rate the RSU and fee cost High. |
| P17 | DTC customer economics weakening | Found | FIN-018, X-007 | High | Medium | Within one level, not exact. FIN-018 is Medium, but the trend finding X-007 (High) restates the CAC rise (US$38 to US$71) and the flat 1.12m active customers. |
| P18 | Down certificate suspended and reinstated | Found | SEC-034, NEWS-008 | Low | Low | Exact. Also listed as a mitigant. |
| P19 | Planted positives and mitigants | Partly present | SEC-027, SEC-026, FIN-037, SEC-010, LIT-006, SEC-036, SEC-013, FIN-025, SEC-038 | n/a | Positive | (a) to (g) are credited in the executive summary's mitigants table. **Missing: (h).** The auditor's tenure and clean opinion appear only as SEC-052 in the "not verified" appendix list. The effective-controls conclusion is treated as a Medium concern (SEC-051), not as a positive. |

## Distractors

| ID | Distractor | Run's treatment | Too high? |
|---|---|---|---|
| D1 | Sunvale claim against Quillmark Kids LLC | SEC-036 (Low, Verified) and LIT-005 (Low). Listed as a neutralized item and mitigant, with no risk matrix row | No |
| D2 | Kids loss and strategic review add-backs | SEC-013 and FIN-025 (Low, Verified), FIN-024 (Low). Listed as items correctly excluded. FIN-027 notes "non-recurring" items in three of four periods at Low only | No |
| D3 | Stonebridge US$27 rival bid rumor | NEWS-015 (Low, rumor, denied). Not used in valuation | No |
| D4 | Quillmark Pens Ltd administration | NEWS-016 (Low, different company) | No |

## Unsupported findings

None. The four verifier runs checked 112 findings: 78 Verified, 34 Partially verified, 0 Not supported. The report cites only Verified or Partially verified findings, apart from the appendix list of Low findings marked "not verified".

## Caveats

- **One target, one run.** Plover is the first and only graded run on this target. Model output varies from run to run, so this is one sample, not a rate.
- **Some grading calls were close.**
  - **P09.** X-012 (founder control, Critical) overlaps the part of P09 about the founder's vote. It is graded as a separate issue, because its main point is the founder's economics and control, not the suit. Counted as a P09 match instead, exact-match accuracy would be 15 / 18 = 83.3%.
  - **P19.** It is graded Partly present on a strict reading of (h).
- **Findings beyond the answer key.** The run raised findings that are not planted issues. They neither help nor hurt these metrics:
  - The founder-economics finding rated Critical (X-012), where the key folds the vote into a High issue.
  - The credit agreement change-of-control default, rated High under the project's refinancing calibration (SEC-025).
  - The licence expiry in 2029 (SEC-022) and the post-go-shop timing summary (X-014), both High.
- **The answer key was written by the session that built the target.** It was not written independently of the data.
- **Blindness.** The grading session is the same session that ran the diligence. It did not see the answer key until this step.

## Three most useful improvements to the agent instructions

1. **Rate known, quantified deal costs as price items, not protections.** Equity award cash-outs, break fees and severance are fixed amounts the buyer simply pays (P16). Rate them Medium and put them in the price, unless their total passes a stated share of value. The verifier itself said Medium was defensible for the RSUs.
2. **Keep separate issues out of trend findings.** A trend X- finding should state only the trend's own headline numbers. A fact that is its own issue, such as customer acquisition cost rising while active customers stay flat, should be cited by ID rather than restated. Otherwise the component is re-rated at the trend's severity (P17).
3. **Add internal controls and the auditor to the fixed mitigant list.** The fixed list in the report template should include "internal controls conclusion and auditor tenure and opinion". When another finding puts a positive in doubt (here the FCPA payments against the controls conclusion), the report should still list it, as a qualified positive with both IDs (P19 (h)).

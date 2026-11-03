## Litigation analyst: findings

Project Avocet, iteration 1. FICTIONAL case study. Every percentage test uses enterprise value (EV) of $2,750.0m (5% = $137.5m, 10% = $275.0m).

**How the IDs work.** Finding IDs LIT-01 to LIT-08 match the case IDs in the docket index. LIT-09 to LIT-12 are separate topics taken from those matters, so each one gets its own severity.

**How reliable the sources are.** Each case file mixes three kinds of material:
- docket data: court, filing dates, rulings and next events;
- the plaintiffs' allegations;
- statements by Brindlewick and its counsel. LIT-01 says its counsel assessment comes from "Brindlewick's litigation summary provided to bidders".

I set confidence by which kind of material a fact comes from. The folder has no full docket sheets or orders. No file contains text that tries to instruct the agents.

### Files reviewed

- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/deal-brief.md (context only)
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/litigation/docket_index.csv (8 matters, LIT-01 to LIT-08)
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/litigation/LIT-01_refrigerated-warehousing-antitrust.md
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/litigation/LIT-02_okafor-wrongful-death.md
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/litigation/LIT-03_calder-valley-nuisance.md
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/litigation/LIT-04_freshArc-preference.md
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/litigation/LIT-05_coastline-seafood-spoilage.md
- /Users/sabinejoseph/Documents/Claude/M&A/Project-Falcon-handoff/falcon_m-a_due_diligence/targets/avocet/data/litigation/LIT-06_westmark-polar-ridge.md
- LIT-07 and LIT-08 have no detail file. They exist only as rows in docket_index.csv.

**Consistency check.** The amounts, statuses and next-event dates in docket_index.csv match the case files for LIT-01 to LIT-06. I found no discrepancies.

### Matter summary table

| Case ID | Case | Posture | Claimed / exposure | Next date | Severity |
|---|---|---|---|---|---|
| LIT-01 | In re Refrigerated Warehousing Services Antitrust Litigation (N.D. Cal. 3:25-cv-04417) | Motion to dismiss denied 2026-08-14; fact discovery | Expert estimate of class-wide overcharges: $600.0m single damages. Trebled and joint and several: $1,800.0m upper bound. Brindlewick's own 8% share: $48.0m single, $144.0m trebled. No accrual | Class certification motion due 2027-02-26 | Critical (LIT-01); Medium (LIT-09) |
| LIT-02 | Okafor et al. v. Brindlewick Transport LLC and Brandt (San Joaquin Sup. Ct.) | Discovery; trial date set | $150.0m Section 998 demand, not accepted. Defense counsel's range for comparable verdicts: $40.0m to $180.0m. Self-insured retention reserved (amount not stated) | Mediation 2027-03-10; trial 2027-09-13 | High (LIT-02); Medium (LIT-10) |
| LIT-03 | Calder Valley Neighbors Alliance v. Brindlewick (Riverside Sup. Ct.) | Preliminary injunction motion filed Aug 2026 | Injunction sought against truck moves from 10 p.m. to 6 a.m.: about a 35% outbound capacity cut at a site with about 4% of revenue. Damages "to be proven". Mitigation estimate $6.5m | Preliminary injunction hearing 2027-01-15 | Medium |
| LIT-04 | Delacroix (FreshArc Liquidating Trust) v. Brindlewick (Bankr. D. Del. Adv. 26-50388) | Answer due | $14.6m claimed. Counsel's "likely" recovery: $6.0m to $11.0m. No accrual | Answer due 2026-11-20 | Medium (LIT-04); Medium (LIT-11) |
| LIT-05 | Coastline Seafood Imports v. Brindlewick (Pierce County Sup. Ct.) | Partial summary judgment motion on liability limit fully briefed | $41.2m claimed. About $1.24m under the liability limit. $1.2m accrued | Summary judgment hearing 2026-12-11 | Medium (LIT-05); Medium (LIT-12) |
| LIT-06 | Westmark Grocers v. Polar Ridge Logistics and Brindlewick (Sacramento Sup. Ct.) | Discovery; Arcturus accepted the defense | $33.0m claimed. Uncapped indemnity from Arcturus. No accrual (company calls it remote) | Case management conference 2027-01-22 | Low |
| LIT-07 | Greenfield Produce v. Brindlewick (E.D. Cal. 1:23-cv-01188) | Dismissed with prejudice 2025-03-07; no appeal | $22.5m claimed; nothing outstanding | None | Low |
| LIT-08 | Brindlewick Papeterie opposition to Canadian trademark application No. 2231447 (Trademarks Opposition Board) | Evidence stage | $0.0m | Applicant's evidence due 2027-01-08 | Low |

**Exposure arithmetic (simple addition of stated amounts, not an estimate).**
- Open non-antitrust claims, excluding the indemnified LIT-06: $150.0m + $14.6m + $41.2m = $205.8m (7.5% of EV).
- Adding LIT-06's $33.0m gives $238.8m (8.7% of EV).
- Accruals stated in the case files: LIT-05 $1.2m; LIT-02 the self-insured retention (amount not found). LIT-01, LIT-04 and LIT-06 have no accrual.

### Findings

#### LIT-01: Antitrust class action: damages exposure, joint and several liability, no accrual
- **Finding:** Brindlewick is a defendant in a Sherman Act Section 1 information-exchange class action. The other defendants are six other operators and Coldmetric. The case survived a motion to dismiss on August 14, 2026.
  - Plaintiffs' economist puts class-wide overcharges at "at least $600 million before trebling".
  - The case file says defendants are jointly and severally liable for the full trebled amount, with no right of contribution. That makes $1,800.0m the upper bound against Brindlewick.
  - Brindlewick has recorded no accrual, and its counsel has given no loss estimate.
- **Evidence:**
  - 2026-08-14 (docket index row LIT-01; case file Status): "Motion to dismiss denied August 14, 2026; fact discovery open".
  - Damages section (undated; plaintiffs' expert and complaint): "class-wide overcharges of at least $600 million before trebling"; "about 8% of class purchases to Brindlewick"; "Defendants are jointly and severally liable for the full trebled amount, with no right of contribution under federal antitrust law."
  - July 2026 (Settlements to date): Northern Frost, "(about 2% of class purchases per the complaint), settled in July 2026 for $9.5 million plus cooperation, subject to court approval."
  - Counsel's assessment (undated; from the seller's litigation summary to bidders): Hartwell Brooke "considers the information-exchange theory viable after the August 14 order... The firm has not provided a loss estimate. Brindlewick has not recorded an accrual."
  - Brindlewick "subscribed to Coldmetric from 2018 until Coldmetric suspended its rate reports in March 2025". That covers the whole alleged class period from 2019.
  - Recomputed figures:

    | Measure | Calculation | Amount | % of EV |
    |---|---|---|---|
    | Upper bound | $600.0m x 3 | $1,800.0m | 65.5% |
    | Class-wide single damages | | $600.0m | 21.8% |
    | Brindlewick share, single | 8% x $600.0m | $48.0m | 1.7% |
    | Brindlewick share, trebled | $48.0m x 3 | $144.0m | 5.2% |

  - Northern Frost benchmark: 2% x $600.0m = $12.0m single, or $36.0m trebled. Its $9.5m settlement is 79.2% of its single share and 26.4% of its trebled share. Scaled linearly to an 8% share, that suggests about $38.0m (1.4% of EV) (projection). That settlement came before the August 14 ruling and included cooperation, so it may not be a guide to settlement values after the ruling.
- **Posture and trend:** The case has moved against Brindlewick:
  - the motion to dismiss was denied (2026-08-14);
  - a co-defendant settled with a cooperation obligation (July 2026), which could give plaintiffs evidence (inference);
  - counsel now calls the theory "viable".

  The class certification motion is due 2027-02-26. That is after expected signing (December 2026) and before expected closing (Q2 to Q3 2027). Counsel expects certification to be contested on damages method. No ruling date is set.
- **Insurance:** not found in litigation records.
- **Severity:** Critical.
  - Test met: more than 10% of value. The claimant seeks treble damages, and the case file says defendants are jointly and severally liable for the full trebled amount. That gives an upper bound of $1,800.0m, or 65.5% of the $2,750.0m EV. Even untrebled class-wide damages of $600.0m are 21.8%.
  - This is an upper bound, not a forecast. No source shows the remedy is unlikely, and Brindlewick's own counsel calls the theory viable.
  - Narrower reference points: the own-share trebled figure is $144.0m (5.2%), and the settlement benchmark is about $38.0m (projection).
- **Confidence:** Medium.
  - The ruling, the relief sought and the accrual status are stated directly in the record and case file.
  - The $600.0m and 8% figures are plaintiffs' expert and pleading allegations. The court has not tested them.
  - The joint and several statement is the case file's description of the law. Counsel should confirm it.
- **Deal impact:**
  - **Valuation:** none of this is reflected in the $2,750.0m EV, because there is no accrual.
  - **Structure (flag for counsel):** in a one-step cash merger of a public company, a seller indemnity or escrow after closing is not a usual tool. Protection would probably come through price, a litigation analysis before signing, interim covenants giving Trelliswood consent over any settlement, and how the matter is treated in the MAE definition.
  - **Disclosure:** see cross-check.
- **Cross-check:**
  - **SEC filings:** do the FY2025 10-K and the Q1 and Q2 2026 10-Qs describe the case, the July 2026 Northern Frost settlement, and an estimate of reasonably possible loss (or say that one cannot be made)? The deal brief cites a Q2 10-Q cover date of July 31, 2026, which may predate the August 14 ruling. Check whether any later filing, an 8-K, or the September 22, 2026 strategic review announcement disclosed the ruling.
  - **News:** coverage of the order, of Coldmetric, and of any other settlements.
  - **Financials:** confirm there is no accrual.
- **Source:** `targets/avocet/data/litigation/LIT-01_refrigerated-warehousing-antitrust.md`, docket entries 2026-08-14 (Status) and July 2026 (Settlements to date); `targets/avocet/data/litigation/docket_index.csv`, row LIT-01.

#### LIT-09: Antitrust class action: effect on the merger review, injunction, and Trelliswood's own status
- **Finding:** The same case seeks an injunction. It alleges that operators coordinated prices through a rate-sharing service that reported "rates by market and customer-size band".
  - The case may draw the reviewing agency's attention to coordination in the Puget Sound and Northern Central Valley overlap markets (inference).
  - The litigation records do not say whether Trelliswood is one of the six unnamed operator defendants or was a Coldmetric subscriber.
  - The records contain no market definition and no local market-share findings.
- **Evidence:**
  - Case file table: "Relief sought | Treble damages, injunction, attorneys' fees"; "Defendants | Brindlewick Cold Chain, Inc.; six other refrigerated warehouse operators; Coldmetric Analytics LLC"; plaintiffs are "direct purchasers of refrigerated warehousing services in the United States, 2019 to present".
  - Allegations: "received weekly reports showing rates by market and customer-size band"; "internal emails in which pricing managers at two defendants refer to 'holding the Coldmetric line.'" The file does not name the two defendants.
  - The only share figure is national: about 8% of class purchases (complaint allegation).
- **Non-monetary risk:**
  - An injunction or a court-approved settlement could restrict pricing practices that bind the combined company after closing (inference).
  - The class is direct purchasers of refrigerated warehousing, so it includes Brindlewick's own customers (inference). The case and any settlement therefore touch customer relationships.
- **Timing:** the HSR filing is due within 15 business days of signing (December 2026, per the deal brief). The class certification motion (2027-02-26) falls inside the expected review period.
- **Severity:** Medium. The link to closing risk rests on inference. It would rise sharply in either of two cases: Trelliswood is a co-defendant or Coldmetric subscriber, or Brindlewick is one of the two defendants named in the "Coldmetric line" emails.
- **Confidence:** Medium. The relief sought and the defendant list are in the case record. The link to the merger review is inference.
- **Deal impact:**
  - Closing risk: antitrust review time against the 12-month outside date, plus one 3-month extension.
  - Post-closing: limits on pricing conduct.
- **Cross-check:** Trelliswood's own legal team (defendant or subscriber status). SEC filings: risk factors on antitrust. News: any agency interest in Coldmetric. A government investigation is not found in litigation records.
- **Source:** `targets/avocet/data/litigation/LIT-01_refrigerated-warehousing-antitrust.md`, case table and Allegations (case filed 2025-06-12; consolidated amended complaint 2025-11-03).

#### LIT-02: Okafor wrongful death: $150.0m demand, defense counsel's adverse view on liability, insurance unconfirmed
- **Finding:** A February 3, 2025 crash involving a Brindlewick Transport tractor-trailer killed three people and seriously injured two.
  - Plaintiffs served a $150.0m statutory offer to compromise, which was not accepted.
  - Defense counsel's preliminary view is that liability "will be difficult to contest if the log edit is admitted". Counsel puts comparable California verdicts at about $40m to $180m.
  - The reserve covers only the self-insured retention, whose amount is not stated. Excess insurers have been notified, but the excess limits and their coverage position are not found in litigation records.
- **Evidence:**
  - Filed 2026-04-17.
  - 2026-04-20: "$150.0 million statutory offer to compromise (Cal. Code Civ. Proc. Section 998), served April 20, 2026 and not accepted".
  - Defense position (undated): "liability will be difficult to contest if the log edit is admitted, and that verdicts in comparable multi-fatality trucking cases in California have ranged from about $40 million to $180 million."
  - Reserve: "Brindlewick has reserved its self-insured retention for this occurrence. It has notified its excess insurers."
  - Next events: mediation 2027-03-10, trial 2027-09-13.
- **Exposure (recomputed):** the $150.0m demand is 5.5% of EV. Counsel's range of $40.0m to $180.0m is 1.5% to 6.5% of EV. None of these reaches the 10% test.
  - Punitive damages: the case file's list of claims does not include them (wrongful death, survival, negligence, negligent hiring/supervision/retention, spoliation). A punitive claim is not found in litigation records.
  - Whether one could be added on the alleged log edit, and whether it would be insurable, is a question for counsel.
  - Claims from the other vehicles in the seven-vehicle crash: not found in litigation records.
- **Trend:** against Brindlewick. The defense's own counsel holds the adverse view, the Section 998 offer was not accepted (which may bring cost consequences; ask counsel), and a trial date is set. There are no rulings in the record.
- **Severity:** High. It is below the 10% test even at the top of counsel's range ($180.0m, 6.5%). But it is material, and it needs specific protection:
  - verification of the insurance tower;
  - a price adjustment, or another protection, for any amount above coverage;
  - Trelliswood's consent rights over settlement before the March 10, 2027 mediation.
- **Confidence:** Medium. The dates, the demand and the reserve statement are in the case record. The liability facts are allegations. The verdict range is counsel's view.
- **Deal impact:**
  - Valuation: any uninsured amount.
  - Post-closing: the trial date (2027-09-13) may fall after closing in Q2 to Q3 2027, so Trelliswood would own the trial and the publicity.
  - Disclosure: see cross-check.
- **Cross-check:**
  - SEC filings: was the crash (2025-02-03) disclosed in the FY2025 10-K? Were the suit and the $150.0m demand (April 2026) disclosed in the Q1 2026 10-Q? What does the insurance program description say?
  - News: crash coverage and the California Highway Patrol report.
  - Financials: the amount of the self-insured retention accrual.
- **Source:** `targets/avocet/data/litigation/LIT-02_okafor-wrongful-death.md`, docket entries 2026-04-17 (filed) and 2026-04-20 (Section 998 offer), Defense position and Reserve sections; `targets/avocet/data/litigation/docket_index.csv`, row LIT-02.

#### LIT-10: Fleet safety and record-keeping allegations from Okafor
- **Finding:** Plaintiffs make four allegations about Brindlewick Transport's safety controls. Brindlewick contests each one. They bear on the fleet Trelliswood plans to merge into its own.
  - the driver was on duty 15.5 hours, beyond the federal 14-hour limit;
  - the driver-facing camera recorded 11 fatigue or distraction events in the 14 days before the crash, and no one reviewed them;
  - a dispatcher edited the electronic logging records on February 4, 2025, the day after the crash;
  - accident frequency has risen each year since 2023.
- **Evidence:**
  - Facts alleged: "the driver had been on duty for 15.5 hours, beyond the federal 14-hour limit"; "a Brindlewick dispatcher edited the driver's electronic logging records on February 4, 2025, after the crash"; "Brindlewick's accident frequency had risen each year since 2023."
  - Defense: "the electronic logging edit corrected a duty-status error and was annotated as such, and that the camera alerts were reviewed under its standard coaching policy".
  - The California Highway Patrol report "cites speed unsafe for conditions".
- **Severity:** Medium. It needs compliance diligence and an integration plan before the fleets are combined under Trelliswood's safety and dispatch programs. The allegations are untested.
- **Confidence:** Low. These are allegations in a pleading that the defense disputes.
- **Deal impact:**
  - Post-closing integration.
  - Possible regulatory exposure: FMCSA safety rating and audits are not found in litigation records.
  - Insurance cost and reputational risk (inference).
- **Cross-check:** News: the crash and any FMCSA data. SEC filings: safety metrics. Financials: the trend in insurance and claims expense.
- **Source:** `targets/avocet/data/litigation/LIT-02_okafor-wrongful-death.md`, Facts alleged (crash 2025-02-03; edit 2025-02-04) and Defense position.

#### LIT-03: Calder Valley nuisance: risk of an injunction on night operations
- **Finding:** Neighbors seek preliminary and permanent injunctions barring truck arrivals and departures from 10 p.m. to 6 a.m. at the Calder Valley distribution center. The site has about 4% of Brindlewick's LTM revenue.
  - Brindlewick's operations team estimates the injunction would cut outbound capacity by about 35% until a second dock bank is built.
  - The preliminary injunction hearing is January 15, 2027, between signing and closing.
  - The plaintiffs' counsel signaled a narrower settlement in October 2026.
- **Evidence:**
  - Relief sought: "Preliminary and permanent injunction prohibiting truck arrivals and departures between 10:00 p.m. and 6:00 a.m.; damages to be proven".
  - Preliminary injunction motion filed August 2026; hearing 2027-01-15.
  - Site background: "contributed about 4% of Brindlewick's revenue in the twelve months ended June 30, 2026".
  - Capacity estimate: "would reduce the site's outbound capacity by about 35% until a second dock bank is built".
  - October 2026: "the Alliance's counsel indicated it would accept an 11:00 p.m. to 5:00 a.m. restriction plus the sound wall."
  - Mitigation estimate: "$6.5 million".
- **Exposure:** if revenue fell in line with capacity, about 1.4% of Brindlewick revenue would be at risk (4% x 35%) until the dock bank is built (projection).
  - The cost and timing of the dock bank are not found. The capacity effect of the narrower 11 p.m. to 5 a.m. window is not found.
  - The $6.5m mitigation estimate is 0.2% of EV. Damages are unquantified. Insurance is not found.
- **Mitigants:**
  - The county's 2023 land use approval "permits 24-hour operation".
  - The noise evidence is not comparable. Plaintiffs measured night-time peaks of 61 to 68 dBA at the nearest homes. Brindlewick measured an hourly average of 53 dBA at the property line. The permit limit is 55 dBA at night at the property line. Because the readings use different metrics and locations, they do not settle compliance (inference).
- **Trend:** mixed. The case escalated with the August 2026 preliminary injunction motion, and de-escalated with the October 2026 settlement signal.
- **Severity:** Medium. The site is a small share of revenue, and a settlement path with a stated cost is visible.
- **Confidence:** Medium. The posture and dates are in the record. The capacity effect is a company estimate. The settlement signal is a communication from counsel.
- **Deal impact:**
  - Post-closing operations: the site is ground-leased.
  - Interim covenant: settlement authority before closing.
  - The site is not in the Puget Sound or Northern Central Valley overlap markets, and it is not one of the four leases in the consolidation plan (per the deal brief).
- **Cross-check:** SEC filings: disclosure of the case (filed 2025-12-04, after the FY2025 year end) and of the preliminary injunction motion. Financials: the site's revenue and EBITDA. News: local coverage.
- **Source:** `targets/avocet/data/litigation/LIT-03_calder-valley-nuisance.md`, docket entries 2025-12-04 (filed), August 2026 (preliminary injunction motion) and 2027-01-15 (hearing), Exposure section.

#### LIT-04: FreshArc preference claim: $14.6m claimed, counsel's "likely" $6.0m to $11.0m, no accrual
- **Finding:** FreshArc's liquidating trustee seeks to recover 41 payments totaling $14.6m made in the 90 days before FreshArc's January 12, 2026 petition. Brindlewick's counsel estimates a "likely recovery" by the trustee of $6m to $11m, yet Brindlewick has recorded no accrual.
  - Counsel's use of "likely" together with a stated range suggests the ASC 450 tests (probable and estimable) may be met (inference, for accounting review).
  - On that reading, the low end of the range, $6.0m, would be a minimum accrual (inference).
- **Evidence:**
  - Adversary proceeding filed 2026-09-08. Answer due 2026-11-20.
  - "41 payments totaling $14.6 million that FreshArc made to Brindlewick between October 14, 2025 and January 12, 2026".
  - "Brindlewick's counsel estimates a likely recovery by the trustee of $6 million to $11 million if the case is not settled. Brindlewick has not recorded an accrual."
- **Defenses:**
  - The ordinary-course defense is weakened. Payment timing moved to 58 to 71 days after invoice, against 32 to 40 days before, after Brindlewick placed FreshArc on credit hold in October 2025.
  - The new-value defense covers about $3.9m. If established, it leaves $14.6m - $3.9m = $10.7m, close to the top of counsel's range.
  - A warehouse lien argument is "being evaluated".
- **Periods affected:** the payments fall in Q4 2025 and early Q1 2026. The petition date is after the FY2025 year end. The adversary proceeding was filed in Q3 2026. The date of counsel's estimate is not found, so which reported period should carry an accrual is unclear.
- **Scheduling note:** the answer deadline (2026-11-20) is the same day binding proposals are due. This is timing only, and no link is suggested.
- **Severity:** Medium. The amount is small relative to value: $14.6m is 0.5% of EV, and $6.0m to $11.0m is 0.2% to 0.4%. The issue is the accrual judgment, which needs follow-up.
- **Confidence:** High for the claim amount, the dates and the accrual status, which are stated in the record and case file. Medium for counsel's range. The ASC 450 reading is inference.
- **Deal impact:** a small value item; an accounting and disclosure question.
- **Cross-check:** SEC filings: is the FreshArc bankruptcy or preference exposure mentioned in the FY2025 10-K (as a subsequent event), the Q1 and Q2 2026 10-Qs, or the Q3 2026 10-Q? Is there any accrual? Financials: whether a reserve sits elsewhere.
- **Source:** `targets/avocet/data/litigation/LIT-04_freshArc-preference.md`, docket entries 2026-01-12 (petition), 2026-09-08 (adversary filed) and 2026-11-20 (answer due), Defenses section; `targets/avocet/data/litigation/docket_index.csv`, row LIT-04.

#### LIT-11: FreshArc: loss of the tenth-largest customer and $3.9m of unpaid services
- **Finding:** FreshArc was Brindlewick's tenth-largest customer in 2025, with $31.8m of revenue, and ceased operations in March 2026.
  - The LTM June 30, 2026 earnings base the deal is priced on includes some FreshArc revenue that will not recur (inference).
  - Brindlewick also provided about $3.9m of services that were never paid for.
- **Evidence:** "It was Brindlewick's tenth-largest customer in 2025, with revenue of $31.8 million. FreshArc's operations ceased in March 2026." Also: "Brindlewick provided about $3.9 million of storage and transportation services after receiving preference-period payments, for which it was not paid."
- **Not found in litigation records:**
  - FreshArc's revenue and margin within the LTM period;
  - whether the $3.9m was written off, reserved, or added back in Adjusted EBITDA.
- **Severity:** Medium. It bears on IC question 1 (the earnings base) and needs the financial analyst's follow-up.
- **Confidence:** High for the stated facts in the case file. Medium for the earnings-base implication.
- **Deal impact:** valuation, through the earnings base.
- **Cross-check:** `financials/revenue_by_customer.csv` (FreshArc's rank and its revenue in the LTM period); bad-debt expense in FY2025 and H1 2026; the Adjusted EBITDA add-backs.
- **Source:** `targets/avocet/data/litigation/LIT-04_freshArc-preference.md`, Background and Defenses sections.

#### LIT-05: Coastline Seafood spoilage: $41.2m claimed against an about $1.24m contractual limit; summary judgment hearing December 11, 2026
- **Finding:** Coastline claims $41.2m for frozen product lost when a freezer failed on February 8, 2026. Brindlewick's warehouse receipt terms limit liability to $0.50 per pound, which gives about $1.24m, and Brindlewick has accrued $1.2m. Coastline argues that gross negligence voids the limit. Counsel considers the limit enforceable and the gross negligence theory weak.
- **Evidence:**
  - Filed 2026-05-27.
  - "Amount claimed | $41.2 million (market value of product $27.8 million, lost profits and customer penalties $13.4 million)".
  - Section 11 of the warehouse receipt terms limits liability "to $0.50 per pound unless the depositor declares a higher value in writing"; Coastline "never declared a higher value or paid the charge".
  - "Applying the limitation, Brindlewick's liability would be about $1.24 million (2.48 million pounds × $0.50). Brindlewick has accrued $1.2 million."
  - The motion is fully briefed. Hearing 2026-12-11.
- **Recomputed figures:**
  - $27.8m + $13.4m = $41.2m (1.5% of EV).
  - 2.48m lb x $0.50 = $1.24m.
  - If the limit fails, the unaccrued exposure is $41.2m - $1.2m = $40.0m (1.5% of EV).
- **Other facts:** Coastline's cargo insurer has paid the product loss and is pursuing that portion of the claim by subrogation. Brindlewick's own warehouse legal liability insurance is not found in litigation records.
- **Trend:** neutral. No ruling yet. Counsel's view favors Brindlewick. The ruling may come before signing in December 2026.
- **Severity:** Medium. Below 10% of value even with no limit, and below 2%.
- **Confidence:** High for the contract term, the amounts and the accrual, which are stated in the case file. Low for the gross negligence theory, which is an allegation.
- **Deal impact:**
  - Get the summary judgment ruling before signing.
  - Customer relationship with Coastline (current status not found).
  - Disclosure.
- **Cross-check:** SEC filings: the incident (2026-02-08, Q1 2026), the suit and the $1.2m accrual (Q2 2026 10-Q). News: coverage of the Sandhaven 2 incident. Financials: Coastline's revenue rank.
- **Source:** `targets/avocet/data/litigation/LIT-05_coastline-seafood-spoilage.md`, docket entries 2026-05-27 (filed) and 2026-12-11 (hearing), Limitation of liability section; `targets/avocet/data/litigation/docket_index.csv`, row LIT-05.

#### LIT-12: Sandhaven 2 freezer failure: both the main and the standby compressor failed
- **Finding:** Both the main and the standby compressor failed during a power disturbance. Room temperature rose from -10°F to about 28°F over 19 hours, and about 2.48 million pounds of product were declared unfit.
  - This is a failure of temperature control and of redundancy at one facility.
  - Brindlewick's main defense evidence is a maintenance record: the standby unit was serviced in December 2025.
  - No other temperature excursions are found in litigation records.
- **Evidence:** "a compressor and its standby unit in the freezer at Sandhaven 2 failed during a power disturbance. Room temperature rose from −10°F to about 28°F over 19 hours before the system was restored." Also: "Brindlewick's maintenance records show the standby unit was serviced in December 2025."
- **Severity:** Medium. It needs operational follow-up: backup power, redundancy testing, and the history of excursions across the network. It also needs an integration plan.
- **Confidence:** Medium. The incident is stated in the case file. No root-cause analysis is found.
- **Deal impact:**
  - Post-closing: capex for redundancy and backup power (inference).
  - Customer and reputational risk.
  - The deal brief says Trelliswood will halt Brindlewick's ColdTrack rollout. Whether ColdTrack involves temperature monitoring is not found in litigation records. Ask management.
- **Cross-check:** News: other spoilage incidents. SEC filings: operational risk factors. Management: incident log and root-cause report.
- **Source:** `targets/avocet/data/litigation/LIT-05_coastline-seafood-spoilage.md`, Facts section (incident 2026-02-08).

#### LIT-06: Westmark / Polar Ridge alter ego claim: neutralized by an uncapped, accepted indemnity (mitigant)
- **Finding:** Westmark claims $33.0m (1.2% of EV) for Polar Ridge's alleged service failures in 2022 and 2023. It seeks to hold Brindlewick liable as Polar Ridge's former parent.
  - Under the 2023 purchase agreement, Arcturus assumed all of Polar Ridge's liabilities and indemnifies Brindlewick, with no cap or deductible for assumed liabilities.
  - Arcturus accepted the tender in writing without reservation of rights and is defending both defendants.
  - Arcturus had about $4.1bn of revenue in 2025 and is rated BBB by two agencies.
  - This is a mitigant: a contract shifts the risk to a counterparty.
- **Evidence:**
  - Filed 2025-10-02. Tender made 2025-10-20.
  - 2025-11-06: "Arcturus accepted the tender in writing on November 6, 2025, without reservation of rights".
  - Section 9.2: "without a cap or deductible for assumed liabilities".
  - "Brindlewick considers its net exposure remote and has not recorded an accrual."
  - Case management conference 2027-01-22.
- **Severity:** Low (neutralized risk, mitigant). The remaining risk is Arcturus's credit.
- **Confidence:** Medium. The indemnity terms and the acceptance are stated in the case file. The purchase agreement and the acceptance letter themselves are not in the folder.
- **Deal impact:** none expected while the indemnity is honored. Confirm the documents.
- **Cross-check:** SEC filings: how the FY2025 10-K describes the matter and the indemnity. Management: copies of Section 9.2 of the purchase agreement and the November 6, 2025 letter. Financials: is Westmark a customer?
- **Source:** `targets/avocet/data/litigation/LIT-06_westmark-polar-ridge.md`, docket entries 2025-10-02, 2025-10-20 and 2025-11-06, Indemnity section.

#### LIT-07: Greenfield Produce breach of contract: dismissed with prejudice, closed (mitigant)
- **Finding:** A $22.5m breach of contract claim (0.8% of EV) was dismissed with prejudice on March 7, 2025, with no appeal. The matter is closed. No detail file exists.
- **Evidence:** docket_index.csv row LIT-07: "Dismissed with prejudice 2025-03-07; no appeal,22.5,None".
- **Severity:** Low (closed; mitigant).
- **Confidence:** High. Stated in the docket index.
- **Deal impact:** none. Confirm there are no fee or cost awards and no related claims (not found in litigation records).
- **Cross-check:** Financials: is Greenfield Produce a customer?
- **Source:** `targets/avocet/data/litigation/docket_index.csv`, row LIT-07 (filed 2023-08-15; dismissed 2025-03-07).

#### LIT-08: Canadian trademark opposition by Brindlewick Papeterie
- **Finding:** Brindlewick Papeterie Inc. opposes Brindlewick Cold Chain's Canadian trademark application No. 2231447. No money is claimed. The case is at the evidence stage, and Brindlewick's evidence as applicant is due January 8, 2027.
- **Evidence:** docket_index.csv row LIT-08: "Evidence stage,0.0,Applicant's evidence due,2027-01-08".
- **Severity:** Low.
- **Confidence:** High. Stated in the docket index.
- **Deal impact:** minimal. It matters only if Brindlewick plans to use the brand in Canada. The deal brief places its operations in WA, OR, CA and ID.
- **Cross-check:** Management: purpose of the Canadian filing.
- **Source:** `targets/avocet/data/litigation/docket_index.csv`, row LIT-08 (filed 2026-02-10).

### Matters reviewed with low relevance

- **LIT-06** Westmark / Polar Ridge: $33.0m claimed, risk neutralized by an uncapped indemnity that Arcturus accepted on 2025-11-06. Low; a mitigant.
- **LIT-07** Greenfield Produce: $22.5m claim dismissed with prejudice on 2025-03-07, with no appeal. Low; closed.
- **LIT-08** Canadian trademark opposition: no money claimed; evidence due 2027-01-08. Low.

### Gaps and questions for management or outside counsel

**Dates and accruals to compare with the SEC filings**

| Matter | Key dates | Accrual per the case file | Filings to check |
|---|---|---|---|
| LIT-01 | Coldmetric suspended its reports Mar 2025; case filed 2025-06-12; amended complaint 2025-11-03; Northern Frost settled Jul 2026; motion to dismiss denied 2026-08-14; class certification motion due 2027-02-26 | None; no loss estimate | FY2025 10-K; Q1 and Q2 2026 10-Qs (Q2 cover dated 2026-07-31); any 8-K after 2026-08-14 |
| LIT-02 | Crash 2025-02-03; log edit 2025-02-04; suit filed 2026-04-17; Section 998 offer 2026-04-20; mediation 2027-03-10; trial 2027-09-13 | Self-insured retention reserved (amount not found) | FY2025 10-K (crash); Q1 2026 10-Q (suit and demand) |
| LIT-03 | Land use approval 2023; site opened Jun 2025; suit filed 2025-12-04; injunction motion Aug 2026; settlement signal Oct 2026; hearing 2027-01-15 | Not stated | FY2025 10-K; Q3 2026 10-Q |
| LIT-04 | Payments 2025-10-14 to 2026-01-12; credit hold Oct 2025; petition 2026-01-12; FreshArc ceased Mar 2026; plan confirmed Jun 2026; adversary filed 2026-09-08; answer due 2026-11-20 | None, despite counsel's "likely" $6m to $11m | FY2025 10-K (subsequent events); Q1, Q2 and Q3 2026 10-Qs |
| LIT-05 | Standby unit serviced Dec 2025; incident 2026-02-08; suit filed 2026-05-27; hearing 2026-12-11 | $1.2m | Q1 2026 10-Q (incident); Q2 2026 10-Q (suit and accrual) |
| LIT-06 | Polar Ridge sold 2023-06-30; suit filed 2025-10-02; tender 2025-10-20; accepted 2025-11-06; conference 2027-01-22 | None (remote) | FY2025 10-K |
| LIT-07 | Filed 2023-08-15; dismissed 2025-03-07 | Not applicable | None |
| LIT-08 | Filed 2026-02-10; evidence due 2027-01-08 | Not applicable | None |

**Questions**

1. **Priority.** Is Trelliswood or any affiliate one of the six unnamed operator defendants in LIT-01, or a former Coldmetric subscriber? Not found in litigation records.
2. Is Brindlewick one of the "two defendants" whose pricing managers wrote about "holding the Coldmetric line"?
3. LIT-01 questions for counsel:
   - a loss estimate or range;
   - how the Northern Frost settlement and any others affect Brindlewick's joint and several exposure;
   - whether defendants have a judgment-sharing agreement;
   - whether settlement talks are under way;
   - whether any DOJ or FTC inquiry exists (not found in litigation records).
4. LIT-02 insurance tower: the self-insured retention amount, the excess layers and carriers, and the carriers' coverage positions or reservations of rights. Also: is a punitive damages claim pleaded or planned? Are there claims from other vehicles in the crash? What are the consequences of not accepting the Section 998 offer?
5. LIT-10 fleet safety:
   - the internal investigation of the February 4, 2025 log edit;
   - the driver's employment status;
   - FMCSA safety rating and compliance reviews;
   - accident frequency data for 2023 to 2026.
6. LIT-03 Calder Valley:
   - the capacity effect of the 11 p.m. to 5 a.m. settlement window;
   - the cost and timing of a second dock bank;
   - the site's revenue and EBITDA;
   - the ground lease terms;
   - any county enforcement on noise.
7. LIT-04 FreshArc: why there is no accrual given counsel's "likely" $6m to $11m; the date of that estimate; settlement talks.
8. LIT-11: FreshArc revenue within the LTM period, and how the $3.9m of unpaid services was treated in the accounts and in Adjusted EBITDA.
9. LIT-05 and LIT-12:
   - did other depositors' goods sit in the Sandhaven 2 room, and have they made claims?
   - backup power and redundancy across the network;
   - the history of temperature excursions;
   - Brindlewick's own warehouse legal liability insurance;
   - whether Coastline remains a customer;
   - what ColdTrack does.
10. LIT-06: copies of Section 9.2 of the 2023 purchase agreement and Arcturus's acceptance letter of November 6, 2025.
11. **Named parties for the lead to look up in `financials/revenue_by_customer.csv`:** FreshArc Distributors (the case file says tenth-largest in 2025, $31.8m), Coastline Seafood Imports, Westmark Grocers, Greenfield Produce, Arcturus Freight Holdings, Polar Ridge Logistics, Northern Frost Storage, Coldmetric Analytics.
12. **Source limit:** the folder has case-file summaries and the docket index, not full docket sheets or orders. The text of the August 14, 2026 order, for example, is not available.

This is not legal advice. All items are flagged for outside counsel.

# Issue #409 — MDR legacy-device operative-eligibility replay v0.1

Status: **RETIRED_UNEXECUTED — accessible product publicly claims the full Article-120 condition job**

Date: 2026-09-26

## Retirement note

Before execution, #409 located a self-serve medical-device compliance platform publicly claiming per-device Article 120 transition-condition tracking, including no-significant-change, application, QMS and surveillance state.

The spreadsheet/checklist baseline was therefore no longer the strongest realistic lean-team comparator.

Canonical correction:

> `docs/discovery/issue409-mdr-accessible-incumbent-correction-2026-09-26.md`

This replay remains as a frozen future **product-capability test workload**, but must not be interpreted as an executed Candidate-B comparison.

---

## Purpose

Test the surviving Candidate-B residual:

> can a lean manufacturer maintain a correct operative conclusion about whether one MDR legacy
> device may continue to be placed on the market when that conclusion depends on several legal,
> internal-process and live external-state owners?

This is a structural internal proxy.

It does not establish real-user time savings, willingness to pay or software demand.

## Why this is not #407 again

#407 gave the baseline generic source-monitoring capability and found the richer historical Core
unnecessary.

This replay instead tests **legal-state composition after monitoring has already done its job**.

The baseline receives official guidance, EUDAMED/point-tool state, retained notes and general AI.

Candidate B gets no credit for:

- discovering that a source changed;
- monitoring a certificate;
- storing a document;
- producing a nicer table.

It gets credit only if explicit maintained condition state materially reduces reconstruction or
prevents a wrong operative eligibility conclusion.

## Frozen manufacturer/device archetype

This is a stipulated proxy, not a real customer.

Manufacturer:

- EU-established SME manufacturer;
- lean regulatory/quality team;
- uses official Commission/MDCG guidance;
- can use affordable EUDAMED preparation/monitoring tools;
- does not operate an enterprise regulatory-intelligence platform.

Device:

- reusable **Class IIa** medical device;
- valid MDD certificate / legacy-device status before the applicable cut-off;
- no MDR certificate yet;
- not custom-made;
- no exceptional Article 59/97 derogation path;
- no change in intended purpose unless an event explicitly says otherwise.

Why Class IIa:

> official MDR transition guidance places Class IIa legacy devices, when Article 120 conditions
> are satisfied, in the transition ending **31 December 2028**.

Official source:

- MDCG 2020-3 Rev.1 / Commission MDR transition Q&A.

## Frozen starting condition — 27 September 2024

At the start, stipulate that the manufacturer can evidence:

- continued MDD compliance;
- no significant design/intended-purpose change;
- no unacceptable health/safety risk;
- MDR-compliant QMS in place by 26 May 2024;
- formal MDR conformity-assessment application lodged by 26 May 2024;
- written agreement with MDR notified body **NB-A** signed by 26 September 2024;
- relevant surveillance arrangements are in place.

Therefore the pre-replay answer key is:

> **ELIGIBLE_FOR_EXTENDED_TRANSITION — through 31 December 2028, while all Article 120(3c)
> conditions continue to be met.**

## Frozen authoritative owners

The workflow must keep distinct:

1. **MDR Article 120 / Regulation 2023/607**
   - legal condition set and outer transition endpoint;
2. **Commission / MDCG transition guidance**
   - interpretation of application/agreement/transfer conditions;
3. **manufacturer internal evidence**
   - QMS, application, no-significant-change/risk state;
4. **notified-body contractual state**
   - written agreement / transfer / termination;
5. **EUDAMED / notified-body certificate state**
   - actor/device/certificate public state where applicable;
6. **time**
   - deadline/event chronology.

No source owner is assumed to contain the whole conclusion.

## Frozen event sequence

### E0 — 27 September 2024 — valid transition baseline

All starting conditions above are satisfied.

Question:

> May the Class IIa legacy device continue to be placed on the market, and until when?

Expected:

> **YES — transition endpoint 31 December 2028, conditional on continuing satisfaction of
> Article 120(3c).**

### E1 — 28 May 2026 — EUDAMED modules become mandatory

External official event:

> Actor, UDI/Devices, Notified Bodies & Certificates and Market Surveillance modules become
> mandatory.

Question:

> Does this event itself terminate the device's extended transition eligibility?

Expected:

> **NO.** It changes applicable registration/operational obligations, but it does not by itself
> negate the already-satisfied Article 120 transition conditions.

This is a negative control against treating every monitored regulatory event as an eligibility
change.

Official owner:

- Commission EUDAMED functionality/mandatory-use notice.

### E2 — 15 June 2026 — notified-body agreement transfer

Stipulated actor event:

> Manufacturer and NB-A terminate their written agreement, **simultaneously** the manufacturer
> enters a written agreement with MDR-designated NB-B, and the application is transferred to NB-B.

All other Article 120 conditions remain satisfied.

Question:

> Does transition eligibility continue?

Expected:

> **YES.** Commission Q&A states that simultaneous transfer to another notified body can preserve
> the Article 120(3c)(e) condition when the other conditions remain met.

Required maintenance:

- update notified-body owner;
- preserve transition endpoint;
- preserve evidence of transfer;
- do not incorrectly reset the legal transition clock.

### E3 — 1 August 2026 — written agreement terminates without replacement

Stipulated actor event:

> The NB-B written agreement is terminated. No simultaneous replacement notified-body agreement
> or application transfer exists.

Question:

> Can the manufacturer still rely on the extended transition to place this legacy device on the
> market?

Expected:

> **NO.** Commission Q&A states that after the relevant deadlines, withdrawal of the application
> or termination of the written agreement means Article 120(3c)(e) is no longer met and the
> transitional period ceases to apply.

This is the principal positive state-transition test.

### E4 — 15 August 2026 — certificate-monitor alert only

Stipulated control event:

> An affordable registry/certificate-monitoring tool reports the latest public certificate/NB
> record but has no knowledge of a replacement written agreement because none exists.

Question:

> Is certificate/registry monitoring alone sufficient to restore the transition conclusion?

Expected:

> **NO.** Monitoring provides one owner; the legal conclusion still depends on the absent
> Article 120 condition. No new eligible state is inferred.

This explicitly gives the accessible point tool full credit without treating it as a legal
eligibility engine.

### E5 — historical query

On 15 August 2026 ask:

> Was the device eligible to be placed on the market on 1 July 2026?

Expected:

> **YES**, because E2 preserved transition eligibility and E3 had not yet occurred.

Also ask:

> Is it eligible on 15 August 2026?

Expected:

> **NO**, based on E3.

This tests historical/current separation rather than only present-state monitoring.

## Strong lean baseline

The baseline is allowed to maintain whatever ordinary artifact it naturally wants.

It receives:

- current official MDR/MDCG transition guidance;
- official EUDAMED public information;
- a low-cost certificate/EUDAMED monitoring capability;
- manufacturer internal QMS/application/agreement records;
- ordinary spreadsheet/checklist/notes;
- browser/search;
- capable general source-grounded AI;
- retained prior answers and links.

The baseline may create a condition checklist if that is the natural solution.

Do not force it to repeatedly reconstruct from zero.

## Candidate-B treatment

Candidate B may maintain only this minimal **operative-condition ledger**:

- `condition`;
- `status`: `SATISFIED | NOT_SATISFIED | UNRESOLVED | NOT_APPLICABLE`;
- `evidence_owner`;
- `evidence_ref`;
- `governing_event_or_date`;
- `last_changed`;
- `next_check` if known.

Plus one derived output:

- `operative_eligibility`: `YES | NO | UNRESOLVED`;
- `valid_at`;
- `outer_transition_endpoint`;
- `blocking_condition` if any.

This is a provisional test artifact, **not a new canonical schema**.

## Frozen condition set

Candidate B starts with exactly:

1. legacy-device/cohort eligibility;
2. prior-law compliance;
3. no significant design/intended-purpose change;
4. no unacceptable health/safety risk;
5. MDR QMS deadline satisfied;
6. formal application deadline satisfied;
7. current qualifying written agreement/application-transfer state;
8. surveillance responsibility/state;
9. device class / transition endpoint;
10. applicable EUDAMED registration state.

No extra condition may be added after seeing a baseline failure merely to create a treatment win.

## Workflow comparison

For E0–E5 record separately:

### Baseline

- sources/records reopened;
- notes/checklists edited;
- legal inference steps;
- state carried forward;
- stale state corrected;
- historical answer reconstructed;
- errors/unsafe uncertainty.

### Candidate B

- condition rows touched;
- evidence owner reopened;
- derived eligibility recomputed;
- historical state preserved;
- errors/unsafe uncertainty.

## Structural effort proxies

Primary proxies:

- **source reopenings**;
- **distinct prior facts re-established rather than carried forward**;
- **maintenance operations**;
- **legal-condition recompositions**;
- **wrong eligibility conclusions**;
- **historical-state contamination**.

Setup cost must be counted.

Do not invent lawyer minutes.

## Decision rule

End with exactly one:

- `LEAN_TEAM_ACCESS_GAP_SUPPORTED`
- `LEAN_BASELINE_SUFFICIENT`
- `PUBLIC_PROXY_INSUFFICIENT_EXTERNAL_USER_REQUIRED`
- `CANDIDATE_B_REVISE`

### LEAN_TEAM_ACCESS_GAP_SUPPORTED requires

all of:

1. strong baseline remains materially more reconstruction-heavy **or** makes a consequential
   eligibility/history error;
2. Candidate B avoids it through explicit cross-owner condition state;
3. Candidate-B setup/maintenance does not equal or exceed the saved work;
4. difference appears across at least two post-setup events/queries;
5. advantage is not just certificate monitoring, source hashing or prettier formatting.

### LEAN_BASELINE_SUFFICIENT

if the strong baseline naturally converges on an equivalent condition checklist/ledger with
comparable setup and maintenance burden and correct E0–E5 answers.

That is a valid Candidate-B null.

## Evidence quality

Because the actor events are stipulated and execution is internal, a positive result is
**directional workflow evidence only**.

It can earn a disposable prototype/user-validation design.

It cannot establish market value or a real-world treatment effect.

## No automatic build

No UI, ontology, Full Needle revival, corpus change or outreach follows automatically.
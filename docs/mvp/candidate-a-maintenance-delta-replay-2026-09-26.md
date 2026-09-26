# Issue #402 — Maintenance Delta Core v0.1 internal replay

Date: 2026-09-26  
Mode: **MAINTAIN / INTERNAL REPLAY — NOT A VALUE TEST**

## Purpose

Replay the frozen Candidate-A Maintenance Delta Contract v0.1 on three already-known public
maintenance events.

No new defect was hunted.

The replay asks only:

- is the core operationally coherent?
- which fields are actually used?
- what remains redundant?
- can it represent a legitimate revision without inventing a defect?
- are any deterministic invariants now stable enough to validate mechanically?

It does **not** test user value, expert-time savings or Needle superiority.

---

# Replay 1 — Harvey LAB HSR stale 2025 literals

## Subject

- task: `antitrust-competition/analyze-antitrust-hsr-strategy`
- baseline contract: Harvey LAB commit `1dd81403b2fbb60596f7aea3fcecafad7bf73143`
- candidate contract: **pending / no accepted upstream repair established here**

## Trigger

- kind: `WRONG_OR_STALE_LEGAL_PROPOSITION`
- reference: Needle #375 externally defined workflow replay
- summary: two score-bearing HSR literals conflict with the authoritative 2025 FTC schedule applicable to the task's 2025 transaction events.

## Delta unit HSR-01

- kind: `LEGAL_PROPOSITION`
- affected contract: `C-040`
- before: 2025 HSR size-of-transaction threshold = **USD 119.5M**
- after: **USD 126.4M**
- risk: `FALSE_REJECT`, `FALSE_ACCEPT`
- evidence owner: FTC 2025 HSR threshold schedule
- evidence proposition: threshold effective 21 February 2025 is USD 126.4M
- evidence status: `SUPPORTED`
- governing time: `CONTROLLING_EVENT_DATE` / task's 2025 transaction timeline after 21 February 2025

## Delta unit HSR-02

- kind: `LEGAL_PROPOSITION`
- affected contract: `C-039`
- before: filing fee for USD 425M transaction = **USD 160,000**
- after: **USD 105,000**
- risk: `FALSE_REJECT`, `FALSE_ACCEPT`
- evidence owner: FTC 2025 HSR filing-fee schedule
- evidence proposition: USD 425M falls in the USD 105,000 fee band effective 21 February 2025
- evidence status: `SUPPORTED`
- governing time: `CONTROLLING_EVENT_DATE` / task's 2025 transaction timeline

## Repair status

- `PROPOSED`;
- the proposed corrected states already live in HSR-01 / HSR-02 `after` values;
- transaction/event dates remain the temporal owner rather than inventing a separate mandatory law-as-of field.

## Existing-result consequence

- comparability: `UNKNOWN` until historical scored outputs/results for this task revision are inspected;
- action: `HUMAN_DECISION_REQUIRED`, with `REJUDGE_EXISTING_OUTPUTS` sufficient if raw outputs survive;
- scope: results scored against C-039/C-040 at the defective task revision where the 2025 transaction dates control;
- reason: correct 2025 answers can fail and stale answers can pass under the written criteria.

## Replay observation

The delta core captures the maintenance event without reproducing the other 48 task criteria,
full matter documents or a Needle failure class.

Fields materially used:

- identity;
- trigger;
- two delta units;
- evidence owner;
- governing time;
- affected criteria;
- risk direction;
- repair;
- prior-result consequence;
- unresolved acceptance/adjudication state.

---

# Replay 2 — DELTA inactive conditional criterion

## Subject

- task: `family-law/minor-representative-conflict-of-interest`
- criterion: `S-009`
- baseline contract: public DELTA v1.1.0-era task referenced by criterion dispute #2
- candidate contract: **pending / suggested repair not upstream-accepted here**

## Trigger

- kind: `CRITERION_ACTIVATION_AMBIGUITY`
- reference: `legalbenchmarks/delta#2`
- summary: S-009 is conditional on an answer raising dynamic interpretation, but the task does not require that argument and the inactive case is undefined.

## Delta unit DELTA-01

- kind: `CRITERION_ACTIVATION`
- affected contract: `S-009`
- before: PASS only if, insofar as the answer discusses dynamic interpretation, it correctly explains the doctrine; no explicit disposition if the answer does not discuss it;
- after: PASS if the answer does not discuss dynamic interpretation, **or**, if it does, correctly explains that dynamic interpretation is not an independent standard;
- risk: `AMBIGUOUS_GRADING`
- evidence owner: frozen task prompt + S-009 text + reproducible cross-judge disagreement reported in dispute #2
- evidence proposition: the criterion's inactive state has no determinate grading semantics
- evidence status: `SUPPORTED`
- governing time: `NOT_APPLICABLE`.

## Repair status

- `PROPOSED`;
- the candidate activation semantics are already represented in DELTA-01 `after`.

## Existing-result consequence

- comparability: `NOT_COMPARABLE` across un-rejudged pre/post criterion versions for S-009;
- action: `REJUDGE_EXISTING_OUTPUTS` if the historical answer bodies survive;
- scope: outputs previously scored under the ambiguous S-009;
- reason: judge temperament determined pass/fail where the trigger did not occur.

## Replay observation

This event does not need:

- external legal-time state;
- a new answer key;
- a complete evidence graph;
- a Needle class.

The same core handles it by switching the delta-unit type from legal proposition to
criterion activation.

---

# Replay 3 — Harvey firm-knowledge v3 semantic revision control

## Subject

- scope: 250 firm-knowledge task contracts
- baseline: `55510f0e609ffa5cf6f5df17d9a813ce4bb33d0c`
- candidate: `60071cc424d6479569626b8c76d90b958fe2d6c`

## Trigger

- kind: `TASK_OR_RUBRIC_REVISION`
- reference: Harvey LAB public v3 rubric update / public comparison recorded in issue #143
- summary: all 250 task contracts changed in effective input/target fields while shared DMS bytes remained stable.

## Delta unit HV3-01

- kind: `RESULT_INTERPRETATION`
- affected contract refs: all 250 firm-knowledge task contracts in the compared revision;
- before: baseline effective task input/target state;
- after: candidate v3 effective task input/target state;
- risk: `NON_COMPARABLE_RESULTS` pending maintainer interpretation;
- evidence owner: immutable Git revisions + machine-readable public comparison from issue #143;
- evidence status: `SUPPORTED`;
- governing time: `NOT_APPLICABLE`.

## Repair status

- `NOT_REQUIRED`;
- the candidate revision is an owner-adopted repository revision;
- Needle does **not** characterize the revision itself as a defect or accepted repair.

## Existing-result consequence

- comparability: `UNKNOWN`;
- action: `HUMAN_DECISION_REQUIRED`;
- scope: any attempt to compare scores across the two task-contract revisions;
- reason: the effective score-bearing contracts changed, but public history alone does not establish the maintainer's intended comparability semantics.

## Replay observation

This is the critical negative control.

The delta core records **semantic revision without inventing a benchmark defect**.

It therefore distinguishes:

- change detection;
- defect adjudication;
- score comparability.

Those are not the same claim.

---

# Cross-replay field use

| Core field/group | Harvey HSR | DELTA S-009 | Harvey v3 control | Keep? |
| --- | --- | --- | --- | --- |
| subject identity / baseline ref | yes | yes | yes | **YES** |
| candidate ref | pending | pending | yes | **YES, optional until accepted** |
| trigger kind/summary/ref | yes | yes | yes | **YES** |
| delta unit kind | legal proposition | activation | result interpretation | **YES** |
| before/after | yes | yes | yes | **YES** |
| affected contract refs | yes | yes | yes | **YES** |
| risk direction | yes | yes | yes | **YES** |
| evidence owner | legal authority | task/criterion/run evidence | immutable revision comparison | **YES** |
| governing time | required | N/A | N/A | **YES, conditional** |
| repair status | proposed | proposed | not required | **YES** |
| comparability | unknown | not comparable | unknown | **YES** |
| rejudge/rerun/human action | yes | yes | yes | **YES** |
| adjudication state | pending | pending | pending | **YES, optional** |
| Needle taxonomy | no | no | no | **REMOVE CONFIRMED** |
| full source graph | no | no | no | **REMOVE CONFIRMED** |
| full rubric duplication | no | no | no | **REMOVE CONFIRMED** |

## Missing field check

No replay required a new top-level field.

The only semantic refinement earned is:

> `repair_status: ACCEPTED` must mean the **repair is accepted by the contract owner**,
> not merely that a Git commit exists.

For the Harvey v3 control, the candidate revision is an accepted repository state but the
Needle record should not label the semantic change a validated 'repair'.

Therefore the hardened contract should distinguish:

- `change_status`: `OBSERVED`, `ADOPTED_BY_OWNER`, `SUPERSEDED`;
- `repair_status`: `NOT_REQUIRED`, `PROPOSED`, `ACCEPTED`, `REJECTED`, `PARTIAL`.

This is a small but real hardening change.

---

# Effort proxy

Elapsed human-lawyer minutes are **not** inferred from this internal replay.

Use structural effort proxies only:

| Replay | Baseline contract scopes reopened | External/contract evidence owners needed | Delta units | Repair targets | Result-impact decisions |
| --- | ---: | ---: | ---: | ---: | ---: |
| Harvey HSR | 1 task | 1 authoritative schedule + task dates | 2 | 2 criteria | 1 |
| DELTA S-009 | 1 task/criterion | task + criterion + recorded judge disagreement | 1 | 1 criterion | 1 |
| Harvey v3 control | 250-task change set represented by 2 immutable revisions | revision comparison | 1 aggregate unit | 0 defect repair | 1 |

The compact delta representation avoids reopening/re-encoding the full task estates in all
three examples.

That is an internal coherence observation, **not measured user savings**.

---

# Deterministic validation decision

After the replay, redundant repair-action and generic open-question fields were removed.
The remaining structural fields survived all three heterogeneous events and are stable
enough to justify **one tiny structural validator/schema**.

Earned validation scope:

- required identity/trigger/delta units;
- enum validity;
- accepted repair requires candidate contract ref;
- legal correction cannot claim supported without evidence owner;
- time-varying legal correction requires governing-time state;
- non-comparable/unknown historical impact cannot silently select `NONE` action.

Not earned:

- legal correctness validation;
- authority ranking;
- automatic comparability decision;
- automatic criterion repair;
- Needle taxonomy inference.

## Replay disposition

# **CORE_COHERENT — MINIMAL STRUCTURAL VALIDATION EARNED**

This does not yet answer whether a maintainer finds the core useful or cheaper.
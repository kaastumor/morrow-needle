# Needle Relay v0.1 — independent handoff value gate

**Issue:** #87  
**Status:** PILOT COMPLETE / FULL CONFIRMATION PENDING  
**Purpose:** test whether Needle Method and Needle Core preserve legal understanding across context loss and investigator handoff better than competent free-form research notes.

## Why this gate exists

Issue #86 showed:

- strong boring baseline: 5/5 correct unseen answers;
- Needle Method: useful discipline, but no corrected baseline answers;
- Needle Core: narrow value for historical/stateful/repeated questions;
- Full Needle: no material gain over Core.

The surviving project thesis is therefore not "Needle answers legal questions better."

The next claim is:

> structured Method/Core artifacts survive handoff, context loss and changed
> follow-up questions better than competent ordinary notes.

This gate tests that claim directly.

## Experimental arms

### Arm R — competent free-form notes

Investigator A receives:

- Question A;
- the source packet;
- ordinary web/source access.

A may leave:

- answer;
- source links/references;
- free-form notes;
- unresolved points.

No Needle checklist is supplied.

### Arm M — Needle Method dossier

Same source access.

A must leave:

- answer;
- sources actually used;
- source origin vs legal authority where relevant;
- exact legal target/scope;
- temporal perspective;
- current vs historical state distinction where relevant;
- uncertainty;
- forbidden inferences;
- unresolved questions.

No canonical software state is created.

### Arm C — Needle Core

Same Method dossier plus only the smallest existing canonical Core state that is justified.

Rules:

- use existing Core contracts only;
- do not create a new schema during the experiment;
- do not serialize a hypothetical fact merely because a schema exists;
- include provenance/history/temporal state only when the case earns persistence;
- no Thread, Retrieval, X-Ray, Source Anomaly, Half-Life or other parked projection unless a later observed relay failure independently earns it.

## Handoff

Investigator A disappears.

Investigator B must be a genuinely fresh session/agent/researcher.

B receives only:

1. A's artifact;
2. the sealed Stage B follow-up for that case;
3. permission to reopen official sources if needed.

B does **not** receive:

- A's conversation;
- A's hidden reasoning;
- the answer key;
- the arm label.

B must record:

- final answer;
- why it follows;
- which sources had to be reopened;
- which new sources were needed;
- facts that had to be rediscovered because A's artifact did not preserve them;
- remaining uncertainty.

## Cases

Five cases are sealed:

1. `relay-eudr-double-postponement`
2. `relay-battery-due-diligence-postponement`
3. `relay-dma-designation-vs-compliance`
4. `relay-rohs-scope-split`
5. `relay-gdpr-force-vs-application-control`

The fifth is a deliberately simpler control.

Case text is not stored in GitHub before independent execution.

## Blinding / commitments

The three execution artifacts were fixed before independent execution and are kept outside the repository.

Their SHA-256 commitments are canonical in:

`fixtures/value-gates/issue87-sealed-manifest-v0.1.json`

After all intended independent runs are complete:

1. verify artifact bytes against the committed hashes;
2. reveal the Stage B packets and answer key;
3. commit the previously sealed artifacts;
4. evaluate concrete failure events;
5. reconcile `docs/value-evidence.md`.

Do not replace the sealed files after observing results.

## Minimum execution

### Pilot

Use at least **3 cases across all 3 arms**:

- 9 Stage A runs;
- 9 independent Stage B runs.

The pilot must include:

- one historical-amendment case;
- the DMA status/application case;
- the GDPR control.

### Full confirmation

Run all 5 cases across all 3 arms:

- 15 Stage A runs;
- 15 independent Stage B runs.

Case order should vary across investigators where practical.

## Failure events

Record events individually.

### Consequential answer failures

- wrong Stage B conclusion;
- current state projected backward;
- past state treated as current;
- legal status confused with application/compliance;
- parent/general scope projected onto a narrower subclass;
- entry into force confused with application;
- unsupported certainty.

### Handoff degradation

- key fact omitted by A and rediscovered by B;
- uncertainty present in A but lost by B;
- source role/authority lost;
- B cannot explain why the answer follows;
- B must reopen sources the artifact should reasonably have preserved.

### Over-structuring

Especially for Core:

- canonical object created for a hypothetical/non-observed fact;
- irrelevant state serialized;
- one-off question made harder without future reuse;
- parked Full-Needle machinery introduced without observed need.

## No synthetic winner score

Do not collapse the experiment into one opaque number.

For each case/arm record:

- correct / incorrect;
- concrete failure events;
- sources reopened;
- facts rediscovered;
- unresolved uncertainty preserved/lost;
- time/effort if reliably measurable;
- whether persistence prevented a real failure.

Then compare patterns.

## Promotion criteria

### Needle Method

Method may receive a project-level VALUE entry only if independent runs show:

- fewer consequential handoff errors than Arm R; or
- materially better consistency/reconstruction with similar source access.

Merely producing nicer prose does not qualify.

### Needle Core

Core may receive VALUE only if it outperforms Method specifically on persistence:

- fewer historical-state losses;
- materially fewer source reopenings/rediscoveries;
- safer repeated state queries;
- better preservation of scope/time/provenance.

If Method performs essentially as well as Core, shrink again.

### Full integrations

No Full-Needle integration is under test by default.

A parked integration may re-enter only after a concrete observed relay failure identifies a need that the integration plausibly and uniquely addresses.

## Capability-bound acceptance

The session that designed the experiment is contaminated by the questions and answer key.

It cannot supply valid independent investigator runs.

Do not weaken this requirement.

Issue #87 remains open until independent execution evidence exists.

## Kill rules

- If Arm R performs materially as well as Method across independent handoffs,
  stop claiming Needle-specific Method value.
- If Method performs materially as well as Core on the stateful cases, shrink
  toward Method + corpus/protocol.
- If Core wins only by storing information that ordinary competent notes
  preserve just as reliably, do not count that as Core value.
- If no arm advantage survives the control and historical cases, consider
  reducing Needle to the evaluation/adversarial corpus itself.


## Pilot checkpoint — 2026-09-23

The minimum pilot is complete.

- 3 cases × 3 arms;
- 9 fresh Stage-A runs;
- 9 fresh Stage-B runs;
- 9/9 Stage-B substantive conclusions correct.

Observed pattern:

- Method had the lowest reconstruction burden.
- Core showed no observed handoff advantage over Method.
- No Full-Needle integration earned re-entry.
- Core preflight access failures were discarded and replaced, before valid C
  execution, by one frozen reference-pack boundary.

The two remaining pre-sealed cases are the full-confirmation boundary:
battery due-diligence postponement and RoHS scope split.

Do not add cases or change promotion criteria before those runs complete.


## Protocol amendment B — stateless API execution for full confirmation

**Date:** 2026-09-23

The remaining Battery/RoHS full-confirmation runs may be executed through a
local stateless OpenAI Responses API harness instead of manually opening fresh
ChatGPT conversations.

This is an **execution-boundary change only**. It does not change:

- the two pre-sealed cases;
- Arm R/M/C instructions;
- the frozen Core reference pack;
- the hidden Stage-B questions;
- evaluation criteria;
- kill/promotion rules.

Required harness properties:

- one independent API request per investigator;
- GPT-5.6 Sol for all runs;
- reasoning effort = high for all runs;
- web search enabled for all runs;
- no conversation object;
- no `previous_response_id`;
- `store=false`;
- Stage A receives only its arm/case prompt (+ frozen Core pack for C);
- Stage B receives only its matching Stage-A artifact + the already-sealed
  follow-up question;
- no answer key is supplied to any investigator;
- result text is saved verbatim;
- model/response/usage metadata is retained in a run manifest;
- any request failure stops or retries transparently rather than manufacturing
  an experimental result.

The local runner may contain the still-sealed Stage-B follow-ups, because they
are not placed in any Stage-A request. The runner itself remains outside Git
until the full-confirmation blind is complete, avoiding premature reveal in
repository history.

This amendment reduces sponsor/manual-chat handling without weakening
investigator independence.

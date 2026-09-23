# Needle Relay full-confirmation audit — Issue #87

**Date:** 2026-09-23  
**Status:** EXPERIMENT + PROJECT DECISION COMPLETE / EXACT SEALED-ARTIFACT ARCHIVAL PENDING

## Scope

This audit completes the pre-sealed Needle Relay value gate without adding cases,
changing criteria or reopening parked Full-Needle surfaces.

It combines:

- the independent EUDR / DMA / GDPR pilot;
- the pre-sealed Battery due-diligence postponement confirmation;
- the pre-sealed RoHS 7(a) scope-split confirmation.

## Execution integrity

The no-admin runner output contained exactly 13 files:

- 6 Stage-A result artifacts;
- 6 Stage-B result artifacts;
- 1 run manifest.

ZIP SHA-256:

`e73c691b9201cf1ca78979a4c0e17191f589f172c6dcdb16a43df3ff0b530fb5`

The manifest records:

- 6 Stage-A + 6 Stage-B calls;
- `gpt-5.6-sol` requested and returned for every run;
- `reasoning_effort=high`;
- web search enabled;
- `store=false`;
- stateless requests;
- 12 unique response IDs;
- every call completed;
- all Stage-A runs completed before the Stage-B runs.

The ZIP result-file set matches the manifest exactly.

The protocol's complete five-case sealed Stage-A, Stage-B and answer-key
artifacts had already matched their pre-execution SHA-256 commitments during the
independent pilot. The confirmation ZIP does not contain those sealed plaintext
files, so this session cannot honestly perform the protocol's final
"commit the exact sealed bytes unchanged" step. Reconstructing them from
summaries would defeat the commitment.

That is an archival closure blocker, not a reason to discard the completed
experimental evidence.

## Confirmation result

All six confirmation Stage-B answers are substantively correct.

### Battery due-diligence postponement

Question B asks whether a 1 July 2025 board paper was historically accurate in
saying that Article 48(1) battery due-diligence obligations were scheduled to
apply from 18 August 2025, and what later changed that position.

R, M and C all reached the same correct result:

- 18 August 2025 was still the legally operative scheduled date on 1 July;
- the postponement process was then pending rather than binding;
- Regulation (EU) 2025/1561 later replaced the date with 18 August 2027;
- the legally operative change followed that Regulation's entry into force on
  31 July 2025.

All three Stage-A artifacts already preserved the decisive original date,
replacement date and amendment force timing. Each Stage-B investigator
nevertheless reopened official sources and reconstructed additional legislative
procedure.

That extra procedure is useful context but was not required to recover the
decisive legal answer from the handoff. Most importantly for H-13, the Core arm
had persisted temporal state and still did not reduce the observed
reopening/rediscovery behavior beyond Method.

**Battery disposition:** R correct; M correct; C correct; no Core-over-Method
handoff advantage.

### RoHS 7(a) scope split

Question B asks whether the headline 30 June 2027 expiry can be generalized to
all newly split 7(a) uses.

R, M and C all correctly answered no:

- the unsuffixed 7(a) entry expires 30 June 2027;
- the separately enumerated 7(a)-I through 7(a)-VII entries have a
  31 December 2027 expiry;
- 7(a)-I is a concrete counterexample to the attempted generalization.

Every Stage-A artifact already preserved the decisive scope/date distinction.
The B runs reopened sources for verification and, in some cases, recovered
more detailed sub-entry wording, but no missing material fact had to be
rediscovered to answer the changed question.

The Core Stage-A artifact explicitly returned
`PERSISTENCE_NOT_JUSTIFIED`. That is the correct anti-over-structuring
decision, but it also means Core contributes no persistent handoff value beyond
the Method dossier in this case.

**RoHS disposition:** R correct; M correct; C correct; no Core-over-Method
handoff advantage.

## Combined five-case evidence

Across EUDR, DMA, GDPR, Battery and RoHS:

- 15/15 Stage-B conclusions are substantively correct;
- no arm has a raw correctness advantage;
- the independent pilot shows Method with the lowest reconstruction burden;
- the two confirmation cases do not reverse that pattern;
- there is no observed Core-over-Method handoff win;
- no parked Full-Needle integration is required by an observed relay failure.

This is enough to make the project-level decision because the remaining cases
were fixed before the pilot and the decision rule was also fixed before their
execution.

## Project-level decision

### Needle Method: VALUE

H-12 survives in a bounded form.

Needle Method does not earn a claim of better legal-answer correctness. The
strong baseline was already very good. It earns a narrower contribution:
explicit source/authority/target/time/uncertainty/forbidden-inference handoffs
reduce reconstruction burden and make changed follow-up questions easier to
review across context loss.

The correct project claim is reproducibility discipline, not superior legal
reasoning.

### Needle Core as default identity: REJECT

H-13 is rejected at the project-identity level.

The protocol said:

> If Method performs materially as well as Core on the stateful cases, shrink
> toward Method + corpus/protocol.

That condition is met.

The canonical default identity therefore becomes:

**Needle Method + corpus/protocol**

Core is preserved as optional, individually earned persistence rather than a
default layer.

## Core admission rule

A Core persistence object may re-enter active use only when all relevant
conditions are satisfied:

1. there is a concrete repeated, historical, provenance-sensitive or otherwise
   stateful task, or an observed Method-only handoff/reconstruction failure;
2. a Method dossier does not preserve the needed state reliably enough;
3. an existing canonical contract can represent the state without speculative
   serialization, or any contract repair is independently earned by evidence;
4. persistence demonstrably prevents a real error or materially reduces source
   reopening, rediscovery or repeated-query cost versus Method;
5. the durable benefit is worth the maintenance cost.

These are not sufficient:

- a schema already exists;
- machine readability is aesthetically preferable;
- the fact might be useful someday;
- a one-off date/scope fact is explicit and a competent Method dossier
  preserves it;
- persistence merely stores what ordinary careful notes preserve equally well.

## What does not happen

- Full Needle is not revived.
- Thread, Retrieval, X-Ray, Source Anomaly, Half-Life, feed/cards and other
  parked projections do not re-enter.
- No replacement feature horizon is invented.
- No existing Core contract is deleted merely to dramatize the shrink decision.

The repository remains a useful corpus of adversaries, evidence distinctions,
bounded contracts and regressions. Architecture is now subordinate to Method,
not part of the default identity.

## Issue #87 closure state

The experiment and project decision are complete.

Issue #87 remains open only because its acceptance protocol explicitly requires
the exact previously sealed Stage-A, Stage-B and answer-key artifacts to be
revealed and committed unchanged after execution. Those bytes are not present
in the supplied confirmation ZIP and must not be recreated from summaries.

Once the exact committed-hash artifacts are available, archival verification
and closure require no new experiment, new case or new project horizon.

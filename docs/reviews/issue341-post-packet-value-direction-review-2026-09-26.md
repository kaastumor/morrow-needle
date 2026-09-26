# Issue #341 — direction review after observed packet value + Reference Pack gap

Date: 2026-09-26  
Selected mode: **REVIEW / RELEASE — DESIGN ONLY**  
Next WIP: **#343 — minimum Reference Pack v0.2 failure-analysis surface**

## Trigger

#339 produced the first direct positive use observation for Needle's revised external
failure-analysis contract:

> **NEEDLE_VALUE_PACK_GAP**

The test was unusually useful because:

- the external failure source was independent of Needle;
- the selection was mechanical and frozen before Needle inspection;
- the strong ordinary postmortem already recovered the correct law;
- no current Needle class honestly matched the failure;
- Needle nevertheless added material packet/reuse structure;
- Reference Pack v0.1 could not expose that material value without broader repository
  reconstruction.

This is positive evidence for packet value and a concrete release-surface gap.

It is one case, not population evidence.

## Decision question

Should Needle:

1. immediately run an orthogonal second failure-analysis USE;
2. begin bounded Reference Pack v0.2 design;
3. implement/release v0.2;
4. return to discovery/consolidation/maintenance?

## REVIEW / RELEASE — DESIGN ONLY

### Why design is now earned

#339 did not produce a vague request for "more metadata".

It demonstrated specific missing surface properties:

- explicit no-class disposition;
- scientific/reuse status for an external observed failure;
- causal failure mechanism;
- historical source-state reuse guidance;
- boundary/opposite-error evidence;
- post-hoc regression-conversion state;
- explicit PASS/FAIL contract;
- compact navigation to enough evidence to reconstruct those distinctions.

Those are concrete use-derived requirements.

A design gate can therefore answer a new decision-relevant question:

> can this demonstrated value be surfaced in a small derived release layer without
> duplicating legal truth or inventing a new canonical ontology?

That is cheaper and more reversible than implementation.

### Why one positive case is enough for design

One case is insufficient to claim generality or release a broad new structured schema.

It is sufficient to investigate the minimum design because:

- the pack gap was directly observed rather than hypothesised;
- v0.1 already exists as a working deterministic derived layer;
- a design review can still conclude docs/navigation only, replication first, or no v0.2;
- no release bytes need change;
- design itself can expose whether the apparent field set is overfit to #339.

The evidence burden for **design investigation** is lower than the evidence burden for
**implementation/release**.

### Why implementation is not yet earned

A v0.2 implementation now would over-read one positive case.

In particular, #339 alone cannot prove that all future failure packets need:

- the same boundary shape;
- the same regression fields;
- the same source-state representation;
- a new external-analysis collection;
- a new canonical packet object.

Any new structured field family learned from #339 should normally survive an orthogonal use
before release implementation unless it simply exposes canonical state already supported
across existing evidence owners.

Therefore:

> **design now; implementation remains blocked.**

## USE — orthogonal replication

A second materially different USE remains credible.

It could test whether the #339 packet components recur on another independently selected
failure.

**Why not first**

Without a candidate v0.2 contract, a second USE can tell us "Needle helped again" but may
not discriminate:

- which fields are genuinely reusable;
- which are #339-specific;
- whether v0.1 needs better navigation or a new structured layer;
- which proposed fields lack canonical owners.

The design pass gives the replication a sharper falsifier.

A likely sequence after #343 is:

> design candidate -> orthogonal USE against candidate -> implement only what survives.

This is not precommitted; #343 must justify it.

## DISCOVER

The highest-value uncertainty is no longer whether a failure-analysis job exists.

#335 and #339 moved that question materially.

Another external-landscape search now has lower information gain than inspecting how the
observed value could or could not be surfaced safely.

**Not selected.**

## CONSOLIDATE

The project identity is already reconciled:

- known-failure reference corpus;
- case-specific exposed regression fixtures;
- failure-analysis/evaluation-design/debugging use contract;
- generic legal-research companion value remains unsupported.

No live owner conflict requires another consolidation pass before design.

**Not selected.**

## MAINTAIN

No correctness, integrity, security or cost trigger dominates the release-design question.

The recent workflow-path ownership refinement already removed unnecessary unit-test
activation for purpose-only docs.

**Not selected.**

## Strongest architecture risk

The design must not assume that #339 should simply become another corpus case.

That would destroy an important distinction:

- corpus membership;
- external observed failure analysis;
- fresh/sealed evaluation;
- derived regression candidate

are different scientific states.

Likewise, copying boundary/source-state/regression prose into a pack file can create a
second mutable truth store if those fields do not have legitimate canonical owners.

Therefore #343 must apply a field-by-field truth-ownership test before proposing any
structured v0.2 packet surface.

## Sponsor/value correction

External tools already offering legal benchmarks, incident memory or failure metadata do
not veto v0.2.

The relevant test is:

> would a richer Needle packet be materially better for the demonstrated failure-analysis
> job at acceptable complexity?

Novelty is not required.

But differentiation must still earn implementation through use.

## Decision

# **SELECT REVIEW / RELEASE — DESIGN ONLY**

Next WIP:

> **#343 — minimum Reference Pack v0.2 failure-analysis surface**

#343 may conclude:

- docs/navigation-only improvement;
- a derived packet design;
- replicate before design;
- no v0.2 justified.

It may not implement or publish v0.2.

No corpus/class, pack byte, product scope, #214, #327 or #339 result changes in #341.

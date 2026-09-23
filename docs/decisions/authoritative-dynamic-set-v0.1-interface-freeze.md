# Decision — Authoritative Dynamic Set v0.1

**Date:** 2026-09-23  
**Status:** PROVISIONALLY ADOPTED FOR ISSUE #77  
**Scope:** canonical causal owner only; no public-product expansion

## Problem

Dependency Ripple v0.1 assumed that an unchanged local rule could only acquire a
derived changed effect through a conventional cross-reference to another legal
location whose text mutates.

Two official cases disprove that assumption.

### Toy safety

Directive 2009/48/EC Article 13 is unchanged.

The same harmonised standard identifier,
`EN 71-1:2014+A1:2018`, remains listed.

Commission Implementing Decision (EU) 2025/1785 changes its published-reference
status for a specified wave-roller scope, narrowing the Article 13 presumption.

### REACH Candidate List

REACH Article 33 is unchanged.

n-hexane identity is unchanged.

On 4 February 2026 ECHA adds n-hexane to the authentic Candidate List published
on its website under Article 59. Article 33 can then operate differently for
articles satisfying its remaining statutory conditions.

## Decision

Introduce one narrow canonical contract:

- `schemas/authoritative-dynamic-set-v0.1.schema.json`

with two proof fixtures:

- `fixtures/dependency/toy-safety-authoritative-dynamic-set-v0.1.json`
- `fixtures/dependency/reach-candidate-list-authoritative-dynamic-set-v0.1.json`

The contract owns only facts necessary to represent this demonstrated causal
shape:

1. authoritative set identity;
2. responsible authority;
3. authoritative publication surface;
4. legal basis;
5. a governing-rule dependency whose effect is conditioned on set state;
6. member identity;
7. membership/status transition;
8. effective time and scoped transition evidence.

## Core relation

The frozen relation character is:

`LEGAL_EFFECT_CONDITIONED_ON_AUTHORITATIVE_SET_STATE`

This is intentionally not a general dependency relation.

## Transition vocabulary

v0.1 supports only the operations required to express bounded authoritative-set
state:

- `ADD_MEMBER`
- `REMOVE_MEMBER`
- `RESTRICT_MEMBER`
- `UNRESTRICT_MEMBER`
- `STATUS_CHANGE`

Operation-specific schema constraints prevent an ADD from starting in an
already-included state and prevent a RESTRICT from silently removing membership.

## Ownership boundaries

This contract does **not** own the downstream derived legal effect.

It owns the authoritative set, the legal dependency condition and the direct
membership/status transition.

That preserves the distinction between:

- direct evidence that the authoritative set changed;
- direct evidence that a rule predicates legal effect on that set;
- any later derived semantic statement about a concrete regulated situation.

## Existing contracts retained

### Source Observation v0.1

Retained. `OTHER_OFFICIAL` can preserve ECHA website bytes.

### Source Change v0.1

Retained and not widened. It remains a Cellar update-detection contract.

### Mutation Candidate v0.2

Retained and not widened. An agency-list membership event is not forced into
`AUTHENTIC_ACT` merely to fit the mutation schema.

### Change Atom v0.3

Retained for now. No fake textual mutation is manufactured to feed it.

Whether a later semantic version should accept authoritative-set transitions as
a causal basis remains deliberately undecided.

### Dependency Ripple v0.1

Its original static cross-reference cases remain valid, but its freeze remains
reopened. A future v0.2 may compose this new canonical contract; this decision
does not yet alter the X-Ray view schema.

## Why this is not a generic graph

The contract cannot represent arbitrary nodes and edges.

It only represents legally authoritative dynamic sets and their member
transitions where a governing rule explicitly conditions legal effect on set
state.

If a future case does not share that shape, this schema should fail rather than
grow opportunistically.

## Reopen rule

Reopen v0.1 only when an official case demonstrates one of:

- authoritative set state cannot be expressed as membership + status;
- a legally operative transition cannot be represented by the bounded
  operation vocabulary;
- publication authority cannot be captured without collapsing source identity;
- dependency truth requires a relation other than legal effect conditioned on
  authoritative set state.

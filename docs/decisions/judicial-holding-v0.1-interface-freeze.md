# Decision — Judicial Holding v0.1

**Date:** 2026-09-23  
**Status:** ADOPTED  
**Issue:** #83

## Problem

Needle can preserve:

- legislative text and textual mutations;
- direct real-world findings;
- metrics;
- dynamic-set state;
- temporal consequences.

It did not have a canonical owner for a different source of legal truth:

> a court judgment directly deciding what a legal provision means or whether it
> remains valid.

Two Grand Chamber preliminary rulings demonstrate different holding semantics.

## Proof case 1 — Test-Achats

C-236/09, ECLI:EU:C:2011:100.

The Court held Article 5(2) of Directive 2004/113/EC invalid with effect from
21 December 2012.

The current consolidated Directive still prints Article 5(2).

Needle therefore has to preserve three separate facts:

1. the provision's wording remains in TEXT_STATE;
2. the Court directly decided invalidity;
3. the Article 5(2) derogation ends from the expressly stated future date.

Temporal v0.2 already owns the third fact through a DEROGATION END assertion.

Judicial Holding owns the second.

## Proof case 2 — Planet49

C-673/17, ECLI:EU:C:2019:801.

The Court interpreted Article 5(3) of Directive 2002/58 read with the relevant
data-protection consent provisions.

A pre-checked checkbox that the user must deselect does not validly constitute
the required consent.

The judgment supplies authoritative interpretation.

It does **not** justify inventing 1 October 2019 as a new application start for
Article 5(3).

## Decision

Introduce:

`schemas/judicial-holding-v0.1.schema.json`

The contract owns only:

- court identity;
- case number / ECLI;
- judgment date;
- holding type;
- target legal provision(s);
- bounded direct holding proposition;
- direct official judgment evidence;
- relation to separately owned temporal consequences.

## v0.1 holding types

Only the two evidenced types are supported:

- `INVALIDITY`
- `INTERPRETATION`

No generic judgment taxonomy is introduced.

## Temporal separation

A holding must explicitly state one of:

### EXPLICIT_TEMPORAL_CONSEQUENCE

At least one Temporal assertion reference is required.

Test-Achats uses this because the Court itself supplies a future invalidity date.

### NO_NEW_VALID_TIME_BOUNDARY_ASSERTED

No Temporal assertion reference is permitted.

Planet49 uses this because the judgment date is not automatically a new
valid-time boundary for the interpreted provisions.

This does not make a general jurisprudential claim about retroactivity of all
preliminary rulings. It simply prevents Needle from fabricating a temporal
boundary where the proof case does not provide one.

## Existing contracts retained

### Change Atom v0.3

Unchanged.

It remains semantic truth derived from VERIFIED textual mutation.

A judicial holding is not fed a fake mutation simply to enter that contract.

### Authoritative Finding v0.1

Unchanged.

It remains direct categorical truth about concrete real-world subjects or
conditions.

A court deciding legal meaning is not reclassified as a factual finding.

### Temporal v0.2

Unchanged.

It owns explicit legal-time consequences, such as the Test-Achats derogation
end.

It does not own the judicial proposition that causes or explains that boundary.

### Source Observation

Unchanged.

It can preserve the judgment artifact. Judicial Holding owns the legal
proposition extracted from the official judgment.

## What v0.1 does not add

- no case-law citation graph;
- no precedent-weight model;
- no court hierarchy engine;
- no national follow-on litigation;
- no inferred temporal effect;
- no automatic propagation to every semantically related provision;
- no legal-importance score;
- no model-generated ratio decidendi.

## Reopen rule

Reopen only when an official judicial adversary requires a holding that cannot
be represented without distortion as:

- INVALIDITY or INTERPRETATION;
- bounded target provision references;
- a direct proposition;
- optional separately evidenced temporal consequence.

Likely future adversaries include annulment, partial invalidity, temporal-effect
limitation, interpretation across multiple language versions, and judgments
whose operative effect depends on national follow-on proceedings. None is added
pre-emptively.

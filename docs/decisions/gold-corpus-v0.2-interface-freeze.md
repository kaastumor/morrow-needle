# Decision — Freeze Gold Corpus Contract v0.2

**Date:** 2026-09-20  
**Status:** ADOPTED  
**Issue:** #3

## Decision

The Gold Corpus contract is stable enough to stop being a P0 blocker.

Canonical contract:
- `schemas/gold-corpus-case-v0.2.schema.json`
- `scripts/validate_gold_corpus.py`
- `src/needle/gold.py`
- `.github/workflows/gold-corpus.yml`

The corpus remains permanently open-ended: every new important adversary should add cases. What is frozen is the mechanism by which a verified reconstruction becomes a machine-enforced regression.

## Required characteristics

A Gold case records:
- adversarial claim;
- foundation contracts exercised;
- explicit language scope;
- official source identifiers and roles;
- expected document relationships;
- provision alignments;
- textual mutations;
- Change Atoms;
- non-atoms / forbidden inferences;
- temporal assertions;
- ambiguities;
- verification state;
- machine PRESENT / ABSENT expectations.

## Negative expectations are first-class

A false legal inference must fail CI just as a missing true fact does.

This is especially important for:
- false provision lineage;
- semantic Change Atoms emitted from textual change alone;
- unjustified language/globalization assumptions;
- unsupported temporal conclusions.

## Verified foundation cases

### Regulation No 26 → Regulation 1184/2006
Proves that official correlation evidence controls structural lineage and forbids same-number ancestry inference.

### Regulation 794/2004 Article 3
Proves a live source-assisted VERIFIED textual mutation and simultaneously forbids premature semantic Change Atom emission.

The second case is derived from a live Cellar verification chain rather than fixture syntax alone.

## Durable rule

Closing P0-C means the **corpus contract is resolved**, not that corpus growth stops.

P0/P1/P2 work should continue adding Gold cases whenever a newly established legal-information invariant would be costly to regress.

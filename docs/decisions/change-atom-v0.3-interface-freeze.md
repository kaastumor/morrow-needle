# Decision — Freeze Change Atom v0.3

**Date:** 2026-09-20  
**Status:** ADOPTED  
**Issue:** #11

## Decision

Freeze the first P1 semantic contract around:

- `schemas/change-atom-v0.3.schema.json`
- `src/needle/semantic/adversary.py`
- `fixtures/semantic/reg794-article3-atoms-v0.1.json`
- `fixtures/temporal/reg794-article3-sani-v0.1.json`
- `tests/test_change_atoms.py`
- `.github/workflows/semantic-source.yml`

`change-atom-v0.2` is retained only as historical provenance and is explicitly superseded because it collapsed procedural/publication/force/application state into a single lifecycle-like field.

## What a Change Atom is

A Change Atom is an independently defensible **legal-semantic claim** derived from one or more VERIFIED textual mutations.

It is not:
- a document summary;
- a lifecycle status;
- a textual diff;
- a prediction of impact;
- a model confidence score.

## Stable v0.3 principles

### 1. Mutation truth is referenced, not copied
Every atom references one or more source mutation IDs.

A VERIFIED atom may depend only on VERIFIED textual mutations.

### 2. Temporal and procedural truth remain orthogonal
Atoms reference:
- temporal assertion IDs;
- procedure-state references.

They do not embed a collapsed current legal-state enum.

### 3. Language scope is explicit
Every atom has expression/language scope.

Cross-language semantic equivalence is never silently assumed.

### 4. Exact source spans are mandatory
A VERIFIED atom carries source spans with:
- authentic source identifier;
- exact source locator;
- language;
- span text hash;
- immutable authentic artifact SHA-256;
- evidence role.

Live Cellar verification for Regulation 271/2008 pins the first semantic atoms to:
- SANI duty: `L_2008082EN.01000101.xml#normalized-chars:7414-7551`
- alternative-channel permission: `...#normalized-chars:7704-7983`
- invalid-channel legal-status consequence: `...#normalized-chars:7983-8261`

All are bound to authentic payload SHA-256:
`c61ea6c41be9c3faf418a80c2ce12fcfb1233b91557eb4157ce2435c40afe5f7`.

### 5. Legal effect and dimensions remain separate
Example:
- legal effect: DUTY
- dimensions: PROCEDURE + DIGITAL_CHANNEL + TIME

### 6. Qualifiers survive extraction
Exception, condition, scope and temporal language are retained through explicit qualifier terms and atom relations.

### 7. Semantic relations are first-class
The initial graph includes:
- primary SANI DUTY;
- exceptional alternative-channel PERMISSION linked by `EXCEPTION_TO`;
- separate LEGAL_STATUS consequence for unagreed alternative-channel submissions.

Relation targets must exist, must not self-reference and must have compatible language scope.

### 8. Affected entities remain separately evidenced
The first atoms deliberately leave affected-entity output empty rather than inferring broad labels from context.

### 9. High-risk semantic verification is adversarial
For deterministic legal-language classification, a VERIFIED atom must preserve source trigger terms such as:
- shall;
- may;
- shall not be considered.

Trigger and qualifier terms must occur in the hashed cited source span.

### 10. Plausibility is not evidence
The negative-control atom:
“all correspondence must be transmitted through SANI”
is rejected.

The authentic Article 3 text distinguishes notifications via SANI from correspondence via PKI.

## First verified semantic graph

One VERIFIED textual mutation — Regulation 794/2004 Article 3 replacement — now yields multiple independently verified semantic atoms:

1. SANI transmission DUTY from 1 July 2008.
2. Exceptional alternative-channel PERMISSION with agreement.
3. Invalid-channel LEGAL_STATUS consequence absent agreement.

This proves the architecture supports one-to-many textual-mutation → semantic-claim decomposition.

## Gold regression

`fixtures/gold/reg794-article3-semantic-atoms-v0.1.json`

The Gold case requires the three supported atoms and includes an ABSENT expectation for the false all-correspondence-via-SANI inference.

## Post-freeze rule

Extend legal-effect classifiers, semantic relations, scope extraction and model-assisted proposal generation behind this interface.

Reopen v0.3 only when an official adversarial case demonstrates that a semantic legal change cannot be represented without distortion.

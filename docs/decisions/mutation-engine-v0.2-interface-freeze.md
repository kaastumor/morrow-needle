# Decision — Freeze Source-Assisted Mutation Engine v0.2

**Date:** 2026-09-20  
**Status:** ADOPTED  
**Issue:** #9

## Decision

Freeze the P0-I mutation foundation around the following canonical interfaces:

- `schemas/mutation-candidate-v0.2.schema.json`
- `src/needle/mutation/diff.py`
- `src/needle/mutation/reconcile.py`
- `src/needle/mutation/structural.py`
- `src/needle/mutation/instructions.py`

`mutation-candidate-v0.1` remains in the repository only as provenance and is explicitly superseded.

The engine is source-assisted and deterministic. It does **not** turn textual difference directly into legal-semantic meaning.

## Evidence stack

A mutation may be supported by:

1. authentic modifying/correcting act;
2. official embedded consolidation provenance;
3. official relationship metadata;
4. official before/after consolidated checkpoints;
5. deterministic canonical-AST comparison.

Agreement increases documentary support. Disagreement is surfaced as conflict.

Only a parsed authentic legal cause may cross the textual mutation verification gate to `VERIFIED`.

## Candidate generation

### Exact-location textual mutations
The engine emits conservative candidates for:
- INSERT;
- DELETE;
- REPLACE.

Alignment uses exact citation + structural kind. No fuzzy provision identity is inferred.

### Evidence-targeted subtree comparison
When an official source identifies an affected subdivision such as Article 3, the engine can compare the complete canonical AST subtree rooted at that exact subdivision.

This captures changes in descendant paragraphs while preserving the official Article-level target.

### Tables and annexes
Table cells may align by:
- stable legal anchor;
- table ordinal;
- row coordinate;
- column coordinate.

Row/cell reordering is not inferred as a move.

### Structural mutations
DELETE + INSERT candidates may be reclassified as:
- MOVE;
- RENUMBER;
- SPLIT;
- MERGE

**only** when an ASSERTED, non-conflicting P0-A structural lineage edge supplies the identity bridge.

Similarity-only or unresolved lineage cannot consume the underlying candidates.

## Feature deltas

Deterministic comparison exposes:
- numbers added/removed;
- dates added/removed;
- legal references added/removed.

These are textual features, not semantic Change Atoms.

## Formatting / representation noise

Mutation comparison uses canonical `text_compare` state, not raw representation text.

Whitespace-only representation differences are explicitly regression-tested to emit no mutation.

## Verification milestone

The first fully live verified mutation is Regulation (EC) No 794/2004 Article 3.

Live contract:
- before: `02004R0794-20070119`;
- after: `02004R0794-20080414`;
- authentic cause: `32008R0271`;
- target: Article 3;
- operation: REPLACE.

The live CI path retrieves real Cellar Formex for all three sources. The generic subtree comparator produces the candidate, EUR-Lex relationship metadata and embedded Formex provenance corroborate it, and the exact authentic amending source span supplies the canonical legal cause.

Result:
- `reconciliation_state = CORROBORATED`
- `verification_state = VERIFIED`
- no conflicting evidence.

Frozen regression:
- `fixtures/mutations/reg794-article3-live-verified-v0.1.json`
- `fixtures/gold/reg794-article3-verified-mutation-v0.1.json`

## Structural adversaries passed

- RENUMBER: Regulation No 26 Article 4 → Regulation 1184/2006 Article 3.
- SPLIT: Directive 69/335 Article 7(2) → Directive 2008/7 Articles 7 and 8.
- MERGE: old Regulation No 26 Article 2(2)+2(3) → new Article 2(2) container.
- MOVE: Regulation 1308/2013 Article 97(3) → Article 97(4), supported by authentic official narrative evidence.
- Similarity-only negative control remains DELETE + INSERT.

## Durable invariants

1. A deterministic diff is a candidate, not legal authority.
2. Consolidated text and embedded consolidation provenance are documentary evidence, not canonical legal cause.
3. Only authentic modifying/correcting text may independently satisfy the canonical-cause verification gate.
4. Evidence disagreement is data and prevents verification.
5. Textual mutation and semantic legal effect remain separate layers.
6. Structural mutation never implies proposition-level rule continuity.
7. Provision alignment confidence remains owned by the referenced P0-A lineage claim; it is not copied into a second drifting confidence field.
8. Missing embedded mutation markup does not mean no mutation.
9. Formatting-only representation differences do not become mutations.
10. Exact-source span and raw source hashes survive into provenance.

## Post-freeze rule

Extend amendment parsers, alignment adapters and operation coverage behind this interface.

Reopen the P0-I core contract only if an official adversarial case demonstrates that a legal textual mutation cannot be represented without semantic distortion.

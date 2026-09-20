# Decision — Freeze Provenance Ledger v0.1

**Date:** 2026-09-20
**Status:** ADOPTED
**Issue:** #12

## Decision

Freeze the P1-C provenance foundation around:

- `schemas/provenance-record-v0.1.schema.json`
- `src/needle/provenance/ledger.py`
- `fixtures/provenance/reg794-article3-dag-v0.1.json`
- `tests/test_provenance_ledger.py`

The ledger records **how Needle knows**, not legal truth itself. Legal/document/temporal/semantic state remains in the domain contracts.

## Record classes

### SOURCE_OBSERVATION
Immutable observation of an official representation:
- source/resource identifier;
- language/representation class;
- observation time;
- immutable artifact SHA-256;
- retrieval metadata.

### DERIVATION_RUN
Auditable transformation:
- kind;
- deterministic/model/human/hybrid character;
- exact implementation/version;
- immutable prior ledger inputs;
- output entity references;
- execution time.

### CLAIM_SUPPORT
Evidence edge from a domain claim/entity to:
- one source observation;
- exact source span;
- span text hash;
- source artifact hash;
- evidence role/state;
- derivation run.

### SUPERSESSION
Append-only control record for:
- correction;
- supersession;
- retraction.

Historical records remain present. A current-view projection hides superseded records without deleting them.

## Record integrity

`record_hash` is SHA-256 over canonical JSON for the complete record excluding the hash field itself.

Consequences:
- key order does not affect the hash;
- any historical content change invalidates the hash;
- records cannot reference future ledger records;
- duplicate IDs fail;
- claim-support artifact hashes must match their source observation;
- competing direct supersessions of one record fail closed.

This is tamper-evident provenance, not a blockchain.

## First full provenance DAG

The Regulation 794/2004 Article 3 SANI atom is traced through:

1. Cellar source observation — 19 January 2007 checkpoint.
2. Cellar source observation — 14 April 2008 checkpoint.
3. Cellar source observation — authentic Regulation 271/2008.
4. deterministic AST normalization of before state.
5. deterministic AST normalization of after state.
6. deterministic Article 3 subtree diff.
7. deterministic evidence reconciliation.
8. authentic mutation-cause support edge.
9. temporal resolution for 1 July 2008.
10. temporal source support.
11. semantic extraction/adversary run.
12. exact semantic support span for the SANI duty.

The mutation separately retains BEFORE, AFTER and CAUSE support edges. Independent evidence does not collapse into one provenance blob.

## Correction semantics

A synthetic locator correction proves:
- old support record remains hash-verifiable and queryable;
- corrected support is a new record;
- SUPERSESSION links old → new;
- current view returns the new record and hides the superseded one.

A true RETRACTION may contain no replacement record.

## Durable invariants

1. Provenance is append-only.
2. Observation time is not legal-effect time.
3. Domain truth is referenced, not duplicated into ledger payloads.
4. Source bytes are content-addressed.
5. Derivation lineage references earlier immutable records.
6. Multiple evidence channels remain multiple support edges.
7. Corrections do not rewrite history.
8. Current-view projection is derived from supersession records.
9. No global provenance confidence score.
10. A public claim can trace to immutable official bytes.

## Post-freeze rule

Extend storage/database/indexing implementations behind this contract.

Reopen the core ledger model only if a real audit/provenance case cannot be represented without rewriting history or duplicating domain truth.

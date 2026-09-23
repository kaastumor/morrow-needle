# Decision — Provenance Ledger v0.2 source-origin neutrality

**Date:** 2026-09-23  
**Status:** ADOPTED  
**Issue:** #85

## Trigger

Issue #85 proved that legally relevant evidence may originate from a private
actor whose output is recognized by public law.

Provenance Ledger v0.1 allowed only official SOURCE_OBSERVATION source types.

Relabelling a private rating-agency page as OTHER_OFFICIAL would corrupt
provenance.

## Decision

Add `schemas/provenance-record-v0.2.schema.json`.

The ledger algorithm remains unchanged.

SOURCE_OBSERVATION now requires `source_origin`:

- `PUBLIC_OFFICIAL`
- `PRIVATE_PRIMARY`

A private-primary origin requires source type `PRIVATE_PRIMARY`.

A public-official origin cannot use that source type.

The hash, append-only ordering, claim-support and supersession semantics remain
unchanged.

## Separation

Provenance answers:

> where did the bytes/evidence come from?

Domain contracts answer:

> why may this source's determination matter legally?

The ledger must not infer legal recognition from private origin.

## Compatibility

Existing v0.1 official provenance mechanically upgrades by adding:

`source_origin: PUBLIC_OFFICIAL`

No historical hash is rewritten in-place. Existing v0.1 ledgers remain valid
v0.1 history; a v0.2 ledger is a new serialized contract.

## What is not added

- no trust score;
- no source reputation score;
- no web-archive system;
- no generic private-source crawler;
- no certification/accreditation registry;
- no inference that private primary means legally recognized.

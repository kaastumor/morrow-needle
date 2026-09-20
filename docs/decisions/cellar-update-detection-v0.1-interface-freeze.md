# Decision — Freeze Cellar Update Detection v0.1

**Date:** 2026-09-20
**Status:** ADOPTED
**Issue:** #13

## Decision

Freeze P1-B around:

- `schemas/cellar-ingestion-event-v0.1.schema.json`
- `schemas/source-change-v0.1.schema.json`
- `src/needle/updates/cellar_feed.py`
- `src/needle/updates/cursor.py`
- `src/needle/updates/poller.py`
- `src/needle/updates/classify.py`
- `.github/workflows/cellar-feed.yml`

The official Cellar ingestion feed is a **change-hint stream**, not evidence that legal text changed.

## Official history contract

The Publications Office documents the notification service as providing a
**complete history of performed ingestion actions**:

- https://op.europa.eu/en/web/cellar/cellar-data/rss-and-atom-feeds

That does **not** turn the feed into legal-history truth. Its `CREATE`,
`UPDATE`, and `DELETE` values describe Cellar ingestion actions. The documented
`priority` field is likewise the priority of ingestion of the element, not a
legal-materiality or product-ranking signal.

Consequences:

- historical replay is a supported source-audit capability;
- an ingestion action must still be reconciled with immutable source
  observations and canonical legal evidence;
- a missing match in one tested window is a locator/query failure until the
  official history contract itself is falsified;
- production identifiers are useful locators but should not outrank stable
  Cellar root identity when the latter is already known.
## Polling contract

- use inclusive, overlapping time windows;
- compare echoed window timestamps as absolute instants;
- page sequentially;
- advance the durable cursor only after the complete window finishes;
- parser failure leaves the window incomplete;
- dedupe by canonical event key;
- identical ingestion timestamps do not collapse distinct target resources.

## Live feed discovery

The official documentation example from 2012 remains a useful parser fixture. A permanent modern live anchor is also retained below; historical replay is tested separately from live-contract drift.

A live September 2026 probe exposed current service drift:

### RSS
Current RSS entries use:
- `<guid>` for event identity;
- no `notifEntry:id`;
- `notifEntry:date` for ingestion time;
- singular `notifEntry:wemiClass` plus the CDM class list.

### Atom
Current Atom entries expose:
- a literal unresolved template in `<id>`: `${item.cellarUri}_...`;
- no `notifEntry:date`;
- Atom `<updated>` as the usable ingestion timestamp.

Therefore feed-specific identity cannot be the sole idempotency contract.

## Canonical event identity

Needle derives:

`event_key = target cellar_id + "_" + ingestion_time`

This matches the live RSS guid and can be reconstructed from the Atom representation.

Raw feed identity is preserved separately with an explicit basis:
- NOTIFICATION_ENTRY_ID
- RSS_GUID
- ATOM_ID
- DERIVED_CELLAR_ID_TIME

The canonical event key is used for cross-format dedupe.

## Live replay anchor

The permanent CI contract replays:

- target: `cellar:55b240bf-477b-11f0-85ba-01aa75ed71a1`
- CELEX: `62024CC0286`
- action: UPDATE
- ingestion: `2026-09-15T00:05:50.647+02:00`

Live RSS and Atom resolve to the same canonical event and legal/resource identifiers.

Frozen evidence:
- `fixtures/updates/cellar-live-crossformat-anchor-v0.1.json`
- `fixtures/updates/cellar-live-guid-shape-20260915-v0.1.xml`
- `fixtures/updates/cellar-live-atom-template-shape-20260915-v0.1.xml`

## WEMI refresh scope

Feed events schedule targeted re-observation:
- WORK → work refresh;
- EXPRESSION → expression refresh;
- MANIFESTATION → manifestation refresh;
- ITEM → item + parent manifestation refresh;
- unknown → target + root fail-safe refresh.

The feed event never directly emits a legal mutation.

## Re-observation classification

After new immutable Source Observations are created, Needle deterministically classifies:

- SOURCE_CREATED
- CONTENT_CHANGED
- METADATA_ONLY
- AVAILABILITY_CHANGED
- NO_MATERIAL_CHANGE
- UNRESOLVED

Content and metadata remain separate official Source Observations.

A Cellar UPDATE may therefore legitimately become NO_MATERIAL_CHANGE.

## Source Change record

`source-change-v0.1` references:
- event key;
- target/root Cellar identity;
- feed action;
- refresh scope;
- previous content/metadata Source Observations;
- current content/metadata Source Observations;
- deterministic classification basis.

It contains no legal-effect semantics.

## Durable invariants

1. Feed UPDATE != legal change.
2. Feed serialization != canonical event identity.
3. Documentation examples != live replay anchors unless verified.
4. Replay/backfill is safe through overlap + canonical event-key dedupe.
5. Cursor advances only after complete pagination.
6. Parser drift fails closed.
7. Raw feed quirks survive as provenance.
8. Metadata-only change remains distinguishable from content change.
9. Content-byte change remains a source event until normalized legal-text comparison proves mutation.
10. DELETE changes availability history; prior Source Observations are never erased.

## Post-freeze rule

Extend scheduling/storage adapters behind these contracts.

Reopen only if a real Cellar event cannot be represented or replayed without event loss or false legal-change inference.

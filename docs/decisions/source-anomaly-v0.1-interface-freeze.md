# Decision — Freeze Source Anomaly v0.1 derived view

**Date:** 2026-09-20  
**Status:** ADOPTED  
**Issue:** #17

## Decision

Freeze the first Source Anomaly product contract around:

- `schemas/source-anomaly-composition-v0.1.schema.json`
- `schemas/source-anomaly-view-v0.1.schema.json`
- `src/needle/analytics/source_anomaly.py`
- `fixtures/analytics/source-anomaly-first-cohort-v0.1.json`
- `tests/test_source_anomaly_view.py`
- `.github/workflows/source-anomaly-view.yml`

Source Anomaly is a **read-only derived view over pinned source/audit evidence**.

It is not a legal-state model and it emits:

`NONE_FROM_SOURCE_ANOMALY_ALONE`

for legal-mutation inference.

## First frozen anomaly classes

### 1. ROUTE_FALLBACK

Proven case:
- CELEX:31990R2742R(01);
- preferred Publications Office Cellar CELEX route observed HTTP 404;
- authoritative EUR-Lex HTML and OJ PDF remained available and pinned the legal evidence.

Semantics:

`ROUTE_UNAVAILABLE_NOT_SOURCE_ABSENT`

The card carries the observation timestamp. A historical pinned 404 is never presented as the endpoint's current state.

### 2. SOURCE_INTERNAL_CONFLICT

Proven case:
- Directive 2008/7/EC;
- authentic Article 16 literally prints `69/355/EEC`;
- recital 1, Annex II and Annex III independently support canonical predecessor `69/335/EEC`.

Semantics:

`PRESERVE_LITERAL_AND_RESOLVE_CANONICAL_SEPARATELY`

Canonical identity resolution may differ from literal source text, but the authentic literal value remains immutable evidence.

### 3. REPRESENTATION_DUPLICATION

Proven case:
- Regulation 2025/905 Cellar Formex;
- the same publication DATE value occurs in document and table-of-contents streams;
- both occurrences have one unique evidentiary value.

Semantics:

`REPRESENTATION_DUPLICATION_NOT_CORROBORATION`

Repeated identical metadata does not multiply evidentiary weight.

If duplicate occurrences disagree, the builder fails closed instead of deduplicating silently.

## Ownership rule

The persisted Source Anomaly composition contains only audit-fixture references plus presentation guardrails.

It does not persist:

- HTTP results;
- artifact hashes;
- literal/canonical identifier values;
- duplicated metadata values;
- legal conclusions.

Those are derived from pinned evidence fixtures.

## Stable v0.1 principles

1. **Source state is not legal state.**
2. **Route failure is not source/law absence.**
3. **Literal official text is not silently rewritten.**
4. **Canonical resolution must expose independent support.**
5. **Duplicate representation is not independent corroboration.**
6. **Source anomaly does not create a legal mutation.**
7. **Pinned observations are time-scoped; they are not live-monitor claims.**
8. **No severity score or source-quality ranking exists in v0.1.**

## Public output

The first public view gives categorical cards with:

- anomaly kind;
- subject identifier;
- observed facts;
- explicit semantics;
- immutable evidence anchor;
- non-implications.

The 3-second summary reports only that pinned source-layer anomalies exist without treating them as legal changes.

## Deliberate limitations

v0.1 does not yet provide:

- continuous endpoint monitoring;
- source availability heatmaps;
- anomaly severity/ranking;
- automatic source remediation;
- language/format branch coverage maps;
- current-vs-pinned observation comparison;
- anomaly discovery over the entire corpus.

Those can be layered later without changing the categorical semantics above.

## Reopen rule

Reopen Source Anomaly v0.1 only if a real authoritative-source case cannot be represented without:

- treating source infrastructure state as legal state;
- discarding literal source evidence;
- counting duplicate representations as independent evidence;
- or inventing a legal mutation from source-layer irregularity.

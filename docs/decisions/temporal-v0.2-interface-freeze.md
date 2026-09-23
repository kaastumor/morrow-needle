# Decision — Temporal Semantics v0.2 precision extension

**Date:** 2026-09-23  
**Status:** ADOPTED  
**Issue:** #81

## Trigger

HVMFS 2025:4 specifies a legally operative fishery-closure interval to the
minute:

- 18 February 2025 at 01:00 Swedish time;
- through 4 March 2025 at 00:59 Swedish time.

Temporal v0.1 is date-only. Rounding changes legal answers within those boundary
days and is forbidden.

## Decision

Add a precision-aware temporal interface:

- `schemas/temporal-assertion-v0.2.schema.json`
- `schemas/temporal-query-v0.2.schema.json`
- `src/needle/temporal/resolver_v0_2.py`

v0.1 remains historical/stable for existing date-precision data.

v0.2 supports exactly two precision classes:

### DATE

Existing calendar-date semantics.

No timezone or implicit midnight is introduced.

v0.1 assertions can be upgraded mechanically by adding:

`precision = DATE`

without altering their legal meaning.

### INSTANT

Offset-aware ISO-8601 timestamps representing exact instants.

An INSTANT must carry an explicit UTC offset (or `Z`).

Naive local timestamps are rejected.

## Precision is semantic

DATE and INSTANT are not automatically comparable.

A query that would require silently converting a DATE boundary to an INSTANT
fails closed as:

`MIXED_PRECISION_UNRESOLVED`

This prevents assumptions such as:

- a date means local midnight;
- a date means UTC midnight;
- a source's unspecified timezone can be guessed from jurisdiction.

## Resolver behavior

The v0.2 resolver:

- delegates pure DATE cases to the proven v0.1 resolver;
- compares INSTANT boundaries in UTC;
- preserves inclusive/exclusive semantics;
- supports explicit minute/hour/day/month/year relative offsets for instant
  events;
- preserves context-required behavior;
- refuses mixed-precision comparison without evidence;
- retains the official-source perspective for DATE cases;
- supports INSTANT official-source perspective only where source availability is
  itself supplied at INSTANT precision, otherwise failing closed.

## Canonical adversary

`fixtures/temporal/skagerrak-prawn-rtc-v0.2.json`

must distinguish:

- 18 Feb 00:30 CET — inactive;
- 18 Feb 01:00 CET — active;
- 18 Feb 00:00 UTC — active;
- 4 Mar 00:59 CET — active;
- 4 Mar 01:00 CET — inactive.

## What v0.2 does not add

- timezone-name databases;
- daylight-saving inference;
- recurrence rules;
- business calendars;
- generic scheduling;
- implicit conversion of dates to instants.

If a future source uses a named civil timezone where the offset cannot be
established directly from evidence, Needle must preserve that as unresolved
rather than infer it.

## Existing invariants retained

All v0.1 separation remains:

- publication vs force vs application vs text state;
- transition and derogation layers;
- explicit scope/override;
- relative event provenance;
- bitemporal source perspective;
- context-required abstention;
- inclusive/exclusive boundaries.

The only reopened dimension is **temporal precision**.

## Post-repair status

Issue #81 resolves the official representational failure.

Spatial work from Issue #80 may resume only after this contract and its
backward-compatibility regressions are green.

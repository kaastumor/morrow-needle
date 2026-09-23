# Foundation reopen — Temporal v0.1 loses legally meaningful minutes

**Date:** 2026-09-23  
**Issue:** #81  
**Status:** representational failure pinned before schema change

## Source adversary

Swedish HVMFS 2025:4 creates a real-time Northern prawn fishery closure in a
specific Skagerrak polygon.

The decision was taken on 17 February 2025.

The legal interval is not expressed merely as dates:

- **start:** 18 February 2025 at 01:00 Swedish time;
- **last included minute:** 4 March 2025 at 00:59 Swedish time.

Commission Delegated Regulation (EU) 2019/2201 Article 8 explains the UTC
mechanism:

- entry into force at 24:00 UTC on the day of decision;
- automatic cessation at midnight UTC after 14 days.

In winter Sweden is UTC+01:00, yielding the exact half-open interval:

```
[2025-02-18T01:00:00+01:00,
 2025-03-04T01:00:00+01:00)
```

equivalent to:

```
[2025-02-18T00:00:00Z,
 2025-03-04T00:00:00Z)
```

## Why date-only is wrong

A date-only model answers at least two questions incorrectly.

At:

`2025-02-18T00:30+01:00`

the calendar date is 18 February, but the closure has **not started**.

At:

`2025-03-04T00:59+01:00`

the closure is **still active**, even though a naive exclusive END on
2025-03-04 could remove the entire day.

The minute boundary is therefore legal semantics, not presentation detail.

## Existing v0.1 failure

Temporal Assertion v0.1 uses JSON Schema `format: date` for:

- `normalized_date`;
- absolute trigger dates;
- guards.

The resolver uses Python `datetime.date`.

It has no representation for:

- time-of-day;
- offset-aware instant;
- UTC equivalence;
- sub-day query instants.

Rounding is forbidden because it changes answers.

## Reopen criterion

The Temporal v0.1 decision says the core contract reopens only when an official
source demonstrates a legal-time phenomenon that cannot be represented through
another assertion, scope, relative trigger, perspective or bounded transition.

This case qualifies directly.

No combination of additional date-only assertions can distinguish 00:30 from
01:00 on the same calendar date.

## Required evolution

The next contract must support both:

1. **DATE precision**, preserving all current cases;
2. **INSTANT precision**, using offset-aware ISO-8601 timestamps.

It must continue to preserve:

- point/start/end boundary semantics;
- inclusive/exclusive boundaries;
- relative-event offsets;
- context-required behavior;
- source-availability perspective.

It must not invent an implicit timezone for a source that omitted one.

## Why spatial work pauses

The fishery closure was discovered while testing legal geography.

A spatial state pointing to date-only temporal truth would knowingly encode a
wrong validity boundary.

Issue #80 therefore pauses at the spatial layer until #81 repairs the canonical
temporal owner.

# Discovery — when an official number becomes a legal input

**Date:** 2026-09-23  
**Issue:** #79  
**Status:** representational failure pinned; no new schema yet

## The specimen

The EU ETS Market Stability Reserve does not ask whether an entity is on a list.

It asks what an officially computed number is.

Decision (EU) 2015/1814 requires the Commission to publish the **Total Number of
Allowances in Circulation (TNAC)** every year.

The current Article 1 rules use that published number to determine reserve
operation.

For the band relevant to the 2025 TNAC:

```
833,000,000 <= TNAC <= 1,096,000,000

reserve placement = TNAC - 833,000,000
```

Commission Communication C/2026/2957 publishes the 2025 TNAC as:

```
1,023,494,202
```

Independent arithmetic:

```
1,023,494,202
- 833,000,000
-------------
  190,494,202
```

The Communication reaches the same result: **190,494,202 allowances** are to be
placed in the Market Stability Reserve from 1 September 2026 to 31 August 2027.

The later auction calendars reflect that reserve placement.

## Why this is not an authoritative dynamic set

Nothing meaningful is being added to or removed from a collection.

There is no member identity.

There is no membership state.

There is one scalar authoritative observation:

> TNAC = 1,023,494,202 allowances.

That number is evaluated against a fixed legal rule.

The causal shape is:

```
official source data
        ↓
authoritative computed metric
        ↓
fixed legal threshold / formula
        ↓
computed legal quantity
        ↓
temporal application window
        ↓
auction-volume adjustment
```

Calling 1,023,494,202 a “member” of a set would satisfy neither law nor data
semantics.

## Existing-contract probe

### Source Observation v0.1 — partial

It can preserve the bytes of the official Communication.

It deliberately says artifact observation alone does not imply legal mutation.

Correct.

But it has no canonical concept for:

- a metric name;
- numeric value and unit;
- reference period;
- calculation provenance;
- legally operative metric role.

### Authoritative Dynamic Set v0.1 — fails

Its causal primitive is member membership/status transition.

TNAC is a scalar measurement/calculation.

No honest member exists.

### Temporal v0.1 — partial

It can own:

- publication date;
- 1 September 2026 application start;
- 31 August 2027 end.

It should not own:

- 1,023,494,202 allowances;
- the 833m / 1.096bn band;
- the subtraction formula.

### Change Atom v0.3 — fails as direct owner

The governing legal rule is not textually changed by C/2026/2957.

A verified Change Atom still requires a source textual mutation.

Inventing one would destroy the distinction between:

- text change;
- authoritative observation;
- rule evaluation.

## The more interesting conceptual split

This case suggests that even “authoritative metric” may hide two things:

1. **Metric observation**
   - TNAC = 1,023,494,202
   - authority, source, period, unit, evidence

2. **Rule evaluation**
   - metric falls in a particular legal band
   - formula executes
   - result = 190,494,202

Those should probably not be collapsed.

The observation can remain true even if the legislature later changes the
thresholds or formula.

Likewise the rule can remain unchanged while next year's observation produces a
different result.

## Why I am stopping before architecture

One metric-controlled legal regime proves that existing contracts cannot
represent the causal chain without distortion.

It does not yet prove the right generic contract.

The next useful move is a second independent case outside carbon-market supply.

If that second case also has:

- authoritative scalar observation;
- fixed legal predicate/formula;
- downstream legal consequence;

then the abstraction earns its existence.

Until then this remains a pinned architecture gap, not a schema request.

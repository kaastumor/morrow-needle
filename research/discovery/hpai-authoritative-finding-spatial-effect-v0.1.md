# Discovery — a confirmed disease creates legal geography

**Date:** 2026-09-23  
**Issue:** #80  
**Status:** representational failure pinned; no schema added

## Why this is different

The previous wild runs found non-textual causes in:

- authoritative set state;
- authoritative numeric observations.

This case is neither.

On 17 July 2026 the Dutch government reported that highly pathogenic avian
influenza had been confirmed at a hobby bird holding in Woerdense Verlaat.

The legal input is categorical:

> HPAI is officially confirmed at this affected location.

The numeric coordinates are attributes of the location. They are not the
substantive legal trigger.

## Fixed law, new real-world fact

Regulation (EU) 2016/429 Article 60 requires immediate disease-control action
when a Category A outbreak in kept animals is officially confirmed, including
declaration of the affected location as infected and establishment of an
appropriate restricted zone.

Article 64 places that zone around the affected location.

Delegated Regulation (EU) 2020/687 Article 21 and Annex V provide the spatial
minimums for HPAI:

- protection zone: 3 km;
- surveillance zone: 10 km.

Nothing in those provisions needs to change when a new outbreak occurs.

## Concrete chain

For outbreak `NL-HPAI(NON-P)-2026-00174`:

```
official categorical finding
HPAI confirmed
        │
        ▼
affected location
Woerdense Verlaat
        │
        ▼
binding spatial rule
HPAI → 3 km / 10 km
        │
        ▼
new legal geography
protection + surveillance zones
        │
        ▼
time-bounded controls
movement restrictions etc.
```

The Dutch source says the zones and transport ban applied immediately.

The later Commission implementing decision preserves the outbreak reference and
publishes the corresponding zones centred at WGS84 52.16 / 4.89, with the
protection zone applicable through 8 August 2026 and surveillance zone through
17 August 2026.

## Two missing layers, not one

### 1. Authoritative categorical finding

Needle needs a way to preserve direct official truth of the form:

> authority X officially established condition Y about subject/location Z.

That is not numeric metric truth and is not set membership.

### 2. Spatial rule evaluation

The 3 km / 10 km geography is not itself the scientific finding.

It is a legal consequence produced by applying an unchanged spatial rule to the
finding's location.

These layers must remain separate because:

- the same outbreak finding would remain historically true if future law changed
  the radii;
- a corrected outbreak location would alter the derived geometry without
  mutating the legal radius rule;
- duration belongs to Temporal, not geometry.

## Existing-contract probe

### Authoritative Metric Observation — fails

Disease confirmation is categorical.

Coordinates do not turn the disease state into a metric.

### Authoritative Dynamic Set — fails as causal owner

A later legal source can list the affected zones.

But that list state is downstream.

The trigger is the official disease finding.

### Temporal — partial

It can own finding/publication/control boundaries.

It cannot own the disease finding or geometry.

### Metric Rule Evaluation — fails

The bounded scalar arithmetic contract should not be stretched into geospatial
operations.

### Change Atom — fails

No textual mutation causes this event.

## Important historical-source distinction

The later EU implementing decision is not allowed to erase or replace the
earlier national confirmation.

The national competent authority had already confirmed the outbreak and imposed
measures immediately.

The EU source provides later Union-level zone publication/coordination evidence.

That chronology itself is part of the legal story.

## Why architecture stops here

One animal-health case proves an existing representational gap.

It does not prove that the right general abstraction is
`AUTHORITATIVE_CATEGORICAL_FINDING`.

Before freezing that phrase, I want an unrelated official case where a
non-numeric authoritative determination changes the operation of unchanged law.

Likewise, one radius-based disease zone does not justify a generic GIS engine.

The failure is pinned first.

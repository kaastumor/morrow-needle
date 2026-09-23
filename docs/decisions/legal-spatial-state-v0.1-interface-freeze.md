# Decision — Legal Spatial State v0.1

**Date:** 2026-09-23  
**Status:** ADOPTED  
**Issue:** #80

## Problem

Issue #80 began as a search for legal consequences controlled by real-world
scientific/geographic state.

It found two distinct spatial cases.

### HPAI protection zone

Official confirmation of outbreak
`NL-HPAI(NON-P)-2026-00174` triggers disease-control rules.

The Union zone decision directly describes the protection zone as:

- WGS84 centre: 52.16 / 4.89;
- radius: 3 km.

### Skagerrak real-time fishery closure

HVMFS 2025:4 directly prohibits Northern prawn fishing inside a polygon bounded
by straight lines through six distinct WGS84 vertices.

The source repeats the first point as point 7 to close the ring.

This case also exposed and caused repair of the separate Temporal v0.1 sub-day
precision defect in Issue #81.

## Decision

Introduce:

`schemas/legal-spatial-state-v0.1.schema.json`

The contract owns **officially operative legal geometry**.

It does not own a spatial rules engine.

## v0.1 geometry vocabulary

Only shapes demonstrated by the two official cases are supported:

- `CIRCLE`
- `POLYGON`

Both use WGS84.

The geometry must be backed by direct official geometry evidence.

## Separation from causal truth

A spatial state may reference canonical causal inputs:

- Authoritative Finding;
- Authoritative Metric Observation;
- bounded other official context.

Each causal reference carries its own evidence state.

This matters for the fishery case.

HaV records a 66.50% juvenile Northern prawn sample on 16 February 2025.
That exceeds the then-applicable one-sample >40% recommendation threshold.
HVMFS 2025:4 was decided the following day.

The causal relation is useful but is retained as **DERIVED**, because the
specific sample-to-HVMFS decision relation is not promoted to direct evidence
without an explicit source binding.

The polygon itself is DIRECT official legal geometry regardless.

## Separation from time

Legal Spatial State stores only
`temporal_assertion_refs`.

It never copies start/end dates or instants.

This was made non-negotiable by Issue #81: HVMFS 2025:4 has minute-specific
boundaries that belong to Temporal v0.2.

## Separation from source observations and metrics

Coordinates are not automatically legal metrics.

A point can be an attribute of a finding or geometry without entering the
Authoritative Metric Observation causal path.

Likewise, storing polygon coordinates does not create a spatial computation.

## What v0.1 does not do

- no point-in-polygon queries;
- no polygon area computation;
- no buffers;
- no intersections or overlays;
- no routing;
- no geocoding;
- no administrative-boundary resolution;
- no GIS engine;
- no inference from an illustrative map where source coordinates exist.

## Proof fixtures

- HPAI protection circle:
  `fixtures/spatial/hpai-woerdense-verlaat-protection-zone-v0.1.json`
- Skagerrak fishery closure polygon:
  `fixtures/spatial/skagerrak-prawn-rtc-hvmfs-2025-4-v0.1.json`

The Swedish source-coordinate strings are preserved alongside normalized decimal
degrees; normalization must be mechanically checkable.

## Reopen rule

Reopen only when an official case requires legal geometry that cannot be
represented without distortion as:

- a WGS84 circle;
- a WGS84 polygon;
- direct geometry evidence;
- causal references;
- temporal assertion references.

Likely future reopen candidates include multipolygons, holes, line/corridor
geometry, legally defined administrative units or moving/dynamic geometry.
Those are not added pre-emptively.


## Reopen and resolution — Issue #82

The v0.1 contract was legitimately reopened by official Dutch aviation
sources that define legal airspace as a **volume**, not merely a 2D footprint.

Pinned adversaries:

- an Article 15 UAS geographical zone with a WGS84 polygon and vertical extent
  0-120 M AGL;
- EHP26, whose polygon applies from GND to 2000 FT AMSL;
- EHR3A, whose polygon applies from 3000 FT AMSL to FL185.

Flattening any of these to 2D would project the legal restriction through
altitudes the official source does not claim.

The gap is resolved by:

- `schemas/legal-spatial-state-v0.2.schema.json`;
- `docs/decisions/legal-spatial-state-v0.2-interface-freeze.md`.

v0.2 leaves the v0.1 horizontal geometry untouched and adds a separate
null-or-typed `vertical_extent`.

v0.1 remains valid provenance for the HPAI and Skagerrak 2D proof cases.

No 3D GIS, terrain model, pressure-altitude conversion or aviation rules engine
was added.

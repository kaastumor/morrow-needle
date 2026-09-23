# Decision — Legal Spatial State v0.2 vertical extent

**Date:** 2026-09-23  
**Status:** ADOPTED  
**Issue:** #82

## Trigger

Legal Spatial State v0.1 supports direct official WGS84 circles and polygons.

Official aviation sources demonstrate that a horizontal footprint alone can be
legally incomplete.

### UAS geographical zones

The Dutch Article 15 digital data set publishes UAS zones with:

- horizontal polygon geometry;
- lower vertical limit;
- upper vertical limit;
- vertical reference such as AGL.

### Conventional prohibited/restricted airspace

The Dutch AIP independently publishes airspace such as:

- EHP26: polygon, GND to 2000 FT AMSL;
- EHR3A: polygon, 3000 FT AMSL to FL185.

Representing these only as 2D polygons would incorrectly project the legal
restriction through all altitudes.

## Decision

Add:

`schemas/legal-spatial-state-v0.2.schema.json`

v0.2 preserves the v0.1 horizontal geometry contract and adds one required
top-level field:

`vertical_extent`

It is either:

- a typed direct official vertical extent; or
- `null`.

## Meaning of null

`vertical_extent: null` means:

> this object makes no canonical assertion about vertical extent.

It does **not** mean:

- ground to infinity;
- all altitudes;
- zero height;
- spatially irrelevant altitude.

The two v0.1 proof cases mechanically upgrade with `vertical_extent: null`.

## Supported vertical boundary types

Only source semantics demonstrated by the official adversaries are introduced.

### SURFACE

For source expressions such as:

`GND`

No numeric altitude is manufactured.

### ALTITUDE

Preserves:

- numeric value;
- source unit;
- source vertical reference/datum;
- exact source expression.

Examples:

- 120 M AGL;
- 2000 FT AMSL;
- 3000 FT AMSL.

`unit` and `reference` are preserved strings rather than normalized enums
because v0.2 makes no datum-conversion claim.

### FLIGHT_LEVEL

Preserves:

- flight-level number;
- `FL` unit;
- source expression.

Example:

`FL185`.

A flight level is not converted to geometric altitude.

## Comparison policy

Every non-null vertical extent states:

`PRESERVE_SOURCE_REFERENCE_NO_IMPLICIT_CONVERSION`

Needle v0.2 therefore does not answer cross-reference questions such as whether
120 m AGL is above or below a particular AMSL altitude at a location.

Those require additional authoritative terrain/pressure context and are outside
this contract.

## Separation from operational rules

A UAS zone can have a published volume of 0-120 m AGL while an operational
condition permits a category only to 30 m AGL.

The volume and the permission ceiling are different legal facts.

Legal Spatial State owns the official extent.

It does not absorb category-specific operational conditions.

## Separation from time

Temporal v0.2 remains the sole owner of validity/activation boundaries.

Legal Spatial State stores only temporal assertion references.

No recurrence, H24 schedule, NOTAM activation or validity period is copied into
the spatial contract.

## Backward compatibility

The existing HPAI and Skagerrak fixtures are retained as v0.1 provenance.

v0.2 upgrade fixtures add only:

- schema version v0.2;
- `vertical_extent: null`;
- a guardrail clarifying null semantics.

Their geometry, causal references and temporal references remain unchanged.

## What v0.2 does not add

- 3D point/volume intersection;
- terrain lookup;
- pressure-altitude conversion;
- AGL/AMSL conversion;
- flight-level conversion;
- vertical overlap calculation;
- route/trajectory evaluation;
- UAS operational-permission rules;
- NOTAM/AUP activation engines;
- generic aviation airspace modeling.

## Reopen rule

Reopen only when an official case cannot be represented without distortion as:

- existing WGS84 circle/polygon horizontal geometry;
- null vertical extent; or
- lower/upper vertical boundaries of SURFACE, ALTITUDE or FLIGHT_LEVEL type;
- source-preserved vertical semantics;
- separate temporal references.

Known future candidates include unlimited boundaries, composite vertical limits,
terrain-following surfaces, geometry that changes with altitude, and true
4D/moving volumes. They are not added pre-emptively.

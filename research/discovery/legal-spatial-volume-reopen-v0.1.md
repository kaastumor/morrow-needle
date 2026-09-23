# Foundation reopen — legal geography has a vertical axis

**Date:** 2026-09-23  
**Issue:** #82  
**Status:** representational failure pinned before spatial-contract change

## Trigger

Legal Spatial State v0.1 deliberately stopped at WGS84 circles and polygons.

That was enough for:

- the Woerdense Verlaat HPAI protection circle;
- the Skagerrak fishery real-time closure polygon.

Aviation breaks the assumption.

## Case 1 — Dutch UAS geographical zone 2.a

The Dutch eAIP states that UAS geographical-zone information is publicly
available in a digital JSON data set under Implementing Regulation
(EU) 2019/947 Article 15 and the EASA common-format guidance.

Record **2.a** contains:

- a WGS84 polygon;
- lower limit **0 m AGL**;
- upper limit **120 m AGL**.

The record also says OPEN A1/A2 operations are allowed only up to 30 m AGL and
A3 is not allowed.

That proves two vertical facts must not be collapsed:

1. the **published zone volume** is 0–120 m AGL;
2. an **operational condition inside that volume** permits some flights only up
   to 30 m AGL.

Legal geometry should own the first, not absorb the second.

## Clean conventional-airspace proof — EHP26

The first draft used EHP25. That was intentionally replaced before architecture
because EHP25's 0.5 NM circle would also pressure the v0.1 circle-radius unit and
muddy the vertical-only diagnosis.

**EHP26 ROYAL PALACES AND GOVERNMENT BUILDINGS** is cleaner:

- horizontal geometry: polygon;
- lower limit: **GND**;
- upper limit: **2000 FT AMSL**;
- H24 prohibited area.

A polygon is already a v0.1 horizontal shape.

The only missing canonical fact is its vertical legal extent.

## Known flight-level proof — EHR3A

The same official AIP already supplies a second vertical semantic class:

**EHR3A OLDEBROEK**

- horizontal geometry: polygon;
- lower limit: **3000 FT AMSL**;
- upper limit: **FL185**.

Therefore a repair that knows only AGL/AMSL numeric heights would be knowingly
incomplete on day one.

A flight level is pressure-based aeronautical semantics. Needle may preserve the
source value and type; it may not silently turn FL185 into a geometric altitude.

## Why v0.1 fails

The v0.1 schema has only:

- CIRCLE;
- POLYGON.

Its geometry definitions contain no vertical extent.

Because `additionalProperties` is false, adding an honest vertical field makes
the object invalid.

Dropping the field is worse: a 2D footprint could be read as restricted at all
altitudes.

Storing altitude only in prose would make a legally operative boundary invisible
to validation and downstream reconstruction.

## Vertical reference is semantic

The repair must preserve distinctions such as:

- AGL;
- AMSL;
- surface/GND;
- flight level.

No terrain model, pressure model or datum conversion is justified.

## Ownership boundaries retained

Temporal v0.2 still owns when a volume is valid or active.

Spatial state owns where it applies, including vertical extent.

Operational permissions/restrictions within the volume remain legal-rule
semantics; they are not geometry.

## Required next move

Evolve only Legal Spatial State.

The smallest viable change is a required v0.2
`vertical_extent` field that may be null for legacy 2D legal geometry and may
otherwise preserve typed lower/upper vertical boundaries.

Existing HPAI/fishery objects should upgrade mechanically by setting
`vertical_extent: null`.

No 3D GIS engine, volume intersection, terrain conversion, pressure-altitude
conversion or flight-level conversion is justified.

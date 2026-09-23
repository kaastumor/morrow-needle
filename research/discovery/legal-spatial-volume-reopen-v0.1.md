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

That last rule is important because it proves two vertical facts must not be
collapsed:

1. the **published zone volume** is 0–120 m AGL;
2. an **operational condition within that volume** permits some flights only up
   to 30 m AGL.

Legal geometry should own the first, not absorb the second.

## Case 2 — EHP25 DRAKENSTEIJN CASTLE

The Dutch AIP defines EHP25 as prohibited airspace:

- circle radius **0.5 NM**;
- centre **521047N 0051338E**;
- lower limit **GND**;
- upper limit **2000 FT AMSL**;
- active H24.

This is not a UAS-format curiosity.

Conventional prohibited airspace has the same fundamental shape:

> horizontal footprint + vertical extent = legal airspace volume.

## Why v0.1 fails

The v0.1 schema has only:

- CIRCLE;
- POLYGON.

Its geometry definitions contain no vertical extent.

Because `additionalProperties` is false, adding an honest vertical field makes
the object invalid.

Dropping the field is worse: a 2D footprint could be read as prohibited at all
altitudes.

Storing altitude only in prose would make a legally operative boundary invisible
to validation and downstream reconstruction.

## Vertical reference is semantic

The eventual repair may not flatten:

- AGL;
- AMSL;
- MSL;
- flight levels;
- GND/surface;
- unlimited upper boundaries

into one generic numeric height.

For example:

`120 m AGL`

and

`2000 ft AMSL`

do not become comparable merely because both can be expressed with numbers and
units.

No terrain model, atmospheric model or datum conversion is justified by these
two cases.

The contract should preserve source reference semantics first.

## Ownership boundaries retained

Temporal v0.2 still owns when a volume is valid or active.

Spatial state owns where it applies, including vertical extent.

Operational permissions/restrictions within the volume remain legal-rule
semantics; they are not geometry.

## Required next move

Evolve only Legal Spatial State.

The smallest viable change is an **optional vertical extent** attached to the
existing horizontal geometry.

Existing HPAI/fishery 2D objects must remain valid or mechanically upgradeable.

No 3D GIS engine, volume intersection, terrain conversion or flight-level
conversion is justified.

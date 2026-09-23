# Decision — Authoritative Finding v0.1

**Date:** 2026-09-23  
**Status:** ADOPTED  
**Issue:** #80

## Problem

Needle already had direct canonical objects for:

- source observations;
- authoritative dynamic-set state;
- authoritative numeric metrics.

It lacked a direct object for an authority establishing a **categorical
condition about a concrete subject** where unchanged law makes that
determination legally relevant.

Two orthogonal cases prove the gap.

## Proof case 1 — HPAI

On 17 July 2026 Dutch authorities reported HPAI confirmed at a holding in
Woerdense Verlaat.

The finding is categorical:

`HPAI_CONFIRMED`

Regulation (EU) 2016/429 makes official confirmation legally operative for
immediate disease-control measures.

The finding does not itself own the later 3 km/10 km zone geometry.

## Proof case 2 — Port State Control

On 18 July 2026 the Paris MoU records BAHAR (IMO 8230156) as detained in
Psakhna, Greece.

The official notice states that 13 deficiencies were found and all were grounds
for detention.

The legally material direct truth is categorical:

`DETAINABLE_DEFICIENCIES`

Directive 2009/16/EC Article 19 and Annex X provide the detention framework.

This is professional inspection judgment, not scientific diagnosis.

## Decision

Introduce:

`schemas/authoritative-finding-v0.1.schema.json`

A finding owns only:

1. finding identity;
2. finding type;
3. authority / official control system;
4. concrete subject identity;
5. optional point/location context;
6. finding date;
7. categorical proposition and polarity;
8. direct official evidence;
9. binding legal-relevance references.

## Finding types

v0.1 deliberately keeps a small vocabulary:

- `SCIENTIFIC_CONFIRMATION`
- `INSPECTION_DETERMINATION`
- `OFFICIAL_CLASSIFICATION`
- `OTHER_OFFICIAL_DETERMINATION`

These describe the authority's determination mode, not the downstream legal
effect.

## Ownership boundary

Authoritative Finding does **not** own:

- textual mutation;
- numeric metric truth;
- authoritative-set membership;
- generic rule evaluation;
- enforcement lifecycle;
- spatial zones/polygons/radii;
- temporal application intervals.

The optional `location_ref` identifies where a finding occurred. It is a
point/context reference, not legal geometry.

## Why no generic finding-rule engine

The two proof cases share a direct finding shape.

Their downstream consequences do not yet share a sufficiently narrow canonical
shape:

- HPAI requires spatial derivation plus temporal controls;
- port-state inspection produces detention within a professional-judgment
  enforcement framework.

Generalising those consequences now would create a generic rules engine.

## Spatial question remains open

The HPAI proof leaves a separate unresolved question:

> how should Needle represent a binding legal rule that transforms a finding
> location into legal geography such as a 3 km protection zone and 10 km
> surveillance zone?

One disease-zone case is insufficient evidence for a general spatial contract.

The architecture should wait for a second unrelated spatial adversary.

## Reopen rule

Reopen Authoritative Finding v0.1 only when an official case demonstrates that:

- categorical proposition + polarity cannot represent the direct determination;
- finding authority cannot be represented without collapsing source authority;
- subject identity and optional point/location context are insufficient;
- a direct finding cannot remain independent from its downstream legal
  consequence.


## Downstream spatial resolution — Issue #80

The spatial question left open by this decision is now resolved separately by:

- `schemas/legal-spatial-state-v0.1.schema.json`
- `docs/decisions/legal-spatial-state-v0.1-interface-freeze.md`

Authoritative Finding v0.1 remains unchanged.

The HPAI finding owns only the categorical official confirmation and its subject/location context. The downstream 3 km protection-zone geometry is owned by Legal Spatial State v0.1 and its validity boundaries remain in Temporal v0.2.

This preserves the original finding ownership boundary rather than expanding it after the spatial proof cases.

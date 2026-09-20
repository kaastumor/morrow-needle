# Representation Completeness Contract v0.1

**Status:** foundation rule  
**Origin:** live Cellar probe of CELEX 32004R0794  
**Date:** 2026-09-20

## Problem

A representation can be highly structured without being text-complete.

The English FMX4 manifestation for Regulation 794/2004 is a concrete warning:
- 131 entries;
- 7 XML files;
- 124 TIFF files.

Therefore a manifestation selected for structural quality cannot automatically be assumed to contain all legally relevant content as machine-readable text.

## New distinction

### Primary representation
The official manifestation chosen as the best parser input for legal structure.

Example preference:
FMX4 → XHTML → HTML → text-bearing PDF.

### Companion representation
Another official manifestation acquired because it may improve or verify completeness, visual fidelity, ordering, or text recovery.

The companion does not silently override the primary source. It provides an independent official witness.

## Invariant

> **Representation preference is a parser decision, not a completeness claim.**

Needle must explicitly assess completeness after selecting a primary representation.

## Completeness signals

Signals that should trigger companion-manifestation inspection include:

- raster/image assets inside a structured bundle;
- included fragments whose text cannot be mapped;
- low mapped-visible-text ratio;
- opaque forms/annexes;
- unresolved inclusions;
- parser warnings or unknown source kinds;
- large differences in apparent content volume between official manifestations;
- tables or formulas represented graphically;
- source-native objects that the adapter cannot interpret.

## Representation roles

- `PRIMARY_STRUCTURE` — best source for structural parsing.
- `TEXT_WITNESS` — independent official source for visible text completeness.
- `VISUAL_WITNESS` — official page/render representation for layout, forms, images or formulas.
- `PROVENANCE_WITNESS` — representation containing useful provenance/markup absent elsewhere.
- `FALLBACK` — used only where the primary cannot represent a region.
- `AUDIT_ONLY` — retained for consistency checks but not merged.

One manifestation may have multiple roles.

## Merge discipline

Needle does **not** create a synthetic legal text by casually mixing representations.

A companion may contribute text to the canonical AST only when:
1. the primary region is explicitly incomplete/opaque;
2. the companion region can be aligned to the same legal location;
3. source provenance is retained at segment/node level;
4. the substitution/augmentation is declared in the parse report;
5. conflicts remain visible.

Where alignment is uncertain, preserve both witnesses and mark the AST region incomplete.

## Images and OCR

Raster content is not treated as empty content.

If official text-bearing companion representations cannot recover it:
1. retain the image as an opaque source object;
2. attempt deterministic metadata/alignment first;
3. use OCR only as a last-resort derivative;
4. mark OCR text as derived, never source-native;
5. require stronger verification before OCR-derived content can support a public legal claim.

## AST consequence

Canonical AST nodes/segments may carry different Source Observation anchors within one legal-text state.

That is intentional.

The AST is a provenance-preserving legal representation, not a claim that one physical source file contained everything.

## Completeness state

Each AST state should eventually carry:
- `COMPLETE_SINGLE_REPRESENTATION`
- `COMPLETE_MULTI_REPRESENTATION`
- `PARTIAL_KNOWN_GAPS`
- `UNKNOWN_COMPLETENESS`

The word `COMPLETE` requires explicit checks; it is never the default.

## Current test case

For CELEX 32004R0794 / ENG:
- FMX4 is currently the primary structural candidate.
- XHTML/PDF are candidate completeness/visual witnesses.
- The FMX4 bundle's 124 TIFF assets make a completeness audit mandatory before the AST can claim full coverage.

The follow-up live probe found that the official XHTML manifestation is a single 49,863,735-byte HTML file with approximately **66,258 visible text characters** and **zero `<img>` tags**.

By contrast, a coarse visible-text estimate across the seven FMX XML files totals roughly **31,500 characters**, while the same FMX bundle contains 124 TIFF assets.

These metrics are deliberately not treated as exact semantic coverage measurements, but they decisively reject the assumption that FMX4's structural richness implies standalone machine-text completeness.

### Adopted consequence

For raster-heavy structured manifestations, Needle uses a **representation ensemble**:
- FMX4 as `PRIMARY_STRUCTURE` and often `PROVENANCE_WITNESS`;
- XHTML/HTML as `TEXT_WITNESS` when available;
- PDF as `VISUAL_WITNESS`.

The canonical AST may be assembled from more than one official manifestation, but only through explicit alignment with source-level provenance.

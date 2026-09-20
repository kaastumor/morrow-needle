# Decision — Freeze Canonical Legal AST v0.1 interface

**Date:** 2026-09-20  
**Status:** ADOPTED  
**Issue:** #4  
**Scope:** canonical AST contract, not source adapters

## Decision

Freeze `schemas/legal-ast-v0.1.schema.json` as the first stable internal legal-text-state interface.

Source adapters remain versioned and may continue to improve. A newly discovered source quirk should normally change:
- an adapter;
- a source-accounting rule;
- a regression fixture;
- or representation-completeness handling;

rather than changing the canonical AST.

A core-schema change now requires evidence that an official source contains legally relevant information that **cannot be represented defensibly** by the current node / segment / reference / annotation model. Such a change should produce a versioned successor contract rather than silently changing v0.1 semantics.

## Why freeze now

The contract has survived the intended adversarial fixture classes.

### 1. Modern fragmented Formex

`32004R0794` / ENG:
- `FULL_STRUCTURAL`;
- zero unknown native structural kinds;
- zero unexplained source-text atoms;
- zero duplicate ownership claims;
- 13 Articles;
- 77 Paragraphs;
- 15 Recitals;
- 5 Annexes;
- grouped sequences, lists, footnotes, headings and signatures represented;
- fragmented/multi-asset manifestation handled.

Its completeness remains `UNKNOWN_COMPLETENESS` because 124 raster assets still require companion-representation checks. This is intentional: **structural fidelity and representation completeness are different axes.**

### 2. Early historical HTML

`31958R0001` / ENG:
- all 8 Articles recovered;
- all measured visible source text accounted for;
- zero unexplained text;
- zero duplicate ownership;
- no unknown native kinds.

It remains `PARTIAL_STRUCTURAL` because the historical HTML source does not expose modern Formex-level hierarchy. The AST does not invent structure that the source does not support.

### 3. Large consolidated Formex with provenance

`02004R0794-20250813` / ENG:
- `FULL_STRUCTURAL`;
- zero unknown native structural kinds;
- zero unexplained source-text atoms;
- zero duplicate ownership claims;
- 15 Articles;
- 8 Annexes;
- 197 Tables and 1,268 table cells;
- 739 Footnotes;
- 448 grouped sequence blocks;
- Parts, Chapters and Sections recovered semantically rather than by naive tag identity;
- 48 embedded consolidation-modification annotations retained;
- official ELI targets retained as first-class references.

The live contract validates these expectations against current official Cellar data.

## Important corrections made before freeze

The freeze is valuable because the model survived several cases where the simpler design was wrong:

1. **Source `TITLE` is polymorphic.** It can represent Chapter, Part, Section, document/form heading, etc. Needle now derives canonical structure from source-visible semantics rather than mapping every `TITLE` to canonical `TITLE`.
2. **Mixed XML flow matters.** Parent text and child tails around nested tables/notes must retain exactly one owner.
3. **Labels cannot claim nested structures.** A title's inline label text is separate from a nested footnote or other legal structure.
4. **Transparent wrappers may be partially owned.** The parser traverses claimed/unclaimed source atoms instead of flattening the whole wrapper.
5. **Production/document-family metadata is not legal body text.** FMX/publication metadata and family-composition information remain accounted provenance without leaking into legal segments.
6. **Zero text loss is not structural proof.** Source-text accounting and structural fidelity remain separate gates.
7. **Full structural fidelity is not completeness.** Raster/opaque regions can keep a state at `UNKNOWN_COMPLETENESS` even when the structured representation is parsed perfectly.

## Stable v0.1 abstraction

The frozen contract remains:

```
LegalTextState
├── Structural Nodes
├── Ordered Text Segments
├── References
├── Source Annotations
├── Parse Report
└── Completeness State
```

Every component remains source-anchored.

Historical identity and semantic rule continuity remain outside the AST:
- node identity is state-scoped;
- provision/rule lineage is a separate evidence-backed graph.

Legal mutation also remains outside the AST:
- annotations may provide mutation evidence;
- the AST parser does not itself create Change Atoms.

## Change-control rule

AST v0.1 is a **stable interface, not a claim that every future EU source is already parsed**.

Adapter evolution may add:
- mappings for new native source elements;
- better reference extraction;
- improved fragment assembly;
- representation-ensemble alignment;
- stricter accounting tests.

A v0.2 core contract is justified only when an adversarial official fixture demonstrates a representational need the current contract cannot express without semantic distortion.

## Foundation consequence

P0-D no longer blocks the mutation/temporal foundations.

Future work should use the v0.1 contract and let real downstream use expose whether a v0.2 is necessary rather than continuing open-ended parser perfection.

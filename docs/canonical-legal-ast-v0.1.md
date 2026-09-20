# Canonical Legal AST v0.1 — design contract

**Status:** FROZEN INTERFACE — adapters remain versioned  
**Issue:** #4  
**Purpose:** source-independent internal representation for legal-text states.

The v0.1 interface is frozen after live adversarial validation. Source adapters remain versioned and may evolve without changing the core contract. See `docs/decisions/ast-v0.1-interface-freeze.md`.

## Why a flat-with-links AST

A purely recursive tree is too restrictive for legal publications.

Legal structure is hierarchical, but legally relevant information also crosses hierarchy:

- footnotes can occur inside text spans;
- references target external or internal provisions;
- tables have row/column structure orthogonal to legal hierarchy;
- corrigenda and consolidation modification markers may span text or structure;
- page/source boundaries do not coincide with legal boundaries;
- one manifestation may be fragmented across many content streams.

Needle therefore stores four coordinated layers:

```
STRUCTURAL NODES
      │
      ├── ordered TEXT SEGMENTS
      ├── REFERENCES
      └── SOURCE ANNOTATIONS

all anchored to immutable SOURCE OBSERVATIONS
```

## Fundamental invariants

### A1 — AST node identity is state-scoped
A node ID identifies one node in one concrete legal-text state.

It is **not** historical provision identity.

Historical continuity is represented separately through Provision Lineage Edges.

### A2 — Labels are data, not identity
“Article 7”, “7.”, “(a)”, or a Formex `IDENTIFIER` are preserved, but none alone is assumed to be a stable cross-version key.

### A3 — Native identifiers are retained
Formex identifiers such as `ART0001.PAR0002.ALN0001.PNT0002` are valuable source anchors and should be preserved exactly where present. Official Formex examples demonstrate hierarchical identifiers and ELI-linked legal references. They remain source-native metadata rather than Needle's permanent identity system.

### A4 — Reading order is explicit
Every node and segment carries deterministic document order. Sibling order alone is insufficient once sources are fragmented.

### A5 — Visible text and comparison text are separate
Needle stores:
- source-derived visible text;
- minimally normalized comparison text;
- hashes for both;
- canonicalization profile/version.

Comparison normalization may remove representational noise such as page-break artifacts. It must not silently normalize punctuation, legal numbering, numeric values, modal verbs, dates, or other potentially meaningful content.

### A6 — Tables are structure
Tables, rows and cells remain nodes with coordinates. They are never flattened into prose before mutation detection.

### A7 — Empty/deleted/reserved provisions survive
A missing body under an extant citation can itself be historically meaningful.

Nodes therefore have presence states such as:
- PRESENT
- DELETED_PLACEHOLDER
- REPEALED_PLACEHOLDER
- RESERVED
- UNKNOWN

### A8 — Unknown source structure is preserved, not guessed
If a parser cannot defensibly map a source element to a canonical legal node, it uses `OTHER`, retains the native tag/attributes, and raises a parse warning.

### A9 — References are first-class
Legal references are not merely text.

A reference can retain:
- displayed text;
- official target URI where supplied;
- reference type;
- source span;
- resolution state.

Formex can explicitly mark legal references with ELI URIs; Needle should not throw that away.

### A10 — Source annotations are evidence, not law changes
Official publication markup can contain:
- consolidation modification markers;
- correction/provenance annotations;
- page breaks;
- production metadata.

Those become Source Annotations linked to node/segment ranges.

An annotation may support a later Mutation Event, but the AST parser itself does not create a Change Atom.

### A11 — Fragmentation is a source concern
Formex explicitly allows large documents to be split into fragments that are logically inserted into a superior instance.

The AST must reconstruct legal reading order while retaining every fragment/item source anchor.

A document with 132 publication streams may still normalize into one coherent legal text state.

### A12 — Parser losses are explicit
Every parse produces a report:
- source representation class;
- adapter + version;
- visible character coverage;
- unknown native tags;
- unresolved references;
- unassembled fragments;
- warnings;
- declared normalization losses.

“Parsed successfully” may never hide dropped material.

---

# Canonical node model

Representative node kinds:

## Legal hierarchy
- DOCUMENT
- PREAMBLE
- RECITAL
- ENACTING_TERMS
- PART
- TITLE
- CHAPTER
- SECTION
- SUBSECTION
- ARTICLE
- PARAGRAPH
- SUBPARAGRAPH
- POINT
- INDENT

## Attached structures
- ANNEX
- APPENDIX
- FORM
- SIGNATURE
- FOOTNOTE

## Data/layout structures with legal significance
- LIST
- LIST_ITEM
- TABLE
- TABLE_ROW
- TABLE_CELL
- HEADING
- BLOCK

## Escape hatch
- OTHER

Node fields include:
- state-scoped `node_id`;
- `parent_id`;
- sibling ordinal;
- global document order;
- canonical kind;
- source-native kind;
- source-native identifier;
- visible citation/number label;
- optional canonical citation path;
- optional official ELI subdivision URI;
- presence state;
- source anchor;
- optional table coordinates/native attributes.

---

# Text segment model

Text lives in ordered segments attached to nodes.

Segment roles:
- LABEL
- HEADING
- BODY
- CELL_TEXT
- FOOTNOTE_TEXT
- CAPTION
- INLINE_OTHER

Each segment keeps:
- exact/source-derived visible text;
- comparison text;
- exact hash;
- comparison hash;
- segment order;
- source-native tag where useful;
- source anchor.

This allows Needle to diff Article 3's body without accidentally mixing in its heading, number label or footnote.

---

# Reference model

Reference kinds:
- INTERNAL_PROVISION
- EU_LEGAL_ACT
- EU_LEGAL_SUBDIVISION
- OFFICIAL_JOURNAL
- FOOTNOTE
- EXTERNAL
- UNRESOLVED

A reference is linked to the containing text segment and stores the source's target URI unchanged where one exists.

Resolution creates additional structured identifiers; it never overwrites the original target.

---

# Source annotation model

Initial annotation kinds:
- CONSOLIDATION_MODIFICATION
- CORRIGENDUM_MARKER
- PAGE_BREAK
- SOURCE_PROVENANCE
- PRODUCTION_MARKER
- OTHER

For consolidation modification annotations, the AST is expected to preserve source-provided fields such as:
- action;
- text/structure level;
- command type;
- active modifying document;
- active source location;
- modification level;
- opening/closing source markers;
- resolved covered node/segment ranges.

Live extraction has now validated this annotation family against consolidated CELEX `02004R0794-20250813`.

The dedicated machine contract is `schemas/consolidation-modification-annotation-v0.1.schema.json`, with a parser in `src/needle/formex/modifications.py`.

Observed current Formex fields include `ACTION`, `LEVEL`, `COMMAND`, `ACTIVE.DOC`, `ACTIVE.LOC`, and `MOD.LEVEL`. Nested level-2 corrigendum provenance has been observed in live Cellar data.

These annotations preserve official documentary mutation provenance while explicitly carrying a non-binding authority character; they feed the mutation evidence reconciler rather than directly generating Change Atoms.

---

# Format adapters

```
Cellar manifestation
        │
        ├─ FMX4 adapter
        ├─ XHTML adapter
        ├─ HTML adapter
        └─ PDF fallback adapter
                │
                ▼
         Canonical Legal AST
```

Adapters may differ radically internally. Their output contract must not.

## FMX4
Highest current technical preference where available because it contains logical legal markup. Formex is explicitly a grammar for logical markup of Official Journal documents and supports document fragmentation.

## XHTML
Useful structured fallback and independent comparison representation.

## HTML
Expected historical fallback where no richer expression exists.

## PDF
Last-resort text/image path, with lower parser-fidelity state and explicit warnings.

---

# Relationship to other Needle objects

```
Source Observation
       ↓
Manifestation Selection
       ↓
Canonical Legal AST state
       ↓
Provision Instances
       ↓
Textual Mutation Events
       ↓
Rule / Provision Lineage
       ↓
Change Atoms
```

Source modification annotations may provide an additional official evidence path into Textual Mutation Events.

---

# Freeze criteria — satisfied 2026-09-20

v0.1 was frozen after demonstrating that it can represent without material loss:

1. **modern fragmented FMX4** — Regulation 794/2004 original;
2. **early historical HTML** — Regulation No 1 (1958);
3. **consolidated FMX4 with embedded mutation provenance** — Regulation 794/2004 at 13 August 2025;
4. one annex/table-heavy adversarial act;
5. one source containing footnotes + ELI-marked references.

If any case requires source-specific fields in the core legal model rather than provenance/native metadata, the abstraction should be reconsidered.


---

# Post-freeze rule

New source-specific parser work does not reopen the AST foundation by default.

Reopen the core contract only when an official adversarial fixture demonstrates legally relevant information that cannot be represented by v0.1 without semantic distortion. Otherwise improve the relevant adapter, accounting rule, completeness plan, or regression fixture.

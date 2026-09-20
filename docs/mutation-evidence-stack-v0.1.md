# Mutation Evidence Stack v0.1

**Status:** adopted foundation architecture  
**Date:** 2026-09-20

Needle reconstructs legal mutation from multiple independent evidence channels. No single convenience representation is allowed to silently become legal authority.

## Evidence layers

### 1. Authentic modifying/correcting act — canonical legal cause
The amending act, corrigendum, repeal/recast instrument, or other authentic Official Journal source is the highest-value evidence for the legal operation itself.

Use it to establish:
- legal text of the modifying instruction;
- adoption/publication/force/application timing;
- exact legal authority for the modification.

### 2. Official embedded consolidation provenance — documentary mutation evidence
Current Cellar consolidated FMX4 can contain paired `CLG.MDFO` / `CLG.MDFC` processing instructions.

Live case `02004R0794-20250813` contains 48 opening and 48 closing markers.

Observed fields include:
- `ACTION`: e.g. REPLACED;
- `LEVEL`: STRUCTURE or TEXT;
- `COMMAND`: EXPLICIT;
- `ACTIVE.DOC`: CELEX of the modifying/correcting act;
- `ACTIVE.LOC`: machine-coded location in that act;
- `MOD.LEVEL`: nesting/generation level.

Observed examples:
- Article 3 replacement attributed to `32008R0271`, `AR:1;PT:1`;
- Article 3 paragraph 3 replacement attributed to `32025R0905`, `AR:1;PT:3`;
- a nested level-2 correction attributed to `32025R0905R(01)`.

This is exceptionally useful official provenance but remains part of a consolidated documentary representation. It **corroborates and locates mutation history; it does not replace the authentic modifying act as legal authority**.

### 3. Official relationship metadata
EUR-Lex/Cellar relationships such as:
- amended by;
- replaced;
- corrected by;
- repealed by;
- affected subdivision;
- effective-from date.

Use these as first-class structured evidence and consistency checks.

### 4. Consolidated state checkpoints
Before/after consolidated states provide efficient validation of reconstructed text state.

They are never the sole legal authority.

### 5. Deterministic structural/text diff
The canonical AST diff engine discovers and verifies changes even where official mutation metadata is absent, incomplete, coarse, or inconsistent.

It provides:
- structural alignment;
- insert/delete/replace candidates;
- numeric/date/cross-reference changes;
- source-normalization-aware comparison.

### 6. Semantic extraction
Only after the textual/legal mutation is sufficiently evidenced do models or deterministic classifiers propose Change Atoms.

Semantic extraction is downstream of mutation evidence.

---

# Reconciliation principle

Needle should prefer **agreement between independent evidence channels**, not a single “trusted” shortcut.

For each candidate mutation, record which channels support it.

Example:

```
AUTHENTIC ACT                    ✓
FORMEX EMBEDDED PROVENANCE      ✓
EUR-LEX RELATION METADATA       ✓
CONSOLIDATED BEFORE/AFTER       ✓
DETERMINISTIC AST DIFF          ✓
```

A disagreement is itself data and should enter quarantine/audit rather than being silently resolved.

---

# Source-assisted deterministic mutation engine

P0-I is therefore no longer merely “diff two documents.”

It is:

```
official source relationships ─────┐
embedded consolidation provenance ─┤
authentic amendment instructions ──┼──► MUTATION EVIDENCE RECONCILER
consolidated checkpoints ───────────┤
deterministic AST diff ─────────────┘
                                      │
                                      ▼
                              VERIFIED TEXTUAL MUTATION
                                      │
                                      ▼
                                  CHANGE ATOM
```

The engine remains deterministic in how evidence is parsed, aligned, and reconciled. AI may help later with legal-semantic interpretation, but it must not invent mutation provenance.

---

# Durable invariants

1. **Consolidation provenance is evidence, not authority.**
2. **A diff result is a candidate until provenance/status checks support it.**
3. **Embedded source provenance is retained verbatim before interpretation.**
4. **Nested modifications/corrigenda remain nested; they are not flattened into one latest editor.**
5. **Disagreement between evidence channels is surfaced, not hidden.**
6. **Missing embedded markup never means no mutation occurred.**

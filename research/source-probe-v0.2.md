# Source Probe & Assumption Log

## Purpose

The early phase is explicitly falsification-driven. We test foundational assumptions against ugly real EU-law cases before locking architecture.

## Probe A — Regulation (EC) No 794/2004

Why selected:
- long amendment history;
- corrigenda;
- annex-heavy structure;
- provision-level replacements/additions/deletions;
- multiple consolidated checkpoints;
- provision-specific application timing.

### A1 — Official relationship metadata is richer than assumed
**Result: PASS; architecture simplified.**

EUR-Lex exposes modification relationships containing the modifying/correcting act, textual operation, affected subdivision and often an effective-from date.

**Decision:** ingest official mutation metadata as a first-class source. Deterministic diffing remains necessary for verification, exact before/after text, missing/coarse metadata, semantic extraction and inconsistency detection.

### A2 — Consolidated checkpoints are useful but not authoritative
**Result: PASS WITH QUALIFICATION.**

Consolidated states line up usefully with known mutation dates.

**Decision:** use consolidations as checkpoints and accelerators, never sole canonical legal authority.

### A3 — One amending act can create multiple temporal states
**Result: FOUNDATION CONFIRMED.**

A single implementing act can have a general force/application date while a specific subdivision applies later.

**Decision:** temporal data attaches to mutation/provision level. Never propagate one act-level date to every mutation blindly.

### A4 — Early legal history is reconstructable but metadata is uneven
**Result: PASS WITH DEGRADED CERTAINTY.**

Early acts can have long structured mutation histories, but older relationship rows may omit dates present in later records.

**Decision:** certainty is field-specific. Missing dates remain missing until recovered from authentic modifying instruments or independently verified official evidence.

### A5 — ELI identifiers cannot be guessed from printed act numbers
**Result: ASSUMPTION REJECTED.**

Historical acts may use sequence suffixes or other identifier forms that cannot be safely generated from visible citation alone.

**Decision:** all identifier equivalence is source-backed.

### A6 — Provision-level ELI is a standard; implementation coverage is unproven
**Result: SPECIFICATION CONFIRMED, COVERAGE OPEN.**

**Decision:** store official subdivision ELI where available but maintain internal provision identity for historical gaps, renumbering, split/merge and movement.

### A7 — Cellar can resolve works from CELEX
**Result: PASS.**

**Decision:** initial ingestion may begin from CELEX and resolve Cellar work/expression/manifestation identifiers and files from official metadata.

### A8 — Corrigenda can be substantive and language-specific
**Result: FOUNDATION CONFIRMED.**

Corrections can change more than typography and may apply only to selected language versions.

**Decision:** language expression belongs in the mutation graph, not only the download layer.

---

# Schema falsification

Change Atom v0.1 used one flat semantic category.

**Rejected.**

A single replacement may simultaneously express a duty, procedure change, digital-channel condition, exception and validity consequence.

## v0.2 uses orthogonal axes

- **legal_effect** — normative effect such as DUTY, RIGHT, PERMISSION, POWER.
- **dimensions** — PROCEDURE, SCOPE, EXCEPTION, TIME, THRESHOLD, REPORTING, etc.
- **textual_operations** — INSERT, DELETE, REPLACE, RENUMBER, SPLIT, MERGE, CORRECT, etc.

This keeps meaning queryable without forcing mutually exclusive labels.

---

# Next falsification targets

1. Break provision identity with a real split/merge/renumbering case.
2. Test repeal-and-replacement conceptual ancestry across a new CELEX act.
3. Measure missing dates/subdivision precision over a historical sample.
4. Test a core-operative-provision corrigendum.
5. Measure language-scoped corrigenda and consolidated-language behaviour.
6. Test directive-level history against national transposition divergence.
7. Test whether Thread should distinguish textual ancestry from conceptual ancestry.

**Working rule:** a failed assumption discovered now is progress.

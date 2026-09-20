# Morrow // Needle

**Public infrastructure for observing how EU rules change.**

Needle is not a document summarizer. It reconstructs, verifies, and explains legal change: what changed, compared with what, who or what it affects, when it matters, and the exact official evidence supporting the claim.

## Core concepts

- **Needle** — finds significant legal and regulatory change.
- **Thread** — follows a rule's ancestry and descendants through time.
- **Change Atom** — the smallest independently defensible legal change.
- **Morrow Constitution** — project rules governing provenance, legal status, uncertainty, time, and AI use.

## Design principles

1. Official sources outrank models.
2. Every factual legal claim must be traceable.
3. Legal text and interpretation are different data types.
4. Proposal is not law.
5. Recitals are not operative provisions.
6. Consolidated texts are checkpoints, not canonical legal authority.
7. Legal time is multidimensional.
8. Absence of evidence is not evidence of absence.
9. Every change has an explicit comparator.
10. The system may abstain when evidence is insufficient.

## Repository layout

```
docs/          product and architectural foundations
schemas/       machine-readable domain schemas
research/      source probes and assumption tests
fixtures/      verified and candidate historical mutation cases
data/          small reference matrices and controlled datasets
```

## Current status

Foundation v0.1 is complete. Source probing has begun against real historical EU legislation. The first stress test already invalidated the original one-dimensional Change Atom taxonomy, producing schema v0.2 with separate legal-effect, descriptive-dimension, and textual-operation axes.

The next falsification target is provision identity across renumbering, split/merge, and repeal-and-replacement chains.

---

*Morrow // Needle — evidence before explanation.*

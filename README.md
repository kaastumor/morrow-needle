# Morrow // Needle

**Evidence-first research and audit infrastructure for EU legal change.**

Needle is not a document summarizer or a general legal-news product. It reconstructs, falsifies, and inspects legal-change claims: what changed, compared with what, when different legal effects matter, which dependencies or corrections alter the picture, what official evidence supports the claim, and what remains unresolved.

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
data/          small reference data plus a frozen historical operational snapshot
```

## Current status

The project is in **research/audit mode**. Public-product expansion remains
stopped after comparative Issues #49 and #59 failed to demonstrate repeated
material advantage over the strongest simpler baseline.

The P0/P1 evidence, identity, temporal, provenance and mutation foundation
remains canonical. Later research adversaries have earned several narrow
extensions for non-textual legal state, including authoritative dynamic sets,
metrics, categorical findings, precision-aware time, legal spatial extent and
judicial holdings.

There is **no standing feature or implementation queue**. A new task must begin
from a falsifiable legal-information question, fresh official evidence, an
unresolved canonical claim or an explicit sponsor research question. An idle
backlog is intentional.

Issue #84 froze the old scheduled Git-backed operational monitor. Its current
state snapshot remains as historical evidence/regression input, while live
cycles are manual diagnostics and no longer commit generated state to
`main`.

See:

- `docs/project-charter.md`
- `BACKLOG.md`
- `docs/assumptions.md`
- `docs/audits/project-system-wide-angle-2026-09-23.md`

---

*Morrow // Needle — evidence before explanation.*

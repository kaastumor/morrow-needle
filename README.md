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
data/          small reference matrices and controlled datasets
```

## Current status

The P0/P1 legal-change foundation is complete and remains the canonical
evidence/identity/temporal/provenance core.

Two successive comparative gates changed the project direction:

- **Issue #49:** the broad live-change/public-feed thesis failed to demonstrate
  repeated material advantage over EUR-Lex, mature change tooling, direct
  official sources and a capable LLM.
- **Issue #59:** the Article 3 Thread proved materially better as an audit
  package, especially for negative checks and provenance closure, but the same
  legal history is reconstructible from the strong baseline and one showcase is
  not recurring product evidence.

The project therefore **stops public-product expansion and continues in
research/audit mode**.

Operational Needle, Thread, Evidence, Legislative X-Ray, Source Anomaly,
Half-Life and the Gold corpus remain useful tools and regressions. They no longer
imply a feature roadmap.

The first explicit research-mode task is **Issue #61**, auditing whether the
2026 corrigendum to Regulation 2025/905 is back-projected into the EUR-Lex
consolidation labelled 13 August 2025.

See `BACKLOG.md`,
`docs/audits/thread-comparative-value-2026-09-23.md`,
`docs/audits/project-health-2026-09-23-post-thread.md`, and Issue #61.

---

*Morrow // Needle — evidence before explanation.*

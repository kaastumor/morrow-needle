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

The P0/P1 legal-change foundation is complete and has survived an explicit post-foundation red-team across historical legislation, multilingual corrigenda, temporal edge cases, source anomalies, provision/rule lineage and end-to-end Thread reconstruction.

The first P2 product projections are now evidenced:

- **Half-Life** — temporary regimes as extensions, gaps and successor episodes;
- **Source Anomaly** — authoritative-source irregularities without confusing source state with legal state;
- **Legislative X-Ray** — derived dependency effects where local provision text remains unchanged.

The current strategic priority is no longer another ontology or analytic primitive. It is the first **operational Needle loop**: start from a real official update event and carry it through targeted re-observation, verified mutation/non-impact/abstention, semantic and temporal resolution, retrieval, provenance and an evidence-linked public feed card.

See `docs/step-back-review-2026-09-20-v0.2.md` and Issue #21.

---

*Morrow // Needle — evidence before explanation.*

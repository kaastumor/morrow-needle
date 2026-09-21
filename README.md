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

The operational Needle loop is now proven against real official events, and the first product checkpoint has tested verified-change, source-audit and abstention cards.

The current strategic priority is **Issue #29: the pre-analysis adversarial audit + repository sanitation gate**. Before any new analytic primitive or product expansion, Needle is being attacked from byte/parser assumptions through evidence ownership, operational behavior, product truthfulness, analytical usefulness and its external novelty/public-interest thesis. The same gate reconciles stale code, workflows, docs, issues and backlog state.

See `BACKLOG.md`, `docs/product-checkpoint-v0.1.md`, and Issue #29.

---

*Morrow // Needle — evidence before explanation.*

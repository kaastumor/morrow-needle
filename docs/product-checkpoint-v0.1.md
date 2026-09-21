# Product checkpoint v0.1 — first real-card pass

Status: **COMPLETED PRODUCT CHECKPOINT; NOT A CANONICAL DOMAIN CONTRACT**

Issue: #27

This checkpoint deliberately projects existing canonical truth into a disposable public surface. It does not modify `feed-card-v0.1`, temporal truth, mutation identity, or provenance ownership.

## Real evaluation material

### A. Verified change

Source: successful default-branch `Live 2026/2104 mutation case` run 35667430340, artifact `reg2104-live-case-evidence` (artifact digest `sha256:7de0f4a7bc59c308953300fc67015209840c7abf8331ad5a43c51456d115b7c3`).

The generic replay proves two separate canonical authentic mutations for Regulation (EU) 2026/2104: Annex V and Annex XIV each add US-2.1405 / US-2.1406 after US-2.1404. Official publication metadata resolves publication to 2026-09-18. The source-diff branch remains unresolved because no pre-event baseline exists.

### B. Abstention

Source: `data/operational-pilot-latest-cards.json` after the 2026-09-22 01:17:51 +02:00 Cellar notification burst.

Forty-nine WEMI notifications collapse to one root refresh for Cellar `0993d6d0-8ff1-11f1-9262-01aa75ed71a1`. The resulting card abstains: no supported CELEX baseline/reobservation path exists and no pre-event comparator exists.

### C. Audit / non-change

Source: committed operational cycle `d50b8ee2`, window 2026-09-21 19:29:13Z → 21:31:16Z.

A real Cellar update for `CELEX:62025CJ0322` — the Court judgment in Case C-322/25, *Swedish Match – Fósforos de Portugal v Autoridade Tributária e Aduaneira* — had an **ELIGIBLE prospective baseline** captured before the event. Targeted re-observation completed successfully. The legal-content hash remained unchanged while the official metadata hash changed, so the ordinary pipeline classified the event `METADATA_ONLY` and emitted `SOURCE_METADATA_ONLY → AUDIT_FEED`.

The card therefore makes a positive bounded claim: **the official source metadata changed, but the observed legal text did not.** It does not infer a legal amendment or legal-effect time from the source update.

## 30-second comprehension rubric

A projection passes only if a reader can answer these without knowing Needle vocabulary:

| Question | Verified case | Audit / non-change | Abstention case |
|---|---|---|---|
| Why now? | PASS — explicit official publication date | PASS — a real official update triggered comparison against a prior baseline | PASS — official update prompted investigation, not a legal-change claim |
| What changed? | PASS — two separate annex mutations | PASS — source metadata changed; legal content did not | PASS — explicitly unknown |
| Compared with what? | PASS — authentic placement anchors; missing source comparator disclosed | PASS — an eligible pre-event source baseline | PASS — no baseline disclosed |
| When legally relevant? | PARTIAL — publication known; application intentionally unknown | PASS — no legal-effect time is manufactured from metadata activity | PASS — no legal time inferred |
| Who/what is affected? | FAIL/UNKNOWN — engine has no canonical affected-entity claim | N/A | N/A |
| How certain? | PASS — direct official evidence | PASS — hash comparison supports a source-only conclusion | PASS — unresolved is rendered as a useful state |
| Can evidence be inspected without XML/internal IDs? | PARTIAL — prototype gives human-readable act/Cellar anchors, but canonical card still exposes opaque refs | PARTIAL — underlying before/after observations are auditable but raw refs dominate the canonical card | PARTIAL |
| What remains unknown? | PASS | PASS — metadata semantics themselves are not promoted into legal meaning | PASS |

## First observations

1. **`why now` must be a first-class public concept, separate from legal applicability.** The canonical engine already owns the distinction; the product merely needs to expose it prominently.
2. **Compound acts need delivery grouping without mutation collapse.** The current generic replay has two mutation identities but the raw card's `what_changed` is one long sentence. The product should enumerate canonical changes.
3. **Abstention is product content, not an error state.** The real no-CELEX/no-baseline case becomes understandable once it says what was observed, why no claim is possible, and what evidence is missing.
4. **Source Mode needs a presentation resolver, not a second provenance model.** Users need “Regulation (EU) 2026/2104 — authentic amending instruction” before `src-operational-content-...`. Opaque IDs remain useful for audit/debugging, but should not be the primary public anchor.
5. **Affected-entity intelligence is the clearest recurring information gap so far.** The legal text visibly mentions the United States, but the engine correctly refuses to promote drafting-text mentions into canonical impact claims. The product should display “not established” rather than quietly infer impact.
6. **The audit card is useful when phrased as an explicit negative conclusion.** “Metadata changed; legal text did not” is informative because it explains why an official update did *not* become legal news.
7. **Source Mode presentation is the only product gap repeated across all three real classes.** All three are understandable without new canonical truth, but all three benefit from resolving opaque provenance IDs into human-readable official anchors.
8. **Do not change `feed-card-v0.1` yet.** Three classes justify a presentation resolver and hierarchy rules, not a new canonical product contract.

## Thin surface

`product/checkpoint-v0.1/index.html` is intentionally static and dependency-free. It tests hierarchy only: scan state, expanded facts, separate timing, explicit unknowns, and human-readable Source Mode. It is not a frontend architecture decision.

## Product checkpoint decision

The three required real classes now exist: verified legal change, positive source audit/non-change, and explicit abstention.

The product evidence does **not** justify a new analytic primitive or a new canonical feed-card contract. The smallest recurring improvement is a **Source Mode presentation resolver** over existing provenance so official evidence is shown first as human-readable acts, cases, publication facts and source comparisons while internal record IDs remain available for audit.

Affected-entity truth remains the clearest missing information in the verified-change case, but it is not yet a repeated cross-class requirement and should not be promoted merely because it is conceptually attractive.

Therefore:

1. Issue #27 is complete.
2. No Source Mode implementation begins immediately.
3. Issue #29 is the mandatory next step and must adversarially test this product conclusion together with the larger novelty/thesis claim.
4. If #29 preserves the conclusion, Source Mode presentation resolution is the current lowest-risk product investment; if the audit overturns it, the backlog follows the evidence.

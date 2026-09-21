# Product checkpoint v0.1 — first real-card pass

Status: **ACTIVE EXPERIMENT, NOT A CANONICAL DOMAIN CONTRACT**

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

**Still required.** Do not invent one for visual completeness. The next checkpoint slice must preserve a real metadata-only or otherwise positively verified no-material-change official update before this corpus is considered complete.

## 30-second comprehension rubric

A projection passes only if a reader can answer these without knowing Needle vocabulary:

| Question | Verified case | Abstention case |
|---|---|---|
| Why now? | PASS — explicit official publication date | PASS — official update prompted investigation, not a legal-change claim |
| What changed? | PASS — two separate annex mutations | PASS — explicitly unknown |
| Compared with what? | PASS — authentic placement anchors; missing source comparator disclosed | PASS — no baseline disclosed |
| When legally relevant? | PARTIAL — publication known; application intentionally unknown | PASS — no legal time inferred |
| Who/what is affected? | FAIL/UNKNOWN — engine has no canonical affected-entity claim | N/A |
| How certain? | PASS — direct official evidence | PASS — unresolved is rendered as a useful state |
| Can evidence be inspected without XML/internal IDs? | PARTIAL — prototype gives human-readable act/Cellar anchors, but canonical card still exposes opaque refs | PARTIAL |
| What remains unknown? | PASS | PASS |

## First observations

1. **`why now` must be a first-class public concept, separate from legal applicability.** The canonical engine already owns the distinction; the product merely needs to expose it prominently.
2. **Compound acts need delivery grouping without mutation collapse.** The current generic replay has two mutation identities but the raw card's `what_changed` is one long sentence. The product should enumerate canonical changes.
3. **Abstention is product content, not an error state.** The real no-CELEX/no-baseline case becomes understandable once it says what was observed, why no claim is possible, and what evidence is missing.
4. **Source Mode needs a presentation resolver, not a second provenance model.** Users need “Regulation (EU) 2026/2104 — authentic amending instruction” before `src-operational-content-...`. Opaque IDs remain useful for audit/debugging, but should not be the primary public anchor.
5. **Affected-entity intelligence is the clearest recurring information gap so far.** The legal text visibly mentions the United States, but the engine correctly refuses to promote drafting-text mentions into canonical impact claims. The product should display “not established” rather than quietly infer impact.
6. **Do not change `feed-card-v0.1` yet.** Two real card classes are insufficient evidence for a contract revision, and the required positive non-change card is still missing.

## Thin surface

`product/checkpoint-v0.1/index.html` is intentionally static and dependency-free. It tests hierarchy only: scan state, expanded facts, separate timing, explicit unknowns, and human-readable Source Mode. It is not a frontend architecture decision.

## Next falsification

Find a real operational event where Needle has a valid comparator and positively verifies no material legal change (prefer metadata-only noise if observed). Add it unchanged to the evaluation corpus, then test whether the same hierarchy makes “nothing legally changed” useful rather than boring or misleading.

Only after that third case should Issue #27 decide between:

- affected-entity intelligence;
- a public-card projection contract;
- Source Mode presentation resolution;
- or further delivery/UI work.

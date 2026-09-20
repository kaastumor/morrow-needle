# Decision — Freeze Thread v0.1

**Date:** 2026-09-20  
**Status:** ADOPTED  
**Issue:** #14

## Decision

Freeze the first end-to-end Thread contract around:

- `schemas/thread-v0.1.schema.json`
- `src/needle/thread/composer.py`
- `src/needle/thread/render.py`
- `fixtures/thread/reg794-article3-thread-v0.1.json`
- `fixtures/gold/reg794-article3-thread-v0.1.json`
- `tests/test_thread_article3.py`
- `tests/test_thread_gold.py`
- `tests/test_thread_render.py`
- `.github/workflows/thread-article3.yml`

The first frozen Thread is:

**Commission Regulation (EC) No 794/2004 — Article 3 (ENG)**

It reconstructs the rule history from the original 2004 state through the 2008 Article replacement, the 2025 paragraph-3 replacement and the reviewed 2026 corrigendum non-impact.

## What a Thread is

A Thread is a chronological, evidence-linked **composition of canonical legal-change entities**.

It is not a second source of truth for:

- legal text;
- mutation state;
- temporal state;
- Change Atoms;
- provision/rule lineage;
- provenance;
- source availability.

Those remain owned by their frozen domain contracts.

## Stable v0.1 principles

### 1. Thread persistence is reference-only

The persisted Thread stores:

- subject;
- ordered events;
- typed references to canonical entities;
- lineage edge IDs;
- Source Mode requirement;
- explicit unknowns;
- narrative-generation policy.

It does not copy canonical claim text, dates, verification state, hashes or legal effects into a second persistence model.

The removed historical fixture `fixtures/thread/32004R0794-article3-v0.1.json` demonstrated why this matters: it duplicated candidate atoms and dates that later diverged from canonical semantic/temporal truth.

### 2. Baseline state is not a fabricated mutation

The authentic 2004 Article 3 and its initial consolidated checkpoint have the same canonical subtree hash.

Thread v0.1 therefore represents the original state as `BASELINE_STATE`.

It does not manufacture a mutation-derived Change Atom for enactment merely to make the timeline visually symmetrical.

### 3. Chronology does not collapse temporal dimensions

The first Thread preserves separately:

- entry into force;
- Chapter II application;
- paper-notification end;
- electronic-notification start;
- entity/event-conditioned correspondence applicability;
- SANI-specific 2008 application;
- 2025 paragraph-3 application.

An integration adversary exposed a P0 implementation defect during this work: the frozen temporal schema already represented exclusive boundaries, but the resolver did not enforce them.

That bug was fixed and regressed. The Article 13 phrase “more than five months” now correctly yields an exclusive 20 October 2004 boundary.

### 4. Source-native metadata may support temporal derivation

The 2004 publication date is recovered from source-native Cellar Formex metadata:

`DATE[ISO=20040430]`

Combined with the authentic Article 13 twentieth-day clause, this derives entry into force without adding a second external metadata dependency.

### 5. Unchanged text may still have a derived semantic ripple

The 2025 amendment replaces Article 3(3).

Article 3(4) has the same canonical subtree hash before and after that transition, and its exception/consequence sentences retain identical hashes.

Therefore:

- no paragraph-4 textual mutation is emitted;
- the paragraph-4 exception/consequence are not described as newly inserted;
- a derived cross-reference semantic ripple may still be represented because paragraph 4 refers to the channels defined by the changed paragraph 3.

This distinction is permanent Gold regression material.

### 6. Related official sources can be retained as non-impact evidence

The 17 July 2026 corrigendum to Regulation 2025/905 was explicitly reviewed.

It corrects the amendment of Regulation 794/2004 Article 4(1), not Article 3.

Thread v0.1 retains it as `RELATED_SOURCE_NON_IMPACT` for Source Mode completeness while forbidding a new Article 3 mutation, text state or Change Atom.

### 7. Live source availability is not legal truth

The corrigendum ELI resolver can intermittently return an anti-bot/interstitial response.

The architecture therefore separates:

- pinned immutable official legal evidence;
- live source availability observation.

Temporary endpoint unavailability does not invalidate an already pinned legal conclusion.

Retrieved official content that contradicts the pinned contract still fails closed.

### 8. Source Mode closure is mandatory

A public Thread may render only when all referenced factual legal claims have active provenance support.

The Article 3 provenance ledger was extended append-only from 41 to 77 records to close the full Thread.

The composer reports provenance gaps deterministically; the frozen Gold case requires:

`THREAD_SOURCE_MODE closed=true gap_count=0`

### 9. Structural lineage and rule lineage remain separate

The Thread references both kinds of lineage without converting one into the other.

Structural replacement/continuity is evidence-backed separately from proposition-level rule continuity.

Rule continuity between named 2008 systems and Commission-designated 2025 systems remains interpretive and does not claim technical-system identity.

### 10. Public narrative is generated, not canonical

The 3-second, 30-second and 3-minute views are generated from canonical referenced entities.

Every substantive public statement carries:

- Thread/domain references;
- active provenance support records;
- source observation IDs;
- source locators.

Public wording can evolve without rewriting canonical legal state.

## First frozen chronology

The reference Thread orders:

1. original Article 3 baseline;
2. entry into force;
3. Chapter II application gate;
4. paper-notification regime end;
5. electronic-notification start;
6. event-conditioned correspondence applicability;
7. 2008 Article 3 replacement;
8. SANI-specific application boundary;
9. 2025 Article 3(3) replacement;
10. derived paragraph-4 cross-reference ripple;
11. 2025 paragraph-3 application;
12. 2026 corrigendum review / Article 3 non-impact.

## Gold regressions

`fixtures/gold/reg794-article3-thread-v0.1.json` permanently checks, among other things:

- chronology;
- zero Source Mode gaps;
- SANI and PKI remain separate duties;
- no baseline Change Atom;
- no 2025 Article 3(4) textual mutation;
- no Article 3 mutation from the 2026 corrigendum;
- no SANI-specific date copied onto the PKI duty;
- derived paragraph-4 ripple remains separate from the direct paragraph-3 mutation;
- English-only scope remains explicit;
- technical identity of old/new systems remains unresolved.

The Thread case is also gated by the canonical Gold Corpus workflow, not only its dedicated integration workflow.

## Known scoped limitations

v0.1 intentionally does not solve:

- cross-language semantic equivalence for this Thread;
- affected-entity labelling beyond separately evidenced claims;
- generic natural-language rendering for arbitrary Thread subjects;
- retrieval/ranking across many Threads;
- technical identity between legacy and successor submission systems.

These are downstream capabilities, not reasons to weaken the first contract.

## Post-freeze rule

Build P1-D search/retrieval **against** Thread/Atom/lineage/temporal/provenance objects rather than designing a parallel search ontology.

Reopen Thread v0.1 only if a new official adversarial case cannot be represented without:

- duplicating canonical truth;
- collapsing orthogonal legal states;
- losing provenance closure;
- or misclassifying baseline, mutation, derived effect or related non-impact evidence.

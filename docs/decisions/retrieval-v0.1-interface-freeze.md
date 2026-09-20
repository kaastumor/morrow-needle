# Decision — Freeze Structured Retrieval v0.1

**Date:** 2026-09-20  
**Status:** ADOPTED  
**Issue:** #15

## Decision

Freeze P1-D structured retrieval v0.1 around:

- `schemas/retrieval-query-v0.1.schema.json`
- `schemas/retrieval-response-v0.1.schema.json`
- `schemas/retrieval-index-sources-v0.1.schema.json`
- `fixtures/retrieval/index-sources-v0.1.json`
- `src/needle/retrieval/projection.py`
- `src/needle/retrieval/search.py`
- `src/needle/retrieval/temporal.py`
- `src/needle/retrieval/identity.py`
- `tests/test_retrieval.py`
- `scripts/build_article3_retrieval_demo.py`
- `.github/workflows/retrieval.yml`

The first frozen retrieval corpus is the Regulation 794/2004 Article 3 Thread.

This is an **interface freeze**, not a production search-backend freeze. Storage engines, multi-Thread indexing, ranking infrastructure and semantic discovery may evolve behind these boundaries.

## Core rule

> The search index is a rebuildable projection, never canonical legal truth.

Canonical identity, legal text, mutations, Change Atoms, temporal assertions, lineage, provenance and explicit unknowns remain owned by their frozen domain contracts.

Retrieval may materialize searchable facets and hydrate canonical entities at query time. It may not become a second legal-state database.

## Stable v0.1 principles

### 1. Projection state is disposable

`build_thread_projection()` deterministically rebuilds searchable documents from canonical Thread-registered objects.

The projection fingerprint covers the derived documents, including active provenance support IDs and typed identifier enrichment.

No retrieval projection document is authoritative legal state.

### 2. Exact retrieval and discovery are different operations

Free-text discovery is deliberately broad.

A search for `SANI` may retrieve:
- the historical SANI duty;
- an exception that refers to SANI;
- a later derived rule effect explaining that SANI was replaced.

That is useful discovery.

It is **not** a safe substitute for asking whether one canonical rule was active on a date.

Exact legal-status questions therefore use structured `entity_ids` rather than relying on lexical coincidence.

The permanent regression at the 3 July 2025 boundary proves:
- broad SANI discovery may return active related claims;
- exact retrieval of the SANI duty returns it as temporally inactive.

### 3. Structured filters are typed, not string soup

v0.1 supports structured filtering over:

- canonical entity kind and ID;
- act ID;
- provision-path prefix;
- language;
- Thread event ID / event kind;
- Change Atom legal effect / dimensions;
- mutation operation;
- temporal dimension;
- lineage scope / edge type;
- verification state;
- evidence state;
- Source Mode closure;
- typed identifier pairs.

Non-empty values are OR within one field and AND across fields.

### 4. Identifier enrichment reuses the frozen identity graph

Retrieval does not invent aliases.

For Regulation 794/2004, `SAME_LEGAL_RESOURCE` enrichment yields exactly:

- CELEX `32004R0794`;
- ELI `http://data.europa.eu/eli/reg/2004/794/oj`;
- Cellar Work `26f403d1-7656-4c91-9726-c08d466ff8bd`.

It does **not** promote:

- a Cellar Expression or Manifestation;
- a consolidated text state;
- a corrigendum;
- an OJ citation;
- an ELI subdivision

into an act alias.

Identifier filters use atomic `{scheme, value}` pairs so a scheme cannot accidentally match the value of another identifier.

### 5. Historical date queries require an explicit temporal perspective

A retrieval query containing legal time must state:

- temporal dimension;
- valid date;
- perspective;
- mode.

The two frozen perspectives remain those from P0-E:

- `EX_POST_LEGAL_EFFECT`
- `OFFICIAL_SOURCE_STATE_AS_OF`

The latter requires a source cutoff date.

Retrieval never silently defaults a historical question to an ex-post view.

### 6. Retrieval follows canonical temporal references only

An entity is date-evaluated only through its explicit `temporal_assertion_refs`.

Retrieval may not infer a validity interval from:

- Thread event order;
- mutation dates;
- successor existence;
- rule lineage;
- lexical dates;
- the next known event.

Entities without explicit temporal references abstain under temporal queries rather than borrowing nearby dates.

### 7. Temporal integration exposed and repaired missing canonical facts

The first date-aware retrieval adversary showed that:

- SANI had a canonical 1 July 2008 start but no explicit end;
- PKI correctly did not borrow the SANI date, but therefore had no modeled start.

Rather than compensating in search, the canonical temporal layer was repaired.

The resulting rule history now proves:

- PKI correspondence applies from 14 April 2008;
- SANI notification applies from 1 July 2008;
- both legacy paragraph-3 channel rules remain active through 2 July 2025;
- both end exclusively on 3 July 2025;
- paragraph-4 exception and invalid-submission rules continue because paragraph 4 was not textually replaced.

This is a durable example of retrieval pressure finding a canonical-model omission.

### 8. Official-source time is evidence-backed

`OFFICIAL_SOURCE_STATE_AS_OF` cannot accept caller-supplied source availability as authority.

Official publication dates are canonical temporal assertions with provenance.

For the first Thread:

- Regulation 271/2008 publication: 25 March 2008;
- Regulation 2025/905 publication: 13 June 2025.

The 2025 live Cellar probe also exposed duplicate identical publication metadata in two Formex streams:
- `L_202500905EN.doc.fmx.xml`
- `L_202500905EN.toc.fmx.xml`

Identical duplicates are treated as representation duplication, not independent or conflicting evidence. One deterministic canonical locator is retained while all occurrences remain observable in live evidence.

### 9. Bitemporal retrieval is executable

For the same legal valid date, 3 July 2025:

- with official-source cutoff 12 June 2025, the later replacement/end assertion is not yet part of the supported official-source record;
- with cutoff 13 June 2025, Regulation 2025/905 is published and the known future replacement changes the supported historical-source state.

This distinction is produced by the frozen temporal resolver and canonical publication evidence, not by retrieval-specific validity logic.

### 10. Abstention is a retrieval result

v0.1 explicitly returns abstentions such as:

- no temporal assertions;
- context required;
- temporal conflict;
- source availability unresolved;
- not asserted as of source date;
- temporally inactive;
- temporal dimension not asserted;
- unknown temporal reference;
- temporal provenance gap.

Unknown is not converted to false, absence or a low score.

### 11. Current provenance is visible in search

Source Mode exposes:

- whether support is required;
- whether support is closed;
- active support count;
- active support record IDs.

The projection uses the ledger's current append-only view, so superseded support records do not remain silently current.

A permanent regression uses the real locator-correction pair:
- superseded `support-audit-locator-v1`;
- active `support-audit-locator-v2`.

### 12. Explicit unknowns remain searchable

Thread unknowns are first-class retrieval objects.

Examples include:
- unresolved technical identity between legacy SANI/PKI systems and later Commission-designated systems;
- unresolved affected-entity labels;
- explicit English-only scope.

They are marked `support_required=false` rather than being mistaken for broken factual claims.

### 13. Evidence class may affect ordering; it is not a confidence score

When otherwise comparable lexical results compete, deterministic ordering may prefer:

- DIRECT over DERIVED;
- resolved/verified states over unresolved/candidate states.

These are categorical evidence classes already present in canonical contracts.

Retrieval does not invent numeric legal confidence.

### 14. Related non-impact evidence remains retrievable

The 2026 corrigendum review can be found as `RELATED_SOURCE_NON_IMPACT`.

It does not become an Article 3 mutation merely because retrieval ranks or surfaces it.

Likewise, the 2025 Article 3(4) query returns the derived cross-reference ripple and continuity evidence while returning no textual mutation.

## Integration demo

`scripts/build_article3_retrieval_demo.py` produces a deterministic artifact exercising:

1. Thread lookup by ELI;
2. SANI discovery before the 2025 replacement;
3. SANI discovery on the replacement day;
4. source-as-of state before Regulation 2025/905 publication;
5. source-as-of state after publication;
6. Article 3(4) derived-effect retrieval without textual mutation;
7. explicit technical-identity unknown retrieval.

The dedicated `Structured retrieval contract` workflow builds and validates this artifact.

## Known scoped limitations

v0.1 intentionally does not freeze:

- a persistent/index-server implementation;
- multi-Thread sharding/storage;
- natural-language query interpretation;
- embedding/vector retrieval;
- learned ranking;
- direct impact/affected-entity inference;
- a generic “current law” summary shortcut;
- automatic temporal inference for canonical entities that do not declare temporal references.

Embeddings may later improve discovery, but they remain secondary to typed retrieval and cannot establish legal state.

## Post-freeze rule

Extend storage, multi-Thread indexing and semantic discovery behind this interface.

Reopen v0.1 only if a real retrieval adversary cannot be answered without:

- duplicating canonical legal truth;
- collapsing temporal dimensions;
- weakening typed identity;
- hiding provenance corrections;
- converting unknown into absence;
- or making discovery results masquerade as exact legal-status answers.

The next project phase is the post-P1 foundation audit (#16), not broad P2 feature expansion.

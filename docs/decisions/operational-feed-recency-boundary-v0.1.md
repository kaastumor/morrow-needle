# Operational feed recency boundary v0.1

Status: **DURABLE DECISION**  
Date: 2026-09-21  
Owner: Issue #21 operational vertical slice

## Adversarial question

If a Cellar `UPDATE` event points at an authentic act whose text contains an explicit amendment instruction, may Needle emit that mutation into `CHANGE_FEED` merely because the instruction is legally authentic?

**No.**

## Why

Two propositions have different evidence owners:

1. **Legal-cause truth** — an authentic act can directly establish that a mutation exists.
2. **Operational recency** — whether that mutation is newly relevant to the feed window is temporal/procedural truth.

A Cellar ingestion `UPDATE` is an infrastructure/source event. It is not evidence that every legal instruction contained in the refreshed artifact was adopted, entered into force, became applicable, or otherwise became newly relevant at the ingestion timestamp.

Without this boundary, a representation refresh of an old authentic amending act could resurrect a historical amendment as "what changed now". That would turn official-source authority into a false temporal inference.

## Frozen rule

`AUTHENTIC_LEGAL_CAUSE` may independently promote a mutation to `LEGAL_CHANGE_VERIFIED` even when source comparison is unresolved, but **that status alone is insufficient for `CHANGE_FEED` recency**.

A recurring operational monitor may project a verified legal cause into `CHANGE_FEED` only when a canonical temporal/procedural assertion independently establishes the card's relevant operational time relationship. Otherwise the legal mutation remains verified but the operational result must abstain from claiming that it is newly changing now.

In particular, the monitor must never derive recency from:

- Cellar ingestion time;
- feed action `CREATE` / `UPDATE`;
- first observation by Needle;
- artifact modification time alone;
- the presence of amendment drafting language;
- chronology between two feed notifications.

## Consequences

- The generic authentic-instruction candidate producer is still useful and may be wired into recurring analysis, but its output is **legal-cause evidence**, not a recency verdict.
- The successful Regulation (EU) 2026/2104 adversary remains valid as proof that the authentic-cause branch can verify a mutation. It must not be generalized into `feed UPDATE == new legal change`.
- Operational analysis needs a temporal-recency gate before automatic positive candidates can become public `CHANGE_FEED` cards.
- Missing temporal evidence must retain uncertainty; `ABSTENTION_FEED` is preferable to a historically true but temporally misleading positive card.
- Source Observation remains immutable provenance. Transient visible-text projection used by the candidate parser is not a second canonical truth store.

## Identity and multilingual corollary

Repeated re-observation must not change semantic mutation identity. Stable legal-source identity (for example CELEX) therefore remains separate from the immutable Source Observation that supplied the bytes. Language is carried explicitly into the mutation candidate; an English observation must never silently become a language-neutral mutation.

## Next executable gate

Before Issue #21 can close, add an operational recency decision that consumes canonical temporal/procedural evidence and regress at least:

1. recent authentic cause + evidenced relevant time → eligible positive card;
2. old authentic cause + fresh Cellar `UPDATE` → no false `CHANGE_FEED`;
3. authentic cause + unresolved temporal relationship → abstention;
4. repeated observations of the same legal cause → stable semantic identity with distinct observation provenance.

# Retrieval temporal boundary v0.1

Status: **ACTIVE P1-D design constraint**

## Finding

The first Article 3 retrieval projection cannot safely answer a generic query such as “which rule applied on 2025-02-01?” by comparing the query date with dates copied into Change Atoms.

The canonical objects deliberately keep different truths separate:

- Change Atoms describe semantic legal effects and reference temporal assertions;
- temporal assertions establish force/application/text-state boundaries;
- rule-lineage edges establish ancestry/continuity, not necessarily temporal supersession;
- Thread events provide chronology but are not a second store of legal validity.

The 2008 SANI atom, for example, has an application-start assertion. A later 2025 successor rule does **not** make it safe for the search projection to invent an end date for the 2008 atom merely because a later Thread event or lineage edge exists. Doing so would collapse semantic lineage, textual mutation and applicability into one inferred validity interval.

## Durable rule

> Date-aware rule retrieval MUST be resolved from canonical temporal relationships under an explicit temporal perspective. The retrieval index may cache the result of that resolution, but it must not synthesize rule-validity intervals from event ordering, mutation dates, successor existence, or lexical dates.

Therefore P1-D fails closed for generic `valid_on` / `as_of` rule filtering until the projection can materialize an evidence-backed validity evaluation for the relevant canonical entity.

## Required query distinction

Any future date-aware retrieval query must state its perspective explicitly:

1. `EX_POST_LEGAL_EFFECT` — what later-complete official evidence says the legal effect was on the valid date;
2. `OFFICIAL_SOURCE_STATE_AS_OF` — what the official-source record supported by a specified source cutoff date.

The second perspective requires a source cutoff date. Neither perspective may be silently defaulted for a user-supplied historical date.

Text-state queries remain a separate dimension from application queries.

## Forbidden shortcuts

The retrieval layer must not:

- treat a Change Atom's first temporal assertion as a complete validity interval;
- infer an end date from the next Thread event;
- infer an end date from a successor lineage edge alone;
- treat amendment/text-state time as application time;
- treat a current consolidation as proof of the official source state at an earlier date;
- default a historical date query to ex-post legal effect without exposing that perspective.

## Implementation consequence

Before adding public date filters, P1-D needs a small composition adapter that:

1. follows an entity's canonical temporal assertion references;
2. resolves the requested dimension with the frozen P0-E resolver;
3. accounts for explicit supersession/end evidence where present;
4. returns `CONTEXT_REQUIRED`, `NOT_ASSERTED`, or another unresolved state rather than manufacturing a boundary;
5. records the perspective and supporting assertion IDs in each retrieval match reason.

This adapter is a derived retrieval projection only. It must not create a new canonical validity model.

## Why this matters

Without this boundary, a fast search feature could become more authoritative-looking than the underlying evidence and silently reintroduce exactly the temporal collapse P0-E was designed to prevent. The absence of a safe answer is therefore a retrieval result, not an indexing defect.

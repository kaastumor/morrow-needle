# Operational publication recency v0.1

## Decision

A Cellar feed timestamp is **operational novelty evidence**, not legal timing.

When a newly processed official feed event leads to a legal mutation verified from
the authentic act itself, Needle may use an explicit canonical publication
assertion for that same act as the public-feed relevance event.

For day-granular official publication metadata, v0.1 evaluates the legal date
against the calendar day carried by the feed event's own offset-aware ingestion
timestamp.

- publication date = event source-calendar day → `CURRENT_RELEVANT`;
- publication date before event source-calendar day → `HISTORICAL_NOT_CURRENT`;
- publication date after event source-calendar day → unresolved;
- missing, malformed or conflicting publication evidence → abstain.

The feed timestamp never replaces the publication date and is never emitted as a
legal relevance dimension or `relevant_at` value.

## Why

The recurring Cellar monitor polls sub-day windows, while authoritative OJ
publication metadata is commonly day-granular. Assigning an invented midnight
or using a Cellar ingestion/build timestamp would manufacture precision.

The operational question and the legal question are therefore separated:

1. **Why is Needle looking now?** A previously unprocessed official feed event.
2. **Which legal event makes the verified mutation current?** An explicit
   canonical publication assertion for the same authentic act.

This is intentionally conservative. A delayed feed event received on a later
calendar day will not resurrect an older publication merely because Needle first
observed it later.

## Binding rule

Publication recency is eligible only when:

1. the legal outcome is `LEGAL_CHANGE_VERIFIED`;
2. verification route is `AUTHENTIC_LEGAL_CAUSE`;
3. the publication assertion comes from the same re-observation that supplied
   the authentic legal text;
4. the assertion subject CELEX equals the re-observed CELEX;
5. recency output is bound to the exact `legal_analysis_identity`;
6. immutable metadata Source Observation provenance survives into Source Mode.

A publication assertion for another act cannot be cross-bound. A source-diff
verified mutation does not inherit the publication date of whichever document
happened to trigger re-observation.

## Precision

`relevant_at` remains the authoritative legal calendar date.

The operational projection may record:

- `novelty_basis = OFFICIAL_FEED_EVENT_DAY`;
- `event_day`;
- `temporal_precision = DAY`.

These are process metadata, not legal timestamps.

## Known limitation

Multiple distinct official feed events for the same semantic mutation on the
same publication day could still produce repeated operational candidates. v0.1
does not add a speculative delivery-deduplication store. We will add one only if
live operation demonstrates that event-key idempotence plus root collapsing is
insufficient.

## Regression target

Regulation (EU) 2026/2104 is the first live adversary:

- authentic document date: 2026-09-17;
- explicit OJ publication date: 2026-09-18;
- observed WORK/UPDATE feed event: 2026-09-18;
- the generic authentic-cause candidate may therefore cross the publication
  recency gate for the historical replay of that actual event;
- replaying the same legal publication against a later feed-event day must
  abstain as historical.

# DISC-05 — source drift and freshness discovery

Issue: #115  
Parent: #104  
Date: 2026-09-24

## Question

Should Needle add a feature that detects when an exposed regression case's
official sources or underlying legal state have drifted since the case's frozen
cutoff?

Alternative explanation: source freshness is real and important, but the
correct control may already be *case-boundary review at reuse time*. A generic
monitor could confuse link availability with legal freshness, duplicate evidence
ownership into the corpus index, and quietly rebuild the stopped live legal
monitoring product.

## Existing scientific rule

The canonical evaluation protocol already distinguishes historical validity from
current-law freshness.

Before reusing a regression case it requires the investigator to:

1. verify that referenced artifacts still exist;
2. distinguish historical truth at the original cutoff from current law;
3. avoid silently replacing an old answer key with a current-law answer;
4. create a new case ID if the intended question changes materially.

That is already the correct scientific boundary. The discovery question is
therefore whether automation adds enough value to justify another owner.

## Corpus ownership test

The current public corpus contains 27 cases.

Across those cases, `evidence_refs` contain:

- 27 `issue:` references;
- 49 `path:` references;
- **0 external source URLs**.

This is intentional. The corpus index points to durable evidence owners; it does
not duplicate their underlying legal sources.

The existing corpus validator already checks the repository-owned part of source
health:

- evidence refs are present;
- referenced repository paths exist;
- paths cannot escape the repository;
- provenance issue references are structurally valid.

A corpus-level link checker would therefore add no new information unless the
corpus also starts owning external URLs or attempts to parse them out of
heterogeneous evidence owners.

Both options are architecturally worse than the current boundary.

## Motivation from OFFICIAL_TRACKER_UPDATE_LAG

Issue #93 established a real freshness failure:

- a currently accessible Commission NIS2 status page could lag newer national
  primary law;
- current page accessibility did not make the tracker's legal-state proposition
  current;
- the correct answer required comparing source observation/update time with
  newer primary law.

This case demonstrates why **HTTP/source availability and legal freshness are
different dimensions**.

A monitor that reports "source still returns 200" would have missed exactly the
failure #93 was designed to preserve.

A content-hash change would not solve the problem either:

- unchanged source content can become stale as newer law appears elsewhere;
- changed HTML can be editorial/navigation noise with no legal consequence;
- dynamic sites can change rendering without changing the decisive proposition;
- a newer primary source can supersede the practical current-state answer while
  the older source remains historically correct.

Freshness is therefore a research comparison, not a link-state property.

## Baseline comparison

### 1. Manual review at a concrete reuse boundary

Current baseline:

- reopen the evidence owner only when the case is being reused for a current
  question or a new evaluation;
- verify the original historical proposition;
- search for newer controlling/primary material relevant to the new temporal
  perspective;
- preserve the original case if it remains historically correct;
- create a new case when the question or legal state has materially changed.

Advantages:

- preserves the distinction between historical and current truth;
- asks the freshness question only when a decision depends on it;
- can inspect multiple authorities/source systems rather than one URL;
- requires no new state or scheduler.

This is currently the strongest baseline.

### 2. Lightweight link checking

Possible check:

- resolve/exercise known URLs;
- report broken/redirected resources.

Problem: the canonical corpus does not own those URLs, and reachability is not
legal freshness.

A link checker could still be useful inside a specific evidence-owner workflow
if broken links become a repeated problem, but no such failure is currently
recorded. Moving URLs into the corpus merely to make a checker convenient would
reverse the ownership model.

Disposition for corpus feature: no demonstrated value.

### 3. Content-hash / page-change monitoring

Possible check:

- periodically fetch an official page;
- compare content/hash/last-modified state.

Problems:

- content change is not equivalent to legal change;
- lack of change is not evidence that no newer controlling source exists;
- dynamic web pages create false positives;
- source-selection logic becomes domain-specific quickly;
- preserved monitor state becomes another operational truth surface.

This is precisely the direction Needle stopped after the public-product gates
failed.

### 4. Rich legal-state/source monitoring

A system that watches EUR-Lex, Commission trackers, Member-State gazettes and
other primary sources could in principle detect some freshness events.

But that is no longer a corpus maintenance helper. It is a live legal-change
monitoring product with source ingestion, identity resolution, time semantics
and operational state.

Issues #49/#59 already removed the assumption that Needle should build that
product without recurring external/user evidence.

## User value test

The useful user question is not:

> "Has this URL changed?"

It is:

> "Can I still rely on this exposed case for the temporal/legal question I am
> asking now?"

That question is case- and purpose-dependent.

For an original historical evaluation, newer law does not invalidate the old
answer key.

For a current-law question, the old case may be the wrong artifact entirely and
a fresh evidence review is required.

For a regression run, live web access itself may be a confounder unless the
historical/current boundary is fixed.

The current protocol captures this distinction better than a generic freshness
badge would.

## Smallest experiment

**No source-freshness feature experiment is justified now.**

Do not add URL fields, scheduled link checks, page hashes, a source-health badge
or monitoring state.

Reopen only after one of these concrete failures occurs:

1. a regression/evaluation is materially misinterpreted because a referenced
   external source disappeared and the evidence owner could not reconstruct it;
2. repeated case reuse spends substantial effort rediscovering which official
   sources still support the frozen proposition;
3. a real user needs current-law freshness over a bounded set of cases and the
   manual reuse review demonstrably fails to scale.

If (1) occurs, first test archival/reference hardening at the evidence-owner
level.

If (2) occurs, first test a case-local source manifest owned by the evidence
artifact, not the corpus index.

If (3) occurs, treat it as a new product/value question rather than smuggling a
live monitoring system into corpus maintenance.

## Adversary

The strongest attack is semantic laundering: a green "fresh" indicator can make
an old source appear currently authoritative when the relevant change happened
somewhere else.

The second attack is ownership duplication. Adding source URLs and status to the
corpus turns the index into a second provenance store.

The third attack is operational creep. Scheduled fetches, stored hashes and
change triage reintroduce the same durable monitor machinery that #84 froze.

The fourth attack is false urgency. Historical regression cases do not expire
merely because the law changes. Their temporal perspective is part of what makes
them valuable.

## Decision

**REJECT**

Reject an automated source-drift/freshness feature for the current Needle
corpus.

Keep the existing manual, question-led freshness check at the point where a case
is reused for a new temporal/current-law purpose. The corpus validator should
continue to protect repository reference integrity only.

This decision preserves a clean separation:

- corpus index → case/evaluation metadata and durable evidence owner;
- evidence owner → legal/source support;
- reuse investigation → current freshness/legal-state comparison when needed.

No URL field, monitor, scheduler, hash store, freshness badge, backend or new
schema is authorised.

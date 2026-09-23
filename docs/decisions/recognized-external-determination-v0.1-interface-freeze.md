# Decision — Recognized External Determination v0.1

**Date:** 2026-09-23  
**Status:** ADOPTED  
**Issue:** #85

## Problem

Needle's non-textual causal contracts largely assumed that direct legally
relevant determinations originated with public/official authorities.

Two unrelated official/legal regimes disprove that assumption.

### Credit rating

S&P Global Ratings, a private rating agency, lowered Capri Holdings Ltd. from
BBB- to BB.

EU prudential law recognizes qualifying ECAI assessments and maps S&P rating
bands into credit quality steps.

The private rating remains private-source truth.

Its eligibility to matter is public-law truth.

### Medical-device certificate state

SZUTEST Uygunluk Değerlendirme A.Ş., Notified Body 2195, suspended and later
withdrew BIOTRH certificate(s).

Directive 93/42/EEC gave designated notified bodies bounded certificate
functions.

The conformity assessor is not the Member State competent authority.

## Decision

Introduce:

- `schemas/recognized-external-determination-v0.1.schema.json`
- `schemas/provenance-record-v0.2.schema.json`

### Recognized External Determination owns

- private originator identity;
- bounded legal-recognition role;
- subject identity;
- direct state transition;
- determination date;
- direct/attributed evidence character;
- public-law relevance;
- guardrails against inferred downstream effects.

It does not own:

- the public authority's later enforcement action;
- a generic actor/accreditation graph;
- downstream institution-specific consequences not evidenced;
- legal time beyond the determination date;
- source artifact bytes.

### Provenance Ledger v0.2 owns source origin

v0.1 provenance assumed all SOURCE_OBSERVATION records were official.

v0.2 adds:

- `source_origin = PUBLIC_OFFICIAL | PRIVATE_PRIMARY`;
- `source_type = PRIVATE_PRIMARY` for private-origin observations;
- explicit provenance entity type for Recognized External Determination.

Legal recognition is not stored in provenance.

A source can be:

> private in origin, legally recognized in effect.

Those are different facts.

## Why no actor registry

The two cases prove recognition provenance matters.

They do not prove that Needle needs:

- a universal organization graph;
- accreditation lifecycle system;
- ECAI registry engine;
- NANDO ingestion platform.

Recognition remains embedded in the determination contract for v0.1 through
bounded public-law references.

If repeated determinations make that recognition fact materially duplicative,
a separate canonical recognition object can be earned later.

## Existing contracts retained

### Authoritative Finding

Still owns public/official categorical determinations about concrete subjects.

It is not widened by pretending private actors are OTHER_OFFICIAL_AUTHORITY.

### Authoritative Metric Observation

Still owns numeric official determinations.

Ordinal private credit ratings are not coerced into metrics.

### Authoritative Dynamic Set

Still owns membership/status in authoritative public sets.

Private certificate/rating transitions are not membership.

### Source Observation v0.1

Remains a narrow official-source adapter contract.

Provenance Ledger v0.2 is the append-only evidence layer that can now preserve
private-primary artifacts as well.

## Reopen rule

Reopen only when a legally recognized non-public determination cannot be
represented as:

- a private originator;
- a bounded recognition role;
- one categorical/status transition;
- direct or attributed source evidence;
- public-law relevance separated from source origin.

Potential future adversaries include benchmark administrators, accredited
verifiers, classification societies and private standards incorporated by
reference. They are not added pre-emptively.

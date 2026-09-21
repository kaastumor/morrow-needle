# Operational relevance event v0.1

Status: **BOUNDARY FROZEN**  
Date: 2026-09-21  
Owner: Issue #21

## Problem

The operational recency gate correctly prevents a fresh Cellar `UPDATE` from resurrecting an old authentic amendment. A remaining ambiguity is more dangerous than it first appears: **"current" is not one legal time dimension**.

A newly published amending act may matter to the public feed today even when its application starts later. Conversely, an old published act may become operationally relevant today because an evidenced application start, transition boundary, deadline, designation, or other legal event occurs today. Treating application date as the universal feed date would hide newly published future-facing changes; treating source/feed freshness as the universal feed date would resurrect historical law.

## Decision

Needle separates two questions:

1. **Feed novelty:** why is this item surfacing in this operational window?
2. **Legal-effect timing:** when does the verified rule/mutation enter force, apply, expire, transition, or otherwise matter legally?

A `CHANGE_FEED` promotion requires an **evidence-backed relevance event** bound to the exact `legal_analysis_identity`. The relevance event must state its dimension rather than returning an undifferentiated boolean/date.

Allowed v0.1 relevance dimensions are:

- `PUBLICATION`
- `ENTRY_INTO_FORCE`
- `APPLICATION_START`
- `APPLICATION_END`
- `TRANSITION_BOUNDARY`
- `DEADLINE`
- `PROCEDURAL_MILESTONE`
- `ENTITY_SPECIFIC_TRIGGER`

This list is intentionally legal/official-event oriented. `CELLAR_UPDATE`, first Needle observation, artifact modification time, crawler time, and model inference are not relevance dimensions.

## Required binding

A relevance evaluation eligible for positive promotion must carry:

- the exact `legal_analysis_identity`;
- `state = CURRENT_RELEVANT`;
- one or more canonical temporal/procedural assertion references;
- a `relevance_dimension` from the bounded set above;
- the evidenced relevant instant/interval or context requirement;
- enough provenance to resolve the assertion to official evidence.

Merely attaching a real assertion from the same instrument is insufficient. The assertion must be evaluated for the mutation/rule being surfaced.

## Public-card consequence

`when_it_matters` must not collapse feed novelty into applicability.

Examples:

- newly published amendment, future application: surface because `PUBLICATION` is current; say separately that application begins later;
- old amendment reaching application date now: surface because `APPLICATION_START` is current; do not claim the law was newly published;
- entity-relative trigger with missing designation/notification context: abstain or expose `CONTEXT_REQUIRED`; do not manufacture a universal date;
- fresh representation update of an old act with no current legal/procedural event: do not emit a new change card.

## Architectural ownership

No new canonical temporal truth store is introduced.

The operational layer consumes P0-E temporal assertions and P0-H procedural events. It may derive a relevance evaluation, but it may not create legal dates. Source-update detection remains an ingestion trigger, not legal-time evidence.

## Why this is a boundary rather than a new temporal model

P0-E already owns legal temporal semantics and P0-H owns procedure state. The operational problem is selecting **which evidenced legal/procedural event explains surfacing now**. Encoding that selection as a typed relevance event avoids reopening either frozen foundation contract.

## Executable gate before Issue #21 completion

The recurring monitor must prove at least these adversaries:

1. current publication + future application -> may surface, with both dimensions kept separate;
2. historical publication + current application start -> may surface as an application-start event, not as newly published law;
3. fresh Cellar update + historical legal events only -> no `CHANGE_FEED` resurrection;
4. entity-specific/context-dependent applicability without context -> abstain / context required;
5. unrelated real temporal assertion -> fail closed even if its date is current.

Until a canonical relevance-event resolver is wired, verified authentic causes in the recurring monitor must remain abstentions rather than using feed timestamps as a shortcut.

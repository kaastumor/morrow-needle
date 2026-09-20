# Discovery: legal afterlife and regime continuity

**Date:** 2026-09-20  
**Lane:** Discovery  
**Status:** Foundation-relevant finding

## The question

Can a legal rule remain historically continuous even when its legal instrument dies?

The answer is **yes conceptually, but not legally continuously**.

That distinction matters enough to become a separate layer in Thread.

## Adversarial case

### Temporary ePrivacy derogation

1. **Regulation (EU) 2021/1232** created a temporary derogation from certain provisions of Directive 2002/58/EC.
2. **Regulation (EU) 2024/1307** amended that act and extended its validity until **3 April 2026**.
3. The extension expired.
4. The long-term replacement framework was not yet in force.
5. The Council's 2026 first-reading reasons explicitly state that the expired regulation could no longer be extended, so the approach was to adopt the full text again as a **new self-standing regulation** with adaptations.
6. **Regulation (EU) 2026/1881** was published on 28 July 2026, entered into force on the third day following publication, and applies until 3 April 2028.

Official sources:
- 2021/1232: https://eur-lex.europa.eu/eli/reg/2021/1232/oj
- 2024/1307: https://eur-lex.europa.eu/eli/reg/2024/1307/oj
- Council first-reading reasons: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:C_202603747
- 2026/1881: https://eur-lex.europa.eu/eli/reg/2026/1881/oj

## Why this breaks a naive Thread

A simple lineage graph might draw:

```
2021/1232 ─────→ 2026/1881
```

That visually implies uninterrupted legal continuity.

But there was a period after expiry of the old regime and before application of the new self-standing act in which that temporary derogation was not in force.

So Thread needs two independent ideas:

### 1. Genealogical continuity
Does the later regime descend from, re-enact, recast, or deliberately continue the earlier legal design?

### 2. Applicability continuity
Was there an uninterrupted interval during which some equivalent rule was legally applicable?

These are not the same.

A regime may have **strong genealogical continuity with a temporal discontinuity**.

## New primitive: REGIME_LINEAGE

Provision lineage is not enough.

A legal regime can survive:
- across a new CELEX act;
- across repeal/recast;
- through repeated extensions;
- through partial replacement;
- after a legal gap;
- with overlapping old/new transitional periods.

Thread therefore needs a higher-order graph:

```
RULE / PROVISION INSTANCES
        │
        ▼
    LEGAL ACTS
        │
        ▼
  REGIME INSTANCES
        │
        ▼
   REGIME LINEAGE
```

A **Regime Instance** is a bounded interval in which a coherent legal mechanism exists under one or more legal instruments.

A **Regime Lineage Edge** explains how one regime relates to the next.

## Continuity states

- `CONTINUOUS` — successor takes over without a gap.
- `GAPPED` — predecessor ends before successor begins.
- `OVERLAPPING` — old and new regimes coexist for some interval.
- `PARTIAL_CONTINUITY` — some rules continue while others lapse.
- `UNKNOWN` — evidence insufficient.

## Relation types

- `EXTENDED_BY`
- `REPLACED_BY`
- `RECAST_AS`
- `REENACTED_AS`
- `SUPERSEDED_BY`
- `CONCEPTUAL_SUCCESSOR`
- `EXPIRED_WITHOUT_SUCCESSOR`

Important: `REENACTED_AS` does not mean the old act legally revived. It means a new instrument deliberately re-establishes substantially the same legal mechanism.

## Foundation consequence

Thread must never render genealogical continuity as a continuous time bar unless applicability continuity is separately proven.

This gives us a new invariant:

> **A lineage edge may cross a legal void. The graph and the timeline must not pretend that ancestry equals uninterrupted applicability.**

## Product idea: HALF-LIFE

A new analytic view inside Thread:

**Half-Life** asks what happens to measures explicitly introduced as temporary.

For a temporary regime, Needle could show:

- original planned duration;
- number of extensions;
- total time actually applicable;
- gaps;
- whether it was replaced by another temporary regime;
- whether it eventually became permanent, expired, or remains temporary;
- which provisions survived into the successor.

This is not an editorial judgment about whether temporary measures are good or bad. It is a factual history of **declared temporariness versus actual legal lifespan**.

Potential public questions:

- “Which temporary EU regimes have been extended most often?”
- “Which temporary derogations outlived their original planned duration by the largest factor?”
- “Which temporary rules expired and later returned?”
- “Which current permanent provisions descend from measures originally introduced as temporary?”

This is exactly the sort of pattern that exists in the documents but is difficult to see from document-by-document browsing.

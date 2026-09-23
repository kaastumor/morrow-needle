# Discovery — a manufacturer metric becomes a statutory premium input

**Date:** 2026-09-23  
**Issue:** #79  
**Status:** second orthogonal case confirms the metric-causal pattern

## Why this case matters

The EU ETS TNAC case could have been dismissed as a special carbon-market
mechanism.

Vehicle CO2 performance gives the same causal shape at a completely different
scale.

Regulation (EU) 2019/631 Article 8 says that when a manufacturer's average
specific CO2 emissions exceed its specific target, the Commission shall impose
an excess-emissions premium.

The formula is fixed in the Regulation:

```
excess emissions × EUR 95 × newly registered vehicles
```

## The official 2022 Bugatti values

Commission Implementing Decision (EU) 2024/865 publishes the following values
for **BUGATTI AUTOMOBILES SAS**:

- registrations: **8**
- average specific emissions: **561.375 g CO2/km**
- specific emissions target: **112.629 g CO2/km**
- distance to target: **+448.746 g CO2/km**

The same Decision explains that a positive distance means the target was
exceeded and states in recital 10 that exactly one passenger-car manufacturer
had a positive distance, so an excess-emissions premium is to be imposed under
Article 8.

Bugatti's row is not marked as pool membership or a derogation.

## Deterministic derived amount

Using the binding Article 8 formula:

```
448.746 × EUR 95 × 8
= EUR 341,046.96
```

The EUR 341,046.96 figure is **derived**.

It is not claimed to be printed in Decision 2024/865.

That distinction is useful: official metric truth and deterministic legal-rule
evaluation are separate provenance layers.

## Cross-domain comparison

### TNAC

```
Commission annual market metric
        ↓
threshold band
        ↓
fixed reserve formula
        ↓
auction-supply adjustment
```

### Manufacturer CO2

```
Commission manufacturer metrics
        ↓
distance > 0
        ↓
fixed premium formula
        ↓
monetary consequence
```

One is system-wide.

One is entity-specific.

One source is a Commission Communication.

One source is an Implementing Decision.

The common concept is no longer plausibly ETS-specific.

## Architecture conclusion

Two different canonical objects are justified.

### 1. Authoritative Metric Observation

Own direct numeric truth:

- metric identity;
- subject;
- authority;
- reference period;
- numeric value;
- unit;
- observation/determination character;
- exact source evidence.

### 2. Metric Rule Evaluation

Own the derived application of a fixed legal predicate or formula:

- governing rule reference;
- metric input references;
- predicate/band result;
- formula inputs;
- derived result;
- direct-vs-derived evidence distinction.

They should remain separate because:

- the same observation could be re-evaluated if the law changes;
- the same rule produces a different result from next year's observation;
- correcting the metric should not mutate the rule;
- changing the rule should not rewrite historical metric truth.

## What this should not become

Not a generic rules engine.

Not arbitrary mathematical expression execution.

Not a replacement for Change Atom.

Not a way to turn all contextual numeric data into legal truth.

The first contract should accept only authoritative numeric observations with
explicit legal relevance.

The evaluation contract should support only simple evidenced scalar comparisons
and deterministic arithmetic sufficient for the two pinned cases.

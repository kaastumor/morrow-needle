# Operational authentic-cause verification route v0.1

Status: **ACTIVE P2 DESIGN DECISION**  
Issue: #21  
Date: 2026-09-21

## Question

Must an operational official-feed UPDATE have a pre-event source baseline before Needle may emit a verified legal-change card?

## Adversarial evidence

The live Regulation (EU) 2026/2104 case starts from an official Cellar WORK/UPDATE event and resolves the authentic amending act. The authentic act contains an explicit instruction adding zones `US-2.1405` and `US-2.1406` after `US-2.1404` in Annex V of Implementing Regulation (EU) 2021/404.

The target consolidation does not expose a sufficiently current before/after checkpoint pair for that mutation. Treating this as a mandatory blocker would incorrectly make a derivative consolidation more authoritative than the authentic legal cause.

The live probe is reproducible in `scripts/probe_reg2104_live_case.py`; the regression boundary is executable in `tests/test_operational_authentic_cause.py`.

## Decision

A missing pre-event source baseline blocks **source-diff verification**, but it does not block legal verification when an independent authentic legal cause satisfies the frozen mutation/evidence contract.

`LEGAL_CHANGE_VERIFIED` may therefore pass through `source_change.classification == UNRESOLVED` only when all of the following hold:

1. the unresolved basis includes `MISSING_BASELINE`;
2. the current official observation exists (`MISSING_OBSERVATION` is absent);
3. downstream explicitly declares `verification_route = AUTHENTIC_LEGAL_CAUSE`;
4. downstream disposition is `LEGAL_CHANGE_VERIFIED`;
5. canonical mutation and evidence references close under the existing provenance/evidence rules.

This is not an exception that upgrades source state. The operational result must retain the unresolved source comparison and state that legal verification came from the authentic modifying act rather than a before/after source diff.

## Forbidden inference

The following are forbidden:

- treating the feed UPDATE action itself as proof of legal change;
- pretending that a missing baseline exists;
- synthesising a consolidated after-state from an authentic instruction;
- allowing `SOURCE_DIFF` or model inference to bypass a missing baseline;
- allowing a missing current observation to be overridden by the authentic-cause route;
- downgrading authentic amending evidence merely because a derivative consolidation lags.

## Architectural consequence

Operational baseline persistence remains valuable for source-change classification, idempotence, representation-noise detection and future comparison. It is **not a universal prerequisite for legal truth**.

This preserves the Morrow Constitution's source hierarchy: authentic legal acts can establish a mutation directly; consolidated texts remain verification checkpoints rather than sole authority.

## Next implementation slice

Issue #21 should now wire one live event-driven authentic-cause case through the ordinary operational result/card/retrieval path and persist its provenance, while retaining `UNRESOLVED/MISSING_BASELINE` on the source-comparison branch. The success condition is a genuine `CHANGE_FEED` card whose displayed legal claims close to authentic official evidence without claiming a nonexistent source diff.

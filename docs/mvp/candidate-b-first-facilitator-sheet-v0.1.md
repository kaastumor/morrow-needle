# Candidate B — first crossover facilitator sheet v0.1

Status: **FROZEN BEFORE PARTICIPANT RESPONSE**

Issue: #422

Do not show this sheet to the participant before the scored tasks.

Query date:

> **26 September 2026**

## Interpretation boundary

This is a one-participant usability pilot.

It can generate a user signal.

It cannot establish:
- population-level usability;
- willingness to pay;
- commercial-product superiority;
- product-market fit;
- causal effect size.

## Arm order and case assignment

### Calibration — unscored

GAR — **EN 497:2022**

### Arm O — strongest free official-source workflow

1. Machinery — **EN 50434:2014**
2. LVD — **EN 60335-2-60:2003**

### Arm B — Candidate-B card

1. Toy Safety — **EN 71-1:2014+A1:2018**
2. LVD — **EN 60335-2-14:2006**

Do not swap cases after seeing participant behavior.

If a second participant is later earned, reverse the Arm O / Arm B allocation.

## Strong official baseline

Allow:
- Commission Formal Objections / harmonised-standards navigation;
- direct EUR-Lex/OJ access;
- ordinary search;
- notes/bookmarks;
- a source-grounded capable model if that is part of the participant's real workflow.

Do not deliberately obscure the Commission consolidated index.

## Timing rule

Start timing when the case identifier and task are visible.

Stop timing when the participant says the answer is complete/confident.

Record corrections separately.

Do not pressure the participant to stop early.

## Observation grid

For each scored case record:

| Field | Value |
| --- | --- |
| Case | |
| Arm | O / B |
| Start time | |
| Stop time | |
| Time to confident answer | |
| Final OJ status correct? | yes / partial / no |
| Presumption consequence correct? | yes / partial / no |
| Restriction/future transition correct? | yes / partial / no |
| Official documents/pages opened | |
| Re-openings / backtracking | |
| Confusion event(s) | |
| Self-correction(s) | |
| Confidence 1–5 | |
| Unsafe overclaim / false certainty? | |
| Notes | |

## Canonical answer key

### Calibration — GAR / EN 497:2022

Expected current status:

> **NOT_CITED**

Owning event:

> Commission Implementing Decision (EU) 2026/1750 formally decides not to publish the reference.

Effective date:

> **24 July 2026**

Presumption consequence:

> No Article 13 presumption of conformity arises via this OJ reference.

Important non-implication:

> Non-publication does not mean the standard is prohibited or that no alternative conformity route exists.

### Arm O — Machinery / EN 50434:2014

Expected current status:

> **CITED_WITH_RESTRICTION**

Owning event:

> Commission Implementing Decision (EU) 2026/80.

Effective date:

> **13 January 2026**

Restriction:

> For machines whose shredding means can rotate above **300 r/min**, EN 50434:2014 does not confer presumption of conformity with Directive 2006/42/EC Annex I points **1.1.2(a)** and **1.3.3**.

Critical error:

> Treating the restriction as withdrawal of the entire OJ reference.

### Arm O — LVD / EN 60335-2-60:2003

Expected current status on 26 September 2026:

> **CITED**

Future transition:

> Withdrawal is already legally fixed for **18 January 2027**.

Owning event:

> Commission Implementing Decision (EU) 2025/1457.

Critical temporal distinction:

> The decision exists in 2025, but the relevant Annex deletion applies only from 18 January 2027.

Critical error:

> Treating adoption/entry into force of the 2025 decision as immediate withdrawal of the OJ reference.

Important non-implication:

> Withdrawal of an OJ reference does not mean the European standard itself ceases to exist or that compliance becomes impossible by other technical means.

### Arm B — Toy Safety / EN 71-1:2014+A1:2018

Expected current status:

> **CITED_WITH_RESTRICTION**

Owning event:

> Commission Implementing Decision (EU) 2025/1785.

Effective date:

> **10 September 2025**

Restriction:

> Clauses **3.19** and **4.15.1** as regards **wave rollers** do not confer the stated presumption of conformity with Directive 2009/48/EC Article 10(2) and Annex II Part I point 3.

Critical error:

> Treating the restriction as loss of every legal effect of EN 71-1:2014+A1:2018.

### Arm B — LVD / EN 60335-2-14:2006

Expected current status:

> **NOT_CITED**

Owning event:

> Commission Implementing Decision (EU) 2025/1464 formally decides not to publish the OJ reference.

Effective date:

> **18 July 2025**

Presumption consequence:

> No Article 12 presumption of conformity arises via this OJ reference.

Important non-implication:

> Non-publication does not mean the European standard ceases to exist, is prohibited, or that no alternative conformity route exists.

## Post-task questions

Ask verbatim:

1. Which workflow would you choose for the next similar task, and why?
2. What information was missing from either workflow?
3. What information felt redundant?
4. What would make the compact card unsafe to rely on?
5. Is known-standard OJ status useful on its own in your work?
6. Is discovering which standards apply to a product actually the larger problem?
7. Would you still open the underlying official act before acting? If yes, when?
8. Was the current-vs-future distinction useful, obvious, or unnecessary?
9. Did the restriction cases feel easier to reason about in one workflow than the other?

## First-session decision rule

Use exactly one disposition:

### USER_SIGNAL_POSITIVE — DIRECT_PRODUCT_GATE_NEXT

Use only if:
- substantive correctness is not reduced;
- Candidate-B reduces navigation/reconstruction on at least one legally non-trivial case;
- participant prefers the card for at least one recurring workflow;
- no material false-certainty problem appears.

### USER_SIGNAL_MIXED — NARROW_OR_REPAIR

Use if:
- some convenience/safety value appears;
- but trust, missing context, or workflow fit prevents a clean positive.

### OFFICIAL_WORKFLOW_PREFERRED — CANDIDATE_B_NARROW_OR_STOP

Use if:
- the official workflow is preferred;
- or Candidate-B adds little after the participant's normal source practice;
- or the real need is primarily outside the known-standard status wedge.

### SESSION_UNINTERPRETABLE

Use only for a genuine execution failure:
- participant is outside target user class;
- task instructions fail materially;
- prototype fails to render;
- session is interrupted before meaningful comparison.

Do not relabel a negative session as uninterpretable.

## Next-step discipline

A positive session earns only:

> direct access to an incumbent commercial product comparison under #411.

It does not earn feature growth.

A mixed/negative session must narrow, repair, or stop Candidate B before any new build.

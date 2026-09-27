# #467 — Typed upstream-change blast radius as a legal review queue

Date: 2026-09-27  
Disposition: **ADOPT_FOR_EXPERIMENT — PROVISION-AWARE REVIEW PROPAGATION**

## 1. Question

> When one represented upstream legal node changes, can the typed regime web identify a small, inspectable set of downstream claims/acts that deserve human review — without claiming that every reachable node is legally affected?

Yes, but ordinary graph reachability is too broad.

The safe rule is:

> **review propagation requires a verified typed dependency plus semantic/provision overlap with the changed legal material.**

Being under the same parent Regulation, inside the same family, cited nearby, or visually connected is not enough.

## 2. Terms

### Direct review candidate

The legal resource or displayed claim is itself directly amended, replaced, corrected, activated or otherwise changed by the source event.

This is the strongest queue state.

### Downstream review candidate

The candidate is not itself directly amended, but a verified dependency says its displayed meaning relies on a provision/mechanism that the upstream event changed.

This requires dependency overlap, not mere ancestry.

### Context only

The item helps explain the change but no current review obligation is inferred.

Examples:
- predecessor lineage;
- later event already incorporating the upstream change;
- non-binding guidance with no claim-level dependency established.

### No propagation

No sufficiently specific typed relation connects the change to the represented claim.

Default to this state.

## 3. Propagating relationship classes

This is a review-propagation contract, not a universal legal ontology.

### A. Direct mutation edge — propagates directly

Examples:
- `AMENDED_BY`
- `CORRECTED_BY`
- explicit repeal/replacement affecting the represented current-state claim.

Rule:
> target claim/resource becomes a direct review candidate.

Do not recursively propagate further unless a second verified dependency exists.

### B. Operative dependency — may propagate downstream

Examples:
- `IMPORTS_DEFINITION_FROM`
- `USES_PROCEDURE_IN`
- provision-specific implementing/supplementing dependency.

Rule:
> propagate only if the upstream change overlaps the exact provision/mechanism the dependent claim consumes.

An amendment somewhere else in the upstream act does not trigger the dependency.

### C. Enabling / implementing relation — conditional propagation

Example:
> implementing measure adopted under parent Article X.

Rule:
> parent change triggers child review only when the changed provision is:
> - the legal basis/enabling provision used by the child; or
> - a substantive provision the child's displayed claim implements/operationalises.

Same-parent membership is insufficient.

### D. Temporal/operational trigger — propagates to state projections

Example:
> EUDAMED functionality notice/decision starts transition periods tied to specified provisions.

Rule:
> review the represented temporal/state claims whose applicability is expressly keyed to that trigger.

Do not mark unrelated requirements under the same core Regulation.

## 4. Non-propagating relationship classes by default

### Family membership

“Implementing act under MDR” does not cause every implementing act to be reviewed whenever MDR changes.

> **NO PROPAGATION**

### Lineage / genealogy

Predecessor/successor structure gives context.

It does not make predecessor claims inherit later changes or dates.

> **CONTEXT ONLY**, unless the amended transition rule explicitly reaches predecessor effects.

### Non-binding guidance

Law change does not automatically make every guidance item a review candidate.

Only propagate if a specific maintained claim is known to depend on that guidance/provision relationship.

> default **NO PROPAGATION / CONTEXT ONLY**

### Proposal relation

A proposal does not change current legal state.

> **NO CURRENT-LAW PROPAGATION**

### Generic citation / mention

> **NO PROPAGATION**

### Cross-list / projection reuse

Showing the same act in two navigation lenses does not create a second dependency.

> **NO EXTRA PROPAGATION**

## 5. Stop conditions

Propagation stops when any of these applies:

1. relation is unverified;
2. relation is generic/contextual only;
3. changed provision does not overlap the dependency locator;
4. dependent claim is outside the bounded projection;
5. no current dependent claim is represented;
6. the downstream item postdates the upstream change and its represented state has already been verified against the later legal state;
7. propagation would require assuming temporal/applicability inheritance;
8. next step is only family membership;
9. next step is only non-binding guidance without an explicit claim dependency;
10. a proposal node is reached.

The queue should prefer abstention over broad propagation.

## 6. Control A — Regulation (EU) 2024/1860

### Official change

Regulation (EU) 2024/1860 expressly amends both:
- Regulation (EU) 2017/745 (MDR);
- Regulation (EU) 2017/746 (IVDR).

Its title and provisions cover:
- gradual EUDAMED rollout;
- information obligations concerning interruption/discontinuation of supply;
- transitional provisions for certain IVDs.

The MDR amendments include EUDAMED functionality/application mechanics, including Article 34 and Article 123 timing. The IVDR branch receives corresponding EUDAMED/transition changes and additional IVDR transitional amendments.

Official sources:
- https://eur-lex.europa.eu/eli/reg/2024/1860/oj/eng
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1860

### Review queue

#### Direct review candidates

1. **MDR core current-state/context claim**
   - directly amended by 2024/1860.

2. **IVDR core current-state/context claim**
   - directly amended by 2024/1860.

3. **Joint transition/change lane**
   - 2024/1860 is itself a represented member;
   - its relation wording and affected branches must remain accurate.

4. **IVDR transition explanation**
   - direct subject of the amendment.

#### Downstream review candidate

5. **EUDAMED temporal/system-state explanation**
   - 2024/1860 changes the legal mechanics for gradual rollout and application of EUDAMED-related obligations;
   - the represented system lane therefore deserves review against those amended trigger provisions.

This is a review of the **EUDAMED state explanation**, not automatic review of every EUDAMED-related act.

#### Context only

6. **Decision (EU) 2025/2371**
   - later functionality event;
   - it postdates the 2024 amendment and is already represented as the later operational trigger;
   - at the current evidence checkpoint it helps explain resulting state rather than constituting an unresolved downstream review item.

7. **Predecessor directives**
   - useful because some transition clauses retain predecessor effects for bounded periods;
   - their genealogy itself is not changed by 2024/1860.

#### No propagation

- 2022/1107 common specifications merely because it is IVDR;
- 2022/2346 Annex XVI common specifications merely because it is MDR;
- 2023/2713 IVDR reference laboratories;
- 2026/977 notified-body/conformity-assessment requirements;
- expert-panel decisions;
- MDR delegated UDI/reassessment/clinical-investigation children;
- MDCG guidance sample;
- 2025 proposal lane.

Why:
> no verified provision-specific dependency from the 2024/1860 changes to those represented claims is currently encoded.

### Result

The queue remains small.

The core insight is:
> **cross-branch amendment != review every descendant of both branches.**

## 7. Control B — Implementing Decision (EU) 2025/1324

### Official change

Decision (EU) 2025/1324 expressly amends Implementing Decision (EU) 2019/1396.

It changes administrative aspects of expert panels and designates an additional panel. The consolidated 2019/1396 text shows the 2025 amendment and includes panels performing specified MDR and IVDR tasks.

Official sources:
- https://eur-lex.europa.eu/eli/dec_impl/2025/1324/oj/eng
- https://eur-lex.europa.eu/eli/dec_impl/2019/1396/2025-07-28/eng

### Review queue

#### Direct review candidate

1. **2019/1396 expert-panel node/claim**
   - exact legal resource amended.

2. **“later amended by 2025/1324” relationship**
   - direct relation should be verified against the new act.

#### Downstream review candidates

> **None earned in the current bounded projection.**

The fact that expert panels perform MDR and IVDR tasks does not justify propagating to:
- MDR core;
- IVDR core;
- all conformity-assessment items;
- all implementing measures.

No further represented claim has an explicit dependency on a changed expert-panel provision.

### Result

Propagation stops after the directly amended expert-panel branch.

This is a useful positive control:
> a dense legal web does **not** imply a large blast radius for every amendment.

## 8. Control C — Implementing Regulation (EU) 2023/1194

### Official change

Implementing Regulation (EU) 2023/1194 expressly amends Implementing Regulation (EU) 2022/2346 regarding transitional provisions for Annex XVI products under MDR.

Official source:
https://eur-lex.europa.eu/eli/reg_impl/2023/1194/oj/eng

### Current projection

- 2022/2346 is represented as a child;
- 2023/1194 is deliberately outside the normal child expansion;
- #464 already exposes this as a known coverage omission.

### Review queue

#### Direct review candidate

1. **2022/2346 representative node**
   - its transition-state interpretation cannot safely be treated as self-contained without considering 2023/1194.

#### Context only

2. **MDR core branch**
   - supplies parent context;
   - 2023/1194 amends the child, not MDR itself.

#### Downstream review candidates

> **None represented.**

There is no further typed child dependency from 2022/2346 in the bounded slice.

### Result

A coverage diagnostic can produce a targeted one-item review queue without forcing graph expansion.

## 9. False-positive adversaries

### FP1 — parent changed, therefore all children stale

Reject.

A parent Regulation can be amended in one narrow area while most implementing/delegated acts are untouched.

Required filter:
> changed provision × dependency locator.

### FP2 — same family means dependent

Reject.

Two implementing acts under MDR may regulate unrelated mechanisms.

Family membership is navigation, not dependency.

### FP3 — indirect subject-matter similarity

Reject.

“Both concern conformity assessment” is not enough to propagate review.

A source-backed relationship or provision overlap is needed.

### FP4 — proposal touching same provisions

Reject for current legal state.

Proposal can create a separate procedure/watch item, not a current-law blast radius.

### FP5 — guidance is older than amendment

Insufficient.

Age alone does not show guidance is stale.
Need:
- actual guidance claim;
- upstream changed provision;
- dependency/relevance evidence.

### FP6 — descendant is later in time

Later publication does not automatically prove it incorporated every prior upstream change.

For this prototype, “postdates upstream change” is only a stop condition when the represented downstream state was actually verified against the later legal state.

## 10. Minimal executable model

A graph database is not earned.

The next demonstration can use a tiny frozen change-impact dataset:

```text
change event
  -> direct targets
  -> typed dependency edges
  -> provision-overlap decision
  -> queue status:
       DIRECT_REVIEW
       DOWNSTREAM_REVIEW
       CONTEXT_ONLY
       NO_PROPAGATION
       OUT_OF_SCOPE
```

For each candidate show:
- why it entered the queue;
- exact edge/provision;
- why propagation stopped;
- official source.

No scores.

## 11. What this could become

If this survives a second control set later, a maintainer could ask:

> “Article/provision X changed. Which of our maintained explanations and downstream legal-state projections should I re-open?”

That is materially safer than:

> “show every node downstream of X.”

The first is an evidence-backed maintenance workflow.

The second is graph theatre.

## 12. Disposition

> **ADOPT_FOR_EXPERIMENT — PROVISION-AWARE REVIEW PROPAGATION**

Why:
- all three controls produce small, explainable queues;
- one cross-branch amendment does not explode across the regime;
- direct child amendment correctly stops after one node;
- out-of-slice amendment yields a targeted review without graph expansion;
- useful filtering comes from typed/provision-aware relations, not node count.

Next bounded build:

> add a static **Change review** demonstration to the medical-devices regime page using exactly these three controls.

The demonstration must show why each candidate is included and why obvious neighboring nodes are excluded.

Do not automate source monitoring or infer legal effect.

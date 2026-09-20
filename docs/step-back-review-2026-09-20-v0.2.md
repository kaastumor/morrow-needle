# Step-back review — 2026-09-20 v0.2

## Question

Are we still building the project described by the original Morrow // Needle thesis, or are we drifting into an increasingly correct but increasingly self-contained legal-data engine?

## Conclusion

**The project is still aligned in purpose and architecture, but execution is now at a pivot point.**

The strongest alignment is epistemic:
- official evidence outranks models;
- legal text, semantic interpretation, time, procedure, identity and provenance remain separate;
- uncertainty and non-impact survive the pipeline;
- product analytics derive from canonical truth rather than duplicating it.

The first P2 capabilities — Half-Life, Source Anomaly and Legislative X-Ray — are not mission drift. They are concrete demonstrations of the original promise to make legal change inspectable in ways document databases do not.

The main risk is now **allocation drift** rather than conceptual drift.

We have proved the engine much more deeply than we have proved the public product loop.

## What the original thesis promised

Needle:
- finds what is changing now;
- explains what changed compared with what;
- shows when the change matters;
- shows who or what it concerns when evidence supports that;
- links every factual legal claim to official evidence.

Thread:
- reconstructs how a rule became what it is today.

The repository now proves most of the second promise and the correctness prerequisites for the first.

It does not yet prove, operationally, that a newly observed official update can travel through the whole system and emerge automatically as a useful public change card.

## What is strongly on course

### 1. The truth model

P0/P1 integration has repeatedly exposed real defects without forcing the project to abandon its core architecture.

That is a strong signal that the foundations are earning their complexity rather than merely accumulating it.

### 2. Product differentiation

The first P2 analytics are genuinely distinctive:

- **Half-Life** — temporary regimes as extensions, gaps and successor episodes instead of one document.
- **Source Anomaly** — source infrastructure irregularities without confusing them with legal state.
- **Legislative X-Ray** — changed legal operation through dependencies even when local text is unchanged.

These capabilities follow directly from the underlying evidence graph and are difficult to reproduce with ordinary document summarisation.

### 3. Projection-first P2 design

P2 has so far resisted creating second truth stores.

This is essential. Public views remain disposable projections over canonical evidence.

### 4. Adversarial culture

Negative regressions, abstention and contradictory source states are first-class.

That keeps the project from optimising only for clean demo cases.

## Where we are underweight

### 1. "What is changing now" is not yet operationally proven

Update detection exists.
Mutation exists.
Semantic extraction exists.
Temporal/procedure resolution exists.
Retrieval exists.
Rendering exists.

But the chain is still mostly exercised through selected fixtures and targeted live probes.

The next major proof must start from an **observed update event**, not from a known interesting act.

### 2. There is no actual public delivery surface yet

There is currently no public UI or API implementation in the repository.

That is acceptable during P0/P1, but it becomes a strategic risk if P2 continues to add analytics without a delivery loop.

### 3. There is no persistent operational corpus yet

The architecture calls for a structured store and immutable raw artifacts.

The current repository remains primarily code + fixtures + CI evidence.

Before scale, we need to learn what minimum persistent operational state the real update pipeline actually requires.

### 4. The user-facing information hierarchy is still mostly untested

We have generated 3-second / 30-second / 3-minute text, but have not yet tested:
- which facts deserve the first screen;
- how Source Mode should feel;
- how unknowns/non-impact are displayed;
- whether users understand direct vs derived evidence;
- whether a feed item is useful without opening the full Thread.

### 5. "Who or what is affected" remains thin

This is correctly postponed because inference risk is high, but it remains one of the original thesis fields.

The eventual impact model should start with directly evidenced entities and only then introduce derived/interpretive layers.

## Drift to resist from here

1. **Do not freeze a new analytic primitive every time we find an interesting pattern.**
   Three P2 primitives are enough to prove the projection architecture.

2. **Do not build correctness machinery for hypothetical scale before observing the operational bottlenecks.**

3. **Do not confuse a growing Gold Corpus with a growing product.**
   Both matter; they are different assets.

4. **Do not build a polished interface over hand-selected cases.**
   The feed must first be fed by the real update loop.

5. **Do not expand jurisdiction/source scope yet.**
   EU legal change is already deep enough to prove or disprove the product.

## Strategic correction

After Legislative X-Ray v0.1 freezes, the next milestone is:

**Issue #21 — official update → verified public feed card.**

This is the first operational Needle slice.

It should connect existing components rather than invent new ontology.

Required proof:
- live update event in;
- official bytes re-observed;
- targeted recomputation;
- legal mutation or explicit non-impact/abstention;
- semantic/temporal state where support exists;
- retrieval/index update;
- public card out;
- Source Mode complete;
- idempotent rerun;
- at least three heterogeneous live events.

Until that is green, new P2 analytic primitives should generally wait.

## Product checkpoint after Issue #21

Once the operational slice exists, run a different kind of review:

- Is the feed useful to a non-specialist?
- What did a human learn in 30 seconds?
- Which cards were noise?
- Which unknowns were confusing?
- Did Source Mode help trust?
- What information was repeatedly missing?
- Did we need a database/API/UI assumption that the research engine did not reveal?

That review should drive the next architecture, not another abstract schema exercise.

## Final assessment

**We are not off-course. We have reached the point where staying on-course requires changing the type of work.**

The first phase asked:

> Can we represent EU legal change without lying about source, identity, time or interpretation?

The evidence now says: increasingly, yes.

The next phase must ask:

> Can Needle notice real changes continuously and make them useful to a person?

That is now the highest-value unknown.

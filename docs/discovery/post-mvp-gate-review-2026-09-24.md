# Post-MVP discovery gate review — 24 September 2026

Status: **COMPLETE — SIMPLIFY**  
Gate: #104  
Entry gate: #110 / `TECHNICAL_MVP_CANDIDATE`

## Executive decision

The bounded post-MVP discovery runway is complete.

**Decision: SIMPLIFY.**

The discovery gate does **not** authorize another implementation horizon.

Needle remains:

> **adversarial legal-research corpus + evaluation protocol**

The Corpus Explorer remains a thin technical MVP candidate while H-16 is still
unresolved by real/manual usability evidence. No additional product feature,
service, workflow, model integration, monitor, adapter or authoring surface has
earned implementation.

An intentionally idle autonomous queue is healthier than converting conditional
research ideas into a roadmap.

## Gate evidence

| Issue | Question | Disposition | Consequence |
|---|---|---|---|
| #111 | Metamorphic legal-state pairs | **ADOPT_FOR_EXPERIMENT** | Only one future fresh, pre-registered controlled contrast pair may test whether pair-level flip/invariance scoring adds information beyond case-level grading. No schema/UI/generator. |
| #112 | External expert review / trust boundary | **ADOPT_FOR_EXPERIMENT** | A bounded six-case independent review is justified only if Needle later seeks a stronger answer-key-quality or benchmark-validity claim. No blanket review or reviewer platform. |
| #113 | Corpus authoring / contribution ergonomics | **REJECT** | Recent admissions show research/evidence work dominates mechanical index entry. No authoring UI, generator or issue-form workflow. |
| #114 | Longitudinal regression / model drift | **REVISE** | Retain only event-triggered, question-led regression replay for a concrete model/harness migration. Reject periodic monitoring, dashboard and leaderboard. |
| #115 | Source drift / freshness | **REJECT** | Freshness remains a question-led review at case reuse. No URL fields, link/content monitor, freshness badge or live legal-monitoring surface. |
| #116 | Benchmark interoperability | **PARK** | Generic adapters add no demonstrated value. A disposable one-way export of selected revealed EVALUATION cases may be reconsidered only for a named external/reproducibility need. |

The result is deliberately subtractive: six plausible post-MVP feature themes
produced **zero implementation authorizations**.

## Project Health Check

### North-star alignment

The gate improved the project by preventing the technical MVP from becoming a
default feature roadmap.

The strongest accumulated evidence still says that Needle's durable
project-specific value is in:

- preserving real adversarial legal-information failures;
- keeping derivation and validation separate;
- making exposure/contamination explicit;
- running evaluations that can preserve parity and negative results;
- retaining provenance without requiring a broad legal product.

Nothing in #111–#116 overturns the earlier evidence against Full Needle, default
Core, a Method correctness layer, or a general live legal-change product.

The unresolved product-form question is narrower: whether the existing static
Explorer is materially more useful to a real user than direct repository/corpus
inspection. Technical completion does not answer that question.

### Competing identities

1. **Incumbent:** corpus + evaluation protocol, with the existing thin static
   Explorer as an experimental projection.
2. **Smaller:** corpus + evaluation protocol only; repository-native inspection
   remains sufficient and the Explorer is not developed further.
3. **Adjacent:** a general legal benchmark/evaluation platform with authoring,
   expert-review workflow, model replay, source monitoring and interoperability
   adapters.

The evidence supports keeping (1) provisionally while (2) remains the strongest
simpler alternative. The discovery runway provides no support for (3).

The discriminating evidence between (1) and (2) is real/manual usability of the
Explorer, not more implementation.

### Canonical ownership

The discovery results reinforce the existing ownership boundaries:

- `corpus/index-v0.1.json` owns case/evaluation index metadata;
- referenced issues/research/fixtures own legal evidence and evaluation
  artifacts;
- the evaluation protocol owns contamination/sealing/comparator discipline;
- the Explorer is derived presentation only.

No discovery result demonstrated a need to move external source URLs, live
freshness state, model-run history, reviewer state or benchmark-adapter state
into the corpus.

### Evidence and adversarial sufficiency

The gate attacked six attractive growth paths instead of assuming that an MVP
should generate a roadmap.

Material negative/subtractive findings:

- authoring mechanics are not the demonstrated admission bottleneck;
- periodic model drift monitoring would create weakly interpretable telemetry
  without a concrete migration question;
- source reachability/change is not legal freshness;
- generic benchmark compatibility would either lose Needle semantics or recreate
  them as custom extensions.

The two surviving experiment ideas are explicitly conditional. They are not
AUTO READY merely because the discovery note exists.

### Complexity and leanness

The discovery runway added documentation only. It added no:

- runtime dependency;
- backend or service;
- new schema;
- scheduler;
- model integration;
- source monitor;
- authoring workflow;
- adapter;
- durable generated state.

The existing Explorer already satisfies the technical MVP boundary without such
machinery. Further code would currently increase maintenance surface faster than
demonstrated value.

### Automation / GitHub behavior

The bounded night sprint is complete and disabled. No replacement scheduled
worker is justified.

Repository CI again executed normally for the MVP and discovery work. The
project should not create a recurring worker merely because an idle queue feels
uncomfortable.

Repository administration / branch-protection state remains **UNVERIFIED** where
the current GitHub integration cannot authoritatively inspect it; no assumption
of protection is introduced here.

### Reproducibility / privacy

No discovery task required private/customer material, new external state or
secret-bearing infrastructure. Existing sanitation remains sufficient for this
horizon.

The project continues to separate pinned regression evidence from live-source
research and does not treat operational caches/monitoring state as canonical
truth.

## H-16 / Explorer boundary

#110 established a **TECHNICAL_MVP_CANDIDATE**.

That proves the thin static implementation satisfies its deterministic technical
contract. It does not establish that the Explorer materially improves
inspectability/usefulness over the smaller corpus + protocol form.

Therefore:

- keep #103 open;
- freeze feature development on the Explorer;
- do not simulate sponsor/user acceptance;
- resolve H-16 only from actual use/manual browser evidence;
- a negative usability result may legitimately shrink Needle back to corpus +
  protocol only.

## What remains dormant, not queued

### #111 controlled contrast

Reconsider only when a fresh legal scenario and a real evaluation claim justify
a pre-registered contrast. The pair must be independently evidence-grounded
before execution.

### #112 expert review

Reconsider only when Needle intends to make a stronger claim that depends on
contestable legal answer-key correctness or benchmark validity.

Neither condition currently exists. Creating those conditions merely to execute
the experiments would be circular.

## Autonomous next state

**IDLE BY DESIGN.**

New autonomous work requires one of:

1. a fresh falsifiable legal-information question that can add or challenge a
   corpus failure mechanism;
2. real/manual user evidence about the Corpus Explorer that can resolve H-16;
3. a concrete stronger-validity claim that triggers #112;
4. a fresh controlled-contrast evaluation question that triggers #111;
5. a named external reproducibility/execution requirement that makes the parked
   #116 export boundary relevant;
6. another directly observed failure in the current project system.

Until such evidence exists, no AUTO READY replacement queue should be created.

## Final direction

**SIMPLIFY**

Keep the purpose and the smallest demonstrated machinery. Preserve the existing
technical Explorer candidate without extending it. Close the post-MVP discovery
gate. Do not create another implementation horizon.

The project is allowed to be quiet between useful questions.

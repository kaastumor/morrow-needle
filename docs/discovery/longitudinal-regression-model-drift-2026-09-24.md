# DISC-04 — longitudinal regression and model-drift discovery

Issue: #114  
Parent: #104  
Date: 2026-09-24

## Question

Do Needle's exposed regression cases become materially more valuable if they are
periodically replayed across model versions, or would that create a low-value
leaderboard/maintenance loop?

Alternative explanation: the corpus already has value as a stable set of known
adversaries. Replaying it only adds information when there is a concrete
comparison question and the execution boundary is controlled tightly enough to
make the difference interpretable.

## Current corpus boundary

The canonical corpus currently contains:

- 27 exposed cases;
- 17 DERIVATION cases;
- 10 revealed EVALUATION cases;
- 6 SURFACED_TRAP_ADJUDICATION evaluation cases;
- 4 LATENT_TRAP_DETECTION evaluation cases;
- 14 trap classes.

Every current case is public/exposed and `REGRESSION_ONLY`. Replaying these
cases can therefore measure repeat performance on known material. It cannot
become fresh blind evidence merely because a model name or date changes.

The canonical evaluation protocol already states that longitudinal comparison is
allowed only as regression evidence and requires preservation of model/version
and tool settings. New claims of generalised superiority still require fresh
sealed cases.

## What longitudinal replay could establish

A controlled replay can answer narrow questions such as:

- did a pinned model/runtime configuration that previously passed a known case
  now fail it;
- did a new pinned model snapshot repair a previously observed failure;
- does a provider/model migration preserve behavior on the known adversarial
  surface;
- does a prompt/harness change alter outcomes on exposed regression cases.

These are useful engineering/research diagnostics when tied to a real change.

It cannot establish:

- blind latent-trap detection on exposed cases;
- general legal-research quality;
- superiority across unseen legal problems;
- that a newer model is globally better or worse;
- that an observed difference is caused by model weights when tools, system
  prompts, search behavior, decoding or source state also changed.

## Comparability requirements

Model name alone is not an adequate run identity.

At minimum a meaningful replay needs to preserve or explicitly record:

- exact case/input version;
- model provider and immutable model/snapshot identifier where available;
- system/developer/task instructions;
- reasoning/effort setting where exposed;
- tool/web-search availability and relevant tool policy;
- generation parameters where configurable;
- chat/prompt template;
- sampling/random seed where meaningful;
- execution date;
- source/legal cutoff being scored;
- scorer/rubric version;
- harness version.

This is consistent with established evaluation tooling. EleutherAI's
lm-evaluation-harness exposes model arguments, chat-template choice, generation
arguments, few-shot settings, seeds, output logging and task configuration as
part of evaluation setup, and explicitly versions tasks when breaking changes
occur:

- https://github.com/EleutherAI/lm-evaluation-harness
- https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/interface.md
- https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/new_task_guide.md

The relevant lesson for Needle is subtraction: honest longitudinal comparison
requires more run metadata than a simple "model/date/score" table. If Needle is
not prepared to preserve that boundary for a concrete question, it should not
publish the comparison.

## Source drift is a separate variable

A replay months later can differ because the legal/source environment changed,
not because the model changed.

For a historical regression case, the scoring target should remain the frozen
historical proposition unless the experiment explicitly asks a current-law
question. Live web access can otherwise introduce newer material that makes a
historically correct answer look wrong or vice versa.

This is especially important for Needle because several trap classes are
themselves about source state, temporal boundaries and tracker freshness.

Source freshness therefore belongs to #115, not inside a generic model-drift
metric.

## Manual sample replay versus automation

### Manual/event-triggered replay

A small fixed sample is useful when there is a real event such as:

- changing the model used for Needle experiments;
- changing web/tool availability;
- changing the evaluation harness;
- investigating a reported regression.

Benefits:

- question is known before spend;
- sample can be selected for the affected behavior;
- exact settings can be recorded;
- results can be interpreted case by case;
- no standing infrastructure is required.

This is the strongest boring baseline.

### Periodic automated replay

A schedule such as weekly/monthly model runs creates:

- recurring API/model cost;
- provider availability and deprecation maintenance;
- pressure to aggregate results into a score;
- repeated storage of outputs/configuration;
- false trend interpretation when execution settings drift;
- temptation to treat exposed-case scores as fresh capability evidence;
- a permanent workflow whose unique value is unproven.

Needle previously removed a self-perpetuating scheduled operational monitor
after it generated durable state without serving the active research horizon.
Reintroducing scheduled model runs would recreate the same class of operational
risk in a different form.

### Dashboard / leaderboard

A leaderboard is actively misaligned with current project identity.

The corpus was built to preserve failure mechanisms and evaluation discipline,
not rank models. Aggregation would also hide the most useful information:
*which consequential trap failed, under what exact boundary, and why?*

## Smallest useful experiment

Do not create a periodic experiment now.

When Needle next has a concrete model/runtime migration to assess, run one
event-triggered replay:

1. predeclare the migration question;
2. select a small, reasoned sample from the exposed corpus before running either
   configuration;
3. freeze the exact old/new execution settings;
4. score only the existing consequential pass/fail behavior;
5. preserve per-case outcomes, not a synthetic overall quality score;
6. stop after the migration question is answered.

The experiment earns a reusable replay harness only if manual execution itself
causes a concrete reproducibility or comparison failure.

No recurring cadence is implied.

## Stop rule

Stop longitudinal work when any of the following is true:

- there is no concrete model/harness migration question;
- settings cannot be pinned or reconstructed sufficiently for interpretation;
- source/legal drift dominates the comparison;
- the output would be only an aggregate score over exposed cases;
- repeated replays are not changing any engineering or research decision.

A chart becoming more populated is not project value.

## Adversary

The strongest attack is vanity telemetry: a recurring benchmark can produce
clean-looking time series while adding no new evidence about Needle's core
questions.

A second attack is causal overclaim. If a provider silently changes search,
tooling, prompting or model routing, a changed answer is not automatically
"model drift."

A third attack is contamination. Because all current cases are exposed, improving
on them over time may reflect direct or indirect exposure rather than generalised
capability. Repetition does not repair that limitation.

A fourth attack is operational creep. Scheduled replays, storage, scoring and a
dashboard would become a new product/operations surface before any user or
research decision requires it.

## Decision

**REVISE**

Reject the original *periodic model-drift feature* framing.

Retain only **event-triggered, question-led regression replay** as a research
technique. It requires no standing scheduler, dashboard, leaderboard, new
schema, model integration or implementation horizon.

If a future concrete model/harness migration makes manual replay materially
error-prone, that failure may justify a bounded harness experiment. Until then,
the current corpus + evaluation protocol already contains the necessary
scientific rule.

No scheduled model runs or product feature are authorised by this discovery.

# DISC-06 — benchmark interoperability discovery

Issue: #116  
Parent: #104  
Date: 2026-09-24

## Question

Would exporting/importing Needle cases to adjacent legal-evaluation formats add
real research value, or would it merely turn Needle into another generic
benchmark?

Alternative explanation: Needle's distinctive information is not a generic
input/target pair. Its value lies in failure mechanism, evidence role, exposure
state, evaluation construct and provenance. Generic interoperability may either
discard those semantics or recreate them as custom extensions while adding a new
maintenance surface.

## Current Needle boundary

The corpus currently contains two materially different kinds of artifact:

- **DERIVATION** cases: 17 public cases that preserve a discovered legal-
  information failure mechanism. They are regression/explanation material, not
  necessarily executable benchmark prompts.
- **EVALUATION** cases: 10 revealed cases whose exact prompts/results/answer keys
  are owned by referenced evaluation artifacts. Six tested
  SURFACED_TRAP_ADJUDICATION and four tested LATENT_TRAP_DETECTION.

The public corpus index intentionally does not inline prompt/answer-key truth.
It records:

- stable case identity;
- trap classes;
- domain/jurisdiction;
- DERIVATION versus EVALUATION provenance;
- exposure/reuse state;
- evaluation mode for evaluated cases;
- decisive trap;
- evidence-owner references.

Any interoperability design must preserve the fact that these fields have
scientific meaning rather than being optional metadata decoration.

## Adjacent formats

### BIG-bench

BIG-bench accepted repository-native tasks submitted by pull request. JSON tasks
are fundamentally evaluation tasks built around input/target examples, metrics
and task metadata.

Reference:
https://github.com/google/BIG-bench/blob/main/docs/doc.md

Conceptual compatibility:

- Needle EVALUATION prompt → task input;
- frozen expected conclusion/rubric → target/scoring logic;
- exposed case → public regression example.

Mismatch:

- DERIVATION cases are not automatically tasks;
- Needle's consequential pass/fail logic is often richer than exact target
  matching;
- provenance role, exposure state and evaluation mode have no native equivalent;
- web/source access and temporal/legal cutoff are part of the scientific
  boundary, not merely task text.

### LegalBench

LegalBench is a repository-curated collection of legal-reasoning tasks with
task-specific datasets/evaluation logic.

Reference:
https://github.com/HazyResearch/legalbench

Conceptual compatibility:

- both preserve legal evaluation material in repository-owned task/data files;
- both benefit from explicit task identity and review.

Mismatch:

- a LegalBench task measures a legal-reasoning task category; a Needle case
  preserves a particular adversarial failure mechanism and its evidence history;
- importing a LegalBench task would not make it a Needle case without fresh
  evidence that it satisfies Needle's admission/contamination rules.

### DELTA

DELTA stores practitioner-led Dutch legal tasks in repository folders and a
machine-readable task set, with task-level legal-research cutoffs and explicit
assessment criteria.

Reference:
https://github.com/legalbenchmarks/delta

DELTA is closer to Needle on temporal/legal framing because `law_as_of` and
criteria are first-class. It is still different in purpose: DELTA evaluates
professional legal-work quality across criteria; Needle preserves adversarial
failure hypotheses, source/evidence boundaries and experiment provenance.

### lm-evaluation-harness

EleutherAI's harness provides a general execution layer with task
configuration, model arguments, templates, generation settings, seeds and
logged outputs.

Reference:
https://github.com/EleutherAI/lm-evaluation-harness

This is relevant as a possible *execution target*, not as a replacement Needle
schema.

## Export mapping

A lossless generic export of all 27 cases is not available without changing
their meaning.

### DERIVATION cases

Do not export these as scored benchmark tasks merely because they are in the
corpus.

A derivation case may lack:

- a frozen investigator prompt;
- a frozen answer key;
- a scoring rule;
- an execution boundary.

Inventing those during export would convert discovery evidence into a new
evaluation without pre-registration.

Safe generic representation: descriptive metadata only.

That adds little beyond the existing corpus JSON.

### EVALUATION cases

The 10 revealed EVALUATION cases are the only plausible execution-export
population.

A derived export could in principle resolve the referenced frozen artifacts and
produce:

- exact public prompt;
- evaluation mode;
- frozen expected decisive behavior;
- exposure = public/regression-only;
- temporal/legal cutoff;
- source/tool boundary;
- scoring instructions.

But such an export must remain **derived and disposable**. The canonical truth
stays in Needle's corpus + referenced evaluation artifacts.

If the target format cannot preserve the evaluation mode, temporal/source
boundary and scoring semantics, do not call the result equivalent.

## Import mapping

Generic benchmark import is more dangerous.

A task from LegalBench, DELTA, BIG-bench or another corpus does **not**
automatically qualify as a Needle case.

Needle admission additionally requires evidence for:

- a concrete consequential failure mechanism;
- correct evidence ownership;
- DERIVATION versus EVALUATION role;
- exposure/contamination state;
- independently justified trap class;
- temporal/source boundary where material.

Therefore an import adapter cannot safely "convert" external benchmark rows into
Needle cases.

At most, an external benchmark can be a **candidate discovery source**. A case
would still need ordinary Needle research/admission.

## One concrete interoperability use case

Issue #114 retained one narrow future use for regression execution:

> event-triggered replay when Needle actually changes a model/runtime/harness and
> needs to know whether known exposed adversaries still behave as expected.

If manual replay of a small selected EVALUATION sample becomes materially
error-prone, exporting those selected public prompts into an established
evaluation harness could reduce execution plumbing.

That is the only current concrete interoperability use case.

It is:

- export-only;
- evaluation-case-only;
- event-triggered;
- derived/disposable;
- not a leaderboard;
- not a corpus migration.

No evidence currently shows that manual replay has failed, so the use case does
not yet justify an adapter experiment.

## Strong reason to reject generic interoperability

Generic import/export creates a false equivalence between:

- corpus cases;
- benchmark tasks;
- legal research datasets;
- model-scoring examples.

Needle deliberately separates those categories.

A generic adapter would face two bad choices:

1. **lossy mapping** — drop Needle provenance/exposure/evaluation semantics and
   make exported data look more authoritative/comparable than it is; or
2. **Needle-specific extensions** — embed so much custom metadata that the
   supposed standard format becomes another projection of Needle's own schema.

Neither creates demonstrated research value today.

## Complexity / ownership attack

A maintained adapter introduces:

- target-format version drift;
- compatibility tests;
- mapping policy;
- duplicate fixtures/exports;
- pressure to support multiple benchmark ecosystems;
- temptation to compare aggregate scores across incompatible constructs.

This is exactly the kind of integration surface the project has repeatedly
removed when it did not outperform the simpler baseline.

Interoperability itself is not a user outcome.

## Smallest experiment

**No adapter experiment now.**

Reopen only when one of these becomes concrete:

1. an external evaluator/research collaborator asks to consume Needle's revealed
   EVALUATION cases in a named format;
2. an event-triggered replay under #114 demonstrates that manual execution is the
   bottleneck;
3. a publication/reproducibility requirement names a target harness/format and a
   lossless-enough mapping can be specified.

Then start with one-way export of a small fixed EVALUATION subset.

Do not build import until an actual external-case admission workflow demonstrates
that ordinary Needle research review is insufficient.

## Decision

**PARK**

Benchmark interoperability is conceptually possible but has no demonstrated
current research/user value that justifies implementation.

Park generic import/export and adapter work.

Preserve only this future boundary:

> a disposable one-way export of selected revealed EVALUATION cases may be
> reconsidered for a concrete event-triggered regression or external
> reproducibility requirement.

Do not export DERIVATION cases as synthetic benchmark tasks. Do not import
external benchmark rows as Needle cases. Do not add a common ontology, adapter
framework, leaderboard, dependency or second corpus representation.

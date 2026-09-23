# Needle latent-trap detection gate v0.2

**Issue:** #97  
**Status:** PRE-REGISTERED BEFORE V0.2 EXECUTION  
**Evaluation mode:** LATENT_TRAP_DETECTION  
**Pre-registration date:** 2026-09-23  
**Supersedes:** v0.1, retired unexecuted after pre-run adversarial audit

## Question

Does the bounded Needle Method checklist improve latent-trap detection over a
strong source-grounded baseline on realistic legal-research tasks, when the
hidden legal-information problem is not named in the user request?

## Scope of claim

This gate can support only a bounded claim about the tested workflow:

- GPT-5.6 Sol;
- high reasoning;
- web search enabled;
- stateless independent requests;
- official/primary-source preference;
- four tested adversarial classes.

It cannot establish general superiority for lawyers, humans, other models or
all legal-research tasks.

## Arms

### R — strong boring baseline

Instruction:

- answer carefully;
- use web search;
- prefer official/primary sources;
- state material uncertainty;
- do not overclaim.

### M — Needle Method checklist

Same execution boundary plus an internal pre-conclusion checklist covering:

- source origin vs legal authority/recognition;
- exact target/scope;
- temporal perspective/boundary;
- source-state-as-of vs current/ex-post state;
- language/expression scope where relevant;
- uncertainty/unresolved points;
- forbidden inference checks.

**Important:** R and M must return the **same visible output structure**.

The Method checklist is a reasoning treatment, not a different reporting
template.

## Common output schema

Both arms return only:

- CONCLUSION
- REASONING
- DECISIVE SOURCES
- UNCERTAINTY / LIMITS

No Method-specific headings.

## Stage 1 — 12 calls

Six cases, each run once in R and once in M.

### Adversarial cases

1. EU–Chile parallel instrument lifecycle
   - class: `PARALLEL_INSTRUMENT_LIFECYCLE`
2. Haringvliet / Leenheerenpolder
   - class: `JUDICIAL_VALIDITY_TEXT_DIVERGENCE`
3. EN 50434:2014 garden shredder at 320 r/min
   - class: `DYNAMIC_REFERENCE_STATUS`
4. Temu DSA status as of 15 June 2024
   - class: `STATUS_APPLICATION_SEPARATION`

### Near-miss negative controls

5. EN 50434:2014 garden shredder at 250 r/min
   - same source family as case 3;
   - the >300 r/min restriction must not be over-applied.
6. Temu DSA status as of 15 October 2024
   - same lifecycle family as case 4;
   - the later VLOP obligations must not be treated as still pending.

The controls are deliberately similar to adversarial cases rather than trivial
article lookups.

## Latency rule

An adversarial question fails pre-execution cue review if it:

- names the trap class;
- tells the investigator which distinction to make;
- mentions the corrective source/event solely to reveal the trap;
- labels the supplied fact as suspicious;
- asks for the answer-key distinction explicitly.

Task-native facts are permitted.

The question may be difficult. Difficulty is not an admission criterion.

## Stage-1 scoring

### Adversarial case pass

An arm passes only if it:

1. reaches a materially correct conclusion;
2. detects and acts on the hidden distinction sufficiently to avoid the
   pre-sealed consequential error;
3. does not replace missing evidence with unsupported certainty.

Generic caution without identifying the operative distinction is not detection.

### Near-miss control pass

An arm passes if it reaches the supportable conclusion without:

- inventing a material hidden obstacle;
- over-applying the adversarial rule;
- refusing a conclusion that official evidence supports;
- manufacturing a materially wrong qualification.

Extra structure or harmless caveats alone are not failure.

## Blind grading

After Stage 1:

1. verify all prompt hashes and response IDs;
2. do not inspect arm-level aggregate results first;
3. create per-case blind output pairs with arm/run metadata removed;
4. assign opaque labels A/B in a mapping withheld from the grader;
5. grade each output against the frozen case rubric;
6. lock grades;
7. reveal the arm mapping and compute pair classes.

Because both arms use the same output headings, arm identity should not be
obvious from format alone.

If prose still makes an arm guessable, grading remains rubric-bound; do not use
style as evidence.

## Pair classes

Adversarial:

- R fail / M pass — apparent Method rescue;
- R pass / M pass — parity;
- R fail / M fail — unresolved by either workflow;
- R pass / M fail — apparent Method regression.

Control:

- R pass / M pass — calibrated parity;
- R pass / M fail — apparent Method false-positive/regression;
- R fail / M pass — baseline control failure; report, do not reinterpret as an
  adversarial Method rescue;
- R fail / M fail — control itself was harder than expected.

## Adaptive confirmation of discordance

A single discordant pair **does not count** as a project-level rescue or
regression.

For every Stage-1 discordant case:

- execute **two additional independent R/M pairs** using the exact same frozen
  prompt and arm instructions;
- this yields three R responses and three M responses for that case;
- score the new outputs blind under the same frozen rubric.

Confirmed arm outcome = majority of its three responses.

Confirmed pair class is computed from those arm majorities.

Parity cases receive no replication.

This spends additional money only when there is an apparent signal worth
checking.

## Stage-1 stop rule

If all four adversarial cases are R-pass/M-pass and both controls are calibrated
parity:

> stop after 12 calls.

H-15 is not demonstrated in this gate.

Do not run weaker reserve cases merely because the result is null.

## Project-level interpretation

Using **confirmed** outcomes only:

- 0 confirmed Method rescues:
  - substantive latent-detection value not demonstrated;
  - Method stays optional, not part of default identity.
- 1 confirmed Method rescue:
  - signal only;
  - preserve it, but require a future fresh independent replication before
    changing project identity.
- >=2 confirmed Method rescues across >=2 distinct adversarial classes, with no
  confirmed M-only regression:
  - stronger evidence for a bounded checklist-assisted latent-detection role;
  - Method may earn a documented optional detection role for this workflow;
  - this still does not resurrect Core or Full Needle.
- any confirmed M-only regression:
  - direct negative evidence;
  - cannot be offset by verbosity, source count or packaging.
- matched-control false positives:
  - count as regressions if confirmed.

No synthetic quality score.

## Efficiency rule

Stage 1 is 12 calls rather than v0.1's 16.

Additional calls occur only for discordant cases and therefore only when the
result is scientifically interesting enough to justify confirmation cost.

Token/web-search usage is recorded descriptively as operational overhead but is
not retroactively turned into a winner metric.

## No hidden reserve manipulation

The two v0.1 cases removed for cue risk are **not** automatic Stage-2 cases.

If v0.2 produces a signal requiring broader replication, that is a separate
future gate with fresh pre-registered cases.

## Mutation rule

Before execution, exact questions, case rubrics, arm instructions and run order
will be sealed by SHA-256 commitments.

After sealing:

- no scientific input may change;
- any change requires v0.3 or a new gate;
- transport-only repair is allowed only if no model response was produced and
  exact prompt hashes remain unchanged.

## Acceptance before paid execution

1. v0.1 explicitly marked retired/unexecuted;
2. this v0.2 pre-registration committed;
3. exact six questions written and cue-audited;
4. exact answer-key rubrics independently checked against official sources;
5. R/M output schema identical;
6. exact prompt/key hashes committed;
7. 12-call Stage-1 runner verified with zero API calls;
8. discordance-replication logic documented but not executed unless triggered.

No assumption that Method should survive.

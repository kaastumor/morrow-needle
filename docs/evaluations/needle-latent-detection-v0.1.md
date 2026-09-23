# Needle latent-trap detection gate v0.1

**Issue:** #97  
**Status:** PRE-REGISTERED BEFORE CASE SELECTION  
**Evaluation mode:** LATENT_TRAP_DETECTION  
**Pre-registration date:** 2026-09-23

# Value gate question

Does Needle Method improve **LATENT_TRAP_DETECTION** on realistic legal-research
tasks where the user does not identify the hidden source/time/scope/authority
problem?

This is the distinct construct left unresolved after Issue #95 showed that all
six Issue #88 questions were SURFACED_TRAP_ADJUDICATION cases.

This gate is justified by the original project-value question — whether a
Needle-specific workflow prevents mistakes a strong ordinary workflow would
actually make — not merely by the existence of a measurement gap.

No case may be selected or run before this pre-registration is frozen.

## Tested claim

Needle Method causes a capable source-grounded investigator to notice and safely
handle consequential legal-information traps that the same investigator,
without the Method checklist, sometimes misses when the trap is not named in the
task.

## Arms

### R — strong boring baseline

- same capable model family/version as M;
- same reasoning effort;
- same web/source access;
- fresh stateless request;
- instruction to answer carefully, use reliable primary/official evidence where
  available, and state material uncertainty;
- no Needle vocabulary, checklist, corpus access or failure-class hint.

### M — Needle Method

Same execution boundary as R plus the bounded Method dossier requirements:

- source origin vs authority/recognition;
- exact target and scope;
- temporal perspective and operative boundary;
- source-state-as-of vs ex-post/current representation;
- language/expression scope where relevant;
- uncertainty;
- forbidden inferences;
- unresolved points.

No Core persistence.

## Evaluation mode

**LATENT_TRAP_DETECTION**

The investigator prompt must resemble a realistic ordinary task and must not:

- name the failure class;
- tell the investigator which distinction to make;
- say that the source/date/language/status is suspicious;
- ask the investigator to “watch out for” the expected trap;
- contain evaluator-authored hints whose only purpose is to reveal the answer
  key.

Facts naturally present in the real task are allowed even when they are part of
the trap.

If a proposed prompt strongly cues the decisive distinction, reject or reclassify
it before sealing. Do not silently weaken the construct.

## Case selection — before any arm result

Target: **6 latent adversarial cases + 2 negative controls**.

### Six adversarial cases

Each must:

- be fresh: not already public in the Needle corpus and not a trivial rename of
  an exposed case;
- be selected because it independently instantiates a pre-existing or
  independently discovered failure mechanism, never because R has failed it;
- have a concrete consequential wrong answer;
- be resolvable from public evidence;
- have a hidden distinction that a competent real researcher could plausibly
  overlook without being incompetent;
- support an answer key precise enough to judge detection/correctness without
  style scoring.

Prefer breadth across source systems, jurisdictions and trap families.

No more than two cases from the same trap class.

### Two negative controls

Negative controls are ordinary legal-research tasks where source review supports
the straightforward answer and the evaluator knows of no material hidden trap.

They test whether Method:

- invents a complication;
- over-abstains;
- manufactures uncertainty;
- needlessly refuses a supportable conclusion.

A Method answer is not penalized merely for being more structured. Only a
materially wrong, misleading or unjustifiably noncommittal result counts.

## Candidate-discovery firewall

During case discovery:

- do not run R or M on a candidate;
- do not ask another model whether “baseline would fail”;
- do not retain a case because it looks likely to make Needle win;
- record rejected candidates and the reason;
- freeze the final eight prompts and answer keys before execution.

Case compiler knowledge is allowed; investigator knowledge is not.

## Sealing

Before execution commit only cryptographic commitments to:

- exact eight investigator questions;
- exact answer keys;
- case order;
- R instruction;
- M instruction;
- model/version;
- reasoning effort;
- tool/web access;
- storage/stateless settings;
- judging rule.

Plaintext questions/keys remain outside investigator context until all intended
runs complete.

## Primary per-case outcomes

For each arm record:

- conclusion correct / incorrect;
- latent trap detected / missed;
- consequential false claim;
- unsupported certainty;
- safe abstention when evidence genuinely does not support a conclusion;
- source-state/current-state confusion;
- temporal-boundary loss;
- language/scope projection;
- source-origin/authority confusion;
- identity/status conflation;
- material false-positive complication on negative controls.

Trap detection means the answer identifies and acts on the decisive hidden
distinction sufficiently to avoid the pre-sealed consequential error. Merely
mentioning generic caution does not count.

## Pair interpretation

Adversarial cases:

- **R fail / M pass** — Method rescue for latent detection;
- **R pass / M pass** — parity;
- **R fail / M fail** — failure class remains unsolved;
- **R pass / M fail** — Method regression.

Negative controls:

- **R pass / M pass** — desired;
- **R pass / M fail** — Method false-positive/regression;
- any R failure means the control was not as boring as intended and must be
  reported, not silently replaced post-run.

## Project-level decision rule

No synthetic quality score.

- **0 Method rescues:** substantive latent-detection value not demonstrated.
- **1 Method rescue:** signal only; do not promote Method without independent
  replication.
- **>=2 Method rescues across >=2 distinct trap classes, with no consequential
  M-only regression:** stronger evidence that Method has a real detection role.
- **Any consequential R-pass/M-fail regression:** counts directly against Method
  and must remain visible; do not offset it with verbosity/format advantages.
- **Negative-control false positives:** count as Method regressions if they
  materially distort the answer.

Do not reinterpret these thresholds after results.

## Stop rules

- If all eight pairs are straightforward parity, stop. Do not append harder
  cases.
- If both arms fail a mechanism, record it as unsolved rather than expanding
  architecture during the gate.
- Core does not enter this experiment.
- Do not reuse exposed #88/#91/#93 cases with rewritten prompts.
- Do not add a new Method instruction after seeing an R miss.
- No product/ontology implementation is authorised by the result.

## Acceptance before execution

1. this issue/pre-registration is frozen;
2. fresh candidate discovery is documented;
3. six adversaries + two negative controls are selected without arm testing;
4. latent-prompt cue audit passes before sealing;
5. exact prompt/key commitments are committed;
6. execution boundary is documented.

Only then may R/M runs begin.

No assumption that Method should survive.

---

## Freeze note

This file is the repository copy of the Issue #97 pre-registration as it existed
before fresh candidate discovery.

Do not edit the scientific rules above after candidate discovery or arm
execution begins. If the construct or decision rule must change, create a new
version/experiment rather than silently mutating this one.

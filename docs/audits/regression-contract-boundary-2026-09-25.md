# Issue #311 — regression corpus versus reference catalog

Date: 2026-09-25  
Disposition: **KEEP_REGRESSION_REFERENCE_LABEL**

## Question

Is Needle's current **adversarial legal-research regression/reference corpus** identity
operationally accurate for an external consumer, or does the released Reference Pack
primarily preserve reference material while executable regression contracts exist only
for a subset/deeper repository owners?

## Result

Keep the combined **regression/reference corpus** label, but define its boundary more
precisely:

> Needle preserves exposed cases as **regression/reference material**. It is not a
> uniform turnkey executable regression suite.

That distinction is already broadly compatible with the project's historical meaning of
"regression", and it avoids manufacturing prompts or answer keys for cases that were
never scientifically designed as executable evaluations.

## Pack-level contract

The frozen 81-case Reference Pack records:

- case ID;
- title/domain/jurisdiction;
- trap-class membership;
- provenance role;
- exposure/reuse state;
- one-sentence decisive trap;
- evidence refs;
- evaluation mode/result where applicable.

It does **not** have a standardized field for:

- executable task/question;
- expected answer/conclusion;
- pass/fail requirements;
- fail-if conditions;
- source-access/execution conditions.

Therefore:

> **0/81 pack case records are self-contained executable regression tests by schema.**

This is not a defect in pack reproducibility. The pack was intentionally designed as a
derived reference/navigation layer rather than a task/answer-key bundle.

## Four-slice audit

### 1. DERIVATION + path-backed owner

Representative case:

`reg794-consolidation-backprojection`

The pack gives the decisive trap and points to Issue #61 plus a Git-backed fixture.

The fixture preserves strong regression material:

- exact target identifiers;
- observed language-expression state;
- later correction sources;
- required query distinction between `EX_POST_LEGAL_EFFECT` and
  `OFFICIAL_SOURCE_STATE_AS_OF`;
- explicit forbidden inferences.

Issue #61 also preserves the research question and acceptance criteria.

This is enough to construct or maintain targeted implementation regressions inside the
repository. It is **not** a frozen external end-user task + answer key + scoring rule.

Classification:

> **REGRESSION FIXTURE / MATERIAL — not a turnkey executable case.**

### 2. DERIVATION + issue-only owner

Representative case:

`brussels-i-choice-of-forum`

The pack gives:

- the failure mechanism;
- class membership;
- `issue:276`.

Issue #276 preserves the discovery question, legal boundaries, required research and
decision alternatives. It does not define a standardized end-user prompt, frozen expected
answer object or pass/fail oracle for rerunning the case.

Under the #306 integrity rule, the issue content is also mutable navigation rather than
commit-pinned frozen evidence bytes.

Classification:

> **REFERENCE / REGRESSION MATERIAL — weakest executable form.**

### 3. surfaced EVALUATION

Representative case:

`adv-chatgpt-vlose-applicability`

Issue #88's Git-backed fixtures preserve:

- exact R/M prompts;
- exact answer key;
- correct conclusion;
- consequential failure;
- decisive evidence;
- grading notes;
- execution result.

This is a genuine exposed executable regression/evaluation contract. It can be rerun as
a regression, but because it is exposed it cannot become fresh blind validation.

Classification:

> **EXECUTABLE EXPOSED REGRESSION CASE.**

### 4. latent EVALUATION

Representative case:

`ld2-chile-lifecycle`

Issue #97's Git-backed v0.3 artifacts preserve:

- exact R/M prompts;
- prompt hashes;
- exact answer key;
- expected conclusion;
- `pass_requires`;
- `fail_if`;
- source list;
- grading rule;
- frozen result hashes / arm mapping.

This is also a genuine exposed executable regression/evaluation contract.

One navigation weakness exists in Reference Pack v0.1: the four #97 case records point to
the stage-1 result file and result audit, but do not directly list the existing
`issue97-manual-prompts-v0.3.json` and `issue97-manual-answer-key-v0.3.json` files.
The files nevertheless exist in the frozen repository state. Changing pack v0.1 solely
to improve that link would violate the frozen-release boundary for little substantive
gain; future pack versions may improve navigation if a real use requires it.

Classification:

> **EXECUTABLE EXPOSED REGRESSION CASE at repository level; pack navigation is indirect.**

## Corpus-wide structure

The frozen corpus contains:

- **71 DERIVATION** cases;
- **10 EVALUATION** cases.

The 10 EVALUATION cases are the only cases with a common historical expectation that exact
sealed/revealed execution inputs and grading material exist.

The 71 DERIVATION cases were admitted because they preserve falsifiable consequential
failure mechanisms. Their evidence owners vary:

- some include structured fixtures with expected distinctions or forbidden inferences;
- some include audit/result documents;
- many are issue-backed research records.

There is no uniform derivation-case prompt/oracle contract.

Creating one now would require **post-hoc task synthesis**. That would be useful only as
a new engineering convenience layer and must not be presented as the original scientific
input, answer key or evaluation construct.

## Terminology boundary

Use these terms deliberately:

### Reference catalog

A navigable description of accepted cases/classes/provenance/exposure.

Needle Reference Pack v0.1 is fully this.

### Regression material / fixture

An exposed known failure case, source-backed distinction or structured artifact that can
be used to prevent recurrence of an already understood error.

All 81 cases qualify at this broad project level because each preserves a falsifiable
decisive trap and evidence owner.

### Executable regression case

A case with a concrete runnable task plus expected outcome/pass-fail rule sufficient to
repeat the check without inventing the scientific contract.

The ten revealed EVALUATION cases clearly qualify at repository level. Individual
DERIVATION fixtures may support implementation-specific regressions, but there is no
uniform 71-case executable suite.

### Benchmark / evaluation suite

A deliberately selected set with a defined population/claim, execution boundary,
comparator and scoring/decision rule.

The frozen 81-case corpus is **not** such a representative suite. Historical #88/#97 are
bounded evaluation suites for their exact claims; their exposed cases are now regression
only.

## Why not add a minimal 81-case regression contract now?

The superficially attractive repair would add a generated question and answer criterion
for every derivation case.

Reject that for the current state:

1. it would synthesize tasks after the discovery result is known;
2. the one-sentence decisive trap is not an answer key;
3. different historical fixtures own different forms of expected state;
4. an automatically normalized oracle would flatten important source/time/scope nuance;
5. it could make the polished pack look like a scientifically designed 81-case benchmark;
6. no concrete external consumer has demonstrated a need for turnkey 81-case execution.

If a future real use needs executable regressions, the correct path is to define that new
derived engineering contract explicitly and keep its post-hoc status visible.

## Disposition

**KEEP_REGRESSION_REFERENCE_LABEL**

Reason:

- "reference corpus" is unambiguously accurate;
- "regression corpus" remains accurate in the project's established broad sense of exposed
  known failure material used to prevent recurrence;
- the repository contains genuine executable regression contracts for all 10 EVALUATION
  cases and structured regression fixtures for some derivation cases;
- the current label uses both terms rather than claiming "81-case executable benchmark";
- narrowing to "reference corpus" would throw away a real supported use;
- manufacturing a uniform execution layer is not currently earned.

## Durable wording

> **Regression/reference corpus** means a corpus of exposed, source-backed failure cases
> suitable for known-case regression and reference use. It does **not** mean that every
> case ships as a standardized runnable prompt/oracle, nor that the corpus is a
> representative benchmark.

When executable status matters, consumers must inspect the case's evidence owner. Exact
revealed evaluation contracts remain historical artifacts and never regain fresh-blind
status.

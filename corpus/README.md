# Morrow // Needle — Adversarial Corpus

Status: **CANONICAL CORPUS ENTRY POINT**

This directory is the canonical public **known-failure reference corpus** for the
project's current minimal form. It also points to case-specific exposed regression fixtures
where the evidence owner preserves an executable check.

It does **not** replace the underlying legal fixtures, audits or issues. The index owns
current corpus membership/classification and records evaluation metadata pointing to
those existing evidence owners. Historical reference checkpoints are recorded separately;
do not copy their counts back into this README as live state.

Canonical index:

`corpus/index-v0.1.json`

Canonical evaluation protocol:

`docs/evaluations/adversarial-corpus-protocol-v0.1.md`

## What a corpus case is

A corpus case is a concrete legal-information situation capable of producing a
consequentially wrong conclusion through a specific evidence/reasoning trap.

A case is not admitted because it is complicated, surprising or legally
interesting. It must preserve a falsifiable failure mechanism.

Each public index entry records only:

- stable case ID;
- short title/domain/jurisdiction;
- one or more trap classes;
- provenance issue;
- whether it **derived** a hypothesis or was used to **evaluate** one;
- exposure/reuse status;
- evaluation mode for revealed evaluation cases;
- the decisive trap in one sentence;
- references to existing durable evidence.

Legal facts remain owned by the referenced fixture/audit/source chain.

## Primary reference use

The corpus is primarily a **failure-analysis / evaluation-design / debugging reference**.

Use a case to:
- reconstruct the consequential legal-information distinction;
- inspect the evidence and historical/source-state owner;
- understand the accepted boundary of the failure family;
- preserve derivation/evaluation/exposure status;
- derive or rerun a regression only when a concrete executable contract exists.

Do not assume corpus consultation improves an ordinary legal-research answer merely because
a case is analogous. Issue #327's first mechanically selected real-use test returned
`BASELINE_SUFFICIENT`.

The compact Reference Pack is a navigation surface. Detailed boundary, negative-control and
source-state evidence may still live in the referenced repository owners.

## Reference, fixture and regression status

**Reference status is corpus-wide. Regression status is case/fixture-specific.**

- **Known-failure reference:** every accepted case preserves a stable case identity,
  consequential failure mechanism, provenance/exposure state and evidence owner.
- **Regression source / debugging fixture:** any exposed known failure can inform future
  regression engineering or help inspect recurrence of an understood error.
- **Executable regression case:** use this term only when the evidence owner preserves a
  concrete runnable task/input plus expected behavior and an evaluator/pass condition.
  The ten revealed evaluation cases clearly satisfy this at repository level; derivation
  cases do not share one uniform executable contract.
- **Benchmark/evaluation:** the full public corpus is not a representative benchmark and
  must not be treated as one merely because cases are machine-readable.

External legal benchmark and LLM-evaluation practice strengthens this boundary: known
production failures are normal regression inputs, but they become repeatable regression
tests by pairing the failure with an executable input and expected/evaluator contract.

Do not synthesize post-hoc prompts/answer keys from `decisive_trap` and present them as
historical scientific inputs. See
`docs/audits/regression-contract-boundary-2026-09-25.md` and
`docs/reviews/issue331-external-regression-role-result-2026-09-26.md`.

## Derived metamorphic regressions

A small post-hoc regression layer records evidence-backed cases where one legally material
state variable changes while the controlled scenario remains sufficiently fixed:

`fixtures/regression/frozen-reference-metamorphic-v0.1.json`

These relations test known state-transition properties (for example adjacent temporal or
application boundaries). They add **zero** scientific cases and remain exposed
`REGRESSION_ONLY` material. Same-class analogy is not enough; each relation must already
be supported on both sides by an existing evidence owner.

See `docs/audits/metamorphic-regression-derivation-2026-09-25.md`.

## The contamination rule

**Discovery evidence and validation evidence are different things.**

If a case caused us to discover or formulate a failure mechanism, it is
`DERIVATION` evidence for that mechanism. It must not later be presented as a
fresh blind validation of the same claim.

If a case was sealed and used in an evaluation, revealing it makes it exposed.
It can remain excellent regression material, but it is not fresh blind evidence
again merely because a new session, model version or year arrives.

Every case in the current v0.1 public reference corpus is therefore:

- public/exposed;
- `blind_reuse=false`;
- `future_use=REGRESSION_ONLY`.

Fresh evaluation requires a fresh case selected and sealed before arm results
exist.

## Case lifecycle

1. **DISCOVERED** — a concrete source-backed adversary exists.
2. **ADMITTED** — trap is falsifiable, consequential and sufficiently supported.
3. **SEALED** — exact question/answer key and comparator protocol are fixed;
   Git stores commitments rather than hidden plaintext.
4. **EXECUTED** — independent runs occur under the frozen boundary.
5. **REVEALED** — commitments are verified and exact hidden artifacts are made
   auditable.
6. **REGRESSION_ONLY** — case remains useful, but no longer counts as fresh
   blind validation.

A derivation case normally enters the public corpus already exposed and thus
goes directly to regression-only use.


## Evaluation modes

Evaluation provenance and evaluation construct are separate.

Every revealed `EVALUATION` case must record one of:

- `SURFACED_TRAP_ADJUDICATION` — the question identifies or strongly cues the
  dangerous distinction; the run tests whether it is resolved correctly;
- `LATENT_TRAP_DETECTION` — the realistic task does not reveal the hidden
  failure mechanism; the run tests whether the investigator notices it before
  giving a consequential answer.

All six Issue #88 evaluation cases are
`SURFACED_TRAP_ADJUDICATION`. They must not be cited as evidence that the
baseline or Method would independently detect the same traps when latent.

See `docs/audits/issue88-construct-validity-2026-09-23.md`.

## Admission guardrails

Prefer cases where:

- the decisive conclusion is objectively checkable against primary/official or
  otherwise appropriately recognised evidence;
- the trap reflects a real legal-information failure mode rather than puzzle
  wording;
- the wrong answer would be consequential, not merely less elegant;
- scope, time, language and source roles can be stated precisely;
- the case is independent of the hypothesis it is meant to validate.

Reject or defer cases that:

- are selected because a baseline is already known to fail them;
- require proprietary hidden facts for the decisive answer;
- depend on subjective answer-quality scoring without a pre-registered rubric;
- merely reward verbosity, source count or a preferred formatting style;
- duplicate an already exposed case and call that “fresh” validation.

## Reference-release boundary

`status=CANONICAL_REFERENCE` means the public index is coherent enough to serve as a
versioned regression/reference checkpoint. It does **not** mean:

- the taxonomy is complete or final;
- every legal mechanism is covered;
- the corpus has demonstrated a model/workflow advantage;
- exposed cases become fresh blind validation;
- historical product surfaces are reactivated.

Exact checkpoint evidence belongs in the owning release-review record; the index remains
the live corpus owner.

## Current limitations profile

The current frozen-state concentration, provenance and misuse-risk audit is:

`docs/audits/frozen-corpus-concentration-misuse-2026-09-25.md`

Use it when interpreting coverage. Class support counts describe curated regression
coverage, not prevalence, importance, representativeness or fresh validation.

## Validation

Run:

`python scripts/validate_adversarial_corpus.py`

The validator checks structural invariants and referenced repository paths. It
does not decide whether the legal answer is correct; that remains evidence work.

## Scope discipline

The corpus may point into the repository's older schemas and fixtures because
those files preserve valuable cases. Their existence does not reactivate the
architectures they were originally built to test.

Corpus growth does not by itself justify new ontology, infrastructure or product
surface.

# Morrow // Needle — Adversarial Corpus

Status: **CANONICAL CORPUS ENTRY POINT**

This directory is the canonical public regression/reference corpus for the project's
current minimal form.

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

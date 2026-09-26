# Needle failure-analysis guide

Status: **Reference Pack v0.2 navigation/method surface**

This guide exposes the failure-analysis contract demonstrated by Issue #339 without creating a new legal truth store.

It is for:

- legal failure analysis;
- evaluation design;
- debugging and postmortem work;
- regression-fixture derivation where an executable contract is actually supported.

It is not a benchmark, current-law service, external-failure database or generic legal-research assistant.

## 1. Begin with the failure, not the taxonomy

Record the external/case identity and reconstruct the strongest ordinary source-linked postmortem first.

Then inspect Needle.

Use an existing class only when its **causal failure mechanism** fits.

If none fits, record:

> **NO_EXISTING_CLASS_MATCH**

That is a valid and sometimes important result. Never force a class merely because packaging looks cleaner with one.

## 2. Preserve scientific and reuse status

Keep these distinctions explicit:

- `DERIVATION` evidence can help formulate or explain a failure mechanism;
- `EVALUATION` evidence entered through a predeclared evaluation;
- public/revealed material is exposed;
- an already known external failure remains known-case analysis, not fresh validation;
- exposed material may support reference, debugging or regression work, but does not become blind again with time or a new model.

Follow `docs/evaluations/adversarial-corpus-protocol-v0.1.md` for evaluation semantics.

## 3. Failure-analysis packet checklist

For a known failure, preserve only what accepted owners actually support.

| Packet element | What to preserve | Truth-owner rule |
| --- | --- | --- |
| Identity | Stable external/case ID and originating observation | Exact external record or accepted case owner |
| Class disposition | Causal class match or `NO_EXISTING_CLASS_MATCH` | Canonical corpus for existing classes; accepted analysis owner for no-match result |
| Failure mechanism | The consequential legal-information distinction that failed | Accepted case/analysis result plus decisive evidence |
| Evidence owner | Authoritative primary/official or otherwise appropriate evidence chain | Exact evidence refs/result owner |
| Source-state guidance | Historical/current version/date distinctions when material | Exact legal/source evidence owner |
| Boundary / opposite-error control | What the corrective rule does **not** mean, where supported | Accepted class/issue/audit/result owner |
| Scientific/reuse status | Derivation/evaluation/exposure and permitted future use | Corpus/evaluation protocol or accepted analysis owner |
| Regression conversion | Whether the failure remains reference-only or has an explicit derived/executable check | Exact fixture/result owner |
| PASS/FAIL criteria | Concrete expected behavior and failure conditions | Only an executable fixture/answer key/result or accepted derived analysis |

**Omit rather than synthesize.**

A useful empty field is safer than a neat but invented legal boundary or oracle.

## 4. Historical and source-state discipline

A currently accessible source is not automatically the source state relevant to the failure.

Where time/version matters:

- preserve the target date;
- identify the authoritative source/version used;
- distinguish historical truth from current law;
- do not silently replace an old answer key or historical rule with today's text.

The Reference Pack points to evidence owners. It does not override them.

## 5. Boundary discipline

A one-direction correction can create a new error.

Where accepted evidence supports it, preserve an opposite-error or exclusion boundary.

Example shape:

- wrong state A;
- wrong overcorrection B;
- supported boundary C.

Do not infer this structure merely because a trap class sounds similar.

## 6. Regression conversion

A known failure can become regression material without becoming fresh validation.

Only create an executable regression contract when an owner supports:

- a runnable input/task;
- expected behavior or outcome;
- an evaluator/pass condition.

If the contract is derived after the original observation, label that derivation explicitly. Do not rewrite history by presenting post-hoc engineering as the original scientific design.

## 7. Worked navigation — Issue #339

The first accepted use observation behind this guide is:

- GitHub Issue #339;
- durable owner: `docs/uses/issue339-external-failure-packet-use-2026-09-26.md`;
- disposition: `NEEDLE_VALUE_PACK_GAP`.

The important navigation lesson is structural:

1. the external failure was mechanically selected before Needle inspection;
2. a strong ordinary postmortem was frozen first;
3. the existing classes were inspected and **no class matched honestly**;
4. the accepted result then preserved scientific/reuse status, a supported boundary, source-state guidance and a derived regression contract;
5. the external failure was **not admitted into the canonical corpus**;
6. the result demonstrated repository-level packet value and a v0.1 navigation gap.

Open the durable #339 owner for its actual legal and regression details. This guide intentionally does not duplicate those facts.

## 8. What v0.2 owns

v0.2 owns:

- navigation;
- safe-use instructions;
- the method checklist;
- deterministic views over the frozen corpus;
- links to exact accepted owners.

v0.2 does **not** own:

- the underlying legal facts;
- new class judgments about unowned external failures;
- generalized boundary truth;
- new regression answer keys;
- external-failure membership.

Those remain with the exact corpus, issue, audit, fixture or accepted result that established them.

## 9. Structured external-failure data is deliberately deferred

This release does not contain an `analysis-packets.jsonl` or external-failure index.

Issue #343 found that one positive external use is enough to improve navigation, but not enough to create a generalized structured packet schema.

An orthogonal use should first test whether the same packet elements recur across a materially different failure.

## 10. Rights and citation

The repository is public but currently has no project license.

Treat this pack as **publicly inspectable/reference material**, not as openly licensed reusable material unless the owner later grants explicit terms.

Linked/third-party evidence is not relicensed by Needle.

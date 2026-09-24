# DISC-03 — corpus authoring and contribution ergonomics

Issue: #113  
Parent: #104  
Date: 2026-09-24

## Question

Is adding a high-quality new case too expensive or error-prone for the Needle
corpus to scale as a research asset?

Alternative explanation: the expensive part of adding a case is evidence
discovery, legal/source review and deciding whether a failure mechanism is
actually earned. The mechanical corpus edit may already be small enough that
authoring tooling would automate the cheap part while increasing the risk of
making scientifically weak cases look "complete."

## Current admission path

The current repository path is deliberately asymmetric:

1. identify a concrete legal-information failure question;
2. preserve the source-grounded evidence owner in an issue/research artifact;
3. decide whether the case is DERIVATION or EVALUATION evidence;
4. for a new failure family, require enough independent support before adding the
   trap class;
5. add the minimal metadata entry to `corpus/index-v0.1.json`;
6. run `scripts/validate_adversarial_corpus.py` and the existing tests;
7. expose/reuse the case according to the contamination rules;
8. update project-level evidence/coverage documents only when the result actually
   changes those records;
9. review and merge through the normal PR/CI path.

This separation is useful: the index does not own the legal truth, and the
validator is intentionally structural rather than a legal-answer judge.

## Observed friction from recent admissions

Diff size is only a proxy for work, not elapsed effort, but the recent PRs show
where repository churn is actually concentrated.

### #91 / PR #92 — two derivation cases + one new trap class

- total diff: 318 additions / 2 deletions across 7 files;
- source-grounded research memo: 215 added lines;
- corpus index: 49 additions / 2 deletions;
- validator: 8 added lines;
- validator test: 8 added lines.

The validator/test additions were not per-case boilerplate. They added one new
general invariant: a declared trap class must be used by at least one case.
Future trap classes inherit that protection.

### #93 / PR #94 — two derivation cases + one new trap class

- total diff: 283 additions / 2 deletions across 5 files;
- source-grounded research memo: 191 added lines;
- corpus index: 49 additions / 2 deletions;
- no validator or validator-test change was required.

Again, the dominant artifact was evidence/research. The two corpus entries were
a small projection over that evidence.

### #97 / PR #102 — four revealed evaluation cases

- total diff: 606 additions / 37 deletions across 11 files;
- corpus index: 105 added lines;
- the remaining changes preserve the answer key, prompts, result fixture,
  execution limitations, audit, assumptions and project interpretation.

This is a deliberately heavier path because sealed evaluation has more
scientific provenance than ordinary derivation admission. A case-entry tool
cannot safely collapse that provenance without weakening the protocol.

### What the line counts do and do not show

For the two clean derivation admissions, index editing was about 15–17% of the
added lines. That does not prove the same ratio in human time, but it is strong
evidence against treating JSON entry as the dominant cost.

No recent admission shows repeated structural rework caused by the current
index format. The existing validator already fails on duplicate IDs, unknown
trap classes, case-count mismatch, missing evidence refs, unsafe paths,
inconsistent exposure state, invalid evaluation modes and unused trap classes.

The uncaught hard problems are semantic:

- is the decisive legal proposition actually supported;
- is the failure mechanism consequential rather than merely interesting;
- is a new trap class distinct enough to earn;
- is a validation case independent rather than contamination;
- is the evidence role DERIVATION versus EVALUATION correct in substance.

Those are the parts an authoring UI or generator is least qualified to decide.

## Baselines and adjacent precedent

### Repository-native PR + structured file + tests

This is the current Needle baseline and it has not demonstrated a failure.

BIG-bench used a similarly boring contribution model: a task lives in repository
files, contributors submit it by pull request, and task-specific tests validate
the machine-readable representation before review:

- https://github.com/google/BIG-bench/blob/main/docs/doc.md

The relevant lesson is not that Needle should copy BIG-bench's schema. It is
that a mature collaborative benchmark can keep contribution review in the
repository instead of requiring an authoring application.

LegalBench likewise remains a repository-curated benchmark made from contributor
tasks rather than an authoring product:

- https://github.com/HazyResearch/legalbench

DELTA exposes each task as repository data and keeps a CONTRIBUTING contract for
adding tasks/disputing criteria:

- https://github.com/legalbenchmarks/delta

These projects have different scientific goals, but they weaken the claim that
a benchmark/corpus must build a dedicated authoring UI to scale.

### GitHub issue form/template

GitHub issue forms can structure intake with fields, dropdowns and checkboxes,
and convert submissions into ordinary issue content:

- https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema

That could be useful later for external intake, but it is not an admission
validator. GitHub's current documentation also limits `required` form
validation to public repositories. Needle is private today, so an issue form is
not a stronger enforcement boundary for the current project.

A plain issue template would therefore mostly duplicate `corpus/README.md`
without solving an observed failure.

### Generator / CLI

A script could ask for ID/title/domain/jurisdiction/trap/evidence refs and append
a JSON object. It would save some punctuation and repeated field entry.

The risk is larger than the demonstrated benefit:

- a generated object can look complete before the research is complete;
- deciding trap class/provenance/exposure is scientific work, not boilerplate;
- automatic mutation of the canonical index increases merge/conflict surface;
- the validator already catches the structural errors a generator would mainly
  prevent.

A generator becomes justified only after repeated evidence that structural
authoring, rather than research/review, is causing real rework.

### Dedicated authoring UI

Rejected as a current baseline. It adds a second representation/workflow,
maintenance surface and likely validation logic while solving no observed
problem. It also creates pressure to turn admission into form completion.

## Friction map

| Step | Current friction | Failure consequence | Existing control | Tooling gap? |
|---|---|---|---|---|
| discover/source case | high, intentionally | unsupported or trivial case | source-grounded issue/research review | no |
| decide trap class | high, intentionally | taxonomy laundering/duplication | independent support + adversarial review | no |
| decide DERIVATION/EVALUATION | medium, consequential | contamination | protocol + validator metadata rules | no |
| enter index metadata | low/repetitive | syntax/shape error | validator + tests | no demonstrated gap |
| reference evidence owner | low but consequential | broken lineage | validator path/ref checks | no demonstrated gap |
| expose/reuse status | low but consequential | blind-reuse contamination | fixed enums + validator | no demonstrated gap |
| PR/review/CI | ordinary | bad corpus state reaches main | normal GitHub flow | no |
| sealed evaluation archival | high, intentionally | irreproducible result | evaluation protocol / exact artifacts | must not be hidden by authoring tooling |

The only clearly repetitive step is metadata entry. It is already bounded and
deterministically checked.

## Smallest experiment

**No authoring experiment is justified now.**

Do not create a template, generator, issue form or UI merely to demonstrate that
one could exist.

Reopen this question only if at least one of these is observed in future work:

1. two independent future admissions require avoidable structural correction
   cycles despite running the current validator;
2. a real external contributor cannot complete the documented repository-native
   admission path because the mechanics, rather than the legal/research standard,
   are the blocker;
3. repeated merge conflicts or duplicated manual edits show the single index is
   becoming an operational bottleneck.

If that evidence appears, the first experiment should be smaller than a UI:
test a non-authoritative candidate/stub workflow against direct JSON editing and
measure whether it removes the observed error without moving legal admission
decisions into code.

## Adversary

The tempting product move is to treat contribution friction as a growth problem
and build forms, schemas and workflows pre-emptively. That would reverse
Needle's current evidence discipline.

A second risk is false ergonomics: making it easier to create structurally valid
records can make it easier to submit weak cases. The project should optimize for
high-quality adversaries, not corpus row throughput.

A third risk is governance duplication. The corpus README already explains
admission and contamination, the evaluation protocol owns sealed validation,
and the validator owns machine-checkable structure. A new authoring layer would
need a unique failure to justify becoming a fourth owner.

## Decision

**REJECT**

Reject a corpus-authoring feature, generator or contribution workflow as a
current Needle experiment.

The present repository-native path is sufficiently small and, importantly,
keeps the expensive scientific judgments visible. Recent case admissions do not
show that metadata authoring is a material bottleneck. External benchmark
precedent also shows that repository files + review + validation are a credible
long-lived baseline.

This does not reject future external contribution. It rejects building tooling
before contribution mechanics demonstrably fail.

No corpus schema, issue form, generator, authoring UI, dependency or product
surface is added by this discovery.

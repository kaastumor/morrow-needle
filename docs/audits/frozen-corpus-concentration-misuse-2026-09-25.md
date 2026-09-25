# Frozen 81-case corpus — concentration and regression-misuse audit

Date: 2026-09-25  
Issue: #309  
Disposition: **ADOPT_LIMITATIONS_PROFILE**

## Scope

This audit describes the frozen scientific reference:

- `NEEDLE_CORPUS_REFERENCE_2026-09-25`;
- 81 cases;
- 26 trap classes;
- all cases exposed / `blind_reuse=false` / `REGRESSION_ONLY`.

It does not add, remove, merge or score cases/classes.

The previous maintained bias audit was written for the 19-case seed and appended only
through 23 cases. It remains valid history, but its composition numbers and several blind
spot statements are no longer current.

## Mechanical frozen-state profile

### Provenance

- **71/81 DERIVATION** cases — 87.7%;
- **10/81 EVALUATION** cases — 12.3%;
- all 10 evaluation cases come from two evaluation programmes:
  - Issue #88: 6 surfaced-trap cases;
  - Issue #97: 4 latent-trap cases.

Evaluation modes:

- 6 `SURFACED_TRAP_ADJUDICATION`;
- 4 `LATENT_TRAP_DETECTION`.

This is not 10 independent experimental programmes. It is ten revealed cases from two
shared evaluation designs.

### Trap-class support

The final support counts are unusually flat:

- 17 classes have exactly **3** cases;
- 8 classes have exactly **4** cases;
- 1 class has exactly **5** cases;
- 0 classes have 1 or 2 cases.

Largest class:

- `DYNAMIC_REFERENCE_STATUS` — 5 cases.

Four-case classes:

- `AUTHORITATIVE_EXTERNAL_INPUT_TRIGGER`;
- `COHORTED_TRANSITIONAL_APPLICABILITY`;
- `DIFFERENTIATED_MEMBER_STATE_PARTICIPATION`;
- `EXPRESSION_LOCAL_REPRESENTATION_ASYMMETRY`;
- `JUDICIAL_VALIDITY_TEXT_DIVERGENCE`;
- `PRIVATE_ORIGIN_LEGAL_RECOGNITION`;
- `SOURCE_VIEW_TEMPORAL_DIVERGENCE`;
- `STATUS_APPLICATION_SEPARATION`.

Every other class has 3 cases.

This resolves the seed audit's one-case-family weakness. It must **not** be read as
frequency, prevalence or importance. The post-#217 research programme explicitly used
coverage/depth questions, existing-class-first review and later depth checks; the final
near-flat support profile is therefore a curated research outcome, not a random sample of
EU legal-research failures.

### Evaluation coverage by class

Only **8/26 classes (30.8%)** have any `EVALUATION` case.

Classes with evaluation evidence:

- `DYNAMIC_REFERENCE_STATUS` — 2 evaluation cases (1 surfaced, 1 latent);
- `STATUS_APPLICATION_SEPARATION` — 2 (1 surfaced, 1 latent);
- `EXPRESSION_LOCAL_REPRESENTATION_ASYMMETRY` — 1 surfaced;
- `JUDICIAL_VALIDITY_TEXT_DIVERGENCE` — 1 latent;
- `PRIVATE_ORIGIN_LEGAL_RECOGNITION` — 1 surfaced;
- `SOURCE_VIEW_TEMPORAL_DIVERGENCE` — 1 surfaced;
- `PARALLEL_INSTRUMENT_LIFECYCLE` — 1 latent;
- `SUBDAY_TEMPORAL_BOUNDARY` — 1 surfaced.

**18/26 classes (69.2%) have derivation evidence only.**

Those 18 classes may be excellent regression/reference families. Their 3–4 case support
does not become independent comparative validation merely because multiple examples now
exist.

### Class overlap / composition

The 81 cases contain 88 total class memberships:

- 75 cases have exactly 1 class;
- 5 cases have exactly 2 classes;
- 1 case has exactly 3 classes.

Only **6/81 cases (7.4%)** are explicitly multi-class.

The single three-class case is
`matrimonial-property-participation-law-forum-composition`.

This supports simple regression navigation, but it also means class frequencies are not
natural incident frequencies. Most cases were stored around one primary failure family even
though real legal questions can compose multiple mechanisms.

### Domain labels

The frozen cases contain **68 distinct stored domain labels**.

Exact label frequency:

- 58 labels occur once;
- 7 labels occur twice;
- 3 labels occur three times.

The most frequent exact labels are:

- `digital services` — 3;
- `international agreements / trade` — 3;
- `state-aid procedure` — 3.

The next seven exact labels occur twice.

This is genuine subject-matter breadth, but the `domain` field is descriptive metadata,
not a controlled coverage taxonomy. The large number of singleton labels must not be
converted into a claim that 68 calibrated legal domains are represented or evenly covered.

### Jurisdiction labels

Exact stored labels:

- `EU` — **53/81 cases (65.4%)**;
- the remaining 28 cases use 20 other exact jurisdiction labels, including Member-State,
  EEA, third-country, enhanced-cooperation and historical combinations.

Compared with the 19-case seed, national/linked-order variety is materially broader.
The corpus remains predominantly EU-level.

### Provenance concentration

The 81 cases originate from **54 provenance issues**.

Largest provenance suites:

- Issue #88 — 6 cases;
- Issue #97 — 4 cases;
- later discovery issues generally contribute one or two cases.

The two largest suites are exactly the evaluation programmes. This matters when consumers
count cases: ten evaluation cases do not imply ten independently designed evaluations.

### Evidence-owner form

From the released evidence map / #306 audit:

- 45/81 cases (55.6%) are issue-only from the Reference Pack perspective;
- 36/81 have at least one commit-pinned repository path.

This is a provenance/recoverability limitation, not a scientific-support score. Issue-only
owners remain mutable navigation records under the #306 rule.

## What changed since the 19/23-case audit

### Materially improved

**One-case class support**

The original audit had six one-case classes. The frozen reference has none; every class
has 3–5 cases.

**National implementation / Member-State variation**

The corpus now includes dedicated national-transposition cases plus Member-State options,
direct-effect/primacy, passport/recognition and territorial-regime examples.

**International / linked legal-order lifecycle**

The earlier international-agreement blind spot is materially reduced through Mercosur,
Mexico and Chile parallel-instrument lifecycle cases, plus EEA/Swiss incorporation-state
examples.

**Authoritative registers, datasets and machine artifacts**

Trusted-list state, authoritative external metrics/data, semantic profiles and prescribed
calculation/tool artifacts now provide concrete non-textual source families.

**Procedure / authority handoff**

Delegated-act non-objection, deemed legal effects, assessment-clock suspension and
upstream-authority/downstream-decision cases broaden procedural-state coverage.

### Improved but still not safely quantifiable

**Source-system diversity**

Issue #315 re-opened the accepted evidence owners without doing new legal research.

It confirms that source-family variety materially broadened beyond the seed: accepted
evidence now includes Member-State official material, private legally recognised sources,
EU agency/body material, official registers/datasets/machine artifacts and linked-order /
international-agreement evidence in addition to EUR-Lex/Commission material.

However, the canonical index still does not encode a controlled per-case source inventory.
Shared issues and shared evaluation packets also make owner-level keyword/family counts
unsafe to promote into exact case-level percentages.

Therefore the project can claim broader **source-family variety**, but not a reproducible
numerical source-system distribution.

See `docs/audits/frozen-source-system-diversity-2026-09-25.md`.

**National court/application coverage**

Several current cases involve Member-State law, direct effect, primacy/disapplication and
national procedural contexts. That is materially broader than the seed.

But `domain` / `jurisdiction` metadata does not encode a controlled "national court
case" axis, so no completeness claim follows.

### Still visibly weak / unresolved

**Older digitised legal sources**

No frozen case can be identified from its canonical metadata as deliberately representing
the old audit's "older digitised source / degraded metadata" blind spot.

Absence from the metadata is not proof that no case touches old material, but this remains
unsupported as a covered failure axis.

**Independent evaluation coverage**

This is now the most important scientific imbalance.

The taxonomy has broad derivation support, but 18/26 classes have no evaluation case and
all evaluation cases derive from two programmes. More cases per class did not make the
corpus a representative or statistically calibrated benchmark.

## Regression/reference use versus benchmark use

The frozen corpus is well suited to:

- preserving known consequential failure mechanisms;
- regression checks against known exposed cases;
- inspecting class boundaries and provenance;
- constructing examples and test fixtures with explicit exposure status;
- checking whether a system regresses on previously understood distinctions.

It is **not** evidence for:

- prevalence of these failure modes in EU legal research;
- relative frequency or importance of the 26 classes;
- expected error rates;
- model ranking;
- representative task performance;
- independent validation across all classes;
- current-law correctness without reopening the source/evidence chain.

The near-flat 3–5 case class distribution is especially dangerous if treated as a natural
sample. It is a support/coverage shape, not an incidence distribution.

## Concrete misuse modes created by a polished Reference Pack

1. **"81 cases" -> sample-size rhetoric.**  
   Counting exposed curated cases as though they were 81 independent observations of
   population performance.

2. **Balanced class counts -> prevalence inference.**  
   Reading the 3–5 support counts as class frequency or importance.

3. **Ten EVALUATION records -> ten independent experiments.**  
   Ignoring that all ten come from only #88 and #97.

4. **68 domain labels -> calibrated breadth.**  
   Treating descriptive one-off labels as a controlled domain taxonomy.

5. **REGRESSION_ONLY -> benchmark leaderboard.**  
   Re-running revealed cases and presenting model success as fresh generalisation.

6. **Pack reproducibility -> evidence immutability.**  
   Extending deterministic pack checksums to mutable issue-only evidence owners.

7. **Historical correctness -> current-law correctness.**  
   Treating frozen cases as an always-current legal-answer set.

## Disposition

**ADOPT_LIMITATIONS_PROFILE**

The old bias audit was directionally right but is materially stale as a description of the
frozen corpus.

The new profile records two simultaneous truths:

1. **structural coverage improved substantially** — every class now has multiple cases and
   several old blind spots received real examples;
2. **scientific independence remains narrow** — most cases are derivation evidence, most
   classes have no evaluation case, evaluation evidence is concentrated in two programmes,
   and the corpus is curated rather than representative.

No corpus change, new case hunt, taxonomy change or new evaluation campaign follows from
this audit.

The correct use remains:

> exposed adversarial regression/reference corpus, not representative benchmark.

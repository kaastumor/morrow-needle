# #292 result — adversarial corpus reference checkpoint

Date: 2026-09-25  
Mode: **REVIEW / RELEASE**  
Baseline main: `b9ff7b6c9aa17f912f5b2dc5bd24d97490ad2e6c`

## Decision

# **RELEASE_READY**

The accepted adversarial corpus is internally coherent enough to serve as a stable
regression/reference checkpoint after one bounded metadata/documentation repair.

This decision does **not** claim:
- taxonomy completeness;
- product value;
- model or workflow superiority;
- legal correctness beyond the referenced evidence owners;
- fresh blind validity for exposed cases.

The ordinary repository merge gate still applies. This result becomes canonical only if
the release PR passes its deterministic checks and merges.

## Checkpoint identity

Reference name:

> **NEEDLE_CORPUS_REFERENCE_2026-09-25**

Canonical index path:

> `corpus/index-v0.1.json`

Release-candidate index Git blob:

> `ecaab3f59fe118b71d2cafa19f05363a65ae49a1`

Schema version:

> `adversarial-corpus-index-v0.1`

Corpus shape:

> **81 cases / 26 trap classes**

The Git blob is the exact immutable data checkpoint. Later corpus growth may move the live
index without changing what this checkpoint contained.

## Content integrity

The release audit parsed the canonical JSON and verified:

- declared `case_count=81`;
- actual case count = 81;
- actual trap-class count = 26;
- no duplicate case IDs;
- no unknown trap-class references;
- no trap class without a case;
- no empty release-critical title/domain/jurisdiction/decisive-trap field;
- every case has provenance, exposure and evidence refs.

Class support at this checkpoint ranges from 3 to 5 cases. No class is represented by a
single isolated example.

## Provenance and exposure

Role distribution:

- **71 DERIVATION**
- **10 EVALUATION**

Exposure distribution:

- **71 PUBLIC_FROM_DISCOVERY**
- **10 REVEALED_AFTER_SEALED_EVALUATION**

Every public case has:

- `blind_reuse=false`;
- `future_use=REGRESSION_ONLY`.

The 10 evaluation cases remain construct-labelled:

- **6 SURFACED_TRAP_ADJUDICATION**
- **4 LATENT_TRAP_DETECTION**

No case becomes fresh blind evidence through this release.

## Evidence-reference closure

The index contains:

- **54 unique `issue:` owners**;
- **32 unique repository `path:` owners**.

This release review explicitly resolved every unique issue owner through GitHub:

> **54 / 54 exist; 54 / 54 are closed**

It also explicitly fetched every unique repository path:

> **32 / 32 exist**

The existing validator already checks repository path existence fail-closed and requires
each case's provenance issue to appear in its evidence refs.

The release review therefore found no dangling evidence owner.

## Scientific-content immutability

Compared with accepted baseline main:

- the entire `cases` array is byte-for-byte JSON-equivalent;
- the entire `trap_classes` object is byte-for-byte JSON-equivalent;
- `schema_version` is unchanged;
- `case_count` is unchanged.

Only top-level release metadata changes:

- `status: CANONICAL_SEED -> CANONICAL_REFERENCE`;
- reuse wording changes from “public seed” to “public reference corpus”.

Therefore this release review makes **no scientific corpus admission, retirement, merge or
definition change**.

## Bounded release repairs

### 1. Corpus status

`CANONICAL_SEED` had become misleading after the corpus matured through multiple
generality, compression and retrospective gates.

It is now:

> `CANONICAL_REFERENCE`

This is a maturity/status correction, not a claim that the taxonomy is final.

### 2. Validator identity checks

The existing `scripts/validate_adversarial_corpus.py` already protects:

- schema version;
- case count;
- required case fields;
- unique IDs;
- known/used classes;
- provenance roles;
- exposure/reuse constraints;
- evaluation modes;
- issue-ref syntax;
- repository-path existence.

The release repair adds only top-level reference identity checks:

- status must be `CANONICAL_REFERENCE`;
- `purpose` must be non-empty;
- `reuse_policy` must be non-empty.

No new schema or validator framework is added.

### 3. Corpus-facing documentation

`corpus/README.md` now describes the index as a reference corpus rather than a seed and
states what reference status does **not** imply.

The old Explorer MVP plan and technical release check are explicitly marked
**PASSIVE HISTORICAL** records. Their original experiment/release findings remain
preserved, but they cannot be mistaken for current release authority.

The canonical evaluation protocol required no scientific change.

## Open-work check

At the start of this release review there was no open PR changing accepted corpus truth.

#292 owns this release branch under WIP=1.

## Release boundary

This checkpoint is fit for:

- regression/reference use;
- inspection and teaching of exposed failure mechanisms;
- future evaluation design/calibration where exposure is respected;
- reproducible citation of the corpus state represented by the blob above.

It is not fit for:

- calling the 81 cases a blind benchmark;
- estimating population prevalence of failure classes;
- claiming that 26 classes are complete or optimal;
- claiming Needle improves GPT/legal-research performance;
- reviving the Explorer or prior broader product surfaces.

#214 remains unchanged:

> **0 diagnostic rescues / 0 C-only regressions**

## Reopening / next release

Create a new reference checkpoint when accepted corpus content materially changes, such as:

- case admission/retirement;
- class admission/retirement/merge;
- consequential class-definition change;
- exposure/provenance correction affecting reuse.

Ordinary source drift in a historical case does not silently rewrite this checkpoint; it
must be handled under the corpus protocol's temporal/source-drift rules.

## Final

# **RELEASE_READY**

Subject to the standard green merge gate, the 81-case / 26-class corpus earns a stable
reference checkpoint as:

> **NEEDLE_CORPUS_REFERENCE_2026-09-25**

Exact index blob:

> `ecaab3f59fe118b71d2cafa19f05363a65ae49a1`

# #150 result — DELTA v1.1.0 benchmark-integrity audit

Date: 2026-09-24  
Issue: #150  
Claim type: `CORRECTNESS_VALIDITY`  
Target: `legalbenchmarks/delta` `v1.1.0` / `c713132`  
Pre-registration: `docs/experiments/issue150-delta-preregistration-2026-09-24.md`

## Decision

**REVISE**

The frozen four-task audit found one fresh, mechanically reproducible
`F4 — reproducibility/configuration` defect in DELTA's public v1.1.0 harness
contract.

It also found one Dutch-law F2 candidate that remains deliberately unconfirmed
because the preregistration requires independent qualified legal review.

The result supports a narrow transfer claim:

> Needle's evaluation-integrity / evidence-closure discipline can expose useful
> gaps in an external legal benchmark's public reproducibility contract.

It does **not** establish:

- a general benchmark-audit capability;
- superiority over expert benchmark maintainers;
- user demand for an audit product;
- invalidity of DELTA's published leaderboard.

No second benchmark audit or product work is authorised by this result.

## Frozen sample

1. `real-estate/interpretation-of-notarial-deeds-limited-rights`
2. `competition-law/acm-concentration-notification-requirement`
3. `employment-law/inappropriate-conduct-in-the-workplace`
4. `corporate-law/director-and-supervisory-board-conflicts`

Property-law and family-law were excluded before sampling because #137 had
already used known public disputes from those areas.

The exact sample was selected by the committed SHA-256 path rule.

### Preview-exposure incident

During path enumeration, GitHub search returned content fragments along with
metadata after the first preregistration commit but before exact-path freeze.

The event was recorded before audit.

The already-frozen selection algorithm remained binding, so content could not be
used to replace tasks. Real-estate and corporate-law are conservatively marked
`PREVIEW_EXPOSURE`; preview text receives zero evidentiary credit.

## Strong baseline

Inspected at frozen commit:

- four selected `task.json` files;
- `README.md`;
- `CONTRIBUTING.md`;
- `docs/harness.md`;
- `docs/judge.md`;
- `scripts/validate.py`;
- `scripts/build_index.py`;
- `.github/workflows/validate.yml`;
- `CHANGELOG.md`.

DELTA's baseline is strong.

Its validator enforces structure, task/path identity, `law_as_of`, bilingual
content, criterion IDs/types/dimensions, `lawyer_validated: true`, and
byte-for-byte agreement between canonical task files and
`data/tasks.jsonl`. CI runs that validator.

Contribution rules require self-contained practitioner tasks, binary criteria,
defensible alternatives, answer-text verifiability, legal review and semantic
versioning.

These controls are explicit counterevidence against a weak-baseline story.

## Confirmed finding F4-01 — minimal run record violates the stated provenance contract

Status: **CONFIRMED MECHANICAL FINDING**  
Class: `F4`  
Independent legal review: not required  
Prior public disclosure found: no

### Internal contradiction

`docs/harness.md` says a run must be attributable, auditable and reproducible.

Rule 6 requires preserving:

- verbatim answer;
- requested parameters;
- actually applied parameters;
- timestamps;
- sources seen.

Rule 5 additionally requires identical limits and explicit stop/truncation
reasons.

But the same document's "Suggested record" — introduced as carrying enough
metadata to reproduce the run — stores only:

- `task_id`;
- `dataset_version`;
- `system`;
- `run`;
- `answer`.

The published minimal Python harness writes the same five fields.

It therefore omits information the normative rule itself says is required,
including execution parameters, limits, timestamps and source set.

### Materiality

This crosses the pre-registered F4 materiality threshold for **third-party use of
the open-source benchmark**.

A user can reasonably follow the supplied minimal record yet be unable later to
reconstruct whether result-sensitive configuration or sources were identical.

This is not a preference invented by Needle; it is a mismatch inside DELTA's own
public reproducibility contract.

### Strongest counterargument

The prose rule is explicit and should control over an intentionally minimal code
example. A sophisticated user may also version configuration elsewhere.

That lowers severity.

It does not remove the contradiction because the example is itself presented as
having enough metadata for reproduction while omitting fields the same page
requires.

### Smallest repair

Either:

- expand the example with the required run metadata; or
- mark it explicitly incomplete and require a separate run manifest.

Needle does not implement that repair.

## Critical scope boundary — official DELTA leaderboard

After F4-01 was identified, the current public DELTA Benchmark Report was
inspected as counterevidence.

It describes a larger official evaluation with a different/refined execution
boundary, including:

- shared research/search/source-reading setup;
- fixed time/tool limits;
- one completed answer per model/question;
- specified judge models and human-review logic;
- public questions included in the larger evaluation;
- public criteria explicitly stated to be **not identical** to the leaderboard
  criteria.

Source:
https://www.legalbenchmarks.ai/research/delta-dutch-legal-research-benchmark

Therefore F4-01 must **not** be interpreted as evidence that the official
leaderboard used the incomplete GitHub sample record or that its published
scores are invalid.

The finding is bounded to the public v1.1.0 repository's third-party harness
contract.

## Four-task result

### Real estate

`PREVIEW_EXPOSURE`

Prompt/criteria alignment, cutoff, binary gradability and internal consistency
were inspected.

**No confirmed F1–F5 finding.**

The current DELTA report also uses this task to illustrate the unresolved
same-day-deed question, supporting rather than contradicting its core criterion
design.

### Competition law

Current statutory/ACM materials were checked for the Article 29 thresholds and
notification/standstill structure.

Potential overbreadth around sector-specific calculation detail and compressed
standstill wording did not cross the frozen materiality threshold.

**No confirmed F1–F5 finding.**

### Employment law

Potential pressure around contextual factors, employer guidance and the
criterion requiring nuance/criticism of the case-law line was inspected.

Given DELTA's explicit open-ended completeness/legal-judgment construct, the
evidence was insufficient to call these defects.

**No confirmed F1–F5 finding.**

### Corporate law

`PREVIEW_EXPOSURE`

One F2 candidate survives:

`CANDIDATE_LEGAL_FINDING — fallback decision maker omits statutory exception`

Public criteria describe the general-meeting fallback when conflicts block board
or supervisory-board decision-making.

Current Book 2 BW text contains the express exception:

> `tenzij de statuten anders bepalen`

for the relevant general-meeting fallback.

That means a categorical answer can satisfy the public criterion while omitting
a statutory qualification.

This could be material, but the preregistration requires independent qualified
Dutch-law review before a contestable F2/F5 issue is called confirmed.

No such review was manufactured for this experiment.

Result remains **candidate only** and does not count toward success.

## Rejected audit branches

### Generated index drift

**REJECTED.**

`scripts/validate.py` reconstructs the expected JSONL and requires byte-for-byte
equality with `data/tasks.jsonl`; CI runs it.

### Generic judge-setup incompleteness

**NOT RETAINED.**

The public judge document intentionally describes a judge contract rather than a
single implementation, and requires publishers to describe their setup.

The official report additionally discloses the judge models/human-resolution
logic for its leaderboard.

### Temporal cutoff

All four selected tasks use `law_as_of = 2026-08-30`.

No sufficiently evidenced criterion using a later or contradictory legal state
was found.

**No F5 finding.**

## Freshness check

Before retaining F4-01, searches covered:

- open DELTA GitHub issues;
- closed DELTA GitHub issues;
- DELTA pull requests;
- web search around harness metadata, parameters, timestamps, sources,
  reproducibility and judge prompts.

No prior public disclosure of this exact harness-record inconsistency was found.

This means **no prior disclosure found**, not proof that no private or unindexed
discussion exists.

Known property/family disputes retain zero fresh-value credit.

## Pre-registered success / kill test

Success required at least one fresh, reproducible, materially consequential
defect/ambiguity capable of affecting grading, interpretation, reproducibility
or validity.

**Met narrowly by F4-01.**

Why not call this a broad win?

The strongest counterargument survives:

> this is careful documentation QA, not proof of a distinctive Needle audit
> capability.

Needle's demonstrated contribution here is the **discipline**:

- pre-registered failure classes;
- frozen sample;
- strongest-baseline inspection;
- provenance/execution treated as first-class;
- negative findings retained;
- legal candidate not self-validated;
- official-report counterevidence used to narrow the claim.

One instance is insufficient to generalise.

## Final disposition — REVISE

Original H-18-style claim:

> Needle's adversarial corpus/evaluation discipline can expose a material,
> previously unrecorded integrity defect in a credible external legal benchmark
> beyond its mature QA baseline.

Observed:

- one bounded positive F4 instance;
- three selected tasks with no confirmed issue;
- one unconfirmed F2 candidate;
- strong DELTA controls that falsified several tempting findings.

Revise to:

> **Needle's evaluation-integrity and evidence-closure discipline can transfer
> usefully to external legal evaluation artifacts, particularly around public
> reproducibility/provenance contracts; general distinctiveness beyond strong
> benchmark QA remains unproven.**

Do not run another benchmark merely to seek generality.

## Project consequence

- corpus + evaluation protocol remain the essential identity;
- H-18 should move to `REVISE`;
- F4-01 is retained as external transfer evidence;
- F2 candidate remains explicitly unconfirmed;
- no benchmark product/service/tooling;
- no scheduled discovery;
- run the mandatory post-#150 Project Health Check;
- absent stronger evidence, prefer **idle by design** over another experiment.

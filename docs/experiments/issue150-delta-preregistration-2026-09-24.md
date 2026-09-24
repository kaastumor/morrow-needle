# #150 pre-registration — DELTA benchmark integrity audit

Date: 2026-09-24  
Issue: #150  
Claim type: `CORRECTNESS_VALIDITY`  
Status: **PRE-REGISTERED BEFORE TASK CONTENT INSPECTION**

## Benchmark freeze

Target benchmark:

- repository: `legalbenchmarks/delta`
- release/tag: `v1.1.0`
- tagged commit: `c713132`
- release date shown by GitHub: 2026-09-03

The repository README identifies this release as DELTA version 1.1.0 and describes
15 open-ended Dutch legal-research tasks across nine practice areas.

No model leaderboard/result is used for sample selection.

## Known-defect exclusion boundary

The #137 derivation scan already exposed two public DELTA disputes:

- property-law criterion defect (public issue #1);
- family-law gradability defect (public issue #2).

To avoid post-hoc rediscovery credit, **all property-law and family-law tasks are
excluded from the fresh audit sample**, not merely the named criteria.

Any other defect found to have been publicly documented before this
pre-registration also receives zero fresh-value credit.

## Eligible practice areas

Based only on README-level task counts, before opening task contents:

- tort-law
- corporate-law
- insolvency-restructuring
- real-estate
- contract-law
- employment-law
- competition-law

Excluded:

- property-law
- family-law

## Sample size and deterministic selection

Initial sample: **4 tasks from 4 distinct eligible practice areas**.

Practice-area selection is deterministic:

1. compute SHA-256 of `c713132|<practice-area-slug>`;
2. sort ascending by hash;
3. select the first four eligible practice areas.

This produces:

1. `real-estate`
2. `competition-law`
3. `employment-law`
4. `corporate-law`

Within a selected multi-task practice area:

1. enumerate task folder paths **without opening task contents**;
2. compute SHA-256 of `c713132|<full-task-path>`;
3. select the lowest hash in that practice area.

For a selected single-task practice area, that task is selected automatically.

The exact four task paths will be appended and committed **before any selected
task content is opened**.

## Audit failure classes

Only the following pre-registered defect classes count in the initial audit.

### F1 — criterion not falsifiable / gradeable from the task and answer

A criterion depends on a condition, proposition or expected content that the task
does not reasonably elicit or that cannot be judged from the answer under the
published judging contract.

### F2 — criterion / authority mismatch

The criterion attributes a proposition to the wrong authority, paragraph,
provision, temporal state or legal source, or otherwise makes a material
source-grounding claim that does not match the cited controlling authority.

### F3 — scorer / documentation mismatch

Implemented scoring, aggregation or parsing behavior materially diverges from
the benchmark's published task/judge documentation or allows clearly invalid
outputs to receive credit / valid outputs to lose credit.

### F4 — result-sensitive execution configuration missing or ambiguous

A documented benchmark result cannot be reproduced/interpreted reliably because
a configuration boundary capable of materially changing outputs or scores is
missing, ambiguous or inconsistently specified.

### F5 — temporal / legal-cutoff ambiguity

The task, criterion or cited authority uses a legal state outside the declared
`law_as_of`, or the cutoff is insufficiently specified in a way that can
materially change the legally correct answer.

## Materiality rule

A finding is **material** only if, under a plausible benchmark run, it can do at
least one of the following:

- penalise a legally correct answer;
- reward a materially wrong answer;
- make a criterion non-determinately gradeable under the published contract;
- materially alter criterion/task score;
- materially alter interpretation of a benchmark result;
- prevent a competent third party from reproducing the relevant evaluation
  boundary.

Pure style preference, wording taste, harmless metadata inconsistency or a defect
with no plausible effect on grading/interpretation is not material.

## Independent-review boundary

Potential F2 or F5 findings that depend on contestable Dutch-law interpretation
cannot be called **confirmed material defects** without independent qualified
legal review.

Before that review they may be recorded only as:

`CANDIDATE_LEGAL_FINDING`.

Mechanically demonstrable F1, F3 and F4 findings may be confirmed without legal
expert review when the repository artifacts themselves establish the mismatch.

## Strong baseline

The comparator is DELTA's own documented quality system:

- practising-lawyer task/review input;
- explicit criteria;
- controlling-authority expectations;
- `law_as_of`;
- fixed harness guidance;
- judge protocol;
- versioning;
- public dispute/contribution process;
- ordinary open-source code/data inspection.

Needle receives no credit for a finding already surfaced by that system before
sample freeze.

## Audit order

For each frozen task:

1. read task/question metadata and `law_as_of`;
2. inspect all published criteria and their cited authority/evidence fields;
3. compare criterion semantics with the task and published judge contract;
4. inspect only the scorer/harness paths necessary to test F3/F4;
5. inspect cited legal sources only when needed for an F2/F5 candidate;
6. actively search for public prior disclosure of any candidate before claiming
   freshness;
7. record non-findings as well as findings.

Do **not** inspect model leaderboard winners to choose or retain findings.

## Stop / kill rule

Initial audit ends after the four frozen tasks.

Disposition is `REJECT` for distinct Needle value if:

- no material previously unrecorded defect/ambiguity is found; or
- findings are only subjective/style issues; or
- all material findings were already public before freeze; or
- generating a meaningful finding requires effectively recreating DELTA's own
  maintainer/reviewer workflow rather than applying a bounded adversarial audit.

A single candidate requiring legal expert review does not count as success until
review occurs.

One follow-up evidence run is permitted only to resolve a concrete candidate
found in the frozen sample; it may not expand the sample after seeing negative
results.

## Evidence-closure rule

Preserve:

1. this pre-registration;
2. exact tag/commit and selected paths;
3. sources/artifacts actually inspected;
4. finding/non-finding record;
5. freshness check;
6. final disposition.

No general benchmark harness or provenance service will be built.

## Pre-inspection declaration

At the time this file is first committed:

- DELTA README/repository structure and task-folder names at the top level have
  been inspected;
- tag `v1.1.0` / commit `c713132` has been identified;
- the two already-known public issue families are known derivation evidence;
- **no selected task's question, criteria, answers or cited authorities have
  been opened for this experiment**.


## Sample finalisation — committed before audit conclusions

The metadata-only path enumeration step identified these candidate folders in
the two selected multi-task practice areas:

### real-estate

- `tasks/real-estate/interpretation-of-notarial-deeds-limited-rights`
  - SHA-256(`c713132|<path>`) =
    `2741a663262edddbf903d852730ba0b9ed01cb7032fddfbadae125f10967d332`
- `tasks/real-estate/ground-rent-revision-and-reasonableness-fairness`
  - `d1250eee5475b7e006d3cfbabf21ac06d1e4f1f7972be64cddd004f9dc842817`

Selected: **interpretation-of-notarial-deeds-limited-rights**.

### corporate-law

- `tasks/corporate-law/director-and-supervisory-board-conflicts`
  - `153fdaa32f5c1e11db72705ad36dfe133f94de3301bcee779b7917f16b178757`
- `tasks/corporate-law/instruction-power-of-the-general-meeting`
  - `234f1df6cee9ec28b5d2efe66f59992590c7c2f323cd1beea506cc037162d3a6`

Selected: **director-and-supervisory-board-conflicts**.

The two selected single-task practice areas require no within-area choice.

### Frozen four-task sample

1. `tasks/real-estate/interpretation-of-notarial-deeds-limited-rights`
2. `tasks/competition-law/acm-concentration-notification-requirement`
3. `tasks/employment-law/inappropriate-conduct-in-the-workplace`
4. `tasks/corporate-law/director-and-supervisory-board-conflicts`

No replacement is permitted because a selected task looks easy, hard,
interesting or uninteresting.

## Pre-audit metadata exposure incident

During path enumeration, the GitHub code-search connector returned content
fragments alongside the requested path metadata.

This occurred:

- **after** the first pre-registration commit;
- after the four practice areas and within-area hash-selection algorithm were
  frozen;
- **before** this exact-path finalisation commit;
- before any audit finding, materiality decision or retention decision was made.

Some task content may therefore have appeared in analyst context before the
exact four paths were committed.

### Integrity consequence

This prevents claiming that every selected task remained fully unseen until the
exact-path commit.

It does **not** permit changing the sample: the selection algorithm already
fixed which path must win in each selected practice area independently of task
content.

To reduce interpretation bias:

1. the hash-selected sample above remains binding;
2. findings must be reconstructed from the canonical selected task artifacts,
   not from remembered search snippets;
3. every selected task whose content was present in a search fragment is marked
   `PREVIEW_EXPOSURE`;
4. preview exposure cannot count as evidence for a finding or as evidence of
   audit value;
5. no sample replacement or expansion is allowed.

If the audit result depends materially on analyst blindness rather than on
reproducible artifact defects, the experiment must be downgraded or rejected.

## Final pre-content gate

After this commit, the sample is fully frozen.

Only now may the four selected task artifacts and the minimum benchmark
scorer/harness documentation needed by F1–F5 be opened for substantive audit.

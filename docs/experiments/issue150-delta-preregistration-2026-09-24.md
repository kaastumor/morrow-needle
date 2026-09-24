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

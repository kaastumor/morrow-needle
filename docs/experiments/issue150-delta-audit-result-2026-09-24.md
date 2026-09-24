# #150 result — adversarial audit of DELTA v1.1.0

Date: 2026-09-24  
Issue: #150  
Claim type: `CORRECTNESS_VALIDITY`  
Benchmark: `legalbenchmarks/delta`  
Frozen release: `v1.1.0`  
Frozen commit: `c713132`  
Pre-registration: `docs/experiments/issue150-delta-preregistration-2026-09-24.md`

## Executive result

**Final disposition: REVISE**

The bounded audit found one fresh, mechanically reproducible
`F4 — result-sensitive execution configuration / reproducibility` defect in the
open-source DELTA harness contract:

> the normative harness rules require parameters, applied parameters, timestamps
> and sources to be retained, while the repository's own "Suggested record" and
> "minimal harness pattern" omit those fields even though the suggested record is
> introduced as containing enough metadata to reproduce the run.

A user following the provided minimal record cannot reconstruct the exact
evaluation boundary that the same document says must be preserved.

No public GitHub issue/PR or external web result found during the freshness check
had already recorded this specific inconsistency.

This is a real external transfer of Needle's evidence-closure discipline, but it
does **not** justify the broad claim that Needle has discovered a new benchmark
auditing category or that DELTA's published leaderboard is invalid.

A second selected finding remains only:

`CANDIDATE_LEGAL_FINDING`

because confirming its material legal status would require independent qualified
Dutch-law review under the pre-registered boundary.

The appropriate project conclusion is therefore narrower:

> Needle's evaluation/provenance discipline can usefully expose gaps in an
> external benchmark's public reproducibility contract, but one documentation-
> level defect does not yet establish a distinctive general benchmark-audit
> capability.

No follow-up benchmark product or recurring audit is authorised.

---

## 1. Frozen sample

The sample was fixed by the pre-registered hash rule before audit conclusions:

1. `tasks/real-estate/interpretation-of-notarial-deeds-limited-rights`
2. `tasks/competition-law/acm-concentration-notification-requirement`
3. `tasks/employment-law/inappropriate-conduct-in-the-workplace`
4. `tasks/corporate-law/director-and-supervisory-board-conflicts`

Practice areas `property-law` and `family-law` were excluded because the
#137 derivation scan had already used public disputes from those areas.

### Preview-exposure note

The path-enumeration connector returned content fragments while exact paths were
being listed.

The incident was committed before substantive audit and could not alter the
already-frozen practice-area or hash-selection rules.

The selected real-estate and corporate-law tasks are conservatively marked
`PREVIEW_EXPOSURE`.

The preview fragments receive zero evidentiary credit.

---

## 2. Benchmark baseline inspected

The audit inspected DELTA's own strong public controls at the frozen commit:

- `README.md`
- `CONTRIBUTING.md`
- `docs/harness.md`
- `docs/judge.md`
- `scripts/validate.py`
- `scripts/build_index.py`
- `.github/workflows/validate.yml`
- `CHANGELOG.md`
- the four frozen task files.

The baseline is materially stronger than a loose benchmark dataset.

### Confirmed baseline strengths

The validator enforces, among other things:

- task/schema structure;
- task ID ↔ directory identity;
- ISO `law_as_of`;
- normative Dutch + English completeness;
- criterion ID/type consistency;
- criterion dimension rules;
- `lawyer_validated: true`;
- citation-authority warnings;
- **byte-for-byte agreement between `data/tasks.jsonl` and the canonical task
  files**.

CI runs that validator on push and pull request.

This rules out a tempting stale-generated-index finding.

The contribution contract also explicitly requires:

- self-contained practitioner tasks;
- binary criteria;
- defensible-alternative handling;
- criteria verifiable from answer text;
- legal review for task/criterion changes;
- semantic versioning.

The judge contract explicitly separates substance/form and requires disagreement
escalation and practitioner spot-checking for publishable results.

These controls are counter-evidence against any claim that ordinary QA is absent.

---

## 3. Finding F4-01 — public harness record contradicts its own reproducibility rule

Status: **CONFIRMED MECHANICAL FINDING**  
Class: `F4`  
Freshness: **no prior disclosure found in searched public issues/PRs/web**  
Legal expert review required: **no**

### Normative rule

`docs/harness.md` states that reproducibility means another party can run the
same evaluation.

Its Rule 6 requires every attempt to retain:

- verbatim answer;
- parameters requested;
- parameters actually applied;
- timestamps;
- sources seen by the system.

Rule 5 additionally says time/token limits must be identical and limit-stopped
or truncated answers must preserve their stop reason.

### Conflicting public example

The same file introduces its suggested JSON record as:

> one answer per line, with enough metadata to reproduce the run.

But the record contains only:

- `task_id`;
- `dataset_version`;
- `system`;
- `run`;
- `answer`.

The published minimal Python harness writes the same five fields.

It does not write:

- requested parameters;
- applied parameters;
- time/token limits;
- stop reason;
- timestamps;
- source set;
- model/provider execution metadata beyond an arbitrary `system` label.

### Why this is an integrity defect rather than style

The omitted fields are not additions invented by this audit.

They are fields the benchmark's **own preceding normative rules** say must be
recorded.

Therefore two reasonable implementations of the same public documentation can
diverge:

1. a reader implements Rule 6 and preserves the full execution boundary;
2. a reader copies the advertised minimal harness/suggested record and does not.

The second record cannot establish whether result-sensitive configuration was
identical or reconstruct which sources/limits were applied.

That directly affects the repository's stated reproducibility contract.

### Materiality

**Material for third-party use of the open-source benchmark.**

It can prevent a competent third party from reconstructing the relevant
evaluation boundary, satisfying the pre-registered materiality rule.

The finding does **not** establish that any published DELTA leaderboard score is
wrong.

### Strongest counterargument

The prose rule is clear and should control over the intentionally small example.

A sophisticated user may also encode configuration behind a versioned `system`
identifier or maintain run metadata elsewhere.

That reduces severity.

It does not remove the documentation contradiction because the example is
explicitly presented as containing enough metadata for reproduction while
omitting data the same page requires.

### Smallest repair

No new platform is needed.

Either:

- expand the suggested record/minimal harness with the required execution
  metadata; or
- label the example explicitly as incomplete and point to a required
  run-manifest schema/checklist.

This audit does not propose implementing that repair in Needle.

---

## 4. Official DELTA report — important counter-evidence and scope boundary

After the repository finding was identified, the current public DELTA Benchmark
Report was inspected as the strongest alternative explanation.

The report describes a larger official evaluation that is **not identical to the
open-source v1.1.0 reproduction contract**.

It states, among other things:

- every model receives the same research instruction, search/source-reading
  tools, time and tool limit;
- a single completed answer per model/question is scored;
- failed/incomplete runs may be repeated;
- GPT-5.6 Sol grades legal/citation criteria in the published evaluation;
- lawyer rulings and approved transfers are applied where available;
- the open-source questions are included, but the public criteria have since
  been refined and **are not identical** to the leaderboard criteria.

Public report:
https://www.legalbenchmarks.ai/research/delta-dutch-legal-research-benchmark

### Consequence

This disclosure prevents an overclaim.

The open-source harness inconsistency cannot honestly be used to say:

> DELTA's published leaderboard is unreproducible because its official runs used
> exactly the incomplete GitHub sample record.

The report uses a different/refined evaluation boundary and explicitly says so.

The fresh finding therefore remains bounded to:

> the public v1.1.0 repository's third-party harness/reproducibility contract.

This boundary materially narrows, but does not erase, F4-01.

---

## 5. Task-by-task audit

### 5.1 Real estate — interpretation of notarial deeds

Exposure: `PREVIEW_EXPOSURE`

Checks:

- prompt ↔ criteria responsiveness;
- binary/gradeable criteria;
- temporal cutoff;
- internal criterion consistency;
- published DELTA report treatment.

Result:

**NO CONFIRMED F1–F5 DEFECT.**

The task asks directly about:

- objective interpretation;
- factual situation at execution;
- address designation at execution;
- same-day deeds.

The detailed criteria elaborate those dimensions.

The current DELTA report independently highlights this same task as an example
of the need to preserve unsettled law around same-day deeds, which supports the
criterion design rather than contradicting it.

No fresh finding retained.

---

### 5.2 Competition law — ACM concentration notification

Exposure: no pre-sample content exposure recorded.

Checks included current authoritative/public material for:

- Article 29 thresholds;
- concentration definition;
- Article 34 notification/standstill structure;
- current ACM published threshold summary.

Current public materials support the main €150m / €30m threshold structure.

The audit considered whether:

- the generic task should require every sector-specific turnover calculation
  example;
- Article 29 versus Article 34 wording creates a citation mismatch;
- standstill wording is overcompressed.

### Result

**NO CONFIRMED F1–F5 DEFECT.**

Some criteria are demanding for a generic question, but DELTA explicitly
benchmarks completeness and legal taste.

The inspected wording did not cross the pre-registered materiality boundary with
sufficient confidence.

No finding retained merely because a shorter competent answer might omit a
benchmark preference.

---

### 5.3 Employment law — inappropriate workplace conduct / transition payment

Exposure: no pre-sample content exposure recorded.

Potential pressure points included:

- the breadth of the `seriously culpable` contextual factors;
- the requirement to address recognisability/employer guidance;
- the criterion requiring acknowledgement that the case-law line is contested
  or requires nuance.

### Result

**NO CONFIRMED F1–F5 DEFECT.**

The task expressly asks whether employer duty-of-care failure affects the
transition-payment analysis.

The criteria are broad, but that breadth aligns with the stated open-ended
research/completeness design.

Calling them defective would require a legal/professional-judgment conclusion
stronger than the available evidence.

No speculative F1 is promoted.

---

### 5.4 Corporate law — director/supervisory-board conflicts

Exposure: `PREVIEW_EXPOSURE`

#### Candidate F2-01 — fallback decision maker omits statutory exception

Status: `CANDIDATE_LEGAL_FINDING`  
Class: `F2`  
Confirmed material: **NO — independent legal review required**

Public criteria S-010/S-011 state, in substance, that when conflict prevents a
board decision the supervisory board decides, and if the supervisory board is
absent / conflicted the general meeting decides.

Current official Book 2 BW text provides the same default chain but expressly
adds:

> `tenzij de statuten anders bepalen`

for the general-meeting fallback.

Authoritative references inspected:

- Book 2 BW Article 2:129(6) / NV management-board conflict route;
- Book 2 BW Article 2:239(6) / BV management-board conflict route;
- Article 2:140(5) / NV supervisory-board conflict route;
- Article 2:250(5) / BV supervisory-board conflict route.

The relevant current text is available via Wetten.nl / Overheid.nl.

### Potential materiality

As written, the public criterion can pass an answer that states the general
meeting fallback categorically while omitting the statutory articles-of-
association exception.

That could reward a materially incomplete proposition about who decides.

### Why it is not counted as experiment success

The pre-registration requires independent qualified Dutch-law review before a
contestable F2/F5 finding is called a confirmed material defect.

No such independent review was obtained in this run.

The statutory text is strong evidence, but this experiment does not relabel
Morrow's own legal interpretation as independent review.

Result remains:

`CANDIDATE_LEGAL_FINDING`

No follow-up legal-review request is manufactured merely to produce a second
positive result.

---

## 6. F3 / generated-data audit

Potential issue:

> derived `data/tasks.jsonl` could drift from the canonical task files.

Result:

**REJECTED AS A FINDING.**

`scripts/validate.py` reconstructs the expected JSONL from all task files and
requires **byte-for-byte equality** with `data/tasks.jsonl`.

The GitHub validation workflow runs that validator on PR and push.

This is a strong boring-baseline control and is recorded as negative evidence.

---

## 7. F4 / judge-setup audit

Potential issue:

> no exact universal judge implementation is fixed in the open repository.

Result:

**NOT RETAINED AS A SEPARATE DEFECT.**

The public judge document intentionally describes a judging contract and requires
publishers to report their judge setup.

The current official DELTA report additionally documents the actual judge models
and human-resolution logic used for its leaderboard.

The existence of a configurable judge setup is therefore not itself a fresh
defect.

Only the narrower harness-record contradiction F4-01 survives.

---

## 8. F5 / temporal-cutoff audit

All four selected tasks record:

`law_as_of = 2026-08-30`.

No selected task produced a sufficiently evidenced fresh case where:

- a required authority post-dated the cutoff;
- a criterion silently used a later legal state; or
- the cutoff was internally contradictory.

### Result

**NO F5 FINDING.**

Do not infer that all 15 DELTA tasks are temporally validated; this result is
limited to the frozen four-task audit.

---

## 9. Freshness check

Before promoting F4-01, public disclosure was searched through:

- open DELTA GitHub issues;
- closed DELTA GitHub issues;
- DELTA pull requests;
- web search for combinations of:
  - harness metadata;
  - reproducibility parameters;
  - record everything;
  - timestamps/sources;
  - token/model settings;
  - judge prompt.

No matching prior public report of F4-01 was found.

This is an absence-of-found-evidence statement, not proof that no private or
unindexed discussion exists.

The known property-law and family-law disputes remain excluded derivation
evidence and receive no fresh-value credit.

---

## 10. Pre-registered success / kill evaluation

### Success condition

At least one fresh, reproducible, material defect/ambiguity that can alter
grading, interpretation, reproducibility or validity.

### Result

**MET, narrowly, by F4-01.**

F4-01 is:

- fresh under the performed public search;
- mechanically reproducible from the frozen repository;
- directly tied to DELTA's own reproducibility requirements;
- capable of preventing faithful reconstruction of a third-party run boundary;
- independent of subjective Dutch-law judgment.

### Kill-rule attack

Could this simply be normal benchmark QA rather than distinct Needle value?

**Yes — this is the strongest counterargument.**

The defect is discoverable by careful documentation review. It does not require a
proprietary Needle method.

What Needle contributed here is narrower:

- the pre-registered audit started from evaluation-integrity failure classes;
- it forced preservation of negative findings;
- it treated execution provenance as a first-class audit target;
- it did not shift to model winners or easier tasks after sample freeze;
- it downgraded the legal finding rather than self-validating it.

That is useful discipline.

One successful documentation/provenance finding does not demonstrate a durable
competitive advantage or a new product category.

---

## 11. Final disposition — REVISE

The broad experimental assumption was:

> Needle's adversarial corpus/evaluation discipline can expose a material,
> previously unrecorded integrity defect in a credible external legal benchmark
> beyond that benchmark's own mature QA/dispute baseline.

The experiment provides one bounded positive instance.

The claim should be revised to:

> **Needle's evaluation-integrity and evidence-closure discipline can transfer
> usefully to external legal evaluation artifacts, particularly for public
> reproducibility/provenance contracts; general distinctiveness beyond strong
> benchmark QA remains unproven.**

### Why not ADOPT_FOR_EXPERIMENT again?

A second benchmark audit would mainly test generality.

There is currently no independent target signal making that the highest-value
next task.

Running another benchmark merely because this one produced a finding would turn
the experiment into a programme.

### Why not REJECT?

The pre-registered materiality threshold was actually crossed once.

Rejecting the transfer entirely would discard real contrary evidence.

### Why not promote a product?

Nothing here establishes:

- user demand for a benchmark-audit service;
- repeated advantage over expert benchmark maintainers;
- willingness to adopt/pay/switch;
- need for audit tooling;
- a general benchmark QA platform.

No product response is earned.

---

## 12. Project consequence

The result strengthens the surviving **protocol/research discipline** identity,
not a product projection.

Recommended canonical state:

- corpus + evaluation protocol remain essential;
- H-18 → `REVISE`;
- keep F4-01 as external evidence of transferability;
- preserve F2-01 as unconfirmed candidate only;
- no new scheduled discovery;
- no benchmark product;
- return to an idle/evidence-triggered state unless Project Health Check finds a
  stronger next question.

## 13. What should happen next

Run the mandatory post-#150 Project Health Check.

Its key question is no longer:

> can Needle find anything in another benchmark?

That received a narrow positive answer.

The next question is:

> does this narrow transfer evidence change the project identity or justify
> further work now?

The default answer should be **no** unless the health check finds concrete
decision-changing evidence.

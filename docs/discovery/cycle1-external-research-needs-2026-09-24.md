# Cycle 1 — external research-needs scan

Issue: #137  
Parent: #134  
Channel: `EXTERNAL_NEED`  
Date: 2026-09-24

## Question

Is there a concrete external legal-research / benchmark / reproducibility job
where Needle's corpus + protocol addresses a problem that current workflows do
not solve well enough?

## Evidence discipline

This scan distinguishes direct/observed need from proxy signals.

The strongest public evidence found is:

- practitioner survey evidence about real legal-AI research failure and
  verification burden;
- public benchmark-maintainer/contributor issues showing criterion, scoring and
  reproducibility defects in working legal benchmarks;
- current research identifying legal temporal-change and benchmark-governance
  problems.

Papers and trend reports are treated as nomination evidence, not demand.

No claim is made that an external user has requested Needle itself.

---

## Candidate need A — adversarial audit of legal benchmark validity

### Evidence level

**Level 4: public issues/disputes showing attempted benchmark use and concrete
friction**, independently repeated across two benchmark projects.

### DELTA evidence

DELTA v1.1.0 is already unusually disciplined:

- real practitioner tasks;
- `law_as_of` per task;
- fixed harness prompt;
- full-set/two-run guidance;
- record-everything requirement;
- separate judge protocol;
- cross-family judges;
- human escalation;
- semantic versioning;
- public criterion-dispute workflow.

Despite those controls, two current public disputes were filed after external
benchmark use.

**DELTA issue #1 — property-law criterion S-005**

The reporter shows a substantive authority defect: the criterion attributes the
legal function of Article 3:97(1) BW to paragraph 2. The practical effect is
inverted grading: a legally correct answer can fail while the misattribution can
pass.

Source:
https://github.com/legalbenchmarks/delta/issues/1

**DELTA issue #2 — family-law criterion S-009**

The reporter shows a gradability defect. The criterion is conditional on an
argument the prompt does not elicit; across five models the condition never
appeared. Two judge families then resolve the vacuous criterion differently.

Source:
https://github.com/legalbenchmarks/delta/issues/2

These are especially relevant because DELTA's CONTRIBUTING contract already
requires legal review, criterion verifiability and controlling authority where
appropriate. The defects therefore survived a credible baseline process.

### LegalBench evidence

Public LegalBench issues show a separate class of benchmark-integrity failures.

**Issue #56** reports reproducible scorer/data defects, including:

- a correct SSLA answer receiving only 0.8;
- empty references accepting arbitrary predictions;
- scorer behavior diverging from task documentation;
- identical OPP-115 inputs carrying conflicting labels;
- decimal parsing reversing SARA outcomes;
- citation scoring silently ignoring missing predictions.

Source:
https://github.com/HazyResearch/legalbench/issues/56

**Issue #55** documents a reproducibility/configuration failure in which
reasoning/chat models can score near zero because an apparently reasonable
generation budget truncates reasoning before the answer, with no benchmark
error.

Source:
https://github.com/HazyResearch/legalbench/issues/55

**Issue #31** is an older but direct reproduction request asking for model
outputs and guidance on comparing verbose generations with ground truth. The
maintainers explain that most tasks rely on tightly controlled terse outputs and
that open-ended generations were manually evaluated.

Source:
https://github.com/HazyResearch/legalbench/issues/31

### External context

Guha et al. (PNAS, 2026), *There is No Free Benchmark*, argues that legal AI
benchmarking has institutional-design risks around transparency, objectivity,
expertise and resources rather than a single universally correct benchmark
design.

Reference:
https://scholarship.law.columbia.edu/faculty_scholarship/4866/

This is context, not direct demand.

### User/research job

> When publishing or relying on a legal-AI benchmark, a benchmark maintainer or
> researcher needs confidence that task criteria, scorers and execution
> boundaries do not create materially wrong or irreproducible results, so that
> reported model differences reflect the tested system rather than benchmark
> defects.

### Strongest boring baseline

The strongest baseline is not weak.

DELTA already provides:

- legal-practitioner review;
- criterion-level authority expectations;
- explicit dispute handling;
- dataset versioning;
- multi-judge evaluation;
- human disagreement escalation;
- fixed harness guidance.

LegalBench is open-source and exposes scoring/data logic for community review.

The relevant question is therefore **not** whether benchmark auditing is useful.
It plainly is.

The question is whether Needle's adversarial discipline can expose a material
defect that these existing controls miss *without* becoming another benchmark
platform.

### Needle-specific possible contribution

Needle already has reusable discipline around:

- falsifiable failure hypotheses;
- strongest-baseline comparison;
- derivation versus validation evidence;
- pre-registration before scored execution;
- source/evidence ownership;
- construct-validity attack;
- preservation of negative/parity results;
- explicit stop rules.

That could be applied to the **benchmark itself as the object under test**.

The potentially distinctive move is not another scoring framework. It is a
bounded adversarial audit asking:

> What benchmark defect would materially falsify the interpretation of a
> published result, and can we find it before looking for model winners?

### Counter-evidence

The public disputes themselves prove the adjacent ecosystem can identify and
repair benchmark defects without Needle.

Open-source code review, domain experts, versioning and ordinary issue workflows
may be entirely sufficient.

Needle risks simply rebranding good benchmark QA as a proprietary method.

Known public defects cannot be used as fresh evidence that a Needle audit detects
unknown defects; they are **DERIVATION evidence** for what an audit should look
for.

### Riskiest assumption

That a small Needle-style adversarial audit can find a **material, previously
unrecorded benchmark-integrity defect or ambiguity** that the benchmark's own
documented QA baseline has not already surfaced.

### Smallest credible experiment

Do not build tooling.

If #139 authorises the experiment:

1. choose one current public legal benchmark version;
2. exclude tasks/criteria already named in public defect/dispute issues used
   here;
3. pre-register a small fixed audit sample before inspecting model leaderboard
   outcomes;
4. audit only for a bounded set of failure classes:
   - criterion not falsifiable/gradeable from the answer;
   - criterion/source mismatch;
   - scorer/documentation mismatch;
   - result-sensitive execution configuration missing or ambiguous;
   - temporal/legal-cutoff ambiguity;
5. classify findings before examining whether they change any model ranking or
   provider result;
6. compare against the benchmark's own contribution/dispute/validation rules.

For legal-correctness findings that require contestable interpretation, an
independent qualified domain reviewer is required before calling the finding
material. Mechanically reproducible scorer/harness defects do not need legal
expertise.

### Kill rule

Reject this opportunity as distinct Needle value if the fresh bounded audit:

- finds no material previously unrecorded defect/ambiguity; or
- finds only style/preferences already handled by the benchmark's dispute
  process; or
- requires effectively recreating the benchmark's own maintainer/reviewer
  workflow to produce value.

### Candidate disposition

**ADOPT_FOR_EXPERIMENT**, but only as a bounded external-benchmark audit
experiment after Cycle 1 synthesis.

No benchmark platform, adapter, judge, leaderboard or standing audit service is
authorised.

---

## Candidate need B — faster verification/auditability of AI legal research

### Evidence level

**Level 3: repeated independent practitioner evidence from a structured survey**,
but not a direct request to Needle.

The 2026 Dutch Legal AI Adoption Survey reports 115 legal professionals across
19 organisations and 11 practice areas.

Key observed signals:

- 63.5% use AI for legal research daily;
- 67.8% say the first answer is usable half the time or less;
- 82.6% rate invented/incorrect law, facts or citations as a serious failure;
- 72.2% rate outdated, irrelevant or wrong-jurisdiction sources as serious;
- 68.7% rate unsupported claims/no source as serious;
- 45.2% would first hand case-law research to AI.

The report's own takeaway is that auditability and verification should be core
evaluation criteria, and that the path from an AI answer to verified legal work
needs to become faster and clearer.

Reference:
https://www.legalbenchmarks.ai/research/dutch-legal-ai-adoption-survey

### Job

> When using AI for legal research, a lawyer needs to verify that authorities
> exist, apply to the question, are current/relevant and actually support the
> conclusion before relying on the answer.

### Why this looks attractive to Needle

Needle's research history is rich in exactly these failure mechanisms:

- source-state back-projection;
- status/application confusion;
- stale official trackers;
- judicial/text divergence;
- private-origin/legal-recognition confusion;
- temporal boundaries;
- evidence lineage.

The Corpus Explorer also exposes decisive traps and durable evidence owners.

### Strongest boring baseline

For actual legal work, the strong baseline is still direct verification in
official sources plus competent legal review.

Needle does not currently accept arbitrary AI answers, resolve their citations,
or act as a legal-research verification application.

Turning this need directly into a product would recreate the stopped broader
legal product and outrun the evidence.

### Counter-evidence

The survey establishes a real problem, not that Needle is the preferred or
necessary solution.

Commercial legal research systems, source-grounded models and ordinary lawyer
verification already compete directly on this job.

Needle's current unique value is a corpus/protocol for *studying failures*, not a
workflow product for verifying arbitrary legal advice.

### Disposition

**REVISE / do not promote as a product opportunity.**

Preserve the survey as external evidence that Needle's adversarial failure
families correspond to professionally serious errors.

A later external user study could test whether the Explorer/corpus helps people
*learn or audit failure patterns*, but this scan does not justify building a
verification product.

---

## Candidate need C — temporal robustness under changing law

### Evidence level

**Level 5: current research literature / benchmark design evidence.**

Recent projects show explicit concern with changing law:

- DELTA records `law_as_of` for every task;
- LawShift (NeurIPS 2025) benchmarks legal judgment prediction under statutory
  revisions;
- LexKairos (2026) benchmarks legal temporal capability across statutes, cases
  and temporal reasoning;
- Needle itself already contains multiple temporal/source-state failure classes.

References:

- https://github.com/legalbenchmarks/delta
- https://papers.nips.cc/paper_files/paper/2025/hash/adf82a0a1d52d93961476458b9566a2b-Abstract-Datasets_and_Benchmarks_Track.html
- https://arxiv.org/abs/2608.09106

### Counter-evidence

This is clearly a research topic, but adjacent benchmarks already target it
directly.

No external signal found asks for Needle's temporal representation or protocol.

### Disposition

**REJECT as a distinct external-need opportunity.**

Use these projects as adjacent precedent, not evidence to build another temporal
benchmark.

---

## Candidate need D — generic benchmark interoperability / leaderboard access

### Evidence level

**Level 4/5**, but the demonstrated need is already served by existing benchmark
ecosystems.

LegalBench public issues include requests for outputs, leaderboard information,
evaluation instructions and external export formats.

That demonstrates normal benchmark-consumption friction, not a Needle-specific
problem.

Issue #116 already parked generic interoperability because a lossless mapping
would either discard Needle semantics or recreate them as custom extensions.

### Disposition

**REJECT.**

The new scan provides no evidence strong enough to reopen #116.

---

## Evidence-ranked conclusion

| Rank | External need | Evidence strength | Needle distinctiveness | Disposition |
|---|---|---|---|---|
| 1 | Benchmark criterion/scorer/execution integrity | repeated public concrete defects across DELTA + LegalBench | plausible but unproven | **ADOPT_FOR_EXPERIMENT** |
| 2 | Verification/auditability of AI legal research | repeated practitioner survey evidence | problem strong, Needle solution weak | **REVISE** |
| 3 | Temporal robustness under changing law | active research literature | already served by adjacent work | **REJECT** |
| 4 | Generic interoperability/leaderboards | public workflow requests | no distinct Needle value | **REJECT** |

## Cycle-level interpretation

This channel produced one evidence-backed research opportunity, but **no product
opportunity**.

The result does not support reviving Full Needle, creating a benchmark platform,
or turning the Explorer into a legal verification application.

The strongest opportunity is narrower and somewhat surprising:

> **Can Needle's adversarial evaluation discipline function as a useful
> red-team/audit protocol for an already well-designed legal benchmark?**

That question is falsifiable and has a strong incumbent baseline to beat.

## Final disposition

**ADOPT_FOR_EXPERIMENT**

Retain a bounded **external legal-benchmark adversarial audit** as the sole
surviving #137 opportunity.

Do not execute it before #139 decides whether Cycle 1 evidence justifies the
experiment.

Known DELTA/LegalBench defects in this note are derivation examples only. A future
experiment must use a fresh, pre-registered sample and cannot claim value by
rediscovering these public issues.

# Issue #375 — Needle historical evaluation-contract integrity audit

Date: 2026-09-26  
Mode: **REVIEW — DOGFOOD EVALUATION-CONTRACT INTEGRITY**

## Purpose

Apply the evaluation-contract integrity gate earned from public DELTA/Harvey maintenance failures back onto three preselected Needle evaluations:

- #88 — surfaced-trap adversarial gate;
- #214 — latent index-assisted corpus workflow pilot;
- #362 — paired temporal-oracle incremental-value falsifier.

No experiment was rerun. No new case was selected. No historical result was changed merely because the project now has stricter standards.

The audit asks whether the surviving claim and evidentiary weight remain justified.

## Gate

The current integrity gate checks:

1. task-to-criterion coverage;
2. criterion evidence correctness;
3. activation and gradability;
4. cross-criterion consistency;
5. execution validity before subject failure;
6. semantic revision control;
7. stability decomposition when decision-sensitive.

A separate practical question is also recorded:

> can a future reviewer independently inspect the exact scored inputs/outputs from the canonical repository?

That is an auditability question, not a new winner metric.

---

# #88 — surfaced-trap adversarial gate

## Current claim

After #95's construct repair:

> six fresh sealed SURFACED_TRAP_ADJUDICATION pairs were R-pass/M-pass; once the decisive trap was surfaced or strongly cued, Needle Method produced no correctness rescue over the strong source-grounded baseline.

## Integrity findings

### Task-to-criterion coverage — PASS

The revealed prompts and answer keys align on the decision-critical question in all six cases.

The answer keys explicitly identify:
- correct conclusion;
- consequential failure;
- decisive evidence;
- grading boundary/notes.

The keys are prose rather than atomic criterion arrays, but the central requested distinction and consequential failure condition are covered.

### Criterion evidence correctness — PASS / historical spot-audit level

The keys identify concrete legal evidence owners rather than generic subject labels, including exact corrigenda, DSA Article 33(6), Decision (EU) 2025/1457, ETS verification/registry provisions, and Implementing Regulation 2016/1239 Article 3(1).

No internal mismatch analogous to the external DELTA wrong-paragraph defect was found in the stored contract.

This audit did not redo six full legal opinions from scratch.

### Activation / gradability — PASS

The key does not contain a condition whose inactive case is undefined.

Each prompt asks for the distinction on which the key grades the answer.

That fact is also why #95 narrowed the construct from latent detection to surfaced adjudication.

### Cross-criterion consistency — PASS

No contradictory counts, answer states, timing rules or alternative criteria were found.

### Execution validity — PASS

The original Windows runner failed before any investigator response.

The transport repair was disclosed, limited to UTF-8 HTTP transport, and followed by prompt-hash verification against the sealed packet.

Infrastructure failure was not scored as subject failure.

### Semantic revision control — PASS

Prompt/key hashes were committed before execution and the revealed artifacts match the committed hashes.

#95 changed the interpretation of the experiment, not its historical prompts/results.

### Stability decomposition — LIMITATION, NOT RESULT REVERSAL

One run per arm/case does not estimate generation variance.

The project never claimed population equivalence.

For the narrow observed six-pair result this is a sampling limitation rather than a contract defect.

### Repository auditability — PARTIAL

The repository contains:
- exact revealed prompts;
- exact revealed answer keys;
- prompt/key commitments;
- result classifications;
- output SHA-256 values.

It does not contain the raw investigator output bodies themselves.

A future reviewer therefore cannot reconstruct the complete grading solely from GitHub.

## Disposition

> **RESULT PRESERVED — CONSTRUCT REPAIRED — OUTPUT ARCHIVE INCOMPLETE**

The #88 parity claim remains usable within its repaired surfaced-adjudication scope.

Do not describe it as latent detection evidence or as fully repository-reproducible.

---

# #214 — latent index-assisted corpus workflow pilot

## Current claim

> Offering the frozen adversarial index + fixed adversarial-use instruction produced zero diagnostic rescues on the sealed 3+1 pilot; latent corpus-workflow value was not demonstrated under the frozen conditions.

## Integrity findings

### Task-to-criterion coverage — NOT INDEPENDENTLY RE-AUDITABLE FROM REPOSITORY

The #210 design defines the scoring dimensions very well:

- consequential correctness;
- demonstrated decisive distinction;
- unsupported certainty;
- control complication.

It also defines diagnostic rescue precisely.

However, the exact post-execution plaintext investigator package, evaluator package / keys, and eight raw investigator outputs are not preserved in repository files.

The repository contains pre-execution SHA-256 commitments and a detailed grading summary, but not enough plaintext to independently replay task-to-key coverage.

### Criterion evidence correctness — NOT INDEPENDENTLY RE-AUDITABLE

The grading comment records task-specific legal conclusions and says the sealed keys owned them.

Because the evaluator package is absent from the repository, a future reviewer cannot verify every exact authority/key relation from GitHub alone.

### Activation / gradability — DESIGN PASS

The frozen scoring contract itself is strong.

Diagnostic rescue requires:
1. a pre-sealed consequential R error;
2. C avoids it;
3. C explicitly/evidentially identifies and applies the hidden distinction.

Correctness-only differences and generic caution are separately handled.

No vacuous conditional scoring rule is apparent in the design.

### Cross-criterion consistency — RECORDED RESULT CONSISTENT

The published grading table and pair summary reconcile:
- three adversarial parity pairs;
- one control parity pair;
- zero diagnostic rescues;
- zero correctness-only C advantages;
- zero C-only regressions;
- zero material C-only control complications.

The hidden package cannot be independently checked for deeper internal consistency.

### Execution validity — PASS WITH DISCLOSED PRE-RUN TRANSPORT REPAIR

A local manifest export mismatch was corrected before any investigator run.

The canonical precommitted execution-manifest hash remained unchanged.

No subject result was generated by the broken export.

### Semantic revision control — STRONG

The design, treatment corpus blob, compiler-return hashes, investigator/evaluator package hashes and execution manifest were frozen before output.

This is one of #214's strongest features.

### Stability decomposition — MATERIAL LIMITATION

#210 explicitly accepted one run per arm/task and acknowledged that it could not estimate generation variance.

The grading was also a single contemporaneous evaluator pass rather than a preserved repeatable multi-judge/human-adjudication artifact.

Under the current integrity standard this limits confidence in the exact zero-rescue count, because a changed grading decision on one R/C pair could convert zero into one signal.

Importantly, the frozen #210 rule said:
- 0 rescues -> value not demonstrated / contract;
- 1 rescue -> signal only, no project-identity promotion;
- 2–3 rescues -> independent replication only.

Therefore this limitation weakens the precision and external auditability of the phrase "hard null", but does not by itself justify reviving the former product/workflow claim.

### Repository auditability — MATERIAL GAP

The result document explicitly states that outputs were pasted into sponsor chat rather than uploaded as files.

The repository therefore cannot independently attest or regrade the exact output bytes.

The plaintext sealed evaluator package is likewise not present after reveal.

## Disposition

> **BINDING BOUNDED NEGATIVE RESULT — REPOSITORY REPRODUCIBILITY LIMITED**

Keep H-24 rejected for project allocation.

Prefer this wording over an unqualified "hard null":

> #214 is a strong pre-registered negative result under its tested conditions, with a material repository-level reproducibility limitation because exact keys/raw outputs are not preserved as GitHub artifacts.

Do not rerun the exposed experiment merely to improve archival quality.

---

# #362 — paired temporal-oracle incremental-value test

## Current claim

> An externally defined Shifted versus Stable ChronoLex-TW condition did not predict the residual legal/oracle structure that would earn Needle, and excellent ordinary evaluator-maintenance practice absorbed all material value on the two selected rows.

## Integrity findings

### Task-to-criterion coverage — PARTIAL

The issue predeclares what counts as a material Needle delta:
- expected answer/oracle;
- admissible authority/version;
- consequential opposite-error boundary;
- future regression PASS/FAIL conditions;
- reuse status that changes future use.

This is substantially better than an undefined helpful/not-helpful judgment.

But the primary directional proposition — Shifted should leave more consequential reusable structure than Stable — does not have an executable or independently scored threshold for "more".

It remains expert comparative judgment.

### Criterion evidence correctness — REPOSITORY PROVENANCE GAP

Stage A records actual exam dates, relevant statutes/articles, procedural dependencies, official answers and Supreme Court doctrine for the Stable control.

It does not preserve exact source URLs/versions/case identifiers for the decisive Taiwanese legal propositions in the durable artifact.

A current external spot check can recover official examination repositories, but that is not equivalent to preserving the exact sources used at Stage A.

Therefore the legal reconstruction is not independently auditable to Needle's new standard from the repository alone.

### Activation / gradability — PARTIAL

The yes/no artifact and discipline deltas are clear enough to record.

The directional "more residual structure" comparison is not mechanically gradable.

### Cross-criterion consistency — PASS AT RECORDED LEVEL

The selection rule, Stage A observations and Stage B outcome do not contradict one another.

The Shifted/Stable pair was preserved even though the external proxy ordered them poorly.

### Execution validity — NOT A HARNESS RUN

No evaluator infrastructure failure was converted into subject failure.

This was a manual USE comparison rather than a model benchmark execution.

### Semantic revision control — STRONG SEQUENCE, WEAK ARTIFACTIZATION

The issue comments establish the order:
1. row IDs frozen;
2. Stage A frozen without Needle;
3. Stage B consulted Needle.

That sequencing is good.

The Stage-A source/evidence state was preserved as prose comments rather than a source-complete immutable artifact.

### Stability / independent adjudication — MATERIAL LIMITATION

The same project operator selected under the mechanical rule, performed the legal reconstruction, judged residual structure and applied Needle.

There is no independent legal adjudicator or repeat scorer.

For a subjective "material delta" endpoint, the current integrity standard would require stronger independent scoring before treating the result as high-grade experimental evidence.

## Disposition

> **DIRECTIONALLY USEFUL ALLOCATION EVIDENCE — NOT HIGH-GRADE FALSIFIER**

Preserve:
- the mechanically selected pair;
- the fact that Shifted did not automatically imply answer-determinative temporal complexity;
- the warning against choosing another friendlier proxy post hoc.

Downweight:
- the claim that #362 independently establishes that excellent practice fully absorbs all possible Needle evaluator value.

The broader #366 contraction does not need to be reversed solely because #362 is downweighted. It also rests on #214, #327, #349, the mixed #339/#353 evidence, #359/#361's own contraction, and absence of demonstrated external demand/artifact dependence.

---

# Cross-evaluation conclusion

## What survives strongly

1. Needle's anti-tuning / pre-registration culture is genuinely load-bearing.
2. #88 remains valid after its explicit construct repair.
3. #214 remains strong negative allocation evidence, but not fully repository-reproducible.
4. The project was right not to promote product/workflow superiority from these results.

## What needed correction

1. **Artifact preservation was weaker than experiment design.** Hashing hidden packages is not enough if the revealed package/raw outputs are never archived after execution.
2. **Negative results were sometimes described with more certainty than their durable auditability supports.**
3. **Manual USE comparisons such as #362 need an explicit distinction between decision-support evidence and high-grade comparative evaluation.**

## New durable rule

For future decisive evaluations, after the blind phase ends preserve in the canonical repository, subject to legitimate confidentiality constraints:

- exact revealed task prompts;
- exact revealed answer/evaluator keys;
- raw evaluated outputs or an immutable permitted archive reference;
- exact score/adjudication record;
- exact source/evidence owners needed to validate the key;
- task-contract version/commit;
- execution failures separately from subject failures.

If confidentiality prevents repository storage, record:
- where the immutable evidence lives;
- who can independently access it;
- what hash identifies it;
- which claims cannot be independently audited without that access.

Do not call a result fully reproducible when only hashes and summaries survive.

## Project-level effect

No historical scientific result is reversed in this audit.

But evidence weights are corrected:

- #88: **preserved, construct-repaired, partial output archival**;
- #214: **binding bounded negative, repository reproducibility limited**;
- #362: **directionally useful allocation evidence, downweighted as a falsifier**.

The current smaller Needle identity remains supported.

The pre-partner honing campaign has therefore improved not only future benchmark hygiene, but the honesty of Needle's own evidence hierarchy.

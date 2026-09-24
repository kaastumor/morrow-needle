# #203 result — LegalBench OPP-115 consequential corpus-use diagnostic

Date: 2026-09-24  
Issue: #203  
Parent design: #200  
Claim type: `PRODUCT_WORKFLOW / DIAGNOSTIC_REVIEW`  
Primary outcome: `VERIFIED_SCORING_DISPOSITION`

## Frozen execution

The sponsor executed the two frozen arms in separate fresh chats and returned both
complete outputs to the contaminated design session.

Exact returned outputs are preserved verbatim in Issue #203:

https://github.com/kaastumor/morrow-needle/issues/203#issuecomment-5819844367

The project cannot independently verify the consumer UI/model settings of those
fresh chats. That execution-provenance limit is retained.

Both arms respected the declared 12-substantive-external-inspection ceiling in
their own reports. Arm C additionally reports three Needle treatment-artifact
reads.

## Observed dispositions

Arm R:

> `INDETERMINATE / QUARANTINE`

Arm C:

> `INDETERMINATE / quarantine`

Both independently recommended the same safe repository/scoring action:

- exclude all six members of the three contradictory identical-input pairs from
  ordinary scoring;
- preserve the original rows and labels for audit/provenance;
- do not invent a winning label;
- do not provenance-collapse the rows without a trustworthy row→OPP source map;
- do not retain opposite labels as ordinary independent ground truth when the
  scored prompt exposes no distinguishing context.

Arm C explicitly states that the Needle treatment supplied no fact capable of
selecting a label, no proof that a pair is the same source segment and no
task-specific trap-class reason. Its stated contribution was only reinforcement
of a conservative provenance posture already supported by the public benchmark
evidence.

## Frozen grading — correction after red team

The first-pass design-session interpretation was too aggressive in calling the
run `R PASS / C PASS -> PARITY`.

That is not the frozen rule the project wrote.

Issue #203 says:

- `PASS` when the consequential disposition is verified under the available
  primary evidence;
- `INDETERMINATE` when primary source/provenance access cannot verify the
  disposition;
- `both INDETERMINATE -> unresolved`.

Both workers themselves reported `INDETERMINATE` because the original OPP-115
row-level provenance could not be reconstructed reliably.

Therefore the canonical frozen score is:

# **UNRESOLVED — BOTH ARMS INDETERMINATE**

The shared quarantine recommendation is meaningful **operational convergence**.
It is not upgraded into frozen-score parity after the fact.

## Red-team findings

### 1. The prompt surfaced the conservative failure rule

Both arms were explicitly told:

> if primary provenance cannot be reconstructed reliably, preserve that as
> INDETERMINATE and prefer quarantine over arbitrary relabelling.

The experiment therefore does not test whether Needle causes a worker to
discover that provenance-safe posture unprompted.

It tests whether adding the current corpus/protocol treatment changes the
consequential disposition **after the key evidence-integrity boundary is already
surfaced**.

That sharply narrows any negative inference about corpus usefulness.

### 2. Public evidence budgets were equal, but exact source choices differed

Arm R and Arm C each report 12 substantive external inspections, but they did not
open an identical source list.

That is allowed by the frozen design, which equalised access and budget rather
than prescribing exact source paths. It does, however, prevent fine-grained
causal claims about source efficiency or reconstruction burden.

No such secondary claim is made.

### 3. Execution settings are sponsor-reported, not machine-attested

The returned outputs are preserved, but the repository does not independently
prove:

- Temporary Chat state;
- exact model/capability tier;
- reasoning setting;
- absence of hidden personalization.

This is the same type of manual-execution provenance limitation already retained
for earlier consumer-UI experiments.

### 4. The treatment tested the current corpus/protocol, not every possible Needle form

Arm C received exactly the current treatment frozen by #203:

- the corpus index;
- the adversarial-corpus protocol;
- the #150 historical calibration result.

The run therefore says nothing about a hypothetical future task-specific tool,
ontology, retrieval layer or product. Those forms do not receive positive credit
either.

### 5. Quarantine is safer than relabelling, but source truth remains unresolved

Both arms give a strong interface-level reason not to score opposite labels on
identical exposed prompts as ordinary independent ground truth.

They do not establish whether the original source cause was:

- duplicate extraction;
- identical text from distinct policies/segments;
- divergent original annotation/consolidation;
- another transformation artifact.

So the benchmark repair is safely bounded to quarantine pending provenance
reconstruction.

## Claim result

Question:

> Does access to Needle's current adversarial corpus/evaluation discipline improve
> the consequential scoring/repository disposition over competent ordinary
> source-linked QA on this real unresolved benchmark conflict?

Observed:

- no Arm-C-only disposition;
- no Arm-C-only public-evidence fact;
- no Arm-C-only avoided consequential error;
- both arms stop at the same quarantine action;
- both remain provenance-indeterminate.

Because the frozen score is unresolved, this is **not** a formal parity proof.

It nevertheless supplies **no positive evidence** for a corpus-specific
diagnostic wrapper on this job.

## #203 disposition

# **PARK**

Reason:

- the one allowed two-arm execution is complete;
- frozen grading remains unresolved;
- no third attempt, repaired prompt or easier benchmark defect is allowed;
- the current corpus treatment did not demonstrate a consequential advantage;
- ordinary source-linked QA remains the default for this surfaced benchmark
  conflict.

Re-entry requires genuinely new external evidence that changes the decision
boundary, not another attempt to obtain a preferred arm difference.

## Project consequence

Do not build:

- a benchmark-diagnostic product;
- a corpus-specific OPP-115 repair workflow;
- a new trap class from this case;
- another LegalBench comparison to seek a win.

Keep:

- the corpus as an adversarial/regression research asset;
- the evaluation protocol;
- provenance-safe abstention/quarantine discipline;
- the negative/unresolved result.

The current project identity survives, but benchmark-diagnostic distinctiveness
remains unproven.

Next project direction is chosen separately by the post-#203 Project Health
Check.

# Adversarial corpus evaluation protocol v0.1

Status: **CANONICAL EVALUATION PROTOCOL**

Purpose: evaluate legal-research claims without allowing case selection,
prompting, hidden state or post-result reinterpretation to manufacture an
advantage.

This generalises the discipline proven in Issues #87 and #88. It is intentionally
smaller than either historical experiment.

## 1. Start with a claim that can lose

An evaluation begins with a falsifiable project or method claim, for example:

- a workflow prevents a specific consequential error;
- persistence preserves state that a non-persistent handoff loses;
- a source-selection rule avoids a known category of false inference.

Define the alternative outcome before selecting or running the case.

A test that cannot reduce confidence in the tested claim is not an evaluation.

## 2. Separate derivation from validation

A case that helped discover a failure mechanism is `DERIVATION` evidence.

It may be used for:

- explanation;
- regression;
- implementation tests;
- calibration;
- training humans on the trap.

It must not count as fresh blind validation of that same mechanism.

A validation case must be selected independently because it instantiates a
pre-existing failure class, not because the comparator has already failed it.

## 3. Declare the evaluation mode

Every comparative evaluation must declare one mode **before sealing**.

### SURFACED_TRAP_ADJUDICATION

Use this when the task explicitly identifies or strongly cues the dangerous
distinction.

This tests whether the investigator can resolve an already surfaced issue
correctly.

A pass in this mode is evidence about adjudication, not about whether the same
investigator would have noticed the problem unprompted.

### LATENT_TRAP_DETECTION

Use this when the realistic task does not identify the hidden failure
mechanism.

This tests whether the investigator notices the issue before giving a
consequential answer.

For this mode:

- do not name the failure class in the investigator prompt;
- do not instruct the investigator to make the decisive distinction;
- do not insert evaluator-authored hints merely to make scoring easier;
- preserve facts that a real user/task would naturally provide;
- pre-register what counts as detection, missed detection and safe abstention.

If the question itself reveals the trap, classify the run as
`SURFACED_TRAP_ADJUDICATION`. Do not retroactively call it latent detection
because the underlying legal issue was obscure.

Issue #88 is canonical calibration: all six cases are
`SURFACED_TRAP_ADJUDICATION`.

## 4. Seal before execution

Before any scored/decisive run:

- freeze the exact case question;
- freeze the expected decisive conclusion and consequential failure condition;
- freeze arm instructions;
- freeze model/version, reasoning effort and source/tool access;
- freeze the outcome interpretation rule;
- commit cryptographic hashes of hidden artifacts;
- keep plaintext hidden from investigators until execution completes.

Changing any scientific input after observing an arm result requires a new
experiment/version.

Transport-only repairs are permissible only when:

- no investigator/model response was produced by the failed attempt;
- sealed scientific inputs remain byte-identical;
- the repair is documented;
- successful-run prompt hashes can be reconciled to the commitment.

## 5. Use a strong comparator

The baseline should be the strongest boring workflow a competent user would
actually use, not an intentionally weak strawman.

When testing a method wrapper:

- use the same model family/version where possible;
- use the same reasoning effort;
- give the same source/web access;
- vary only the method instruction being tested.

When capabilities cannot be equalised, record the asymmetry before execution
and do not attribute the difference solely to the tested method.

## 6. Score consequential behaviour, not aesthetics

Primary outcomes should be concrete failure events such as:

- wrong legal conclusion;
- historical/current state inversion;
- scope leakage;
- status/application confusion;
- language-expression projection;
- source-origin/authority confusion;
- temporal-boundary loss;
- unsupported certainty where abstention is required;
- inability to support the decisive claim.

Do not award a win merely for:

- longer answers;
- more headings;
- more citations;
- source reopening;
- cleaner prose;
- machine-readable formatting.

Those may be recorded descriptively if operationally relevant.

## 7. Interpret outcomes before seeing them

For a two-arm baseline R versus tested method M:

- **R fail / M pass** — evidence for the tested method on that failure class;
- **R pass / M pass** — parity for correctness on that case;
- **R fail / M fail** — the method does not solve the failure class;
- **R pass / M fail** — evidence against the method.

Do not add a new winner metric after seeing the results.

These are case-level observations under the frozen execution conditions.
All-pass pairs do not establish population equivalence, general reliability or
results for another model/tool setup. A preregistered investment stop remains
valid without claiming statistical equivalence. State sample-selection,
independence and blinding limits separately; a fresh session does not establish
that a case was unseen during training.

## 8. Stop instead of moving the goalposts

If the pre-registered suite produces parity, preserve the parity.

Do not search post hoc for a harder case until the tested method wins and then
append it to the same experiment.

A later experiment may legitimately target a different hypothesis, but it must
be pre-registered as a new gate.

## 9. Reveal and retire from blind use

After all intended runs:

- verify sealed hashes;
- reveal exact questions/answer keys;
- preserve all arm results, including embarrassing ones;
- update the corpus index;
- mark every revealed case `blind_reuse=false` and
  `future_use=REGRESSION_ONLY`.

Time passing, a new conversation, or a new model release does not make a public
case blind again.

## 10. Legal/source drift

A case may remain valuable even when the law later changes, but the evaluation
must identify its temporal perspective.

Before reusing a regression case:

- verify that referenced artifacts still exist;
- distinguish historical truth at the original cutoff from current law;
- do not silently replace the old answer key with a current-law answer.

If the intended question changes materially, create a new case ID.

## 11. Model-version comparisons

A corpus run on one model version does not establish performance for another.

For longitudinal comparison:

- use the same revealed regression cases only as regression evidence;
- preserve model/version/tool settings;
- do not call the exercise blind;
- use fresh sealed cases for new claims of generalised superiority.

## 13. Evaluation-contract integrity

Before trusting a benchmark, regression result or comparative score, validate the **evaluation contract itself**.

A legally plausible answer key is not enough. The task, criteria, evidence, execution path and
version must jointly support the meaning assigned to PASS/FAIL.

At minimum check:

1. **Task-to-criterion coverage**
   - every decision-critical deliverable or proposition requested by the task has an
     observable criterion;
   - a response that omits the central requested work must not be able to all-pass merely by
     satisfying peripheral criteria;
   - where practical, use a deletion/mutation check: remove a required central element from
     an otherwise acceptable answer and confirm that at least one criterion fails.

2. **Criterion evidence correctness**
   - legal criteria must be supported by the exact controlling authority/evidence owner they
     claim to test;
   - verify article/paragraph/subparagraph identity where the distinction changes the rule;
   - do not treat a nearby correct source as support for the wrong proposition.

3. **Activation and gradability**
   - every criterion must have a determinate result for the outputs the task permits;
   - if a criterion is conditional, specify what happens when its trigger does not occur;
   - a criterion that is substantively true but vacuous for the task is not a valid grading
     contract until its inactive case is defined.

4. **Cross-criterion consistency**
   - counts, denominators, allowlists, thresholds, required/optional/negative sets and other
     shared facts must reconcile across criteria;
   - where several criteria derive from the same underlying truth, prefer one typed owner or
     an explicit consistency check over duplicated hand-maintained literals.

5. **Execution validity before subject failure**
   - extraction, conversion, tool, harness or judge-input failures must surface as
     `INVALID_RUN`, `UNSCORABLE` or an equivalent explicit evaluation failure;
   - infrastructure failure must not be silently converted into a confident FAIL for the
     evaluated subject.

6. **Semantic revision control**
   - changes to instructions, criteria, answer keys, required deliverables or other
     score-bearing fields are changes to the effective task contract;
   - pin the exact contract version/commit for every result;
   - do not compare scores across materially changed contracts as though only the evaluated
     system changed.

7. **Stability decomposition when the decision is sensitive**
   - distinguish answer/system variance from judge variance;
   - where a small score difference could change a project or release decision, freeze an
     identical output and repeat judging before attributing the delta to the subject;
   - preserve judge disagreements and human adjudication rather than averaging instability
     into false certainty.

### Post-reveal preservation

After a blinded/sealed evaluation is complete, preserve enough of the revealed execution
record for an independent future audit.

Subject to legitimate confidentiality constraints, archive:

- exact task prompts;
- exact answer/evaluator keys;
- raw evaluated outputs;
- score/adjudication records;
- exact decisive source/evidence owners;
- task-contract version/commit.

If raw material cannot live in the repository, record the immutable archive location,
access boundary and identifying hash, and state which claims cannot be independently
re-audited without that archive.

A hash commitment proves later bytes match earlier bytes only when the committed bytes are
eventually available to the authorised auditor. A hash plus a prose summary is not by itself
a fully reproducible evaluation record.

These checks are **evaluation hygiene**, not a Needle superiority claim.

They were added after public legal-benchmark defects demonstrated that strong modern
benchmarks can still suffer from criterion/source misalignment, vacuous criteria,
cross-criterion inconsistency, rubric undercoverage, execution failures that masquerade as
subject failures and unresolved judge/run variance.

Passing this gate does not prove a benchmark is representative or a model is reliable. It
only establishes that the evaluation contract is coherent enough for its score to mean what
the project says it means.

## 12. Complexity rule

A corpus failure may justify a method, persistence layer or code repair only if
the simpler workflow demonstrably cannot preserve the required distinction.

A difficult case alone is not permission to expand architecture.

The preferred project outcome is the smallest claim and smallest machinery that
survive the evidence.


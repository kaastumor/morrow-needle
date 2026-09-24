# Needle wide-lens review: project setup and discovery prompts

Issue: #196  
Date: 2026-09-24  
Baseline: `f410b376ec74c8a3869663b35d8440a015ced882`  
Decision: **CONTINUE; SIMPLIFY OPERATIONS**  
Scope: project and prompt review, not a new product or evaluation horizon.

## Judgment

Needle has a credible, deliberately small research asset: source-linked legal
cases and an evaluation discipline that has successfully preserved negative
results. It has not yet demonstrated a broadly useful product, a uniquely
effective research method, or repeated external use of the surviving corpus.

The strongest concern is a substitution of goals. Rejecting unnecessary feature
work can still leave an expanding programme of failure-family discovery,
taxonomy refinement and governance. These can be legitimate research, but
finding another real distinction is not automatically evidence that maintaining
Needle helps anyone make a better decision.

Continue the authorised documentary work. Keep its claims narrow. Before
another broad discovery cycle, prefer one bounded attempt to use the existing
asset for a consequential research task over another search for categories.
This is a recommendation for the next gate, not permission to overwrite an
active experiment or revive rejected product claims.

## Evidence and limits of this review

Reviewed current charter, backlog, assumptions, value ledger, discovery method,
worker runbook, evaluation protocol, corpus, workflows, Cycle 1/2 syntheses,
Cycle 3 findings and #165/#174 protocols/results. The repository snapshot has
527 files, including 112 files under docs, 53 schemas, 78 test files and 25
Actions workflows. The canonical index has 29 cases and 15 trap classes. These
counts describe maintenance surface, not waste or research quality.

Original supplied prompts were read from the current files:

- `Pasted markdown(4).md`: value/novelty review, 13 parts plus 13 requested
  output sections; copies (1) and (2) contain the same retrieved text.
- `Pasted markdown(5).md`: linked discovery, 25 parts plus 16 requested output
  sections; copy (3) contains the same retrieved text, including its tail.

The original September 22 bootstrap prompt was only partially available in
conversation context and recovered summaries. Its precise full wording was
not independently recovered. Conclusions about its implementation are grounded
in the repository, not invented quotations of the missing original.

This is a same-session adversarial review. It is not independent expert legal
validation, a blind model evaluation, a new usage study, or a billing audit.
Changing the model used for this review does not rerun or invalidate historical
experiments. No model-evaluation or live-probe workflow was dispatched.

Concurrent activity was observed on #181 / PRs #192 and #194. A scope correction
was left on #194. Issue #195 was subsequently opened for authority-handoff
generality while this review was underway. #183 and #195 remain owned by that
workstream; this review does not substitute its own synthesis or sample.

## What has actually survived

| Asset or claim | Evidence | Defensible conclusion | Still unknown |
| --- | --- | --- | --- |
| Legal case collection | 29 indexed cases, durable evidence references, exposure and role labels | An inspectable internal research/regression asset exists | Independent reuse, coverage sufficiency and marginal value to a target workflow |
| Evaluation discipline | #87/#88/#95/#97 preserved parity and exposed a surfaced-versus-latent construct error | Useful internal controls against several forms of self-deception | Distinctiveness or advantage over competent existing evaluation practice |
| Needle Method | All tested #88 and #97 pairs passed in both arms; bounded handoff signal in #87 | No demonstrated correctness advantage in those suites; optional handoff convention | Population-level equivalence, other tasks, and results on new model configurations |
| Needle Core | #87 found no observed Core-over-Method handoff win | Keep persistence optional and case-earned | Any future task that actually requires it |
| Corpus Explorer | #136 ran actual UI bytes and preserved provenance; direct corpus route also succeeded | A working thin projection and a route-specific mechanical difference | Human importance, repeat use, preference and switching |
| External benchmark audit | #150 found one public harness-record inconsistency, with other tasks negative/unconfirmed | One bounded transfer result | Repeatability, external usefulness and whether ordinary benchmark QA would do as well |

The smaller identity is an annotated case collection with standard evaluation
practice. The incumbent identity is that collection plus Needle's reusable
protocol. The adjacent identity is a document-evaluation QA practice. The
incumbent remains a reasonable working form, but the smaller alternative has
not been beaten as a way to deliver the surviving contribution. The adjacent
identity is not earned by one inconsistency or an unexecuted transfer test.

## Jobs and alternatives

| Actor and concrete job | Strong real alternative | Possible Needle contribution | Evidence boundary |
| --- | --- | --- | --- |
| Evaluator diagnosing a legal-research system's failure | Existing behavioral-testing practice, official sources, ordinary versioned test cases | Ready-to-inspect legal distinctions and explicit exposure/rubric records | Plausible; no repeated external diagnostic-use result |
| Investigator answering one legal-state question | Competent official-source research, with an equally capable source-grounded model where appropriate | Relevant examples or a reusable source trail | Prior suites did not establish Method correctness superiority |
| Reviewer reconstructing an earlier investigation | Source-linked notes, saved inputs/outputs and versioned files | More consistent handoff/evidence packaging | Narrow #87 signal; exact archival gap remains |
| Reader browsing the corpus | JSON/repository search, local text search or a simple table | Lower navigation burden | #136 used different task families and a particular connector route; not an isolated causal UI comparison |

Novelty of the generic methodology is not necessary for any of these jobs.
Its novelty is also not established here. CheckList already supplies an
established behavioral-testing alternative; its paper reports practitioner
studies finding actionable bugs. Use it as a methodological benchmark, not as
proof Needle is useless or as a mandate to adopt its software.

The useful system-level hypothesis is that legal examples, source trails,
exposure labels and scoring boundaries work together to reduce diagnostic or
reconstruction burden. Each part may be ordinary. The interaction still needs
evidence against ordinary source-linked cases. Access, expertise and setup
burden could erase its advantage. None is measured by adding another class.

## Findings and strongest counterarguments

### F1 — High: the surviving asset is being called proven more broadly than its use

**Observed:** the corpus exists and internal investigations produced findings.
H-16 remains parked; #150 supplies one narrow external-artifact result.

**Attack:** the project may be preserving its own research effectively while
assuming that preservation is a useful product or external evaluation resource.
Research validity, internal usefulness and external demand are different claims.

**Counterargument:** a research collection need not have customers to be worth
doing. Correct. Sponsor-supported inquiry and reusable internal regression
evidence are legitimate outcomes. They should be named as such rather than
borrow the stronger language of validated product value.

**Disposition: REVISE.** Retain the asset; state the supported outcome per task.
Do not impose a commercial test on documentary research. Do not count that
research as proof of external adoption either.

### F2 — High: novelty has moved from features into the taxonomy

**Observed:** Cycle 3 repeatedly asks whether a mechanism earns a new class or
generality claim. #171 added two derivation cases; #174 sought a broader label.
The scopes expressly avoid implementation and product claims.

**Attack:** class uniqueness becomes the new proxy for value. The operator can
always find another official ecosystem with a role, time or scope distinction.
Conversely, a useful case might be rejected merely because an existing class
already explains it.

**Counterargument:** distinguishing mechanisms is necessary for a good corpus.
Yes, when it changes coverage, diagnosis, scoring, a regression or a real answer.
A definition change alone does not show improved use.

**Disposition: REVISE.** Before choosing a follow-up, state what practical
research decision differs between support and rejection, and what existing
evidence cannot already decide. A new class is neither necessary nor sufficient.
#195 can finish as a documentary generality test; its result must not be
promoted into model-performance or product evidence.

### F3 — High: prompt integration retains a false-negative rule

**Observed:** discovery v0.2 section 4 still requires evidence that the simpler
baseline failed before delivery. Section 13 correctly allows meaningful
workflow advantage with correctness parity. These instructions conflict.

**Attack:** a future operator follows the shorter, categorical rule and rejects
the precise kind of value the sponsor's value prompt was intended to preserve.

**Disposition: REVISE NOW.** Make section 4 point to the claim-specific section
13 gate. The validity floor remains intact; no failed correctness claim is
retroactively rescued as workflow value.

### F4 — High: small illustrative suites and protocol feasibility do not prove broad claims

**Observed:** #88 used six pairs, #97 four pairs. #165 did not construct a full
sample or execute a model run. #174 stopped before its full sample existed.

**Attack:** observed all-pass pairs become universal equivalence; two source
chains become a broadly validated failure prevalence; ability to express a
non-legal case becomes distinctiveness of the protocol.

**Counterargument:** small tests can justify stopping investment or expose a
decisive counterexample. Correct. An investment stop rule does not require a
population-wide equivalence proof. Keep the decision and qualify its inference.

**Disposition: REVISE WORDING, PRESERVE RESULTS.** State the case, model, tools,
task and exposure boundary. Separate case-selection independence, investigator
blinding, grader independence and possible pretraining exposure. A fresh chat
only addresses part of this. Do not launch a larger benchmark merely to obtain
a more impressive number.

### F5 — Medium: selection rigor is exceeding the question's requirements

**Observed:** #174 froze a single web search for a negative control and disallowed
replacement after exposure; #165 encountered several inaccessible transports.
The final outcomes honestly record no scientific conclusion. The new metadata
smoke test is a useful correction, but does not verify full eligibility.

**Attack:** the runtime's search quirks increasingly decide what is investigated.
The project responds by starting a new research branch instead of gaining an
answer to the original high-value question. "Information gain" ignores the
probability that the test can actually be completed.

**Disposition: REVISE FUTURE DESIGN ONLY.** Distinguish exploratory documentary
case-building from confirmatory evaluation. Where needed, allow an explicitly
exposed feasibility pilot, retain its exposure record, and exclude pilot cases
from later fresh validation. Then freeze the scientific inputs and necessary
selection safeguards. For model comparisons, preserve exact prompts, access,
scoring and stop rules. Neither #165 nor #174 may be repaired retroactively.

### F6 — High: canonical Git history is not coherent current state

**Observed:** at the baseline, the backlog/charter still name #178 as next while
Runs 3A–3D are merged. The worker hard-codes completed #105–#116. It says to
resume any unfinished automation PR. Another session was actively editing one.
The main-branch response reports `protected: false`; no wider administration
audit was performed. All four visible Needle scheduled tasks are disabled.

**Attack:** two well-intentioned operators both follow WIP=1 and still race the
same task. A worker can take over a live PR; a stale queue can undo a later
decision. Actions concurrency limits jobs, not conversational writers.

**Disposition: REVISE NOW, WITHOUT NEW LOCK INFRASTRUCTURE.** The backlog owns
current order; the parent owns scope. Remove the duplicate fixed queue. Record
issue/PR ownership and inspected base; inspect head and changed files before
writing or merging; never force over unexplained newer work. A recently active
PR is not abandoned. Existing issue records are sufficient coordination for
now, but they are advisory rather than an atomic lock. Do not claim protection
settings were fixed. #183's owner reconciles its current queue.

### F7 — Medium: cost is generated by execution habits as well as architecture

**Observed:** 25 workflow files survive historical experiments. The global unit
workflow runs the full Python suite, while foundation and several specialist
workflows rerun subsets. Some specialist workflows also own unique builds,
validators or live artifacts, so duplication is not established for every job.
The recent Actions sample was dominated by sanitation around per-file branch
updates, PRs and merges. #193 removed feature-push duplication for sanitation
and unit tests; their PR and main checks passed.

**Disposition: KEEP THE FIX; DEFER BROADER CONSOLIDATION.** Batch coherent changes
and keep live probes manual unless a concrete task needs them. Map each
specialist job's unique gate/artifact before demoting it. Do not blindly disable
all CI or add an expensive permanent cost dashboard. Two rather than three
runs for a one-commit PR is an event-count saving, not a measured invoice saving.
Disabled scheduler tasks are not a current recurring-cost cause.

## Red-team the supplied prompts themselves

The principles are sound: inspect evidence, separate novelty from value, compare
real alternatives, map structural rather than superficial analogies, seek
boundaries, and stop searches with diminishing returns. Keep these.

Three prompt-design hazards remain:

1. **Assumed proven core.** Both prompts begin by asserting a core with evidence
   of usefulness. An agent may fill that premise even when only technical
   feasibility or internal use is supported. Begin by testing the premise and
   allow the answer "no externally validated core yet".
2. **Exhaustive deliverable pressure.** The long section/output lists compete
   with their own anti-theatre rules. Treat them as an occasional review library,
   not a template to reproduce for every scout. Omit inapplicable analysis and
   write only what changes a decision.
3. **Mechanism before identification.** An articulate causal story is easy to
   produce. Require rival explanations and a contrast that distinguishes them.
   For example, #136's different cases and search routes cannot isolate the UI
   as the cause of reduced burden; preserve that as a hypothesis.

The repository wisely declined to build the generic prompt's permanent
discovery graph and already added an evidence gate, three-hypothesis ceiling
and one-follow-up limit. The problem is primarily execution and incentives,
not a need for another framework. Do not delete the safeguards because they
are long; use their applicable subset and retire stale active-state copies.

## Compact operating prompt for the next bounded run

This is a proposed distillation for Morrow, not a replacement for frozen
experiment instructions or the scheduled worker's narrower authority:

> Inspect the active issue, current backlog, relevant evidence and live PRs.
> State what is actually supported and what remains a hypothesis. Name the
> decision this run can change. Compare the strongest realistic alternative
> under explicit time, tool and expertise constraints; do not weaken it or assume
> unlimited effort. Choose the cheapest feasible observation that distinguishes
> the leading explanation from its strongest rival. State the claim type,
> failure condition and exposure boundary before decisive testing. Novelty,
> class count, citations and activity are not success measures. Preserve useful
> negative results. Report the evidence delta, resulting decision, limitation
> and next trigger. Reuse existing records; batch changes; respect active
> ownership. If a branch is exhausted, redirect bounded active discovery toward
> a different decision, without manufacturing product value or declaring the
> entire project idle by default.

## Next decision and smallest useful test

Finish the already selected Cycle 3 synthesis/generality work without adding a
parallel experiment from this review. At its exit, prefer this test over an
automatic Cycle 4:

**Question:** Does the existing corpus change a concrete diagnosis, test or
review decision relative to ordinary source-linked notes and behavioral QA?

**Method proposal:** freeze one genuine evaluation/review task, its input and
intended decision before selecting helpful corpus cases. Compare the strongest
ordinary workflow with access to the existing corpus under a declared resource
budget. Keep sources equally available. Record consequential defects or
ambiguities found, evidence completeness, review burden and the action each
finding would warrant. Select the primary outcome before execution.

**Encouraging:** an independently checkable difference changes that decision or
removes a material observed burden, without a validity regression.

**Disconfirming:** the ordinary workflow reaches the same usable result within
the declared tolerance, or corpus use adds classification/inspection effort
without changing the decision. Reduce the maintained wrapper accordingly.

**Boundary:** a synthetic or agent-run task can test mechanics and technical
diagnostic utility, not human adoption. If an actual external user task is not
available, use a concrete internal task and limit the inference; do not ask the
sponsor for ceremonial dogfood or invent demand. No external outreach or paid
model run is authorised by this proposal. Freeze task/sample/thresholds in a
separate approved experiment before execution.

Park broad product revival, a new cross-domain identity, further taxonomy
splitting for its own sake, and mass legacy-code deletion. Neither lack of
novelty nor an incumbent's existence kills a worthwhile workflow hypothesis.
Neither an analogy nor successful documentary generalisation establishes one.

## Changes made by this review

- Correct the contradictory baseline-failure sentence in discovery v0.2.
- Add a compact decision-consequence check to its existing quality checks.
- Clarify case-bounded inference in the evaluation protocol without changing
  prior outcomes or frozen scientific inputs.
- Replace the worker's obsolete fixed queue with the current-backlog rule and
  add active-ownership/head checks. Retain #193 cost discipline.
- Preserve this review as one document. No new schema, software dependency,
  product feature, scheduler, model run or standing discovery horizon.

The prospective pilot/design recommendation and next-use experiment are
recommendations, not retroactive protocol amendments or automatically scheduled
work. The current scientific claims remain unchanged.

## Sources and review anchors

Repository references are relative to the baseline unless otherwise noted:

- `README.md`, `BACKLOG.md`, `docs/project-charter.md`, `docs/assumptions.md`,
  `docs/value-evidence.md`, `docs/project-health.md`.
- `docs/discovery/evidence-triggered-continuous-discovery-v0.2.md`, especially
  sections 4, 13 and 17; `discovery-method-amendments-red-team-2026-09-24.md`.
- `docs/discovery/cycle1-explorer-boxed-workflow-2026-09-24.md`, Cycle 1 and
  Cycle 2 synthesis documents; Cycle 3 Runs A–D; Issues #183/#195.
- `docs/experiments/issue165-scholarly-status-preregistration-2026-09-24.md`,
  its result, and #174 preregistration/result.
- `docs/evaluations/adversarial-corpus-protocol-v0.1.md`, `corpus/README.md`,
  `corpus/index-v0.1.json`, `docs/automation/hourly-worker.md`, and workflow files.
- [GOV.UK discovery guidance](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works):
  use problem/user context and the benefits-versus-cost decision as the benchmark
  for discovery; do not transplant its service-delivery model wholesale.
- [Ribeiro et al., CheckList, ACL 2020](https://aclanthology.org/2020.acl-main.442/):
  established behavioral-testing practice and evidence of actionable diagnostic
  use; a strong methodological alternative, not a comparison run against Needle.
- [GitHub concurrency documentation](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency):
  concurrency groups control jobs/workflows. They do not claim cross-session
  ownership of repository edits.

What would most change this judgment is demonstrated reuse that changes a
research decision, or a well-controlled negative result showing that ordinary
source-linked cases are sufficient. Either is more informative now than a
larger opportunity map alone.

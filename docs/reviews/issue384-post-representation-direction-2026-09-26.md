# Issue #384 — direction review after EU-state and evaluation-representation research

Date: 2026-09-26  
Mode: **REVIEW — RESEARCH ALLOCATION**

## Decision

# **SELECT_FALSE_REJECTION**

The next highest-information internally tractable question is:

> **Do legal evaluation contracts systematically risk false rejection because the set of
> professionally acceptable answers is harder to enumerate than it is to recognize?**

This is narrower than #381.

#381 established that evaluation representation must fit the decision. The new question asks
whether **even when atomic criteria are the appropriate representation**, the authoring
process can under-specify the acceptable region and reject valid work.

## Why this wins allocation

### 1. Temporal oracle / benchmark maintenance

**Status: real job, but lower next information gain.**

Evidence already supports that legal/regulatory content and benchmark criteria can drift.

Needle has one source-backed public benchmark example from #375.

But another public-benchmark maintenance hunt now risks:

- repeating the Harvey-style defect search;
- selecting tasks where law changes are likely;
- confusing ordinary legal maintenance with a Needle-specific gap.

Commercial regulatory-change products already claim substantial ownership of:

- continuous change ingestion;
- applicability;
- obligations;
- effective dates;
- control mapping;
- audit trails.

CUBE, Bloomberg Regology and Thomson Reuters all publicly position around continuous
regulatory-change / obligation maintenance.

A benchmark-specific oracle-maintenance product gap remains possible, but public evidence is
not currently strong enough to make another internally selected drift audit the highest-value
next unit.

Disposition:

> **PARK AS PLAUSIBLE OPERATIONAL JOB; DO NOT REPEAT #375 DEFECT HUNT**

### 2. False rejection of professionally valid alternatives

**Status: strongest next scientific question.**

This lane gained new evidence after #381.

Legal Benchmarks explicitly says its lawyer-authored criteria are intended to accommodate
multiple professionally defensible approaches.

That is evidence the problem is recognized.

But recognizing the requirement is not the same as measuring whether the acceptance region
is complete.

A new 2026 paper, **Judging Is Not Enumerating: Silent Omissions in LLM-Authored Acceptable
Sets**, isolates a general mechanism:

- systems can judge whether a candidate is acceptable substantially better than they can
  enumerate all acceptable candidates in advance;
- authored verifier sets can admit only a minority of oracle-correct solutions;
- omission errors are harder to audit than visible over-inclusions;
- probing known-correct alternatives can sharply reduce false rejection.

The paper is **not legal-domain evidence** and much of its strongest result concerns
LLM-authored acceptable sets, not expert lawyer rubrics.

That limitation is exactly why a legal-domain investigation is earned rather than a
conclusion.

The question is falsifiable:

> strong lawyer-authored legal rubrics may already encode alternatives well enough that the
> omission mechanism is negligible.

Needle has unusual but bounded leverage here because its protocol now explicitly owns:

- valid-alternative policy;
- false-rejection checks;
- mutation tests;
- fatal/non-compensatory constraints.

That does not mean Needle solves the problem.

### 3. Legal-agent trajectory assurance

**Status: promising, but current public legal evidence is thin.**

General agent-evaluation research increasingly treats trajectory attribution, runtime
contracts and evidence chains as first-class objects.

Harvey/LAB also performs qualitative trajectory analysis.

Horizontal eval/observability products already expose:

- traces;
- span-level evaluators;
- tool-call inspection;
- trajectory scoring.

The unresolved legal-specific question is whether a final answer can be acceptable while the
research trajectory contains a consequential legal-source/state failure.

That is interesting.

But a serious test needs:

- public legal-agent traces;
- source/tool actions;
- an independently justified trajectory-error contract.

Current public evidence is not strong enough to beat the false-rejection lane on immediate
tractability.

Disposition:

> **KEEP AS SECONDARY SCIENTIFIC LANE**

### 4. Commercial/product contract map

**Status: public-evidence ceiling reached for now.**

The prior market scan already found:

- legal benchmark vendors;
- vendor-internal QA;
- law-firm ML Ops;
- horizontal eval infrastructure;
- regulatory intelligence;
- assurance/audit providers.

Public product pages do not disclose enough implementation detail to determine whether every
Needle-shaped state/evaluation job is actually absent.

Repeating public website inspection risks converting:

> "not documented"

into:

> "not implemented".

A deeper commercial contract test needs demos, procurement material, product access or users.

Disposition:

> **EXTERNAL ACCESS DEPENDENT**

### 5. Customer-specific maintained evaluation estates

**Status: commercial job plausible, Needle advantage unproven.**

Linklaters and large vendors demonstrate that maintained private legal-evaluation estates
are real.

The remaining hypothesis is that smaller organisations may need the same function without
building a full internal ML-Ops/evaluation organisation.

But the next decisive evidence is buyer/workflow evidence:

- current alternative;
- qualified time;
- maintenance burden;
- acceptance;
- willingness to outsource/pay.

That is the #375 DELIVERY family and requires external users.

Disposition:

> **EXTERNAL ACCESS DEPENDENT**

---

## Why false rejection is not just #381 again

#381:

> Which representation is valid for the evaluation decision?

#384-selected question:

> Given a criterion/checklist representation that is otherwise appropriate, has the
> evaluator represented the **full acceptable region** well enough not to reject valid legal
> work?

A rubric can be the right representation and still have an incomplete acceptance boundary.

That is a distinct measurement failure.

---

## Bounded successor WIP

Create one discovery issue:

> **LEGAL RUBRIC ACCEPTANCE-BOUNDARY AUDIT**

Phase 1 should not attempt to prove legal false-rejection prevalence immediately.

It should:

1. inspect public legal benchmarks with inspectable criteria/rubrics;
2. classify how they encode alternative acceptable answers:
   - enumerated alternatives;
   - semantic/predicate criteria;
   - open-text professional-judgment criteria;
   - reference-answer matching;
   - prohibitions/vetoes;
3. test the strongest ordinary safeguards already used;
4. identify whether omission risk is structurally detectable without needing a complete
   oracle;
5. design **positive-alternative probes**:
   - start from independently supported acceptable answers;
   - vary strategy/formulation while preserving legal validity;
   - ask whether the evaluation contract still accepts them;
6. separately preserve **negative/fatal probes** so widening acceptance does not inflate false
   acceptance.

Phase 1 ends with one of:

- `LEGAL_FALSE_REJECTION_RISK_SUPPORTED`
- `EXPERT_RUBRICS_ALREADY_ADEQUATE`
- `PUBLIC_EVIDENCE_INSUFFICIENT`
- `PARK`

## Guardrails

- do not transfer the 58–92% false-rejection numbers from non-legal LLM-authored verifiers
  into law;
- do not equate one valid alternative with infinite acceptable variation;
- do not weaken fatal legal requirements in the name of flexibility;
- do not use Needle's own answer keys as independent proof that an alternative is valid;
- no corpus growth;
- no product build;
- no commercial claim.

## Sources informing allocation

- JudgmentBench:
  https://arxiv.org/abs/2605.25240
- Judging Is Not Enumerating:
  https://arxiv.org/abs/2608.01000
- Legal Benchmarks methodology:
  https://www.legalbenchmarks.ai/methodology
- CUBE regulatory change:
  https://www.cube.global/products/regplatform/regulatory-change-management
- Bloomberg Regology:
  https://www.regology.com/
- Thomson Reuters Regulatory Intelligence:
  https://legal.thomsonreuters.com/en/products/regulatory-intelligence

## Final disposition

# **SELECT_FALSE_REJECTION**

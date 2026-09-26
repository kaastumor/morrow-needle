# Issue #388 — direction review: legal-agent trajectory

Date: 2026-09-26  
Mode: **REVIEW — RESEARCH ALLOCATION**

## Decision

# **SELECT_AGENT_TRAJECTORY**

One bounded public trajectory study is earned before declaring the internal/public evidence frontier exhausted.

This is not because tracing is novel.

It is because current public legal-agent work now exposes a sharper distinction:

> **trajectory as diagnostic evidence** versus **trajectory as part of the legal/evaluation
> object itself**.

The former is already mature and heavily occupied. The latter may or may not define a
separate legal-evaluation job.

---

## 1. Harvey LAB changes the tractability judgment

#384 previously downweighted trajectory research because public legal trace evidence appeared thin.

Harvey LAB's current public architecture and May 2026 results make that assessment stale.

Every LAB run records:

- `transcript.jsonl`;
- tool calls;
- document coverage;
- shell/search/read/write/edit activity;
- finish metadata;
- costs/latency and other metrics.

The standard LAB scorer, however, grades **final deliverables** against task criteria.

Trace analysis is a separate behavioral layer.

Harvey's published baseline analysis then maps action sequences to task performance and reports
associations such as:

- broader pre-draft document coverage -> higher scores;
- post-draft validation -> higher scores;
- revise-after-check loops -> higher scores;
- targeted retrieval / structured analysis / return-to-source behavior -> modest gains;
- noisy tool fan-out and draft-without-review -> worse scores.

Harvey explicitly says that for long-horizon professional work, trajectory should be treated
as a unit of measurement alongside final score.

That is strong evidence for:

> **TRAJECTORY_DIAGNOSTIC**

It does not yet establish:

> **TRAJECTORY_CONSTITUTIVE**

A strange or inefficient path can still produce a legally correct work product.

Sources:
- https://www.harvey.ai/blog/legal-agent-benchmark-initial-results
- https://github.com/harveyai/harvey-labs/blob/main/docs/architecture.md

---

## 2. LARA proves one genuinely constitutive legal trajectory class

Aithos LARA evaluates a different object.

It places an AI agent in a simulated workplace with tools such as:

- email;
- messaging;
- customer records;
- calendars;
- social media.

Each scenario is anchored to a specific GDPR or EU AI Act provision.

The auditor pressures the agent into a situation where completing the objective would require
illegal conduct.

Three judges evaluate the **full conversation / behavior trajectory** against the verbatim
legal provision, with human legal review/overrides in the published study.

Here the path is not merely explanatory.

If the agent:

- harvests protected data;
- performs prohibited emotion inference;
- manipulates a vulnerable person;
- conceals required AI status;
- or otherwise takes the prohibited action,

the violation occurs **during the trajectory**.

A benign final summary cannot erase it.

That is genuine:

> **TRAJECTORY_CONSTITUTIVE**

But it is a legal-compliance benchmark for deployed agents, not a benchmark of legal
research/work-product quality.

It therefore proves the category exists without proving a Needle-shaped legal-research gap.

Sources:
- https://lara.aithos.org/
- https://aithos.substack.com/p/introducing-aithos-lara

---

## 3. Generic trajectory infrastructure is already occupied

The technical layer is not a Needle opportunity.

Arize/Phoenix publicly provides:

- full traces/spans;
- ordered tool-call extraction;
- trajectory-level LLM evaluators;
- trace/session evaluation;
- production monitoring;
- human/automated annotation.

Its own guidance explicitly notes that an agent can reach the right final answer through a
poor path that wastes resources or exposes risk.

LangSmith and other horizontal observability/evaluation platforms similarly instrument tool
calls and trace-level evaluators.

Therefore:

> **"capture and score agent trajectories" is not a market gap.**

Needle should not build generic trace infrastructure.

Sources:
- https://arize.com/docs/ax/cookbooks/agents/agent-trajectory-evaluations
- https://arize.com/phoenix

---

## 4. The surviving research boundary

Use three categories.

### OUTCOME_ONLY

The path has no independent consequence once the final deliverable is:

- legally correct;
- adequately supported;
- professionally usable;
- compliant with the task.

Examples:

- the agent read documents in an odd order;
- used more searches than necessary;
- drafted before searching and later repaired the result;
- used shell analysis where manual reading would also work.

These may affect cost/reliability but are not legal failure by themselves.

### TRAJECTORY_DIAGNOSTIC

Path features explain or predict final performance, cost or stability.

Examples from LAB:

- document coverage;
- targeted retrieval;
- validation/revision loops;
- tool fan-out;
- return to source after drafting.

These are useful for agent engineering.

They are not automatically part of the legal evaluation contract.

### TRAJECTORY_CONSTITUTIVE

The path itself must satisfy an independently justified legal/professional constraint.

Potential families:

- processing/accessing data the agent is not permitted to use;
- disclosure of privileged/confidential material;
- legally prohibited action taken through a tool;
- required human approval/escalation bypassed;
- mandatory verification or audit step not performed where the process requirement itself
  is binding;
- use of a prohibited source/tool;
- an evidentiary/provenance chain that must be preserved as part of the deliverable/service
  contract and cannot be reconstructed after the fact.

Only this third category can support a distinct legal trajectory-evaluation job.

---

## 5. Red team

### Process fetishism

A high-quality legal answer is not invalid because the agent researched inelegantly.

Do not turn preferred associate workflow into law.

### Outcome leakage

Many apparent trajectory requirements are already testable from the deliverable.

If the final answer contains:

- correct authorities;
- traceable citations;
- required calculations;
- appropriate caveats;

then "the agent did not visibly read source X" may be irrelevant.

A trajectory criterion is earned only where the process fact is not losslessly recoverable
from the final output.

### LARA transfer problem

LARA evaluates whether a deployed agent itself violates law.

That is different from whether an agent *performing legal work* followed a legally valid
research process.

Do not use LARA's compliance rates as evidence about legal research agents.

### Incumbency

Generic trajectory evaluation is already mature.

Any surviving Needle role would need to define **legal/professional trajectory constraints**,
not instrumentation.

### Needle inflation

Needle's historical interest in source lineage does not automatically imply a trajectory
product.

A source-state distinction belongs in trajectory evaluation only if the path-level evidence
is independently consequential.

---

## 6. Why this wins over temporal maintenance now

Temporal/oracle maintenance remains plausible.

But:

- #375 already found a public stale-legal-value contract defect;
- regulatory-change vendors heavily occupy general legal maintenance;
- another public benchmark hunt risks selection toward mutable law.

Trajectory now has a materially newer and more orthogonal public evidence surface:

- LAB for legal work;
- LARA for constitutive legal agent behavior;
- mature horizontal incumbents for the generic infrastructure.

One bounded classification study can therefore close or sharpen the lane without a model run.

---

## Bounded successor WIP

Create one issue:

> **DISCOVER — legal-agent trajectory consequentiality**

Core question:

> **Which trajectory properties in legal-agent work are independently consequential, rather
> than merely correlates of a good final output?**

Phase 1 should:

1. map public legal-agent evaluation contracts;
2. classify observed/process criteria as:
   - OUTCOME_ONLY;
   - TRAJECTORY_DIAGNOSTIC;
   - TRAJECTORY_CONSTITUTIVE;
3. require an independent legal/professional owner for every constitutive claim;
4. test whether the process fact is already recoverable from the final deliverable;
5. inspect whether generic trace tools can already express the constraint once defined;
6. ask whether Needle contributes anything beyond supplying domain-specific failure
   hypotheses.

Phase 1 outcomes:

- `LEGAL_TRAJECTORY_CONTRACT_EXISTS`
- `TRAJECTORY_IS_DIAGNOSTIC_ONLY_FOR_NEEDLE_SCOPE`
- `PUBLIC_EVIDENCE_INSUFFICIENT`
- `EXTERNAL_GATE_REACHED`

No model runs, no agent harness build, no corpus/class growth.

## Final disposition

# **SELECT_AGENT_TRAJECTORY**

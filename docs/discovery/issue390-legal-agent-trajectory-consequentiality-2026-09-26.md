# Issue #390 — legal-agent trajectory consequentiality

Date: 2026-09-26  
Mode: **DISCOVER — LEGAL-AGENT TRAJECTORY CONSEQUENTIALITY**

## Result

# **TRAJECTORY_IS_DIAGNOSTIC_ONLY_FOR_NEEDLE_SCOPE**

The public evidence clearly establishes two things:

1. legal-agent trajectories are highly useful for diagnosis and agent engineering;
2. some deployed-agent trajectories are themselves the object of legal compliance.

It does **not** establish a distinct trajectory contract inside Needle's surviving
legal-research/reference identity.

For Needle's current source/time/authority failure classes, the consequential legal result
is normally assessable from:

- the final proposition/conclusion;
- the cited/evidence owner;
- the relevant legal/source time;
- the final provenance/evaluation record.

How the agent privately sequenced searches, reads, drafts and revisions is not independently
part of legal correctness unless an external law, policy or task contract makes the process
itself binding.

The strongest constitutive cases found belong to **agent compliance/security/workflow
governance**, not to a new Needle legal-research layer.

---

## 1. Harvey LAB — trajectory is diagnostic, final work product remains the score owner

Harvey LAB's public architecture separates run trace from task score.

Every run records:

- full `transcript.jsonl`;
- tool activity;
- document coverage;
- output files;
- run metrics and finish metadata.

The standard evaluation path then scores the **deliverables** criterion by criterion.

The judge receives the task/criterion and scoped output; it does not turn the hidden sequence
of reads/searches/writes into an additional all-pass requirement.

Harvey's published behavioral analysis uses the traces to explain performance.

Reported positive associations include:

- broad pre-draft research;
- post-draft validation;
- actual revision after validation;
- targeted retrieval;
- structured analysis;
- returning to source documents after drafting.

Negative associations include:

- noisy tool fan-out;
- drafting without later review.

These findings are valuable.

But the published claims are about:

> **what trajectories correlate with stronger agent performance**

rather than:

> **a legal deliverable is invalid if the agent failed to follow that sequence**.

A model can research inefficiently, then repair its work and deliver a correct memo. Nothing
in LAB's ordinary legal-work contract says that the inefficient path independently fails the
legal assignment.

Classification:

> **TRAJECTORY_DIAGNOSTIC**

Sources:
- https://www.harvey.ai/blog/legal-agent-benchmark-initial-results
- https://github.com/harveyai/harvey-labs/blob/main/docs/architecture.md
- https://github.com/harveyai/harvey-labs/blob/main/docs/tutorial.md

---

## 2. Legal Benchmarks / DELTA — output contract is deliberately primary

Legal Benchmarks' public application methodology grades the application's **final
submission**, including written answers/files.

It explicitly says it does not grade the reasoning/process that produced the submission.

DELTA similarly grades the final legal answer against:

- substance;
- citation;
- form.

This matters because many apparent trajectory concerns already leak into observable output
quality.

Examples:

- wrong authority used -> citation/source criterion can fail;
- material issue omitted -> substance criterion can fail;
- unsupported certainty -> substance/judgment criterion can fail;
- required source missing -> citation criterion can fail.

The evaluator does not need to know whether the model searched authority A before authority B
if the final legal support is complete and correct.

Classification for ordinary legal-research sequence:

> **OUTCOME_ONLY**

The path remains useful for debugging a failure after it occurs.

Sources:
- https://www.legalbenchmarks.ai/methodology
- https://github.com/legalbenchmarks/delta

---

## 3. LARA — trajectory can genuinely be constitutive

Aithos LARA demonstrates the opposite class cleanly.

The evaluated object is a deployed AI agent acting inside a simulated workplace with tools.

Scenarios are anchored to provisions of the GDPR or EU AI Act.

The agent can:

- send/read messages;
- access records;
- manipulate customer/user interactions;
- process personal data;
- take other actions during the simulation.

Judges evaluate the full interaction against the verbatim legal rule.

In this setting, the trajectory is not merely explanatory.

If the agent takes a prohibited action during the run, a later benign summary does not
erase that action.

Examples include scenarios involving:

- prohibited emotion inference;
- exploitative/manipulative conduct;
- impermissible personal-data processing;
- concealment of AI status where the tested legal rule requires disclosure.

Classification:

> **TRAJECTORY_CONSTITUTIVE**

This is strong evidence that legal trajectory contracts exist in agentic systems generally.

It does not transfer directly to an agent whose job is to research/draft legal work.

Sources:
- https://lara.aithos.org/
- https://aithos.substack.com/p/introducing-aithos-lara

---

## 4. Horizontal infrastructure already owns trajectory instrumentation

Arize/Phoenix directly supports:

- ordered tool-call extraction;
- span and trace instrumentation;
- trajectory-level evaluators;
- session-level evaluation;
- custom LLM or deterministic judges;
- production monitoring.

Its public trajectory guidance explicitly considers cases where the final answer can be right
while the path is inefficient or risky.

That means the generic engineering job is already well defined:

> trace -> extract tool/action sequence -> apply trajectory contract -> log/evaluate.

Needle does not need infrastructure for that.

A legal domain can simply supply a domain-specific trajectory policy to generic tooling.

Classification:

> **INCUMBENT_INFRASTRUCTURE_SUFFICIENT ONCE THE DOMAIN CONTRACT EXISTS**

Sources:
- https://arize.com/docs/ax/cookbooks/agents/agent-trajectory-evaluations
- https://arize.com/phoenix

---

## 5. Outcome-leakage tests

The following candidate Needle-adjacent trajectory requirements were attacked.

### "The agent must read the correct authority"

Suppose the final answer:

- states the correct proposition;
- cites the controlling authority;
- gives enough evidence for independent verification.

Whether the trace contains a literal `read(authority-X)` event is not independently legal
truth.

A model may have retrieved the proposition another valid way, or the final evidence package
may be independently checkable.

Result:

> **OUTCOME_ONLY / DIAGNOSTIC**

If the final answer cites unsupported authority, that is already an output/evidence defect.

### "The agent must search broadly before drafting"

Harvey's behavioral evidence supports this as a useful prior.

But broad-search-before-draft is not a legal rule.

Result:

> **TRAJECTORY_DIAGNOSTIC**

### "The agent must validate and revise"

Again, Harvey finds positive performance association.

But a first draft that is already correct does not become invalid because no edit occurred.

Result:

> **TRAJECTORY_DIAGNOSTIC**

### "The agent must preserve provenance"

Needle does require final source/evidence lineage for supported claims.

For the surviving project scope, that means preserving:

- source identity;
- legal/source time;
- evidentiary owner;
- exposure/reuse state.

Those facts can be expressed in the final evidence/result contract.

Needle has not demonstrated a separate requirement to preserve every hidden retrieval/action
step that led to them.

Result:

> **OUTCOME/EVIDENCE CONTRACT SUFFICIENT FOR CURRENT NEEDLE SCOPE**

### "The agent must not send confidential material to an unauthorised external tool"

Here the path itself matters.

Even if the final legal answer is perfect, the impermissible disclosure already occurred.

Independent owner:

- confidentiality / privacy / security / client-policy rule.

Result:

> **TRAJECTORY_CONSTITUTIVE**

But:

> this belongs to deployed-agent compliance/security, not a new Needle legal-research
> failure class.

### "The agent must obtain human approval before action"

If a binding law, client policy, risk control or task contract requires approval, bypassing
it is independently consequential.

Result:

> **TRAJECTORY_CONSTITUTIVE WHEN EXTERNALLY OWNED**

Again, the owner is the workflow/compliance contract.

Needle does not create it.

---

## 6. Needle corpus/protocol review

The charter defines Needle's demonstrated contribution as preservation of:

- legal-information traps;
- decisive consequential failures;
- source/evidence lineage;
- exposure/reuse status;
- negative/parity evidence;
- evaluation boundaries.

The canonical evaluation protocol's consequential outcomes include:

- wrong legal conclusion;
- historical/current inversion;
- scope leakage;
- status/application confusion;
- source-origin/authority confusion;
- temporal-boundary loss;
- unsupported certainty;
- inability to support a decisive claim.

Those are primarily **result/evidence states**.

The protocol freezes source/tool access for experiment fairness, but does not claim that one
specific research sequence is legally mandatory.

The project also repeatedly rejected generic workflow advantage.

Therefore a trajectory layer would need a new demonstrated failure:

> final legal/evidence output passes every current consequential check, yet the hidden path
> itself violates a Needle-owned legal-research requirement.

No accepted evidence owner currently demonstrates that failure.

---

## 7. Why LARA does not rescue the Needle trajectory thesis

LARA is highly relevant to **legal compliance of agentic systems**.

Its success proves:

> legal rules can attach directly to agent behavior over time.

Needle's current domain is different:

> adversarial legal-research known failures and evaluation discipline.

Importing LARA's constitutive trajectory logic into Needle would silently broaden the
project from:

> legal-information correctness / regression

to:

> legal compliance and governance of autonomous agents.

That expansion is not earned.

---

## 8. Commercial implication

There is no obvious Needle trajectory product opening.

The stack is already naturally separable:

1. **generic observability/eval infrastructure** records and scores trajectories;
2. **legal/compliance owners** define prohibited/required behavior;
3. **legal-work benchmarks** grade resulting work product;
4. **Needle** can remain a source of known result/evidence failure distinctions where
   relevant.

If a customer later says:

> "we need to prove that a legal agent never used source/tool/data X, always obtained approval
> Y, and preserved evidence path Z,"

that is a concrete trajectory contract.

It can then be tested against generic trace infrastructure.

Nothing currently shows that Needle materially reduces the effort or improves correctness
of that job.

---

## Final disposition

# **TRAJECTORY_IS_DIAGNOSTIC_ONLY_FOR_NEEDLE_SCOPE**

Supported:

- legal-agent trajectory analysis is valuable;
- trajectories correlate with legal-agent performance;
- trajectory-constitutive legal requirements exist in deployed-agent compliance;
- generic tools can operationalize such contracts.

Not supported:

- Needle needs a trajectory layer;
- Needle's source/provenance corpus implies hidden-path requirements;
- legal research work is invalid merely because the agent's private sequence was unusual;
- a distinct Needle trajectory product/service;
- corpus/class expansion.

## Allocation consequence

Close #390 without implementation.

The remaining high-quality questions now increasingly require:

- customer workflow contracts;
- private product behavior;
- qualified external adjudication;
- measured delivery burden;
- real incident traces.

That is strong evidence that the project has reached an **external evidence gate** for
further value/product discovery.

A final allocation review should confirm whether any materially different public scientific
question remains before making that gate canonical.

# Cycle 1 — current-approach failure audit

Issue: #138  
Parent: #134  
Channel: `CURRENT_FAILURE`  
Date: 2026-09-24

## Question

Has the current corpus / evaluation protocol / Explorer / GitHub operating model
produced a real failure that should drive the next discovery opportunity?

## Result in one sentence

Yes: Needle's evaluation work has produced **two independent evidence-closure
failures at different points of the execution lifecycle**.

The current protocol is strong on what should be frozen and interpreted, but the
actual evidence package has not always preserved enough independent proof of
what was executed or enough exact reveal material to close the experiment
durably.

No current product, corpus-authoring or CI failure clears the same threshold.

---

# Failure map

## Failure A — sealed artifact commitments verified, exact reveal bytes not durably archived

### Evidence

Issue #87 deliberately sealed three external plaintext artifacts before
execution:

- Stage-A packets;
- Stage-B packets;
- answer key.

Their SHA-256 commitments were committed before execution. During the pilot the
supplied files matched those commitments.

However, the final full-confirmation result bundle contains the run artifacts
and manifest but **does not contain the exact previously sealed Stage-A,
Stage-B and answer-key plaintext bytes**.

The canonical result fixture therefore records:

- `sealed_five_case_hashes_verified_before_pilot_evaluation=true`;
- `sealed_plaintext_present_in_full_confirmation_zip=false`;
- `post_blind_exact_archival_complete=false`.

Issue #87 remains open solely because those exact bytes must not be reconstructed
from summaries.

Canonical evidence:

- Issue #87 and its execution comments;
- `fixtures/value-gates/issue87-full-confirmation-results-v0.1.json`;
- `docs/audits/needle-relay-full-confirmation-2026-09-23.md`.

### Consequence

The scientific commitment was valid at execution time, but the repository cannot
currently provide a complete post-reveal artifact set from which a later
researcher can reconstruct the exact sealed experiment inputs.

This is not a correctness failure in the result.

It is a **durable reproducibility / archival-completeness failure**.

### Current workaround

- preserve the committed hashes;
- preserve the fact that they were verified during the pilot;
- refuse to reconstruct or fabricate missing plaintext;
- keep #87 open indefinitely unless the original exact bytes reappear.

That is honest, but not ideal.

---

## Failure B — result bytes preserved, execution settings not independently verifiable

### Evidence

Issue #97 used eight manual consumer-ChatGPT Temporary Chats for the
LATENT_TRAP_DETECTION gate.

The project preserved:

- exact prompts after reveal;
- exact answer key after reveal;
- eight submitted result files;
- SHA-256 hashes;
- run mapping;
- pre-registered stop rule.

The manifest specifies:

- Temporary Chat;
- unpersonalized mode;
- GPT-5.6 Sol;
- high reasoning;
- web search;
- no project context;
- no follow-ups.

But the result audit explicitly records that the submitted result text does
**not** independently prove those UI/model settings.

Canonical evidence:

- `fixtures/value-gates/issue97-manual-manifest-v0.3.json`;
- `docs/audits/issue97-latent-detection-result-2026-09-24.md`.

The final conclusion therefore correctly carries an execution-provenance
limitation.

### Consequence

A later reader can verify what answers were submitted and how they were scored,
but cannot independently verify the full execution boundary.

This weakens the strength of claims about the exact tested workflow.

Again, this does not invalidate the observed 4/4 R-pass/M-pass result. It limits
what can be claimed from it.

### Current workaround

Make the limitation explicit and avoid promoting the result beyond the evidence.

That is scientifically acceptable, but it shows the current evaluation workflow
does not always create a self-contained evidence package.

---

# Why these are one opportunity

The two failures occur at different lifecycle points:

- #87: **pre-execution/reveal artifact custody**;
- #97: **execution-environment provenance**.

Their common failure is:

> the evaluation protocol can specify and verify important conditions during an
> experiment without guaranteeing that the final durable evidence package
> contains enough information to independently reconstruct what was sealed,
> executed and revealed.

Working opportunity label:

**EVALUATION_EVIDENCE_CLOSURE**

This is not proposed as a corpus trap class. It is a project/research-process
opportunity.

---

# Strongest boring baseline

The existing protocol is already strong:

1. pre-register the claim and alternative;
2. seal prompts/keys/settings;
3. commit hashes;
4. execute independently;
5. reveal;
6. preserve outputs and negative/parity results;
7. record limitations.

Issue #87's later API confirmation improved execution evidence materially:

- stateless API requests;
- returned model recorded;
- response IDs unique;
- reasoning/web/store configuration in a manifest;
- result ZIP hashed.

That demonstrates that the problem does not require a benchmark platform.

The boring baseline is therefore:

> experiment-local manifest + exact artifact custody + explicit limitation
> handling.

Any Needle-specific response has to remain smaller than that.

---

# Smallest evidence-backed response

Do **not** build a service, database, execution platform or universal schema.

At the next genuinely authorised sealed evaluation, pre-register a minimal
**closure pack** as part of the experiment design.

The closure pack should prove or honestly delimit four things:

## 1. Commitment

Before execution:

- exact hidden-artifact filenames;
- cryptographic commitments;
- exact execution/configuration contract.

## 2. Execution

For every valid run preserve the strongest available direct evidence of:

- exact prompt/input hash;
- verbatim output;
- run identity;
- model/runtime identity where exposed;
- requested and applied settings where exposed;
- tool/access mode;
- failure/retry history.

For API execution, response IDs and returned settings/usage may be sufficient.

For consumer UI execution, if the platform does not expose independently
verifiable settings, record that as a hard evidence limit rather than inventing
proof.

## 3. Reveal

After execution:

- exact previously committed plaintext hidden artifacts must be placed in the
  durable evidence package byte-for-byte;
- hashes must be automatically or manually reconciled against the pre-execution
  commitments;
- no reconstruction from summaries.

## 4. Closure

The experiment cannot be marked `ARCHIVE_COMPLETE` unless:

- all required exact reveal bytes are present; and
- every claimed execution property is either independently evidenced or marked
  explicitly `SPONSOR_ATTESTED / PLATFORM_NOT_VERIFIABLE`.

This is a research convention first, not a new system.

---

# Riskiest assumption

That a small experiment-local closure contract can materially improve
reproducibility **without** forcing every evaluation onto a custom API harness,
collecting sensitive platform/user data, or creating another permanent
governance/schema layer.

---

# Kill rule

Reject further machinery if the next sealed evaluation shows that:

- a simple manifest + exact artifact bundle closes the evidence gap;
- remaining UI settings are genuinely not exposed by the platform and no
  lightweight evidence can improve that;
- stronger provenance would require disproportionate automation, account
  instrumentation or sensitive data capture.

In that case the correct endpoint is explicit limitation, not infrastructure.

A future service/database/harness is justified only if repeated authorised
evaluations demonstrate that simple experiment-local evidence capture fails.

---

# Candidate response risks

## Validity / evidence integrity

Primary risk and primary motivation.

Failure to close the package can weaken later claims or make exact reproduction
impossible.

## Viability / operations

Over-specifying evidence capture can make small experiments expensive and create
artifact bureaucracy.

## Privacy

UI screenshots, exported account metadata or session records may contain
personal/private information. The project must not collect them merely to create
a prettier provenance claim.

## Feasibility

API execution often offers stronger machine-verifiable provenance than consumer
UI execution, but forcing API use can change the tested workflow and therefore
the construct.

The execution medium must remain driven by the research question.

---

# Explicit non-findings

## No current corpus-authoring failure

Recent derivation admissions show that research/evidence work dominates
mechanical index entry. #113 already rejected authoring tooling.

No repeated structural correction cycle has appeared since then.

**Disposition: no opportunity.**

## No current CI/automation failure

The MVP delivery and the current discovery PRs have executed their required
repository checks successfully after the earlier Actions budget incident was
resolved.

There is no present runner/CI failure driving architecture.

**Disposition: no opportunity.**

## No observed Explorer usability failure yet

#103 remains unresolved because real/manual use has not yet occurred.

Absence of human evidence is not itself evidence that the Explorer failed.

#136 owns that question.

**Disposition: evidence gap, not failure.**

## No current evidence that a canonical legal model cannot represent a new case

#135 found a possible new judicial-document-role failure mechanism but did not
show that Needle needs a persistence/schema representation for it.

The corpus can already preserve the research finding as an indexed adversarial
case if the family later earns admission.

**Disposition: no representation failure.**

## Historical Full-Needle complexity is not a current failure

Unused old architecture, contracts and parked projections remain historical
provenance.

Their existence is not a reason to refactor or delete them during #138.

**Disposition: no opportunity.**

---

# Defined opportunity

> When Needle runs a sealed comparative evaluation, the final durable evidence
> package must preserve enough exact artifact and execution provenance to
> support the bounded claim later, without reconstructing hidden inputs or
> pretending platform settings are independently verified when they are not.

The problem is observed twice and affects scientific trust rather than
convenience.

---

# Final disposition

**ADOPT_FOR_EXPERIMENT**

Retain one bounded future experiment:

> On the next independently justified sealed evaluation, use an
> experiment-local evaluation evidence closure pack and test whether it closes
> the #87/#97 provenance gaps without introducing heavy execution
> infrastructure.

Do not create the evaluation merely to test the closure pack.

Do not build a universal harness, provenance service, database, UI feature or
new project-wide schema now.

#139 must decide whether this opportunity should survive Cycle 1 synthesis.

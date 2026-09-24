# Red-team — discovery method amendments from strategy/linked-search prompts

Date: 2026-09-24  
Parent: #134  
Target: the two proposed discovery-method amendments:

1. **relative value / alternatives / adoption**;
2. **linked discovery search from proven evidence**.

## Decision standard

The amendments survive only if they improve information quality **without**
creating a route around Needle's existing anti-theatre rules.

The project must remain able to say:

- correctness parity can coexist with product/workflow value;
- workflow advantage cannot excuse a correctness or evidence-integrity regression;
- a linked hypothesis is not yet an opportunity;
- an interesting analogy is not evidence of transfer;
- a successful transfer is not evidence of customer value;
- empty discovery remains acceptable.

---

# Amendment A — relative value / alternatives / adoption

## Attack A1 — relabel a failed correctness claim as workflow value

### Failure mode

A Needle-specific correctness layer fails to outperform the strong baseline, then
the project preserves it by saying it is "faster", "clearer" or "better
packaged".

This would defeat the value gates that already rejected Method/Core/Full claims.

### Required boundary

Every experiment must declare the **claim type before execution**:

- `CORRECTNESS_VALIDITY`; or
- `PRODUCT_WORKFLOW`.

A failed `CORRECTNESS_VALIDITY` claim cannot be rescued by a post-hoc
`PRODUCT_WORKFLOW` reinterpretation.

A separate workflow claim may later be tested, but it requires its own job,
alternative, hypothesis and evidence.

### Disposition

**SURVIVES WITH HARDENING.**

---

## Attack A2 — speed/effort gains launder an unsafe result

### Failure mode

A faster route appears valuable while silently losing provenance, nuance,
uncertainty or correctness.

### Required boundary

Product/workflow value has a **validity floor**.

A workflow advantage cannot be promoted when it introduces a material:

- correctness regression;
- unsupported certainty;
- evidence-lineage loss;
- evaluation contamination;
- provenance weakening.

"Faster but less trustworthy" is not a Needle advantage unless the exact
trade-off is the tested user job and is itself safe.

### Disposition

**SURVIVES WITH HARDENING.**

---

## Attack A3 — choose a weak comparator to manufacture relative advantage

### Failure mode

Explorer is compared only with raw JSON, or another intervention with an
artificially clumsy baseline, making ordinary usability look distinctive.

### Required boundary

Use the **strongest realistic alternative the intended actor would actually
choose**, not merely the smallest technical baseline.

For Explorer this may include repository inspection, GitHub search, direct JSON,
or another realistic path depending on the task and user.

Record why the comparator is realistic.

### Disposition

**SURVIVES WITH HARDENING.**

---

## Attack A4 — stated preference becomes behavioural consequence

### Failure mode

A participant says "yes, I would use this" and the project upgrades that to
adoption evidence.

### Required boundary

Evidence strength remains explicit:

1. observed repeated choice / real reuse;
2. observed task behavior with a clear friction difference;
3. concrete commitment/action;
4. stated preference/intention;
5. internal inference.

A sponsor saying they would use the Explorer again is useful but remains weak
behavioral evidence until actual repeated choice occurs.

### Disposition

**SURVIVES WITH HARDENING.**

---

## Attack A5 — system-level value resurrects Full Needle

### Failure mode

Because combinations may create value, old parked surfaces are recombined into a
large product without each additional dependency earning itself.

### Required boundary

A system-level claim must compare:

- the proposed combination;
- the strongest smaller identity containing only already-earned elements.

The combination earns value only when the interaction creates an observed or
falsifiably testable advantage that neither smaller component produces alone.

"More coherent" is not enough.

### Disposition

**SURVIVES WITH HARDENING.**

---

## Attack A6 — adoption/switching analysis becomes speculative strategy prose

### Failure mode

The project writes plausible stories about habits, learning costs, trust or
switching without observing any of them.

### Required boundary

Switching/adoption factors are hypotheses unless behavior supports them.

Do not require full market strategy analysis during early discovery. Record only
the friction capable of killing the specific opportunity.

### Disposition

**SURVIVES.**

---

## Amendment A conclusion

Retain the amendment.

It corrects a real false-negative risk: **correctness parity is not necessarily
workflow/product-value parity**.

But the following rules are mandatory:

1. declare claim type before evidence collection;
2. workflow value never overrides a validity regression;
3. compare with a realistic strong alternative;
4. distinguish observed behavior from stated intention;
5. system-level value must beat the strongest smaller identity.

---

# Amendment B — linked discovery search from proven evidence

## Attack B1 — linked search becomes a fifth evidence channel

### Failure mode

The agent can always derive another analogy or transfer from existing project
knowledge. Discovery becomes self-fueling even when no new evidence exists.

That directly violates the four-channel evidence-trigger rule.

### Required boundary

Linked search is **not an evidence channel** and does not directly create a
candidate opportunity.

It may create only a:

> `SEARCH_HYPOTHESIS`

A search hypothesis enters the ordinary opportunity funnel only after target
evidence is found through an authorised evidence channel.

Example:

- "tracker lag may generalise to other derived official registers" is a search
  hypothesis;
- a real current register/source mismatch found through official-source research
  is a legal-adversary evidence signal.

### Disposition

**SURVIVES ONLY WITH THIS BOUNDARY.**

---

## Attack B2 — analogy becomes evidence by eloquence

### Failure mode

A distant field uses similar language or an attractive method, and the quality of
the analogy narrative is mistaken for evidence.

### Required boundary

For non-near transfers record only:

- source mechanism;
- target mechanism;
- shared causal/relational structure;
- material non-transferable differences;
- falsifier.

If this cannot be stated narrowly, park it as speculative inspiration.

No analogy counts as target-context evidence.

### Disposition

**SURVIVES WITH HARDENING.**

---

## Attack B3 — search explosion creates discovery theatre

### Failure mode

Near, adjacent, structural, distant, failure-led and recombination search create
an effectively infinite graph.

### Required boundary

No permanent discovery graph, ontology or branch inventory is created.

A linked-search pass is bounded to **at most three active search hypotheses**.

Stop a branch when:

- two consecutive search steps produce only examples of an already-understood
  mechanism;
- connection to proven evidence becomes indirect;
- no cheap discriminating test or target-evidence search exists;
- the branch depends on multiple unproven assumptions;
- another question has higher expected information gain.

The three-hypothesis cap is an operational ceiling, not a quota. Zero or one is
often correct.

### Disposition

**SURVIVES WITH HARDENING.**

---

## Attack B4 — recombination is feature brainstorming in disguise

### Failure mode

Known elements A and B are combined because the combination sounds useful.

### Required boundary

Recombination is permitted only when existing evidence supports a specific
interaction:

- A removes a demonstrated limitation of B;
- B removes a demonstrated limitation of A; or
- their interaction enables a currently observed job neither handles alone.

Otherwise it is ordinary ideation and is rejected from discovery.

### Disposition

**SURVIVES WITH HARDENING.**

---

## Attack B5 — successful technical transfer is mistaken for customer value

### Failure mode

A mechanism works in another context, therefore the project treats it as a
product opportunity.

### Required boundary

Transferability and product value remain separate gates.

A successful target-context transfer proves only that the mechanism generalises
for the tested construct.

It must then pass the ordinary value lens:

- user/job;
- real alternative;
- difference;
- importance;
- behavioral consequence;
- adoption/switching friction;
- strategic fit;
- validity floor.

### Disposition

**SURVIVES WITH HARDENING.**

---

## Attack B6 — "proven core" is abstracted until everything fits

### Failure mode

The core is described as something vague such as "find hidden relationships" and
then almost any domain becomes structurally analogous.

### Required boundary

A transferable principle must remain falsifiable and mechanically tied to project
evidence.

Use the smallest abstraction that explains the observed value.

If a principle cannot predict both:

- a positive transfer; and
- a plausible nearest boundary/failure,

it is too vague to drive linked search.

### Disposition

**SURVIVES WITH HARDENING.**

---

## Attack B7 — distant search rewards cleverness rather than evidence

### Failure mode

The project spends effort on forensics, medicine, intelligence or other domains
because the analogy is intellectually attractive.

### Required boundary

Search distance is not quality.

Distant search is optional and should normally occur only when:

- the mechanism is already sufficiently understood;
- nearer search is saturated or a distant domain offers a clearly relevant
  mature practice;
- there is a cheap way to falsify transfer.

Do not force portfolio diversity.

### Disposition

**SURVIVES WITH HARDENING.**

---

## Attack B8 — internal search quietly bypasses Cycle 1 bounds

### Failure mode

The new operator is used immediately to spawn new Cycle 1 issues before #139.

### Required boundary

Cycle 1 remains unchanged.

Linked search may inform #139's interpretation and possible future experiment,
but **no new Cycle 1 sensing task or Cycle 2 queue is authorised by this
amendment**.

### Disposition

**SURVIVES WITH HARDENING.**

---

# Combined-system attacks

## Attack C1 — the two amendments amplify each other into rationalised expansion

Linked search can generate many hypotheses, while the relative-value lens can
find some plausible workflow advantage for nearly any hypothesis.

### Required boundary

The sequence is asymmetric:

```text
EVIDENCE SIGNAL
  -> optional linked search
  -> SEARCH_HYPOTHESIS
  -> target evidence
  -> candidate opportunity
  -> relative-value / validity assessment
  -> smallest experiment
```

**No target evidence = no opportunity.**

**No observed/credible value difference = no product hypothesis.**

The relative-value lens is a filter, not a justification engine.

---

## Attack C2 — documentation becomes the product

The project can now produce sophisticated search maps, alternative maps and
red-team notes indefinitely.

### Required boundary

No new mandatory artifact is created.

Use ordinary issue text or a short research note only when the search materially
changes a decision.

The anti-theatre kill rule remains controlling.

---

# Final decision

## Relative-value amendment

**ADOPT — HARDENED**

It corrects a real conceptual defect and directly improves #136/#139.

## Linked-search amendment

**ADOPT AS AN OPTIONAL BOUNDED SEARCH OPERATOR — HARDENED**

It fills a real gap: the project can now deliberately ask what existing evidence
makes newly investigable without returning to feature ideation.

It does **not** become:

- a fifth evidence channel;
- a discovery graph/ontology;
- a recurring scheduled process;
- a requirement to search every distance band;
- a source of automatic backlog;
- permission for Cycle 2.

## Final operating model

```text
EVIDENCE TRIGGER
    ↓
OPTIONAL LINKED SEARCH
    ↓
SEARCH HYPOTHESIS
    ↓
TARGET EVIDENCE REQUIRED
    ↓
CANDIDATE OPPORTUNITY
    ↓
CLAIM TYPE
  ├─ CORRECTNESS / VALIDITY
  └─ PRODUCT / WORKFLOW
    ↓
REAL ALTERNATIVE + RELATIVE-VALUE / VALIDITY CHECK
    ↓
RISKIEST ASSUMPTION
    ↓
SMALLEST DISCRIMINATING EXPERIMENT
    ↓
REJECT / PARK / REVISE / ADOPT_FOR_EXPERIMENT
```

This is a refinement of v0.2, not a new discovery bureaucracy.

# Red-team — discovery method amendments

Date: 2026-09-24  
Parent: #134

Targets:

1. relative value / alternatives / adoption;
2. linked discovery search from proven evidence.

The amendments survive only if they improve information gain without giving the
project a new route to rationalise expansion.

## Decision

| Amendment | Decision |
|---|---|
| Relative value / alternatives | **ADOPT — HARDENED** |
| Linked discovery search | **ADOPT AS OPTIONAL BOUNDED SEARCH OPERATOR — HARDENED** |

Cycle 1 scope remains #135–#139. Neither amendment authorises Cycle 2 or product
delivery.

## A. Relative-value amendment

### A1 — post-hoc claim switching

**Attack:** a failed Needle correctness claim is preserved by relabelling it
"workflow value".

**Guard:** freeze the primary claim before discriminating evidence:

- `CORRECTNESS_VALIDITY`; or
- `PRODUCT_WORKFLOW`.

A failed correctness claim cannot be rescued post hoc. A later workflow claim
needs a separate hypothesis and evidence. Secondary observations may be
recorded, but they do not change the frozen primary claim.

### A2 — faster but less trustworthy

**Attack:** speed or convenience hides weaker correctness, uncertainty handling,
provenance or evidence lineage.

**Guard:** product/workflow value has a **validity floor**. A material
correctness, provenance, evidence-integrity or uncertainty-handling regression
blocks promotion.

### A3 — comparator gaming

**Attack:** Needle is compared with an artificially awkward baseline.

**Guard:** compare against the strongest realistic alternative the intended
actor would actually choose. Record why the comparator is realistic.

### A4 — preference becomes behavior

**Attack:** "I would use this" is treated as adoption evidence.

**Guard:** keep evidence strength explicit. Observed repeated choice/reuse is
stronger than observed one-off task behavior, which is stronger than stated
intention, which is stronger than internal inference.

Sponsor dogfood can expose a real defect or friction advantage; it cannot alone
establish broad adoption.

### A5 — system value resurrects Full Needle

**Attack:** ordinary capabilities are recombined into a large product under an
"activity system" argument.

**Guard:** compare any combination against the strongest smaller identity. The
combination must create an interaction advantage the smaller form does not.

### A6 — switching-cost prose becomes pseudo-evidence

**Attack:** plausible stories about habits, trust or learning costs become facts.

**Guard:** adoption/switching factors remain hypotheses unless behavior supports
them. Record only frictions capable of killing the specific opportunity.

### A conclusion

The amendment corrects a real false-negative risk:

> correctness parity is not automatically product/workflow-value parity.

It survives only with:

1. frozen claim type;
2. validity floor;
3. realistic strong alternative;
4. behavior/preference distinction;
5. smaller-identity comparator for system claims.

## B. Linked discovery search

### B1 — becomes a fifth evidence channel

**Attack:** the agent can always derive another analogy from existing knowledge,
making discovery self-fueling.

**Guard:** linked search is not an evidence channel. Its only output is
`SEARCH_HYPOTHESIS`.

A search hypothesis enters the ordinary funnel only after **target evidence** is
found through one of the authorised channels.

Example:

- "tracker lag may generalise to other derived registers" = search hypothesis;
- a real current register/source mismatch = legal-adversary evidence signal.

### B2 — analogy becomes evidence by eloquence

**Attack:** a convincing analogy is mistaken for target evidence.

**Guard:** for non-near transfers capture only:

- source mechanism;
- target mechanism;
- shared causal/relational structure;
- material non-transferable differences;
- nearest predicted boundary/failure;
- falsifier.

No analogy counts as target-context evidence.

### B3 — abstraction becomes so vague that everything fits

**Attack:** the proven core becomes "finding hidden relationships", making almost
anything analogous.

**Guard:** use the smallest abstraction that explains observed value. A
transferable principle must predict both a plausible positive transfer and a
nearest boundary/failure.

If it cannot, it is too vague to drive search.

### B4 — search explosion

**Attack:** near, adjacent, failure-led, recombination and distant search create
an infinite discovery graph.

**Guard:**

- no permanent discovery graph or ontology;
- at most three active `SEARCH_HYPOTHESIS` items;
- three is a ceiling, never a quota;
- zero is valid;
- distant search is optional;
- stop when searches add examples rather than mechanisms, the evidence link
  becomes indirect, no cheap discriminating test exists, or multiple unproven
  assumptions stack up.

### B5 — recombination is feature ideation

**Attack:** A + B is proposed because the combination sounds useful.

**Guard:** recombination is admissible only when existing evidence supports a
specific interaction: one element removes a demonstrated limitation of another,
or the interaction enables an observed job neither handles alone.

### B6 — technical transfer becomes customer value

**Attack:** because a mechanism generalises, it is treated as a product
opportunity.

**Guard:** successful transfer proves only transferability for the tested
construct. Product relevance still requires:

- user/job;
- real alternative;
- difference;
- importance;
- behavioural consequence;
- adoption/switching friction;
- strategic fit;
- validity floor.

### B7 — distant search rewards cleverness

**Attack:** unrelated domains are searched because the analogy is interesting.

**Guard:** search distance is not quality. Distant search is optional and
normally justified only when the mechanism is understood, nearer search is
saturated or the distant field has a mature relevant practice, and transfer is
cheaply falsifiable.

### B8 — bypasses Cycle 1 bounds

**Attack:** the operator spawns new work before #139.

**Guard:** Cycle 1 remains unchanged. Linked search may inform #139, but does not
authorise a new sensing issue or Cycle 2.

### B conclusion

Linked search fills a real gap: active creativity can be anchored in existing
evidence rather than feature brainstorming.

It survives only as an optional bounded operator, never as a work generator.

## C. Combined-system attack

The dangerous combination is:

> linked search generates many attractive hypotheses + relative-value analysis
> supplies a plausible advantage for each.

The required asymmetric sequence is:

```text
EVIDENCE SIGNAL
  -> optional linked search
  -> SEARCH_HYPOTHESIS
  -> target evidence required
  -> candidate opportunity
  -> frozen claim type
  -> validity / relative-value assessment
  -> smallest discriminating experiment
```

Hard stops:

- **no target evidence = no opportunity**;
- **no credible user/research consequence = no product hypothesis**;
- **validity regression = no workflow promotion**;
- **documentation volume = no value evidence**.

No new mandatory artifact is created by this method. Ordinary issue text or a
short research note is sufficient when the search changes a decision.

## Final operating decision

Adopt both amendments in the canonical discovery method with the guards above.

This is a refinement of evidence-triggered discovery v0.2, not a new framework,
roadmap, ontology or recurring process.

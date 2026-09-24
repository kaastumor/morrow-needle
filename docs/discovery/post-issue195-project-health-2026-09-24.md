# Post-#195 Project Health Check — 2026-09-24

Issue: #195  
Decision: **CONTINUE — #200 NEXT; TAXONOMY SIMPLIFIED IN PLACE**

## What changed

#195 supports one broader failure family:

`OFFICIAL_AUTHORITY_HANDOFF`

Fresh Balversa and N,N-dimethylformamide chains reproduce the same consequential
legal-effect ownership boundary previously seen in the two #171 RTS chains.

A fresh ECHA Candidate List inclusion supplies the counterexample: agency action
can itself own the tested legal effect.

The old technical-standard-specific class is therefore renamed/generalised, not
duplicated.

Corpus impact:

- cases: **29 → 29**;
- trap classes: **15 → 15**;
- persistent code/schema/workflow: **no change**.

## North-star alignment

The result improves the corpus by making one family less implementation-specific
without adding machinery.

It does not strengthen a product thesis. In fact, the strongest boring baseline
remains strong: careful official-source reading resolves all three fresh cases.

That limitation matters. The contribution here is preservation of a reusable
adversarial distinction and its boundary, not exclusive research capability.

The next highest-value question is therefore not another legal taxonomy search.
It is whether the surviving corpus itself changes a consequential review or
diagnostic decision enough to justify a corpus-specific workflow.

## Competing identities

### 1. Incumbent

**Adversarial legal-research corpus + evaluation protocol.**

#195 is consistent with this identity and makes the taxonomy smaller.

### 2. Smaller

**A source-linked adversarial case library with ordinary behavioral QA.**

If the dedicated corpus workflow adds no consequential benefit over well-linked
cases and ordinary QA, Needle should simplify toward this form.

### 3. Adjacent

**A bounded diagnostic/review aid for evaluating legal-research or benchmark
failures.**

This remains only a hypothesis. #150 supplies one external-transfer signal, but
not enough to adopt this identity.

#200 can distinguish the incumbent from the smaller identity and probe the
adjacent one without building product surface.

## Evidence against expansion

- #49/#59 rejected repeated public-product advantage.
- #88/#97 found baseline/Method correctness parity in the constructs tested.
- #171/#195 show that useful legal traps can be found and generalised, but a
  careful official-source baseline can still solve them.
- #195's transport smoke test itself failed to preserve identity-free search,
  reinforcing the need to record exposure rather than manufacture clean samples.

No part of this supports Cycle 4 by default.

## Assumptions and risks

H-23 moves from experiment to **survives**.

H-20 is retired because its narrower class no longer owns an independent current
decision; the two RTS cases remain evidence under H-23.

Largest current project risk:

> continuing to grow a high-quality taxonomy without showing that corpus access
> changes a real consequential workflow.

That is a value/usefulness risk, not a missing-ontology risk.

## Complexity / operations

No new:

- schema;
- Python code;
- dependency;
- service;
- scheduled workflow;
- model call;
- monitor;
- product projection.

The scheduled worker receives no new AUTO READY execution task. #200 is a design
and readiness decision requiring one real task and frozen study conditions.

## Canonical freshness

Reconcile:

- `BACKLOG.md`;
- `README.md`;
- `docs/project-charter.md`;
- `docs/assumptions.md`;
- `docs/value-evidence.md`;
- `corpus/index-v0.1.json`.

Historical #171 and Cycle-3 records remain unchanged as provenance.

## Direction

# **CONTINUE**

But continue into **#200**, not Cycle 4.

Reason:

#200 is already selected by the sponsor-authorised wide-lens review and directly
tests the usefulness of the surviving project core. Both outcomes are valuable:

- consequential corpus benefit → one narrow execution experiment may be earned;
- ordinary-workflow parity → simplify the wrapper;
- no real feasible task → PARK rather than invent demand.

No delivery, taxonomy expansion or execution test is authorised by this health
check alone.

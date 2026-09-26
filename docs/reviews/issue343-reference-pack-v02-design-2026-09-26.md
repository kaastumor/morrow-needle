# Issue #343 — minimum Reference Pack v0.2 failure-analysis surface

Date: 2026-09-26  
Disposition: **V02_DOC_NAV_ONLY**

## Question

What is the smallest truthful Reference Pack v0.2 surface that exposes the material
failure-analysis value observed in #339 without:

- creating a second legal truth store;
- turning one positive use into a general product claim;
- forcing external failures into the canonical corpus;
- synthesizing unsupported boundary/oracle fields;
- duplicating mutable repository state?

## Trigger

#339 produced:

> **NEEDLE_VALUE_PACK_GAP**

The full repository-level Needle method materially improved one mechanically selected,
independently observed legal-AI failure postmortem through:

- explicit `NO_EXISTING_CLASS_MATCH`;
- scientific/reuse status;
- a positive + opposite-error boundary;
- historical source-state reuse guidance;
- post-hoc regression-conversion status;
- explicit PASS/FAIL criteria.

Reference Pack v0.1 could inspect current classes and expose general reuse warnings, but
could not surface that whole packet without broader repository reconstruction.

That gap is sufficient to earn a v0.2 **design**.

It is not sufficient to invent a new canonical packet database.

## Existing pack architecture

Reference Pack v0.1 is intentionally simple.

Its generated data is derived entirely from the frozen canonical corpus index:

- `cases.jsonl`;
- `classes.json`;
- `evidence-map.json`;
- `catalog.md`;
- `manifest.json`.

The builder:

- pins the frozen corpus blob;
- validates the exact 81-case / 26-class shape;
- emits deterministic derived views;
- treats legal facts as owned by existing evidence chains;
- uses no network access.

This is a strong architecture property worth preserving.

The v0.2 design should not weaken it merely because #339 revealed a richer *use contract*.

## #339 replay requirements

A useful v0.2 must make it much easier to understand how to represent all of these without
reading broad project history:

1. `NO_EXISTING_CLASS_MATCH`;
2. known/public external-failure status;
3. derivation / regression-engineering reuse rather than fresh validation;
4. decisive legal-information failure mechanism;
5. material historical/source-state guidance;
6. positive + opposite-error/boundary control;
7. regression-conversion status;
8. PASS/FAIL criteria where actually supported.

The key question is not whether each item is useful.

The key question is:

> **who owns each fact?**

## Truth-ownership matrix

| Packet element | Canonical / legitimate owner | Safe v0.2 treatment | Omission rule | Main misuse risk |
| --- | --- | --- | --- | --- |
| Existing class membership | `corpus/index-v0.1.json` | Derive existing IDs exactly as v0.1 already does | Empty only outside corpus analysis | Forcing a class to avoid an empty/no-match result |
| `NO_EXISTING_CLASS_MATCH` for an external analysis | Accepted analysis result, e.g. #339 durable result | Explain the valid disposition and link exact owner | Omit unless an accepted analysis owner states it | Pack silently making a taxonomy judgment |
| Scientific/reuse status for corpus cases | Corpus index + canonical evaluation protocol | Explain how to read existing provenance/exposure fields | N/A for corpus cases | Calling exposed material fresh validation |
| Scientific/reuse status for a new external failure | Accepted analysis result + evaluation protocol | Explain status rules and link owner | Omit if no accepted analysis exists | Pack inventing scientific status |
| Decisive failure mechanism for corpus case | Corpus `decisive_trap` + evidence owner | Existing case view remains sufficient | N/A | Treating concise trap text as legal authority |
| Decisive mechanism for external analysis | Accepted analysis result | Link to exact owner; do not ingest as corpus fact | Omit absent accepted owner | Converting a worked example into corpus membership |
| Historical/source-state guidance | Exact legal/source evidence owner or accepted analysis result | Teach consumer to preserve it and link exact owner | Omit if not material / unsupported | Current-state substitution or copied stale legal truth |
| Boundary / opposite-error control | Existing class definition where actually expressed; otherwise accepted issue/audit/result owner | Explain requirement; link owner | Omit if no accepted boundary evidence | Synthesizing a neat boundary from class prose |
| Regression-conversion status | Exact evaluation fixture / derived regression artifact / accepted analysis result | Explain allowed states and link owner | No conversion state unless owner exists | Pretending post-hoc engineering was original science |
| PASS/FAIL contract | Exact executable fixture/answer-key/result owner or accepted analysis result | Link exact owner; never infer from class/case label | Omit when no executable owner exists | Turning descriptive traps into fake oracles |
| Evidence navigation | Current case `evidence_refs` + `evidence-map.json` | Keep existing deterministic map | N/A for corpus cases | Assuming navigation URL = immutable evidence |
| External worked-use navigation | #339 durable result for current observed example | Direct owner link from v0.2 guide | No generic external dataset until a canonical owner exists | Creating an ungoverned shadow corpus |

The table yields one central result:

> most of the #339 value is a **method / ownership contract**, not a new corpus field family.

## Architecture option A — documentation/navigation-only v0.2

### Shape

Create a self-contained v0.2 with the same frozen corpus-derived views as v0.1, plus:

> **`failure-analysis-guide.md`**

The guide should expose:

- the supported failure-analysis/evaluation/debugging job;
- explicit permission for `NO_EXISTING_CLASS_MATCH`;
- derivation/evaluation/exposure discipline;
- the packet checklist;
- historical/source-state handling;
- boundary/opposite-error handling;
- regression-conversion rules;
- PASS/FAIL ownership rules;
- direct navigation to the accepted #339 worked-use owner.

The guide does **not** copy #339 into the corpus.

It does **not** create machine-readable external failure records.

### #339 replay

This option can expose all six substantive #339 lessons truthfully:

- **NO_EXISTING_CLASS_MATCH** — as an allowed analysis outcome;
- public/exposed reuse status — through protocol guidance;
- KSR two-sided boundary — by navigating directly to the #339 result owner;
- pre-AIA source-state warning — same owner;
- post-hoc regression status — same owner + canonical protocol;
- PASS/FAIL criteria — same owner.

The consumer still opens the exact evidence/result owner for substantive facts.

That is desirable.

The pack's job is to remove broad project-history reconstruction, not to copy every fact.

### Complexity

Low.

No new truth object.

No external-failure membership registry.

No generalized boundary schema.

No synthetic regression fields.

### Decision

**ACCEPT.**

This is the minimum design that fixes the observed gap.

## Architecture option B — derived packet index

Possible shape:

- `failure-analysis-packets.jsonl`;
- one row per corpus or external analysis packet;
- structured fields for class disposition, mechanism, status, boundary, source-state rule
  and regression conversion.

### What works

For canonical corpus cases, several fields can be derived safely:

- case identity;
- existing class IDs;
- provenance/exposure;
- decisive trap;
- evidence refs.

### What fails today

The fields that made #339 materially better are not uniformly owned in structured
canonical state:

- no-class dispositions for external failures;
- explicit opposite-error controls;
- source-state guidance;
- regression-conversion status;
- PASS/FAIL criteria.

Some are in case-specific issues/audits/results.

#319 explicitly found boundary evidence adequate and rejected creating a maintained
boundary registry merely for internal neatness.

A v0.2 packet index must not recreate that rejected registry indirectly.

### Decision

**REJECT FOR v0.2.**

A derived structured packet index may become justified later, but only after repeated use
demonstrates a stable field family and legitimate canonical owners.

## Architecture option C — separate external-failure analysis layer

This would preserve a useful distinction:

- canonical corpus cases;
- external observed failure analyses;
- executable regression fixtures.

Scientifically, this is cleaner than admitting #339 into the corpus.

But a machine-readable layer requires a membership owner:

> which external analyses are accepted into the layer, and what fields are canonical?

Today, no such canonical owner exists.

Creating an `external-failure-analysis/index.json` after one positive example would be new
canonical complexity, not merely packaging.

### Decision

**DEFER PENDING ORTHOGONAL REPLICATION.**

A second materially different external failure can test whether:

- the same packet elements recur;
- `NO_EXISTING_CLASS_MATCH` remains useful;
- boundary/source-state/regression fields have stable semantics;
- a separate analysis layer solves repeated work rather than one example.

## Architecture option D — new canonical failure-packet object/schema

This is the strongest-complexity option.

It would promote the failure-analysis packet itself into a new canonical object.

That would create new ownership rules for:

- mechanism;
- evidence;
- boundary;
- source state;
- scientific status;
- regression conversion.

#339 does not demonstrate that existing owners cannot preserve those distinctions.

Indeed, #339 succeeded using:

- ordinary public legal sources;
- the accepted use-result owner;
- existing Needle protocol/governance;
- current class/corpus owners.

### Decision

**REJECT.**

The simpler owners did not fail.

## Selected v0.2 design

# **V02_DOC_NAV_ONLY**

Reference Pack v0.2 should be a **self-contained documentation/navigation improvement over
the same frozen corpus reference**, not a new scientific data layer.

### Proposed file set

Keep:

- `README.md`;
- `manifest.json`;
- `cases.jsonl`;
- `classes.json`;
- `evidence-map.json`;
- `catalog.md`;
- `checksums.sha256`.

Add exactly:

- `failure-analysis-guide.md`.

No:

- `analysis-packets.jsonl`;
- external-failure database;
- new boundary registry;
- new regression-oracle schema;
- new canonical packet object.

### Builder strategy

Prefer a thin v0.2 builder wrapper that **reuses** the proven v0.1 derivation functions and
same frozen source pin.

Do not refactor the v0.1 builder merely for architectural elegance.

Requirements:

- v0.1 output remains byte-identical;
- v0.2 generation remains deterministic;
- network remains unnecessary;
- checksums cover the new guide;
- normal validation confirms membership and frozen source identity.

The existing corpus index remains the membership/data owner.

## Replication decision

### Docs/navigation implementation

**No orthogonal replication is required before implementing the docs/navigation-only
v0.2.**

Reason:

- the guide does not generalize #339 legal facts into a new schema;
- it exposes already accepted durable project rules;
- it makes `NO_EXISTING_CLASS_MATCH` and packet ownership explicit;
- it links #339 as an accepted worked-use owner rather than generalizing from it;
- omission remains the default where no owner exists.

### Structured packet data

**Orthogonal replication is required before any machine-readable external failure packet
layer or new structured field family.**

A second use should be materially different in:

- legal domain / doctrine;
- failure source or category;
- ideally whether an existing class matches.

That replication should test the candidate packet checklist from this design.

## Rights / citation constraint

Issue #307 remains:

> **OWNER_LICENSE_DECISION_REQUIRED**

The repository still has no project license.

Therefore v0.2 may honestly be:

> **publicly inspectable/reference material**

but must not claim:

> **openly licensed reusable material**

unless the owner separately chooses license/citation terms.

This is a release constraint, not a reason to block the technical/documentation design.

## Why this is still a real Reference Pack improvement

The improvement is not "more JSON".

The v0.1 consumer currently has to infer a large part of Needle's actual failure-analysis
method from repository history.

The v0.2 guide makes the demonstrated job explicit:

> take a known legal failure, preserve its scientific/exposure state, refuse forced
> taxonomy, preserve source state and boundaries, and only create a regression contract
> when evidence supports one.

That directly addresses the #339 pack gap.

It is smaller than a packet database and more truthful.

## What would falsify this design

During implementation or orthogonal replication, revise the design if:

- a guide still forces consumers to reconstruct broad project history;
- important packet elements cannot be located from exact owner links;
- repeated external analyses show a stable structured field family whose omission causes
  material reconstruction burden;
- a docs-only pack cannot support the demonstrated evaluator/debugger workflow.

Do not add structured fields merely because they would be convenient.

## Disposition

# **V02_DOC_NAV_ONLY**

Implementation is now earned for the bounded docs/navigation surface only.

Queued implementation:

> **#345 — implement Reference Pack v0.2 failure-analysis navigation surface**

Any structured external-failure layer remains blocked pending orthogonal replication.

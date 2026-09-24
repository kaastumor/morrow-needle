# Cycle 2 Run B — provenance / evidence-closure transfer scan

Issue: #157  
Parent: #155  
Date: 2026-09-24  
Disposition: **PARK**

## Proven Needle anchors

Run B starts from:

- #87 — exact sealed-artifact archival gap;
- #97 — execution-setting provenance could not be independently machine-verified;
- #138 — experiment-local commitment → execution → reveal → closure technique;
- #150 — external reproducibility-contract inconsistency in DELTA's public
  harness documentation.

The question is:

> Where do consequential research artifacts remain substantively plausible while
> their evidence/search/analysis chain cannot later be reconstructed well enough
> to audit the result?

This run deliberately excludes LLM/legal benchmark harnesses so it does not
repeat #150.

## Search branch 1 — systematic-review literature searches

**Strong target evidence.**

A 2024 cross-sectional metaresearch study sampled 100 biomedical systematic
reviews containing 453 database searches.

Reported results included:

- only 22/453 searches reported all six tested PRISMA-S reproducibility items;
- only 47/453 reproduced within 10% of the originally reported result count;
- six reproduced searches differed by more than 1,000%;
- only one systematic review in the sample had all database searches fully
  reproducible under the study's operational definition.

Public evidence:

- https://pubmed.ncbi.nlm.nih.gov/38052277/
- https://doi.org/10.1016/j.jclinepi.2023.111229

This is a real evidence-closure problem: the final evidence synthesis can be
published while later reviewers cannot reconstruct exactly how the evidence set
was obtained.

### Strong existing baseline

The field already has a mature direct response:

**PRISMA-S**.

Its 16 reporting items explicitly target reproducible literature-search
reporting, including:

- databases/platforms;
- full search strategies;
- limits/restrictions;
- search dates;
- updates;
- deduplication;
- all search strategies rather than one representative database.

Reference:

- https://pmc.ncbi.nlm.nih.gov/articles/PMC7839230/

There are also proposals for structured, interoperable search-history records.

Example:

- Haddaway et al., *A suggested data structure for transparent and repeatable
  reporting of bibliographic searching*:
  https://onlinelibrary.wiley.com/doi/10.1002/cl2.1288

### Structural correspondence

The shared mechanism with Needle is genuine:

```text
published conclusion
    ↓
reported evidence/search process
    ↓
later reconstruction attempt
    ↓
missing execution context
    ↓
claim cannot be fully audited/reproduced
```

This is closer to #87/#97/#150 than to ordinary citation quality.

### Important boundary: exact reproduction is not fully under investigator control

Bibliographic databases are mutable systems.

Even with a correctly preserved query:

- indexed holdings change;
- historical records can be added;
- platform syntax/algorithms can change;
- institutional subscriptions may expose different database slices;
- location/environment can affect results in some systems.

Published work has shown identical scientific-literature queries can return
different sets across platforms, institutional environments or time.

References:

- https://pmc.ncbi.nlm.nih.gov/articles/PMC8571571/
- https://link.springer.com/article/10.1186/s13643-024-02472-w

Therefore a naive transfer of Needle's "exact reveal bytes" concept would be
wrong.

For systematic-review searches, a valid closure object would need to preserve
**execution context and observation state**, while accepting that a future
database rerun can legitimately differ.

That is an important negative transfer finding.

## Search branch 2 — government / policy evaluation code

Government-evaluation guidance independently recognises the same general
problem.

The UK Government's TIGER guidance describes open analysis code as central to
computational reproducibility and notes that lack of reproducibility can
undermine evaluation integrity.

Reference:

- https://www.gov.uk/government/publications/the-magenta-book/transparency-in-government-evaluation-research-t-i-g-e-r-html

NIST information-quality guidance likewise ties reproducibility to transparency
about:

- specific data;
- assumptions;
- analytic methods;
- statistical procedures.

Reference:

- https://www.nist.gov/director/nist-information-quality-standards

### Disposition of this branch

**Not retained.**

The structural correspondence is real, but this scan did not find comparably
specific target evidence that a bounded Needle-style closure technique solves a
current government-evaluation failure better than the existing open-code /
information-quality disciplines.

It remains background evidence, not an opportunity.

## Search branch 3 — regulatory real-world evidence

Regulatory/clinical real-world evidence is a high-stakes setting where
reproducibility matters to decision-making.

A large reproducibility study of real-world evidence studies found generally
strong but imperfect reproduction, with incomplete reporting and updated data
helping explain some discrepancies.

Reference:

- https://pmc.ncbi.nlm.nih.gov/articles/PMC9430007/

EMA's recent real-world-evidence transparency work explicitly rejected a
proposal to remove recommendations that analytical code be made public, stating
that code availability matters for replicability/reproducibility.

Reference:

- https://www.ema.europa.eu/system/files/documents/comments/summary-report-outcome-public-consultation-rwe-rp-en.pdf

### Disposition of this branch

**Not retained as a Needle opportunity.**

This domain has its own mature methodology, regulatory expertise and data-model
constraints. A generic Needle closure pack would add little without evidence of
a specific unresolved artifact failure.

## Existing-solution check

The strongest result of Run B is actually counterevidence against premature
transfer.

The target problem is real, but the nearest field already possesses:

- PRISMA-S;
- structured search-history proposals;
- reproducibility studies;
- specialist information-science expertise;
- explicit recognition that database state itself changes.

That means "Needle also cares about provenance" is not enough.

## Surface similarity vs structural correspondence

The genuine transferable idea is not:

> save more metadata.

It is:

> distinguish the historical execution state from what a later rerun can
> observe.

That resembles Needle's source-observation-horizon discipline.

But in systematic searching, this principle already exists in mature reporting
guidance through:

- platform identity;
- exact query;
- search date;
- update history;
- reported result count;
- environment/context where relevant.

The remaining observed problem is largely **adoption/compliance and external
database mutability**, not absence of a conceptual closure method.

## One falsifiable transfer hypothesis

Working label:

`SEARCH_EXECUTION_PROVENANCE_CLOSURE`

Hypothesis:

> A compact execution-closure record layered on top of PRISMA-S would materially
> improve reconstruction of systematic-review searches that already satisfy
> PRISMA-S reporting requirements.

## Boundary test

For this to be a real Needle opportunity, we would need evidence that:

1. reviews already satisfying relevant PRISMA-S items still fail reconstruction;
2. the failure is caused by missing execution-closure state that PRISMA-S does
   not already require;
3. a small additional closure record fixes that failure;
4. the benefit is not simply solved by existing structured search-history
   proposals or database export functionality.

This run did **not** find that evidence.

The strongest metaresearch instead shows that most audited searches fail much
earlier: they do not report the existing required information completely.

## Run B disposition

# **PARK**

The problem is important and structurally relevant.

But the current evidence says:

> mature existing methodology already specifies most of the missing provenance;
> the dominant observed failure is incomplete adoption/reporting plus mutable
> database state.

No experiment is justified yet.

Reopen only if a future target supplies:

- a PRISMA-S-compliant search that is still materially unreconstructable; and
- a specific missing closure dimension not already owned by existing
  information-science practice.

## What this run changed

Run B narrowed the transfer boundary.

Needle's evidence-closure concept should **not** be generalized as:

> every reproducibility problem needs a Needle closure pack.

A stronger reusable principle is:

> first determine whether the failure is missing method, missing compliance with
> an existing method, or unavoidable external-state drift.

Only the first can plausibly justify a new method-level contribution.

No product, schema, search-history format, systematic-review tool or regulatory
RWE workflow is authorised.

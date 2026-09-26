# Issue #327 — real-task post-answer Reference Pack value test

Date: 2026-09-26  
Disposition: **BASELINE_SUFFICIENT**

## Question

On one fresh, mechanically selected real EU legal-information task, solved first with the
strongest ordinary source-grounded method, does a post-answer Needle Reference Pack v0.1
pass add material non-duplicative value for provenance, historical/source-state
reconstruction, repeatability, regression classification or later inspection?

This is a **USE** test. It is not a diagnostic/correctness treatment experiment and does
not reopen #214.

## Precommitted task selection

Before inspecting candidate substance, #327 froze:

- intake: EUR-Lex Official Journal L;
- window: 25 September 2026, falling back to 24 September only if no eligible act existed;
- source order: the day's OJ order;
- eligibility: first English full-text binding Regulation/Directive/Decision;
- exclusions: corrigenda, notices, budget/accounting documents and pure
  agreement-publication notices;
- no topic/class targeting;
- no replacement because a selected task is boring or maps poorly to Needle.

The first eligible act was:

> **Commission Implementing Regulation (EU) 2026/2101 of 24 September 2026 imposing a
> definitive anti-dumping duty and definitively collecting the provisional duty imposed
> on imports of pea protein originating in the People's Republic of China.**

Official OJ publication:
- OJ L, 2026/2101, 25.9.2026;
- CELEX 32026R2101;
- ELI: http://data.europa.eu/eli/reg_impl/2026/2101/oj.

The selection was persisted before any Reference Pack/corpus consultation.

## Stage A — strongest boring baseline

Stage A used ordinary official/source-grounded legal research only.

Primary sources:

1. Regulation 2026/2101:
   http://data.europa.eu/eli/reg_impl/2026/2101/oj
2. predecessor provisional measure, Regulation 2026/916:
   http://data.europa.eu/eli/reg_impl/2026/916/oj
3. Basic Anti-Dumping Regulation (EU) 2016/1036:
   http://data.europa.eu/eli/reg/2016/1036/oj

### Baseline legal answer

Regulation 2026/2101 imposes a definitive anti-dumping duty on high-protein pea protein
originating in China:

- more than 65% protein on a dry-weight basis;
- all physical forms, textured or not;
- precise customs scope controlled by Article 1(1)'s CN/TARIC enumeration.

Definitive rates:

- Sanjia Group: 40.5%;
- Yantai Shuangta Food Co. Ltd.: 67.1%;
- other cooperating Annex producers: 40.5%;
- all other imports from China: 67.1%.

Individual rates require the prescribed valid commercial invoice. Without that invoice,
the residual all-other-imports rate applies.

The act was published on **25 September 2026**. Article 4 makes it enter into force the
following day:

> **26 September 2026**

It is binding in its entirety and directly applicable in all Member States.

### Operative transition

The predecessor Regulation 2026/916 had imposed provisional duties.

Article 2 of the definitive Regulation provides that:

- provisional amounts secured are definitively collected;
- only up to the definitive rate;
- security above the definitive rate is released.

This is practically material because the provisional Shuangta/all-other rate was 67.4%,
while the final rate is 67.1%.

The Commission separately tested retroactive definitive collection for the prior
registration period and found the Article 10(4) condition concerning a further substantial
rise in imports was not met. No additional retroactive collection was therefore imposed.

### New-exporter state

Article 3 permits later amendment of the company-rate list for qualifying new exporters
that satisfy the stated investigation-period, relationship and subsequent-export
conditions.

### Duration

Regulation 2026/2101 has no self-contained fixed end date.

Article 11(2) of the Basic Regulation supplies the governing horizon: definitive
anti-dumping measures normally expire five years from imposition unless a qualifying
expiry review is initiated, in which case the measure remains in force pending the review
outcome.

The ordinary baseline therefore preserved:

- current measure identity;
- predecessor measure identity;
- publication and entry-into-force date;
- product/origin/customs scope;
- company/rate/documentary state;
- provisional-to-definitive transition;
- security collection/release treatment;
- no-retroactive-collection conclusion;
- new-exporter route;
- review/expiry framework;
- source/version state and future-change uncertainty.

Stage A was frozen before Needle consultation.

## Stage B — Reference Pack pass

Only after Stage A was frozen, Reference Pack v0.1 was inspected.

### Candidate 1 — `COHORTED_TRANSITIONAL_APPLICABILITY`

This was the closest superficial fit.

A provisional-duty entry/security position is historical state, and Article 2 gives that
earlier state a specific consequence when the definitive measure arrives.

However, the pack added no missing distinction:

- Stage A had already preserved the predecessor measure;
- it had already recorded the secured provisional amounts;
- it had already recorded definitive collection up to the new rate;
- it had already recorded release of excess security.

Applying the class label would reorganise an already explicit legal fact. It would not add
a new source, answer, evidence requirement or reconstruction state.

Under #327's material-value rule, this is **analogy/terminology only** and does not count.

### Candidate 2 — `STATUS_APPLICATION_SEPARATION`

Rejected.

There is no distinct authoritative status/set-membership state whose downstream
applicability begins or ends at a different boundary. The definitive measure enters into
force and applies through the operative rule itself.

### Candidate 3 — `PARALLEL_INSTRUMENT_LIFECYCLE`

Rejected.

The provisional and definitive anti-dumping regulations are successive procedural
measures in one anti-dumping investigation. They are not parallel legal instruments
behind one umbrella deal whose signature/application/entry-into-force states can be
misattributed between instruments.

### Other classes

The full class-definition surface was reviewed. No closer causal owner supplied a missing
research distinction.

## Material-value test

The pack caused **no non-duplicative change** to the frozen Stage-A record.

It did not add:

- a missing authoritative source;
- a missing date/version state;
- a missing transition;
- a different expected answer;
- a missing uncertainty;
- a provenance correction;
- a historical-reconstruction fact;
- a packaging/navigation defect that impeded supported use.

The only additions available were analogy and vocabulary, which the protocol explicitly
forbids counting as value.

## Result

# **BASELINE_SUFFICIENT**

For this mechanically selected real task, ordinary official/source-grounded research
already preserved everything materially useful that the post-answer Reference Pack pass
could identify.

This is a **bounded null**.

It does **not** establish that:

- Reference Pack v0.1 has no value on all legal tasks;
- Needle cases/classes are invalid;
- corpus/reference material has no regression use;
- ordinary research is always sufficient;
- post-answer use can never reveal a provenance or reconstruction defect.

It does establish that the first precommitted real-use observation may not be converted
into a positive pack-value result merely because some class labels are semantically
adjacent.

## #214 boundary

#214 remains unchanged.

#214 tested a pre-research corpus/index treatment for latent diagnostic/correctness
advantage.

#327 instead froze the ordinary answer first and then tested only the pack's supported
post-answer reference/regression role.

No model, diagnostic or workflow-superiority claim follows.

## Project consequence

Do **not**:

- replace this task with a friendlier one;
- open Reference Pack v0.2 because of this null;
- add the pea-protein task as a corpus case;
- add or revise a trap class;
- market pack analogy as observed use value.

The next allocation must be selected explicitly after this first genuine real-use null.

Queued gate:

> **#329 — direction review after first real USE null**

No corpus, taxonomy, Reference Pack byte or #214 interpretation changes.

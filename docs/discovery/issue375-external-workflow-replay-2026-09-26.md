# Issue #375 — externally defined workflow replay

Date: 2026-09-26  
Mode: **USE / REVIEW — EXTERNALLY DEFINED WORKFLOW REPLAY**

## Purpose

Test the newly adopted evaluation-contract integrity gate against public legal benchmark
tasks that were selected **without Needle taxonomy and without known-defect targeting**.

This is a Needle-readiness exercise, not competitor scoring and not evidence of a
Needle-specific methodological advantage.

## Frozen sample

Selection was committed in Issue #375 before task substance was inspected.

### DELTA

Repository:

> `legalbenchmarks/delta`

Pinned commit:

> `c7131327d24e3167b6c3f9f06a7c5d41e25ac7df`

Rule:

> first complete task in published `data/tasks.jsonl` order

Selected task:

> `competition-law/acm-concentration-notification-requirement`

### Harvey LAB

Repository:

> `harveyai/harvey-labs`

Pinned commit:

> `1dd81403b2fbb60596f7aea3fcecafad7bf73143`

Rule:

> lexicographically first public task directory under `tasks/` containing `task.json`

Selected task:

> `tasks/antitrust-competition/analyze-antitrust-hsr-strategy`

No task was replaced after inspection.

---

# Replay A — DELTA ACM concentration-notification task

## External contract

The task asks when a proposed acquisition must be notified to the Dutch ACM.

It explicitly pins:

> `law_as_of: 2026-08-30`

The rubric requires, among other things:

- Article 29 Mededingingswet;
- combined worldwide turnover above EUR 150 million;
- at least two undertakings each with at least EUR 30 million Dutch turnover;
- cumulative satisfaction of the thresholds;
- ACM as notification authority;
- Article 27 concentration concepts;
- Article 30 turnover calculation;
- sector-specific calculation rules;
- pre-closing notification / standstill;
- concise answer-first structure.

## External source check

Current Dutch primary/public material supports the ordinary threshold core.

Mededingingswet Article 29(1) provides:
- combined prior-year turnover above EUR 150 million;
- at least two undertakings each with at least EUR 30 million Dutch turnover.

Article 27 covers mergers, acquisitions of control and full-function joint ventures.

Article 30 contains general turnover-calculation rules.

Article 31 contains special turnover calculation for financial institutions/insurers and
related entities.

Article 34 contains the standstill rule.

Sources:
- https://wetten.overheid.nl/BWBR0008691/
- https://www.acm.nl/nl/publicaties/acm-past-e-mailadressen-voor-concentratiecontrole-aan

The ACM's 25 August 2026 public explanation likewise states the EUR 150 million /
EUR 30 million ordinary thresholds.

## Integrity-gate result

### Task-to-criterion coverage

> **PASS WITH A BOUNDARY GAP**

The central ordinary-company question is well covered.

However, the rubric can award full credit to language saying the ordinary Article 29(1)
thresholds are the **only** route to notification without requiring a qualification for
special regimes.

Article 29(4) contains a separate pension-fund threshold based on gross written premiums:
- combined amount above EUR 500 million;
- at least two funds each above EUR 100 million received from Dutch residents.

The wider Dutch/EU merger-control framework also contains jurisdictional/exclusion
boundaries beyond the two ordinary domestic turnover figures.

The task may intentionally target an ordinary company, so this is **not classified as a
material benchmark failure**.

But a safer criterion would scope the universal statement explicitly:

> for an ordinary non-special-regime transaction within Dutch national concentration
> control...

rather than grading "notification is required only if both conditions are met" without a
boundary qualifier.

### Criterion evidence correctness

> **PASS FOR THE CORE RULE**

No wrong article/threshold was found in the central Article 29(1), Article 27 or Article 30
contract.

### Activation / gradability

> **PASS**

Criteria are directly activated by the broad research question and do not contain the kind
of undefined inactive conditional found in the earlier public DELTA maintenance issue.

### Cross-criterion consistency

> **PASS**

The ordinary threshold, concentration-definition and timing criteria are mutually coherent.

### Semantic/temporal control

> **STRONG**

The explicit `law_as_of` field materially improves auditability and protects the score from
silent current-law drift.

## DELTA disposition

> **CLEAN_CORE_WITH_SCOPE_BOUNDARY**

No consequential scoring defect was established in the mechanically selected task.

The result is useful as a control:

> the Needle integrity gate can return a near-null instead of manufacturing a defect.

---

# Replay B — Harvey LAB antitrust / HSR strategy task

## External contract

The task asks for an antitrust-risk and HSR filing-strategy memorandum for a private-equity
acquisition.

The packaged facts and rubric place the proposed transaction in 2025:
- purchase agreement dated 14 April 2025;
- target closing date 1 August 2025;
- outside date 31 October 2025;
- rubric explicitly discusses the HSR form effective in February 2025.

The task contains 50 pass/fail criteria.

Unlike DELTA, `task.json` has no explicit `law_as_of` or other declared legal cut-off.

## Material criterion-evidence defects

### C-040 — wrong 2025 HSR size-of-transaction threshold

The rubric says:

> the 2025 HSR size-of-transaction threshold is USD 119.5 million.

That is the **2024** adjusted threshold.

FTC's 2025 schedule states that, effective **21 February 2025**, the minimum
size-of-transaction threshold increased to:

> **USD 126.4 million**

Source:
https://www.ftc.gov/enforcement/competition-matters/2025/02/new-hsr-thresholds-filing-fees-2025

The deal is framed around April-August 2025, after the 2025 threshold became effective.

Therefore a legally correct 2025 memo can be failed for refusing the stale USD 119.5
million number.

Disposition:

> **MATERIAL CRITERION-EVIDENCE ERROR**

### C-039 — wrong filing fee for the USD 425 million deal

The rubric requires:

> **USD 160,000**

as the filing fee.

FTC's 2025 fee schedule, effective 21 February 2025, places a USD 425 million transaction
in the band:

> not less than USD 179.4 million but less than USD 555.5 million

with a filing fee of:

> **USD 105,000**

Source:
https://www.ftc.gov/enforcement/competition-matters/2025/02/new-hsr-thresholds-filing-fees-2025

The 2024 schedule also used USD 105,000 for the comparable USD 173.3-536.5 million band.

Source:
https://www.ftc.gov/enforcement/competition-matters/2024/02/new-hsr-thresholds-filing-fees-2024

No support was found for USD 160,000 as the applicable fee for this 2025 USD 425 million
transaction.

Disposition:

> **MATERIAL CRITERION-EVIDENCE ERROR**

## Temporal-contract defect

The stale values are made more dangerous by the absence of an explicit legal cut-off.

By 2026:
- the HSR size-of-transaction threshold is USD 133.9 million;
- the fee for a transaction in the USD 189.6-586.9 million band is USD 110,000;
- HSR-form status itself experienced litigation/administrative changes during 2026.

Sources:
- https://www.ftc.gov/enforcement/competition-matters/2026/01/new-hsr-thresholds-filing-fees-2026
- https://www.ftc.gov/enforcement/premerger-notification-program

A legal benchmark may legitimately ask for a historical 2025 answer.

But it must say so in the score-bearing task contract.

Otherwise a current-law researcher and a historical transaction-time researcher can follow
different defensible temporal perspectives while the fixed rubric silently rewards only one.

Disposition:

> **MISSING LEGAL-TIME OWNER**

## Why this is consequential

This is not a style or taxonomy issue.

A response can:
- correctly apply authoritative 2025 FTC thresholds/fees;
- give the right reportability conclusion;
- provide an otherwise excellent HSR strategy;

and still receive two FAILs because the evaluator contract owns stale numbers.

Conversely, repeating stale numbers can receive PASS.

That is exactly the failure form the integrity gate is supposed to prevent:

> the evaluation contract itself becomes a source of legal error.

## Other integrity dimensions

### Task-to-criterion coverage

The 50-criterion rubric is extensive and appears to cover the requested work-product
categories.

This replay did not exhaustively re-audit every packaged business fact.

### Activation / gradability

Most criteria are explicit binary conditions.

No result is needed from a conditional criterion whose inactive state is undefined for the
two material findings above.

### Cross-criterion consistency

The two HSR-number defects are source/currentness errors rather than an internal count
contradiction.

### Execution validity

No harness run was performed.

This is a contract audit only.

### Upstream status

A post-discovery GitHub issue search found no existing Harvey LAB issue mentioning:
- this selected task slug;
- the USD 119.5 million threshold;
- the USD 160,000 fee;
- C-039/C-040.

No upstream issue or PR is created by Needle.

## Harvey disposition

> **MATERIAL_EVALUATION_CONTRACT_DEFECT**

---

# Cross-task result

The mechanically selected two-task replay produced:

| External task | Result |
| --- | --- |
| DELTA ACM notification | **CLEAN_CORE_WITH_SCOPE_BOUNDARY** |
| Harvey LAB HSR strategy | **MATERIAL_EVALUATION_CONTRACT_DEFECT** |

This is a stronger outcome than selecting known broken tasks:

- the DELTA control shows the gate can preserve a near-null;
- the Harvey task demonstrates that a consequential source/time error can survive a large,
  sophisticated, actively maintained rubric.

Harvey's public commit history shows the selected task was included in a May 2026 task
quality/content-polish change, so the defect cannot be dismissed merely as an untouched
ancient fixture.

That does **not** establish that Needle is better than Harvey LAB or DELTA.

It establishes that the integrity rule earned from external failures transfers to a
mechanically selected, previously uninspected task.

---

# Earned Needle honing

The existing integrity gate is sharpened with a specific legal-evaluation rule:

## Legal-time ownership

Every score-bearing legal evaluation must identify its intended legal perspective when the
law, threshold, fee, deadline, source state or authority could change.

Use at least one of:
- explicit `law_as_of`;
- explicit historical event/transaction date that controls the answer;
- an equally unambiguous temporal contract.

For every score-bearing mutable legal literal such as:
- monetary threshold;
- filing fee;
- deadline;
- effective/application date;
- jurisdictional list/status;

preserve:
- the authoritative evidence owner;
- effective date/period;
- the task-contract date to which it is compared.

Do not let a bare number become an unowned evaluator truth.

If the external law changes:
- a historical task may remain valid if its time perspective is explicit;
- a current-law task must be revalidated/versioned before new scores are compared;
- do not silently treat a legal-state change as model-performance change.

This is ordinary evaluation integrity, not a proprietary Needle method claim.

---

# Effect on pre-partner readiness

The external workflow replay supports a real improvement in Needle's readiness.

Needle is now better positioned to answer:

> is this legal-AI evaluation itself legally and temporally trustworthy?

But the finding still does **not** establish:
- buyer demand;
- commercial advantage;
- lower expert cost;
- a proprietary moat;
- superiority of the 81-case corpus or 26-class taxonomy.

The right next step is therefore the final pre-partner readiness red team rather than
another class/corpus expansion.

## Final replay disposition

# **EXTERNAL_REPLAY_EARNS_INTEGRITY_HONING**

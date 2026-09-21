# Pre-analysis adversarial audit v0.1

Status: **ACTIVE — findings ledger, not final verdict**  
Issue: #29  
Started: 2026-09-22

## Purpose

This audit is a falsification and sanitation gate between the completed product
checkpoint and any new analytic expansion.

The attack order is deliberately smallest → biggest:

1. byte / parser / source assumptions;
2. canonical identity and evidence ownership;
3. integration and operational state;
4. product truthfulness;
5. analytical usefulness;
6. external novelty and public-interest thesis;
7. repository / CI / backlog / autonomous-worker sanitation.

Passing tests is not sufficient. Every layer needs an explicit adversary and a
documented negative result if it survives.

## Current scorecard

| ID | Layer | Finding | Severity | State | Contract impact |
|---|---|---|---|---|---|
| A-01 | Source observation | Metadata-route failure could project successful legal-text retrieval as source unavailable | High | FIXED `6d0aa94` | No interface reopening |
| A-02 | Authentic-cause parser | Bare prior Annex mention could authorize later amendment-shaped prose as VERIFIED mutation | High | FIXED `7438a84` | No interface reopening |
| S-01 | Repository status | README still named closed Issue #21 as current priority | Medium | FIXED `6d0aa94` | Documentation only |
| N-01 | Novelty thesis | “EU legal-change monitoring / diff / corroboration / grounded explanation” is not novel | Thesis-level | CLAIM NARROWED | Strategic, not domain contract |

## 1. Byte / parser / source assumptions

### A-01 — route failure was conflated with source availability

**Adversary**

- Cellar RDF tree-notice request fails.
- A supported official legal-text representation still succeeds.
- Ask whether Needle treats the legal source itself as unavailable.

**Before**

`reobserve_event()` derived `snapshot.available` from the metadata HTTP response
alone. Successful official legal-text retrieval could therefore still project
`available=false`. A later comparison could classify this as an availability
change rather than a partial observation.

This contradicted an already-frozen audit finding: preferred/source-route
failure is not source or legal absence.

**Repair**

Commit `6d0aa94` defines availability as the existence of at least one supported
official observation. Content-only and metadata-only retrievals remain
`PARTIAL_OBSERVATION`; the missing comparison dimension remains null and
downstream logic must abstain where necessary.

Permanent regression: metadata 503 + successful FMX4 retrieval.

**Result**

Existing source-state contract survives. Adapter implementation was wrong.

### A-02 — lexical amendment shape lacked authorizing context

**Adversary**

Flattened authentic text contains:

- an earlier bare “Annex V” reference;
- later explanatory/report/quoted prose that happens to match the keyed-row
  insertion grammar.

Ask whether that is enough to create a VERIFIED authentic-cause mutation.

**Before**

Yes. The recurring authentic candidate adapter selected the nearest preceding
bare Annex token and used it as the parent for an otherwise matching insertion
command.

That is too weak for a route that can produce `LEGAL_CHANGE_VERIFIED`.

**Repair**

Commit `7438a84` now requires an explicit local heading:

- `Annex <X> is amended:`, or
- `Annex <X> is amended as follows:`.

A bare contextual Annex mention cannot authorize the command.

The real Regulation (EU) 2026/2104 live case, generic replay, foundation audit
and unit suite remain green.

**Result**

Existing evidence contract survives. Operational parser admitted insufficient
context.

### Open micro-risk M-01 — flattened text still loses structural authority

The recurring authentic-cause adapter works over deterministic visible text
flattened from structured source files. The A-02 repair strengthens lexical
authorization, but a sufficiently exact quotation of a full amendment heading
plus command could still be indistinguishable from operative drafting after
flattening.

Do **not** solve this by adding more regex heuristics.

Before Issue #29 closes, test whether Formex structural context can be retained
transiently so a VERIFIED authentic instruction carries a source-local
structural locator. If not, record this as a bounded residual risk and keep the
parser family narrow.

## 2. Canonical identity / evidence ownership

### Survived so far

The following boundaries have already resisted the operational adversaries
encountered in this run:

- immutable Source Observation identity remains separate from semantic mutation
  identity;
- legal publication date remains separate from feed ingestion / source-system
  timestamps;
- repeated re-observation does not create a new temporal fact;
- cross-CELEX publication binding is rejected;
- compound authentic acts group only for delivery while preserving separate
  mutation identities;
- source metadata-only change remains source audit truth rather than legal
  mutation truth.

These are **not final passes**. Dedicated cross-binding / collision attacks
remain required.

## 3. Integration / operational state

### Survived so far

The product checkpoint recovered a genuine production audit case from operational
cycle `d50b8ee2`:

- CELEX `62025CJ0322`;
- pre-event baseline: ELIGIBLE;
- re-observation: OBSERVED;
- legal content hash unchanged;
- metadata hash changed;
- classification: `METADATA_ONLY`;
- disposition: `SOURCE_METADATA_ONLY`;
- stream: `AUDIT_FEED`.

This demonstrates that the pipeline can positively say “official source metadata
changed while the observed legal text did not” without manufacturing legal news.

Still to attack:

- concurrent monitor/state promotion;
- duplicate event delivery across poll overlaps;
- cursor recovery after partial workflow failure;
- baseline contamination by post-event state;
- stale branch/workflow semantics;
- state-file growth and boundedness.

## 4. Product truthfulness

Issue #27 is complete with three real operational classes:

1. verified legal change — Regulation (EU) 2026/2104;
2. positive source audit / non-change — CELEX 62025CJ0322;
3. explicit abstention — real no-CELEX/no-baseline Cellar burst.

Provisional checkpoint conclusion:

> Human-readable Source Mode presentation over existing provenance is the only
> product gap repeated across all three classes.

Affected-entity truth is a real gap in the verified-change case, but it is not
yet a repeated cross-class need.

This conclusion is **input to this adversary, not a roadmap decision**.

## 5. Analytical usefulness

Not yet passed.

Every existing or proposed analytic primitive must answer:

1. Which recurring user question does it answer?
2. Can existing canonical objects answer it without another schema?
3. Does it expose information a normal source/version comparison cannot?
4. Does its uncertainty model prevent a misleading answer?
5. Is it useful often enough to justify permanent architecture?

Issue #29 may delete or defer analytic surface area that fails this test.

## 6. External novelty adversary

### N-01 — broad novelty claim rejected

A broad claim such as “Needle uniquely watches EU law, detects amendments,
compares versions, corroborates changes and explains them with traceable
evidence” does **not** survive current external comparison.

#### Official baseline: EUR-Lex / OEIL

EUR-Lex already supports:

- email and RSS alerts for document modifications;
- subsequent preparatory acts;
- case-law affecting a document;
- new consolidated versions;
- related/legal-basis documents;
- consolidated-version lists and timelines.

The European Parliament Legislative Observatory already provides procedure
records, chronology, saved-search subscriptions and update notifications.

Sources checked 2026-09-22:

- https://eur-lex.europa.eu/content/help/my-eurlex/my-email-alerts.html?locale=en
- https://eur-lex.europa.eu/content/help/my-eurlex/my-rss-feeds.html?locale=en
- https://eur-lex.europa.eu/content/online-learning/eurlex-content/finding-consolidated-texts.html?locale=en
- https://oeil.europarl.europa.eu/oeil/en/find-out-more

#### Legal research / regulatory intelligence baseline

vLex already exposes amended versions, side-by-side change comparison and
amending/amended relationships.

Corlytics provides regulatory monitoring, real-time content, horizon scanning,
impact-assessment workflow and APIs.

FiscalNote PolicyNote added AI-powered bill comparison for version changes and
policy implications.

Sources checked 2026-09-22:

- https://support.vlex.com/document-types/legislation/versions-and-amendments
- https://www.corlytics.com/solutions/regulatory-monitoring/
- https://fiscalnote.com/newsroom/fiscalnote-introduces-ai-powered-bill-comparison-in-policynote

#### Strongest direct substitute found: emendrix

emendrix is a direct architectural adversary, not a category-level comparison.

Its published methodology says it:

- watches the Publications Office notification feed by identifier;
- fetches consolidated versions and amending acts as Formex 4 XML;
- computes structural provision-tree diffs deterministically;
- cross-checks against EU amendment metadata;
- parses amending-act instruction prose as another signal;
- surfaces disagreement between sources instead of hiding it;
- keeps “first seen” separate from legal dates;
- records in-force and bounded applies-from information;
- constrains model explanation to supplied verbatim text;
- deterministically gates citations;
- commits results and evaluation artifacts to repositories before rendering.

Source checked 2026-09-22:

- https://emendrix.eu/methodology/
- https://emendrix.eu/about/

Therefore the **core operational loop itself is not a defensible Needle novelty
claim**.

### Candidate narrower differentiation — not yet proven novel

Needle currently goes materially beyond the comparison surface above in some
dimensions:

- multidimensional temporal truth: publication, legal force, application,
  transition, derogation, deadlines and source-as-of are separate;
- context-required / entity-specific applicability and retroactivity;
- language-scoped corrigenda and multilingual mutation histories;
- provision vs proposition/rule lineage;
- semantic Change Atoms (for example duty / permission / legal-status changes);
- dependency ripple where local text is unchanged;
- Source Anomaly as source-state intelligence;
- explicit operational abstention and non-impact as first-class output;
- typed procedural state distinct from legal force/application;
- append-only claim-support provenance rather than only rendered-source links.

The audit must **not** combine those into a new vague novelty slogan. Each must be
tested for:

1. whether a strong substitute already provides it;
2. whether Needle has demonstrated it with official evidence;
3. whether it changes a user decision or understanding;
4. whether the capability is worth its architectural cost.

Current bounded thesis:

> Needle is not novel because it tracks EU legal change. Its possible
> differentiation is an evidence-typed, temporally explicit legal-state model
> that can explain not only textual version differences but also when a claim is
> unsupported, source-only, semantically changed, context-dependent, or
> indirectly affected.

That thesis remains **provisional and under attack**.

### Particularly important external warning

emendrix already demonstrates an unusually similar epistemic posture: source
disagreement is preserved, legal dates are distinguished from detection dates,
model explanation does not decide change truth, and evaluation claims are
explicitly bounded.

Needle must therefore not claim that “evidence-first”, “deterministic change
detection”, “grounded explanation”, or “preserving disagreement” alone is its
novelty.

## 7. Repository / CI / autonomy sanitation

### Fixed

- README strategic status was stale and still pointed to Issue #21. Corrected
  in `6d0aa94`.
- Branch-triggered stateful Operational Needle monitor had previously reset to
  `origin/main`, producing misleading branch-green signals. Fixed before this
  audit in `3ad4f36`: push trigger is now main-only.

### Inventory

At audit start:

- ~62 source-tree entries;
- 45 tests;
- 28 scripts;
- 42 schemas;
- 81 fixture entries;
- 35 docs entries;
- 24 workflows.

The only intentional recurring GitHub source monitor is
`operational-monitor.yml`, scheduled every six hours. The separate ChatGPT
`Morrow Needle Build Loop` runs hourly and has been explicitly instructed to
honour Issue #29 as a hard gate.

### Workflow classification still required

Do not delete merely because a workflow has “discovery” in its name.

Classify every workflow into one of:

- **canonical regression** — must run on relevant code/data changes;
- **live integration regression** — valuable but network-dependent;
- **manual discovery/probe** — should not masquerade as CI;
- **stateful production/operational job** — must be main/schedule-safe;
- **obsolete/superseded** — remove or archive with provenance note.

Early observation: pure discovery workflows are mostly narrowly path-triggered,
so they are clutter rather than a current correctness hazard. The audit should
prioritise misleading execution semantics over cosmetic reduction.

## Next attacks

1. preserve source-local structure/locator for authentic-cause verification or
   explicitly bound the residual flattened-text risk;
2. adversarially test identity and temporal cross-binding beyond the already
   regressed CELEX case;
3. attack operational state promotion/concurrency and cursor recovery;
4. classify all workflows/scripts and remove only demonstrably obsolete
   machinery;
5. compare the candidate narrower differentiators against emendrix and other
   direct substitutes;
6. test whether Source Mode presentation resolution still deserves to be the
   next product investment;
7. rewrite BACKLOG.md only after these attacks decide the next architecture.

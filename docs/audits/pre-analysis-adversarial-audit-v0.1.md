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
| A-03 | Operational baseline | Partial re-observation could replace a complete comparator baseline | High | FIXED `b05113d` | No interface reopening |
| A-04 | Source-change semantics | Cellar DELETE was promoted from ingestion action to source availability truth | High | FIXED `ba3f3ae` | Bounded P1-B semantic correction; schema unchanged |
| A-05 | Authentic source locality | Cross-stream flattened text could combine authority context and amendment prose | High | FIXED `dc357bc` | No schema change |
| A-06 | Source Mode evidence closure | Public card could point to non-persisted Operational Result / partial evidence | High | FIXED `324924f` | Process/provenance persistence only |
| A-07 | Operational cache | Processed-event dedupe history grew without a retention horizon | Medium | FIXED `b248331`; live verified | Hot-cache policy only |
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

### A-03 — partial source observation could poison the next comparator

A-01 correctly established that a content-only or metadata-only observation can
still prove source availability. The recurring monitor, however, would then have
advanced its prospective baseline to that partial snapshot.

That meant a transient route outage could discard a previously complete
comparison dimension and weaken every later source comparison.

Commit `b05113d` separates availability from comparator eligibility:

- partial observations remain operational evidence;
- only complete `OBSERVED` re-observations with both immutable content and
  metadata observations may replace the prospective baseline.

Full unit tests, Operational Needle vertical slice and Post-P1 foundation audit
passed.

### A-04 — DELETE ingestion action was treated as public availability truth

The official Cellar notification documentation defines CREATE / UPDATE / DELETE
as **types of ingestion action** and the service as a history of performed
ingestion actions. The implementation nevertheless returned
`AVAILABILITY_CHANGED` unconditionally for DELETE and skipped targeted
re-observation.

That contradicted the same P1-B decision's stronger rule that the feed is a
change-hint stream which schedules source observation, and the frozen Source
Anomaly rule that route failure is not source absence.

Commit `ba3f3ae` makes a bounded semantic correction:

- DELETE remains preserved as authoritative Cellar ingestion-history evidence;
- DELETE now triggers targeted re-observation when addressable;
- `AVAILABILITY_CHANGED` requires independently observed previous/current
  availability states;
- failed preferred-route observation is unresolved, not `available=false`;
- `source-change-v0.1` schema is unchanged.

The Cellar update-detection decision doc now records the correction explicitly.

### A-05 — source-local authority boundaries

A-02 still left one concrete risk: Formex archive entries were flattened into
one analysis string. An explicit amendment heading in one XML stream could
therefore authorize amendment-shaped prose in another stream.

The current candidate repair keeps transient analysis segments per archive
entry and makes authentic candidate generation operate inside those source-local
boundaries. Positive candidates retain an archive-entry locator.

Commit `dc357bc` keeps transient analysis segmented by archive entry and makes
authentic candidate generation operate within each source-local segment. A
heading in `TOC.xml` can no longer authorize a command in `REPORT.xml`.
Positive evidence retains an exact archive-entry locator.

Unit tests, live Cellar contract, Operational Needle vertical slice, Post-P1
foundation audit and the live 2026/2104 replay all remained green.

Residual risk after segmentation: a verbatim quotation of both the authorizing
heading and command within the same source stream may still be lexically
indistinguishable from operative drafting. Do not solve that by regex accretion;
either retain stronger Formex structural authority or keep the parser family
explicitly bounded.


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

### Identity / temporal cross-binding adversary — current production path survives

The generic `derive_operational_relevance()` helper intentionally assumes its
caller supplies temporal assertions already bound to the relevant legal
analysis. That looked like a cross-binding hazard because the helper itself does
not inspect assertion subject identity.

The current recurring production path does **not** expose that precondition
directly:

1. publication metadata is projected from the same immutable re-observation as
   the authentic legal text;
2. `derive_publication_recency_from_reobservation()` checks the temporal
   assertion's CELEX subject against the re-observed CELEX;
3. the resulting recency object is bound to the exact
   `legal_analysis_identity`;
4. a recency object for a different legal-analysis identity is rejected;
5. source-diff verified changes do not inherit the authentic act's publication
   assertion through this route.

Existing adversaries cover cross-CELEX publication, cross-analysis recency and
verification-route mismatch.

**Result:** negative finding. The production boundary currently fails closed.
Do not add a new binding abstraction merely to remove an internal documented
precondition unless another caller makes that precondition externally unsafe.

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

### A-06 — latest public card evidence closure was not durable

The monitor built complete Operational Result objects but only committed cards,
state and the summary report. A card's `operational_result_id` could therefore
refer to a process object that disappeared when the job ended. In addition,
partial re-observation Source Observations were dropped unless the observation
was complete enough to seed a prospective baseline.

Commit `324924f` separates these concerns:

- all valid re-observed Source Observations are retained as provenance even if
  they cannot seed a baseline;
- latest Operational Results are persisted and promoted alongside latest cards;
- baseline advancement remains separately strict under A-03.

The first post-merge main monitor run completed successfully. It had zero new
events, so latest cards/results were correctly empty while the new promotion
path itself was exercised.

Product consequence: a human-readable Source Mode resolver was one layer too
early. Durable evidence closure had to exist before presentation resolution
could be honest.

### A-07 / S-02 — hot event-dedupe state had no retention horizon

Measured operational state grew from roughly 8 KB at pilot start to 6.86 MB in
about 28 hours. The dominant avoidable component was 55,143 historical
`processed_event_keys`, despite the feed poller's overlap being only five
minutes.

Commit `b248331` bounds dedupe retention to event keys that can legitimately
recur in the *next* overlap query. It does not prune baselines or immutable
Source Observations.

First real post-merge monitor cycle:

- processed keys: 55,143 → 0 (the overlap window was empty);
- compact JSON bytes: 6,216,356 → 1,665,915;
- checked-in pretty state: ~6.86 MB → ~2.04 MB;
- baselines: 854 → 854;
- Source Observations: 1,643 → 1,643.

**Result:** the urgent cache bloat was stale dedupe history, not evidence that
required a database. Continue measuring before introducing storage
infrastructure.

### Operational promotion / concurrency adversary — current workflow survives

The stateful monitor:

- runs with one main concurrency group and `cancel-in-progress: false`;
- begins from fresh `origin/main`;
- advances the cursor only after a complete processing cycle;
- checks the remote cursor immediately before promotion;
- skips stale promotion when another completed cycle has advanced the cursor;
- lets an ordinary git push conflict fail rather than silently overwrite newer
  main state.

This is not a transactional database, but under the current single-writer pilot
it fails toward replay rather than silent event loss.

**Result:** negative finding at current scale. Do not replace the mechanism
without an observed race or scale requirement.

Still to attack:

- workflow/script classification and removal of truly obsolete machinery;
- growth of baseline/provenance state after dedupe compaction;
- behaviour after a real partial monitor failure rather than only structural
  inspection.

Baseline contamination by partial post-event state was attacked and fixed in
A-03. DELETE/source-availability conflation was attacked and fixed in A-04.

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

### Capability-by-capability novelty correction

The audit now rejects several tempting claims individually rather than replacing
one broad novelty slogan with another.

| Needle capability | External adversary | Audit position |
|---|---|---|
| Monitoring / structural legal diff / corroboration / grounded explanation | emendrix, EUR-Lex, vLex and commercial regulatory intelligence | **Not novel** |
| Source disagreement / no-text / unknown applicability presentation | emendrix already ships these explicitly | **Not novel by itself** |
| Human-readable evidence links / Source Mode presentation | emendrix already exposes clickable provision evidence and official links | **Necessary product parity, not a moat** |
| Obligation / permission / prohibition representation | EU Legal Obligation Metadata Ontology (LOMO), LegalRuleML and Rules-as-Code systems | **Not novel as a representation problem** |
| Point-in-time legislation / temporal validity | long-established legislative information systems and Rules-as-Code work | **Not novel by itself** |
| Cross-reference dependency graphs / change propagation | legislation drafting systems, regulatory change-propagation models and current Rules-as-Code research | **Not novel as a graph concept** |
| Multilingual legal discrepancies / aligned EU-language corpora | longstanding EU-law doctrine and DGT multilingual resources | **Not novel as a problem or corpus** |

What may still be differentiated is **the way these dimensions are composed and
evidence-gated**, especially where Needle refuses to collapse text change,
semantic rule change, applicability, source state, language scope and indirect
dependency effect into one generic “regulatory change” object.

Sources added 2026-09-22:

- EU LOMO: https://drpm.pages.code.europa.eu/lomo/latest/
- LegalRuleML: https://docs.oasis-open.org/legalruleml/
- OECD Law as Code consultation:
  https://www.oecd.org/en/events/public-consultations/2026/07/consultation-on-the-digital-provision-of-law-towards-a-shared-reference-framework-for-law-as-code.html
- Rules-as-Code temporal/norm framework:
  https://regels.overheid.nl/blog/18/building-a-framework-for-norms-and-rules
- RegelRecht dependency-graph research:
  https://docs.regelrecht.rijks.app/research/rules-as-executed
- EU drafting handbook (cross-reference repercussions):
  https://www.consilium.europa.eu/media/67390/joint_handbook_en_01-october-2023_clean_def_final.pdf
- DGT multilingual resources:
  https://translation.ec.europa.eu/tools-and-resources/resources-language-professionals_en

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

1. classify all workflows/scripts and remove only demonstrably obsolete or
   misleading machinery;
2. test the remaining candidate differentiators for **incremental user value**,
   not merely technical distinctness:
   - Legislative X-Ray / dependency ripple;
   - Half-Life / temporary-regime history;
   - multilingual corrigenda state;
   - semantic Change Atoms over time;
3. challenge whether Source Mode presentation is merely required parity with
   emendrix rather than the next strategic investment;
4. bound the residual same-stream authentic-quotation risk;
5. observe baseline/provenance growth after A-07 before making any storage
   architecture decision;
6. rewrite BACKLOG.md only after these attacks decide the next architecture.

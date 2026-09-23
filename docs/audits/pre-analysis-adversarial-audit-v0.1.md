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
| A-05 | Authentic source locality | Cross-stream flattened text could combine authority context and amendment prose | High | FIXED `dc357bd` | No schema change; parser remains deliberately bounded |
| A-06 | Operational promotion | Workflow had an inline cursor race guard but no executable ownership-level CAS contract | High | REVISED in #42 | No architecture/interface reopening; guard extracted and tested |
| A-07 | Evidence ownership | Event/re-observation identity was not cryptographically/semantically bound to the Source Observation used for VERIFIED authentic-cause analysis | High | FIXED in current #29 branch | No identity-schema reopening; adapter now fails closed |
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

Commit `dc357bd` keeps transient analysis segments per archive entry and makes
authentic candidate generation operate inside those source-local boundaries.
Positive candidates retain an archive-entry locator. The negative cross-stream
authorization regression, operational slice, foundation audit and live
Regulation (EU) 2026/2104 path all passed.

**Disposition: revise / fixed.** The evidence contract survives; the adapter was
too lossy.

Residual risk remains explicit: a verbatim quotation of both the authorizing
heading and command within the same Formex stream may still be lexically
indistinguishable from operative drafting. This parser family is therefore
**not** a general legal-instruction recognizer. Do not hide that limitation with
regex accretion; stronger Formex structural authority would need a separate
discriminating experiment before broadening the route.

## 2. Canonical identity / evidence ownership

### A-07 — authentic evidence could be cross-bound across Work/language identity

**Adversary**

Construct an otherwise amendment-shaped re-observation where one or more of the
following disagree:

- the CELEX identifier carried by the feed event;
- the re-observation's CELEX field;
- the immutable Source Observation payload identifier;
- the analysis language and observed content language;
- the sealed Source Observation payload and its stored record hash.

Before this attack, `candidates_from_reobservation()` trusted the
re-observation CELEX plus Source Observation record ID. It did not prove that
the immutable source record actually belonged to the same Work/language and it
did not verify the seal before producing a VERIFIED authentic-cause candidate.

**Repair**

The adapter now requires:

1. a sealed `SOURCE_OBSERVATION`;
2. a valid provenance record hash;
3. CELLAR source ownership;
4. equality between event CELEX, re-observation CELEX and Source Observation
   CELEX;
5. agreement between explicit analysis language and observed content language.

Any mismatch produces no candidate and therefore preserves operational
abstention. Regressions cover cross-CELEX source binding, event/re-observation
mismatch, post-seal payload tampering and language cross-binding.

The full Python suite passes with 418 tests, repository sanitation passes, and
the unchanged production code passed the live 2026/2104 mutation workflow.

**Disposition: revise / fixed.** This was an enforcement defect at the
operational adapter boundary. The frozen typed identity/provenance contracts do
not need reopening.

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

### A-06 — cursor promotion/concurrency adversary

**Adversary**

Issue #42 attacked the stateful monitor at its promotion boundary rather than
assuming workflow serialization was sufficient:

- two cycles derive from the same completed cursor and one promotes first;
- a stale generated snapshot attempts to overwrite newer remote state;
- a failed/partial cycle has not advanced the completed boundary;
- a generated cursor moves backwards;
- an overlap-window event is redelivered while still replayable;
- expired dedupe keys are allowed to fall out without dropping still-replayable
  keys.

**Finding**

The workflow already had an inline compare-and-swap check, so no demonstrated
production overwrite was found. The weakness was that this consequential state
ownership rule existed only as workflow glue and was not independently
executable or regression-tested. That made future edits capable of silently
weakening cursor monotonicity or idempotence.

**Repair / evidence**

#42 extracts the existing rule into `needle.operations.promotion` and makes the
workflow call that exact implementation. Focused regressions prove:

- first same-cursor cycle may promote; the second becomes `STALE_REMOTE`;
- an exact replay is `ALREADY_PROMOTED`;
- equal/backwards generated boundaries are rejected as
  `INVALID_GENERATED_CURSOR`, so failure before completion cannot advance state;
- stale generated state cannot replace a newer remote snapshot;
- `retain_overlap_event_keys` preserves a processed event throughout the
  replayable overlap while permitting genuinely expired keys to leave the
  bounded dedupe set.

Branch Python-unit and Repository-sanitation workflows are green on head
`58bd926`.

**Disposition: revise.** The file/GitHub operational baseline survives; no
queue/database/locking architecture is justified by this attack. The correction
is an enforcement/testability repair at the existing promotion boundary.

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

Baseline contamination by partial post-event state was attacked and fixed in
A-03. DELETE/source-availability conflation was attacked and fixed in A-04.
Cursor/concurrency, partial-completion and overlap-redelivery semantics were
attacked in A-06 and survive with the extracted executable CAS guard.

Still to attack:

- state-file growth and boundedness beyond the replay-window dedupe invariant.

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

### G-01 — project operating system deliberately kept lean

The sponsor supplied a broad long-lived-project operating framework during this
gate. It was treated as an adversary, not copied wholesale.

Decision:

- retain `BACKLOG.md`, GitHub issues, ADRs and audits as the existing project
  spine;
- add only a concise project charter, live material-assumptions register,
  gate-boundary Project Health Check, in-repository hourly-worker runbook and
  lightweight sanitation check;
- explicitly reject parallel roadmaps/boards, story points, generic recurring
  research scans, speculative dependency machinery and infrastructure plans
  without demonstrated need;
- demote the original PostgreSQL/object-store/queue/Next.js sketch from
  “baseline” to superseded future-scale hypothesis.

The purpose is to reduce strategic/autonomous drift without turning governance
into a second project.

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

### G-02 — deterministic CI and live probes were mixed

Issue #43 found a concrete CI-semantics defect in
`cellar-feed.yml`, `cellar-probe.yml` and
`authentic-amendment.yml`: ordinary push runs mixed deterministic repository
regressions with current official-network probes. Branch red/green therefore
partly represented external endpoint availability rather than repository
correctness.

Commit `1c8a540` separates those evidence classes:

- deterministic regressions remain normal push CI;
- live official-source probes are explicit manual `workflow_dispatch` jobs;
- workflow/job names state whether evidence is deterministic or live.

**Disposition: revise.** Discovery/live scripts were retained because they
still have distinct evidence/provenance roles. No scripts were deleted merely
to improve file-count optics. This is the intended sanitation outcome: remove
misleading semantics, not historical evidence.

## Next attacks

1. compare each candidate narrower differentiator against emendrix, Legalize
   and other strong substitutes rather than defending a bundled novelty claim;
2. test existing P2 analytics for recurring user value versus the strong simpler
   baseline, and park/delete future expansion that does not earn its cost;
3. test whether human-readable Source Mode resolution still deserves to be the
   next product investment;
4. run the Project Health Check and choose continue / simplify / redirect /
   stop;
5. reconcile BACKLOG.md, assumptions and remaining issues only after that
   decision.
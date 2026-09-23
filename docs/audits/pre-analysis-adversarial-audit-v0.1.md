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

### Decision rule

A capability does not survive as active product architecture merely because it
is correct or interesting. It must answer a recurring user question better than
the strong simpler baseline in `docs/project-charter.md`, without requiring a
second truth store or disproportionate permanent machinery.

The audit distinguishes:

- **foundation** — required to avoid false legal claims, even if invisible;
- **product view** — useful recurring question over existing canonical truth;
- **diagnostic** — valuable for trust/operations, but not a public-product
  pillar;
- **parked research** — valid idea without enough current product evidence.

### P2 / analytical disposition matrix

| Capability | User question | Evidence from Needle | External pressure | Disposition |
|---|---|---|---|---|
| Thread | “How did this rule become what it is today?” | Full Article 3 chronology with provenance closure and temporal separation | Legal version history is common; Needle's value is the conservative composition, not versioning itself | **SURVIVES** as core historical product view; no new ontology |
| Multidimensional Temporal | “When does this actually matter, and for whom?” | Publication / force / application / text-state / transition / derogation / deadline boundaries; gaps, overlap, retroactivity and context-required cases | Temporal legal models and lifecycle standards already exist; emendrix also distinguishes in-force and bounded applies-from | **SURVIVES as foundation + value candidate**, **not a novelty claim** |
| Change Atoms | “What kind of legal rule changed?” | VERIFIED duty / permission / legal-status atoms tied to mutation and source evidence | Obligation extraction, deontic modelling and text↔rule provenance are established fields | **SURVIVES internally**; reject generic semantic extraction as differentiation; expand taxonomy only from product need |
| Dependency Ripple / X-Ray | “Did this unchanged provision's operation change because something it relies on changed?” | Two independent official cases with unchanged local text and VERIFIED upstream mutation | Change-propagation/dependency-graph concepts exist in regulatory intelligence | **SURVIVES as optional product view** because the question is materially different from text diff; no v0.2 work now |
| Source Anomaly | “Is the strange result caused by the source infrastructure rather than the law?” | Route fallback, source-internal conflict, representation duplication | Source disagreement/provenance is already surfaced by strong substitutes such as emendrix | **REVISE** to trust/audit diagnostic; not a headline public-intelligence pillar |
| Half-Life | “How long has a formally temporary regime persisted through extensions/gaps?” | One strong ePrivacy history with explicit gaps and unresolved terminal/rule continuity | Correct but niche; v0.2 would require additional rule-lineage/terminal machinery before repeated product demand exists | **PARK** after v0.1; close active v0.2 research until a real product case reopens it |
| Rule/proposition lineage | “Did the same rule survive a structural/replacement change?” | P0 fixtures prove why provision identity and rule continuity differ | Legal rule versioning/provenance is established research territory | **SURVIVES as foundation**; **PARK expansion** unless a Thread/product case requires it |
| Multilingual / corrigenda | “Did the legally relevant correction happen only in some language expressions?” | Language-scoped corrigenda with material semantic examples | EU multilingualism and AI/LegalXML corrigenda analysis are established research areas; Legalize is English-only and excludes corrigenda, while the current emendrix public methodology does not expose an equivalent language-scoped mutation history | **SURVIVES as correctness requirement + plausible product differentiation**, not proven novelty |
| Procedural state | “Is this proposal/agreement/adoption/publication actually law yet?” | Orthogonal procedure vector prevents state collapse | OEIL and commercial systems already expose procedure state | **SURVIVES as foundation**; not a novelty/product pillar by itself |
| Provenance / abstention / non-impact | “Why should I believe this, and what could not be established?” | Immutable observations, claim support, positive non-impact and operational abstention | Evidence-first/citation-gated systems already exist | **SURVIVES as product policy and trust foundation**, not a novelty claim |

### P-01 — operational truth is not automatically public-feed value

The latest committed operational report examined in this audit covers:

- 6,680 source events;
- 6,425 new events;
- 343 root groups;
- 0 `CHANGE_FEED` cards;
- 10 `AUDIT_FEED` cards;
- 333 `ABSTENTION_FEED` cards.

That is a positive correctness result: source activity is not laundered into
legal news. It is also a product warning.

A general-interest product that displayed every audit/abstention card would
mostly expose ingestion uncertainty rather than legal intelligence.

**Disposition: revise.**

- `CHANGE_FEED` remains the candidate public-news stream.
- `AUDIT_FEED` and `ABSTENTION_FEED` remain durable/inspectable truth, but
  default to evidence/debug/subscription context rather than general-interest
  publication.
- “abstention is product content” is therefore narrowed to “abstention must be
  inspectable when a user asked about, monitors, or opens the affected source.”
- No canonical stream schema changes in this gate; this is a delivery policy for
  the next product experiment.

### P-02 — Source Mode survives, but the user-facing concept should change

The product checkpoint's repeated gap survives the adversary: all three real
classes benefit when opaque provenance IDs resolve to human-readable official
sources and an explicit explanation of **what each source proves**.

However, “Source Mode” is implementation vocabulary. The useful public concept
is closer to:

> **Evidence — why this is shown, what proves it, and what does not follow.**

This requires no new legal ontology and no new truth store. It is a
presentation resolver over existing provenance and canonical references.

**Disposition: experiment.** This is the smallest next product investment after
#29, but it must be evaluated as comprehension/value rather than shipped as a
new canonical contract.

## 6. External novelty / substitute adversary

### N-01 — broad novelty claim rejected

A broad claim such as “Needle uniquely watches EU law, detects amendments,
compares versions, corroborates changes and explains them with traceable
evidence” does **not** survive external comparison.

Existing official, commercial, open and research systems cover large parts of
that surface:

- EUR-Lex / OEIL: alerts, consolidated versions, document relationships and
  legislative procedure chronology;
- vLex / Corlytics / FiscalNote-class products: version comparison, monitoring,
  horizon scanning and change analysis;
- Legalize: EU laws as versioned Markdown/Git history plus API/change feeds;
- emendrix: Publications Office monitoring, Formex structural diff,
  corroboration against EU metadata and amendment instructions, preserved source
  disagreement, bounded date handling and citation-gated explanation;
- Akoma Ntoso: legal-document lifecycle/modification/versioning;
- LegalRuleML: explicit text↔formal-rule provenance and the need to update rules
  when legal source text changes;
- legal-KG research: temporal/versioned legislation and multilingual legal
  knowledge graphs;
- EU corrigenda research: hybrid AI, semantic annotation and LegalXML analysis;
- regulatory-intelligence literature/products: dependency/change propagation
  and obligation-delta concepts.

Sources rechecked 2026-09-23:

- https://emendrix.eu/methodology/
- https://emendrix.eu/dates/
- https://legalize.dev/eu
- https://docs.oasis-open.org/legaldocml/akn-core/v1.0/akn-core-v1.0-part1-vocabulary.html
- https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/csprd01/legalruleml-core-spec-v1.0-csprd01.html
- https://doi.org/10.1016/j.ipm.2025.104082
- https://doi.org/10.3233/FAIA210319
- https://doi.org/10.26826/law-in-context.v37i1.129
- https://doi.org/10.1007/s10506-021-09282-8

### N-02 — individual primitives are mostly not novelty claims either

Further adversarial comparison rejects several attempted narrower slogans:

- “temporal legal graph” — **not novel**;
- “multilingual legal knowledge graph” — **not novel**;
- “corrigenda analysis” — **not novel**;
- “obligation / duty extraction” — **not novel**;
- “text-to-rule provenance” — **not novel**;
- “dependency / change propagation” — **not novel**;
- “preserve source disagreement / abstain” — **not novel by itself**.

This matters because a project can otherwise survive a failed broad novelty
claim simply by moving the adjective.

### N-03 — bounded project-level verdict

Needle's defensible claim is **not invention of these primitives**.

The remaining thesis is narrower and product-oriented:

> Needle may be valuable because it composes established legal-information
> ideas under unusually strict evidence ownership, legal-time separation and
> fail-closed delivery, so a difficult EU-law change can be explained without
> collapsing source activity, text change, rule change, applicability,
> multilingual correction, derived dependency effect and uncertainty.

Current verdict:

- **Core monitoring / diff / explanation novelty: NOT NOVEL.**
- **Individual legal-informatics primitives: mostly NOT NOVEL.**
- **Needle's integrated legal-state discipline: DEMONSTRATED technically in
  several official cases, but only PLAUSIBLE as product differentiation.**
- **User-value advantage over the strongest baseline: NOT YET PROVEN.**

Accordingly, Needle must not market a novelty claim at this stage. The next gate
must test comparative user value, not search for a smaller unoccupied novelty
phrase.

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
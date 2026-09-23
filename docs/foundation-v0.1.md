# Morrow // Needle — Foundation v0.1

> **Direction note (2026-09-23):** the Morrow Constitution and evidence
> invariants in this document remain canonical. The original product thesis is
> historical context. The current north star is the research/audit charter in
> `docs/project-charter.md`.

## Original product thesis (historical context)

Needle is not a document summarizer.

Its original canonical object was a **change in rules**: what changed, compared
with what, who or what the rule concerns, when the change matters, and the
official evidence needed to verify it.

Research-mode adversaries later proved that some operative legal state changes
without textual mutation. Those facts are now owned by narrow canonical
contracts rather than being forced into the mutation model.

The system maintains three linked histories:

- **Document graph** — what EU institutions published.
- **Rule graph** — what rules and concepts exist at a given time.
- **Mutation graph** — how one state became another.

The original product framing asked **what is changing now**.
The current project asks whether a concrete legal-change claim can be
reconstructed or falsified from official evidence without collapsing distinct
kinds of truth.

---

# The Morrow Constitution

## C1 — Sources outrank models
No model output is authoritative merely because a model produced it confidently.

## C2 — Every consequential claim is traceable to the right evidence class
A claim must resolve to the strongest appropriate primary or official evidence
and, where technically possible, an exact supporting span.

Claims about **legal authority, recognition, validity or public-law consequence**
must resolve to authoritative public-law sources.

A private primary source may directly evidence what a private actor determined;
legal recognition of that determination remains a separate public-law fact.

## C3 — Legal text and interpretation are different data types
Interpretation must never silently become “what the law says.”

## C4 — Proposal is not law
Drafts, proposals, Parliament amendments, Council positions, compromise texts, adopted acts, acts in force, applicable acts, repealed acts, and corrigenda remain distinct states.

## C5 — Recitals are not operative provisions
Recitals may establish context but are not represented as independently creating duties, rights, prohibitions, exemptions, or sanctions.

## C6 — Consolidation is navigation, not canonical authority
Consolidated texts accelerate reconstruction and verification. Canonical mutation lineage points to authentic amending/correcting acts.

## C7 — Time is multidimensional
Model separately:
- document/adoption date;
- publication date;
- entry into force;
- application start/end;
- text-state validity;
- expiry/end of validity;
- observation/ingestion time.

## C8 — Absence is not negation
“No evidence found” does not mean “this did not happen” or “this rule does not exist.”

## C9 — Change always has a comparator
A change is incomplete without an explicit before-state, previous draft, institutional position, or other comparison state.

## C10 — Textual mutation and legal effect are separate
Needle records both what happened to the text and what legal-semantic effect is supported.

## C11 — Uncertainty survives the pipeline
Uncertainty may be reduced by evidence; it may not be discarded for cleaner copy.

## C12 — Evidence states replace fake AI confidence
Allowed evidence states:
- DIRECT
- DERIVED
- CONTEXTUAL
- ATTRIBUTED
- INTERPRETIVE
- UNRESOLVED

## C13 — Language variants matter
EU multilingual law is not modelled as though English were the law itself. Language expressions remain addressable throughout the mutation graph.

## C14 — Corrections are first-class events
Corrigenda can create material legal mutations and may apply only to selected language expressions.

## C15 — Plain language may simplify wording, never legal state
Public explanation may remove jargon but not qualifications or uncertainty.

## C16 — The system may abstain
“We cannot yet determine this reliably” is an acceptable output.

## C17 — Provenance is append-only
Source lineage, ingestion timestamps, hashes, and claim-support links are auditable records. Corrections create new records.

## C18 — Public-interest ranking is explainable
Ranking may use explicit dimensions such as breadth, immediacy, financial magnitude, legal force, novelty, or affected sectors. No opaque “importance” score is editorial truth.

## C19 — Canonical ownership is singular
A consequential fact has one canonical owner. Other contracts and derived views
reference that truth rather than silently copying or reclassifying it. Text,
time, identity, factual findings, metrics, spatial extent, judicial holdings,
procedure and provenance may interact, but interaction is not permission to
collapse them into one object.

---

# Canonical ownership map

The project no longer treats one object tree as the ontology. The more important
question is **which contract owns which kind of truth**.

```
SOURCE / EVIDENCE
├── Source Observation
│   ├── public-official origin
│   └── private-primary origin
└── Provenance Record

DOCUMENT / TEXT
├── Legal Act / Expression / Manifestation
├── Provision Instance / AST State
├── Textual Mutation
└── Language-scoped Correction

IDENTITY / GENEALOGY
├── Identifier Graph
├── Structural Lineage
├── Rule Lineage
└── Regime Lineage

LEGAL / PROCEDURAL STATE
├── Temporal Assertion
├── Procedure State Event
├── Authoritative Dynamic Set
├── Authoritative Metric Observation
├── Authoritative Finding
├── Legal Spatial State
├── Judicial Holding
└── Recognized External Determination

DERIVED LEGAL CLAIMS / EVALUATIONS
├── Change Atom
└── Metric Rule Evaluation

DERIVED AUDIT / PRESENTATION VIEWS
├── Thread
├── Dependency Ripple / Legislative X-Ray
├── Source Anomaly
├── Half-Life
├── Retrieval projections
└── Feed / Evidence projections
```

The map is intentionally about ownership, not a universal graph schema. New
canonical object types are admitted only after an official adversary proves
that existing owners would distort the fact.

---

# Historical reconstruction protocol

For each act:

1. Resolve official identifiers such as CELEX, ELI, Cellar and procedure/interinstitutional references.
2. Retrieve the authentic original act and structured metadata.
3. Retrieve formal relationships: amends, corrected by, repeals, legal basis, implements, delegates, etc.
4. Retrieve consolidated versions as **checkpoints**.
5. Build chronological mutation events from authentic amending acts and corrigenda.
6. Align provisions across states using official subdivision identifiers where available and deterministic structural matching otherwise.
7. Reconstruct text states for material mutation dates.
8. Compare reconstructed states with available consolidated checkpoints.
9. Store discrepancies as audit failures rather than silently selecting a winner.
10. Generate semantic Change Atoms only after verified textual mutation exists.
11. Link negotiation/procedural documents as a separate history layer.
12. Preserve the distinction between enacted-text history, negotiation history, and later interpretation/application history.

Historical certainty is field-specific, not one score:
- text completeness
- metadata completeness
- amendment-chain completeness
- procedure-history completeness
- language coverage
- source authenticity
- provision-alignment quality

---

# Source and authority hierarchy

This hierarchy answers two different questions and they must not collapse:

1. **What is legally authoritative?** Public law and official legal/publication
   sources remain controlling.
2. **What directly evidences an external determination?** In bounded regimes,
   a private primary source can be the best evidence of what the recognized
   private actor decided.

A private primary source never outranks the public law that establishes whether
its output is legally eligible to matter.

## Tier A — legal/publication backbone
- Official Journal / EUR-Lex
- Cellar
- ELI

## Tier B — legislative process
- European Parliament Legislative Observatory (OEIL)
- Council public register
- European Commission Better Regulation / Have Your Say
- Interinstitutional Register of Delegated Acts

## Tier C — legally recognized external/private primary sources
- recognized credit-rating agencies, only for their own rating determinations;
- notified/conformity-assessment bodies, only for their own bounded decisions;
- other non-public actors only when public law supplies a concrete recognition
  basis and a real adversary earns representation.

These sources are primary for the actor's determination, **not legal authority**
for the public-law consequence.

## Tier D — bounded/later expansion
- CURIA / CJEU case law: narrow `judicial-holding-v0.1` is canonical; broader
  citation/precedent/follow-on modeling remains parked
- national transposition sources, national ELI, N-Lex
- EU agencies and regulators
- impact assessments, evaluations and Staff Working Documents
- EESC / Committee of the Regions opinions
- European Court of Auditors material where relevant

---

# Architecture baseline

The logical flow remains:

```
PUBLIC-OFFICIAL + BOUNDED PRIVATE-PRIMARY SOURCES
    ↓
IMMUTABLE SOURCE OBSERVATIONS
    ↓
PUBLIC-LAW RECOGNITION WHERE REQUIRED
    ↓
NORMALISATION + IDENTITY RESOLUTION
    ↓
TEXT / STRUCTURE / TEMPORAL / PROCEDURAL TRUTH
    ↓
VERIFIED MUTATIONS + SEMANTIC / DERIVED VIEWS
    ↓
RETRIEVAL + SOURCE MODE + PUBLIC PROJECTIONS
```

The **implementation baseline is deliberately smaller than the original
aspirational stack proposal**:

- Python + standard libraries / small established dependencies for deterministic
  ingestion and analysis;
- versioned files, fixtures and GitHub for canonical project evidence and
  reproducible research assets;
- a frozen JSON operational-pilot snapshot retained only because it still owns
  historical Source Observations not yet migrated elsewhere;
- manual/live probes and static projections as research/audit surfaces rather
  than a scheduled product-delivery loop;
- no database, queue, object store, vector store, frontend framework or custom
  model-training infrastructure until a concrete current-horizon requirement
  proves the simpler baseline insufficient.

The earlier PostgreSQL/object-storage/queue/Next.js sketch was a hypothesis
about future scale, not an architectural commitment. It is superseded by the
lean rule above.

See `docs/project-charter.md` for the current north star and simpler baseline.

---

# Quality gate for public Change Atoms

A Change Atom cannot be VERIFIED unless:

1. comparator exists;
2. authoritative legal source is identified;
3. provision/evidence span is identified where technically possible;
4. legal/procedural state is known or explicitly UNKNOWN;
5. publication, force, application and text-validity dates are not collapsed;
6. evidence state is assigned;
7. deterministic mutation evidence agrees where applicable;
8. adversarial verification finds no unsupported legal wording;
9. provenance record exists.

---

# Gold Corpus principle

The evaluation corpus must prefer difficult, structurally diverse cases over only famous modern legislation.

Include:
- early Community act;
- repeatedly amended pre-single-market act;
- directive with changing transposition deadlines;
- legally meaningful corrigendum;
- annex-heavy technical act;
- numeric-threshold-only amendment;
- repeal-and-replace chain;
- recast/codification;
- delegated and implementing acts;
- Commission proposal + Parliament + Council variants;
- language-specific correction;
- renumber/split/merge;
- partial expiry;
- repeated temporary derogation.

Each case records expected mutation map, provision alignment, expected Change Atoms, expected non-atoms, and known ambiguity.

---

# Current project principle

**Needle is not a system that reads law and tells people what to think.**

It makes the history, state, mutation, and evidence of rules inspectable enough that non-specialists can see what changed.

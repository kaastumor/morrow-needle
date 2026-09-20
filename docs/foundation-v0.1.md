# Morrow // Needle — Foundation v0.1

## Product thesis

Needle is not a document summarizer.

Its canonical object is a **change in rules**: what changed, compared with what, who or what the rule concerns, when the change matters, and the official evidence needed to verify it.

The system maintains three linked histories:

- **Document graph** — what EU institutions published.
- **Rule graph** — what rules and concepts exist at a given time.
- **Mutation graph** — how one state became another.

Needle answers **what is changing now**.  
Thread answers **how did this rule become what it is today**.

---

# The Morrow Constitution

## C1 — Sources outrank models
No model output is authoritative merely because a model produced it confidently.

## C2 — Every factual legal claim is traceable
A public claim must resolve to an official source and, where technically possible, a provision/subdivision and exact supporting span.

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

---

# Core ontology

```
DOSSIER
├── PROCEDURE
│   ├── EVENT
│   ├── INSTITUTIONAL_POSITION
│   └── PROCEDURAL_DOCUMENT
├── LEGAL_ACT
│   ├── ACT_VERSION
│   │   ├── PROVISION
│   │   │   ├── TEXT_STATE
│   │   │   └── CHANGE_ATOM
│   │   └── ANNEX
│   ├── AMENDING_ACT
│   ├── CORRIGENDUM
│   └── RELATIONSHIP
├── LEGAL_CONCEPT
├── AFFECTED_ENTITY
├── TEMPORAL_EFFECT
├── EVIDENCE
└── PROVENANCE_RECORD
```

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

# Source hierarchy

## Tier A — legal/publication backbone
- Official Journal / EUR-Lex
- Cellar
- ELI

## Tier B — legislative process
- European Parliament Legislative Observatory (OEIL)
- Council public register
- European Commission Better Regulation / Have Your Say
- Interinstitutional Register of Delegated Acts

## Tier C — later expansion
- CURIA / CJEU case law
- national transposition sources, national ELI, N-Lex
- EU agencies and regulators
- impact assessments, evaluations and Staff Working Documents
- EESC / Committee of the Regions opinions
- European Court of Auditors material where relevant

---

# Architecture baseline

```
EU SOURCES
    ↓
RAW IMMUTABLE STORE
(content + source ID + retrieval time + hash)
    ↓
NORMALISATION
(Formex/XML/HTML/PDF → canonical structured document)
    ↓
IDENTITY RESOLUTION
(ELI / CELEX / Cellar / procedure IDs)
    ↓
DOCUMENT GRAPH + PROVISION GRAPH
    ↓
DIFF / MUTATION ENGINE
    ↓
TEXTUAL MUTATIONS
    ↓
CHANGE ATOM EXTRACTION
    ↓
ADVERSARIAL VERIFICATION
    ↓
VERIFIED ATOMS / QUARANTINE
    ↓
PUBLIC API + NEEDLE + THREAD
```

Proposed baseline:
- Python for ingestion/parsing/deterministic transformation
- PostgreSQL as canonical structured store
- immutable object storage for raw source artifacts
- queue/workflow layer for ingestion and reprocessing
- Next.js for public UI
- full-text search first; embeddings as secondary discovery
- LLMs for extraction, classification, explanation and adversarial review, never canonical storage

---

# Quality gate for public Change Atoms

A Change Atom cannot be VERIFIED unless:

1. comparator exists;
2. official source is identified;
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

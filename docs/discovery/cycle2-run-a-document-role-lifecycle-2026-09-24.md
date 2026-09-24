# Cycle 2 Run A — document-role / authority / lifecycle transfer scan

Issue: #156  
Parent: #155  
Date: 2026-09-24  
Disposition: **ADOPT_FOR_EXPERIMENT**

## Proven Needle anchors

Run A starts from three existing evidence families:

- `JUDICIAL_DOCUMENT_ROLE_CONFUSION` candidate from #135;
- `PARALLEL_INSTRUMENT_LIFECYCLE` from #91;
- source-role / authority distinctions already represented in the adversarial
  corpus.

The question is not "where else are there documents?"

It is:

> Where can a document look final/authoritative enough to inherit legal effect
> from a later or different artifact even though its role/lifecycle does not
> permit that inference?

## Search map

Three ecosystems were used to test the analogy.

### 1. Near transfer — EU Regulatory Technical Standards lifecycle

**Retained.**

The European Supervisory Authorities publish **final draft RTS** and submit them
to the European Commission.

That document can be substantively complete from the authority's perspective but
still not be the binding final legal text.

The Commission can:

1. notify the authority that it intends to endorse the draft **with
   amendments**;
2. transmit a modified version;
3. receive a formal authority opinion on the changes;
4. later adopt the binding Commission Delegated Regulation;
5. publish that adopted text in the Official Journal.

This is not hypothetical.

#### Fixed-overheads RTS

EBA records that it submitted the final draft RTS in December 2020.

In November 2021 the Commission sent a modified version and intended to endorse
with amendments.

EBA's February 2022 Opinion says the Commission version contained a
**substantive change** for market makers.

The binding outcome became Commission Delegated Regulation (EU) 2022/1455.

Official evidence:

- EBA opinion / press release:
  https://www.eba.europa.eu/publications-and-media/press-releases/eba-issues-opinion-european-commissions-proposed-amendments-0
- EUR-Lex adopted regulation:
  https://eur-lex.europa.eu/eli/reg_del/2022/1455/oj/eng

The adopted Regulation contains the market-maker trading-fee deduction that the
EBA described as the Commission's substantive amendment.

#### Crowdfunding RTS

EBA submitted final draft RTS under Article 19(7) of Regulation 2020/1503 on
10 May 2022.

In May 2023 the Commission notified EBA that it intended to endorse the draft
with amendments and supplied a modified version.

EBA recorded one substantive amendment.

The binding outcome became Commission Delegated Regulation (EU) 2024/358.

Official evidence:

- EBA opinion:
  https://www.eba.europa.eu/sites/default/files/document_library/Publications/Opinions/2023/1056402/EBA%20Opinion%20RTS%20Crowdfunding.pdf
- EUR-Lex adopted regulation:
  https://eur-lex.europa.eu/eli/reg_del/2024/358/oj/eng

#### Current recurrence

The mechanism is still active in 2026.

Examples:

- equivalent-legal-mechanism RTS: Commission proposed substantive amendments
  after EBA's 5 August 2025 final draft;
- operational-risk RTS: Commission proposed amendments after EBA's 2025 final
  drafts.

Official evidence:

- https://www.eba.europa.eu/publications-and-media/press-releases/eba-responds-commissions-proposed-amendments-draft-technical-standards-equivalent-legal-mechanism
- https://eba.europa.eu/publications-and-media/press-releases/eba-responds-commissions-proposed-changes-its-draft-technical-standards-operational-risk

### Structural mechanism

The dangerous inference is:

```text
authority final draft
    ↓  INVALID PROMOTION
binding final legal rule
```

The correct lifecycle is closer to:

```text
consultation
    ↓
ESA final draft RTS
    ↓
Commission review
    ↓
possible Commission amendment
    ↓
ESA opinion / response
    ↓
Commission adoption
    ↓
OJ publication / legal effect
```

"Final" therefore belongs to the ESA drafting stage, not to the final binding
legal state.

### Existing strongest baseline

The boring baseline is strong:

- EBA Single Rulebook pages expose status;
- EBA correspondence records Commission amendment steps;
- EUR-Lex owns the adopted delegated regulation and legal status.

A careful researcher using the full official lifecycle can resolve the question
without Needle.

That means this is **not** a product-win claim.

The possible Needle contribution is a reusable adversarial failure identity /
evaluation case for whether research systems preserve authority handoff and
binding-state correctly.

---

### 2. Functional analogue — regulator consultation paper → final rules

**Not retained as the main opportunity.**

FCA consultation papers contain proposed rules; later Policy Statements publish
the final rules.

Final policy can differ materially from the consultation.

Examples include:

- PS25/1, where consultation feedback changed final commodity-derivatives
  reporting rules;
- PS16/21, where final renewal rules/guidance changed several consultation
  details.

Official evidence:

- https://www.fca.org.uk/publications/policy-statements/ps25-1-reforming-commodity-derivatives-regulatory-framework
- https://www.fca.org.uk/publications/increasing-transparency-and-engagement-renewal-general-insurance-markets-ps16-21

### Why this branch is weaker

The lifecycle distinction is real and consequential.

But FCA's publishing model makes the role difference unusually explicit:

- consultation pages are labelled consultation papers;
- Policy Statements say they publish final rules;
- timelines often link consultation → policy statement → effective date.

Confusing proposal with final rule is ordinary source-reading failure unless a
more specific mechanism is demonstrated.

**Disposition for this branch: PARK as boundary/control.**

---

### 3. Distant structural analogue — IETF Internet-Draft → RFC

**Rejected as a Needle opportunity; retained as a boundary.**

IETF's standards-process material explicitly states that Internet-Drafts:

- are working documents;
- have no formal standards status;
- may change or disappear;
- are not the publication mechanism for specifications.

A later RFC is a different publication/status state.

Official process evidence:

- https://datatracker.ietf.org/doc/draft-ietf-procon-2026bis/

### Why this is a useful boundary

The structural analogy is strong:

```text
mature-looking draft
    ≠
authoritative published standard
```

But the official baseline states the distinction so aggressively that a new
Needle-specific mechanism adds little.

This is evidence against overgeneralising every document-lifecycle distinction
into a corpus family.

**Disposition for this branch: REJECT as transfer opportunity.**

## Surface similarity vs structural correspondence

The retained RTS case is not interesting because both artifacts contain
"draft/final" labels.

It is structurally distinct because:

1. the upstream authority has completed its own drafting stage;
2. another institution has formal power to change the text;
3. those changes can be substantive;
4. the later adopted artifact owns legal effect;
5. the upstream "final draft" remains an important authoritative source for
   provenance and policy history but cannot inherit binding status.

That combination is closer to an **authority-handoff lifecycle** than ordinary
document versioning.

## Relationship to current Needle taxonomy

This should not be forced into `PARALLEL_INSTRUMENT_LIFECYCLE`.

That class concerns separate legal instruments under one umbrella political deal.

RTS handoff instead concerns successive institutional states in one regulatory
product pipeline.

It is also not identical to judicial-document-role confusion:

- Advocate-General Opinion and Court judgment have different institutional
  authors/roles in adjudication;
- ESA final draft and Commission Delegated Regulation are linked stages in a
  delegated-rulemaking process.

The common higher-order abstraction is:

> authority and legal effect must remain attached to the exact document role and
> lifecycle stage rather than inherited from semantic continuity.

That abstraction is useful, but too broad to become a corpus class itself.

## One falsifiable transfer hypothesis

Working label:

`TECHNICAL_STANDARD_AUTHORITY_HANDOFF`

Hypothesis:

> In EU delegated technical-standard research, treating an ESA "final draft RTS"
> as the binding final rule can produce a materially wrong legal conclusion
> because the European Commission may substantively amend the draft before
> adopting and publishing the binding delegated regulation.

## Smallest discriminating experiment

Do not build tooling.

If Cycle 2 synthesis selects this opportunity:

1. pre-register two **completed** RTS chains from different mandates where the
   Commission considered/amended an ESA final draft;
2. freeze:
   - ESA final draft;
   - Commission amendment notification / ESA opinion;
   - adopted OJ text;
3. compare the exact proposition(s) that changed;
4. construct one realistic research question per chain that does **not** name the
   lifecycle trap;
5. test whether the current 14-class corpus taxonomy already owns the mechanism;
6. compare a strong official-source baseline with the corpus/evaluation
   discipline only if a distinct claim remains.

Success requires:

- at least one proposition where using the final draft as current binding law
  changes the legal answer;
- the mechanism to repeat across both chains;
- the distinction not to collapse into ordinary "read the final document"
  hygiene once the full official baseline is used.

Kill if:

- exact draft→adopted changes are immaterial to a realistic legal conclusion;
- the second chain does not reproduce the mechanism;
- current taxonomy already owns the failure adequately;
- or the value is only that official pages have status labels.

## Run A disposition

# **ADOPT_FOR_EXPERIMENT**

Retain exactly one bounded candidate:

> `TECHNICAL_STANDARD_AUTHORITY_HANDOFF`

Do not add a trap class or corpus cases yet.

Do not build an RTS tracker, lifecycle graph, EBA/ESMA/EIOPA ingestion system,
or Explorer feature.

The FCA and IETF branches serve as explicit boundaries showing when document
role/lifecycle is already sufficiently obvious that Needle should add nothing.

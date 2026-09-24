# Cycle 1 — fresh legal-adversary scout

Issue: #135  
Parent: #134  
Channel: `LEGAL_ADVERSARY`  
Date: 2026-09-24

## Question

Can fresh official/source-grounded legal research expose an orthogonal,
consequential failure mechanism that the current 27-case / 14-class corpus does
not already preserve?

## Scientific firewall

No model or comparator was run before candidate selection.

Candidates were selected from the corpus bias map and fresh official-source
research. A candidate was not retained because a baseline failed it.

The current corpus remains the comparator for **failure-mode coverage**, not for
model difficulty.

## Candidate set

The scout intentionally sampled four different source/state mechanisms rather
than maximizing case count:

1. CURIA judicial-document role;
2. delegated-act adoption / objection / entry-into-force state;
3. official web-resource legal-role asymmetry;
4. Official Journal manifestation authenticity over time.

Only the first survives as a potentially orthogonal opportunity.

---

## Candidate A — Advocate-General opinion promoted to Court judgment

### Evidence trigger

On 3 September 2026 Advocate General Spielmann delivered an Opinion in
**C-394/25, Volta**, a request for a preliminary ruling from the Dutch Raad van
State.

Current InfoCuria status remains **Pending**. The case overview lists the request
for a preliminary ruling and the 3 September 2026 Opinion; no Court judgment is
listed.

Official references:

- InfoCuria case overview:
  https://infocuria.curia.europa.eu/tabs/affair?lang=EN&publishedId=C-394%2F25
- Opinion ECLI:EU:C:2026:703:
  https://juris.curia.europa.eu/juris/document/document.jsf?docid=314895&doclang=en
- CURIA explanation of Advocate-General role:
  https://curia.europa.eu/panorama/2025/en/judicial-activity.html

CURIA's own description is unambiguous: an Advocate General delivers an
independent Opinion; the Court is not required to follow it.

The same live procedural shape appears in other current cases from different
legal domains, including:

- **C-393/25, Okresný súd Banská Bystrica** — consumer protection, Opinion
  ECLI:EU:C:2026:697, 3 September 2026;
- **C-392/25, Bodegas Sanviver** — trade marks/fundamental rights, Opinion
  ECLI:EU:C:2026:699, 3 September 2026.

### Tempting consequential error

> "In Volta, the Court of Justice ruled on 3 September 2026 that ..."

That statement collapses the identity and legal role of two different judicial
documents:

- Advocate-General Opinion;
- Court judgment.

At the present cutoff there is no judgment in Volta.

The error matters because a legal research note may attribute an authoritative
Court holding before the Court has decided the case.

### Suspected failure mechanism

Working label only:

`JUDICIAL_DOCUMENT_ROLE_CONFUSION`

A document emitted inside a judicial proceeding is promoted to a different
procedural/legal role — e.g. Advocate-General Opinion → Court judgment — because
the researcher follows the proposition without preserving the document type and
case state.

This is not yet a corpus class.

### Existing-taxonomy check

The current judicial classes do not fit cleanly:

- `JUDICIAL_VALIDITY_TEXT_DIVERGENCE` assumes a judicial holding that changes
  validity/legal state while text remains;
- `JUDICIAL_INTERPRETATION_TEMPORAL_OVERCLAIM` assumes a Court interpretation
  exists and guards against fabricating a new prospective start date.

Neither owns the prior question **whether the source is a judgment/holding at
all**.

`PRIVATE_ORIGIN_LEGAL_RECOGNITION` is also different: the issue here is not
private origin, but procedural document identity inside an official court
system.

### Strongest boring baseline

A competent researcher can avoid the error without Needle-specific machinery by:

1. opening the official InfoCuria case overview;
2. checking the document type;
3. checking whether the case is pending;
4. distinguishing Opinion from Judgment before attributing a holding.

No schema or product feature is needed to do this safely.

### Counter-evidence

The mechanism may be too basic to deserve its own named trap class.

CURIA labels document type explicitly, and experienced EU-law researchers know
that Advocate-General Opinions are not judgments. A new class would be taxonomy
bloat if it merely encodes generic "read the document label" hygiene.

The three live examples above also share the same source system and procedural
role. They show recurrence, but not yet orthogonality across judicial-document
role errors.

### Riskiest assumption

That **judicial document-role confusion is a consequential, reusable failure
mechanism distinct enough from generic source-role discipline to deserve
corpus-level identity**.

### Kill rule

Do **not** add a trap class if a bounded follow-up cannot find an independently
useful second judicial-role contrast where confusing document role would change
a legal-research conclusion — for example another procedural document type or
posture, not merely another Advocate-General Opinion.

If the only evidence is "Opinions are not judgments", preserve this note and
reject class creation.

### Role

Current evidence is **DERIVATION** only.

Nothing here is fresh blind validation and no model comparison is authorised.

### Candidate disposition

**RETAIN as the sole surviving opportunity.**

---

## Candidate B — Commission adoption during delegated-act objection period

### Evidence

Two fresh official examples were inspected.

**C(2026)6196 — common training framework for physiotherapists**

- Commission adoption: 15 September 2026;
- foreseen end of objection period: 15 November 2026;
- Directive 2005/36/EC Article 57c(5) says the relevant delegated act enters
  into force only if Parliament/Council do not object (or both waive objection
  early).

References:

- https://eur-lex.europa.eu/legal-content/EN/PIN/?uri=PI_COM%3AC%282026%296196
- https://eur-lex.europa.eu/eli/dir/2005/36/

**C(2026)6262 — medium-chain chlorinated paraffins**

- Commission adoption: 11 September 2026;
- foreseen end of objection period: 11 November 2026;
- Regulation (EU) 2019/1021 Article 18(6) gives the same no-objection
  entry-into-force boundary.

References:

- https://eur-lex.europa.eu/legal-content/EL/PIN/?uri=intcom%3AAres%282025%2910131503
- https://eur-lex.europa.eu/eli/reg/2019/1021/

### Tempting error

> "The Commission adopted the delegated act, therefore the new rule is already
> in force."

### Taxonomy check

This is real and consequential, but it is not sufficiently orthogonal.

The current `STATUS_APPLICATION_SEPARATION` family already preserves the
general failure pattern that an authoritative status/procedural milestone and
the boundary at which legal obligations become operative are distinct.

The delegated-act objection procedure is a valuable **new source-system example**
of that family, not evidence for a new class.

### Disposition

**REJECT as a new opportunity/class.**

It may later be useful as ordinary derivation/regression material if a concrete
research need calls for legislative-procedure coverage.

---

## Candidate C — official web resource does not imply one legal role

### Evidence

Two official EU web resources expose opposite authority relationships.

### ECHA Candidate List

ECHA states that only the Candidate List published on its website is deemed
authentic, and companies can have immediate legal obligations following
inclusion under REACH.

Reference:
https://echa.europa.eu/candidate-list-table

### EU Sanctions Map

Official EU material describes the EU Sanctions Map as an information tool and
states that the Official Journal is the official source of EU law; in case of
conflict, the Official Journal prevails.

Relevant official references:

- https://www.consilium.europa.eu/en/topics/sanctions/
- https://data.consilium.europa.eu/doc/document/ST-11623-2024-INIT/en/pdf

### Potential mechanism

The visual form "official EU website/list" does not itself determine legal
authority.

One official web list can be the legally recognised authentic trigger for
obligations; another official web tool can be derivative/informational only.

### Taxonomy check

This is an excellent source-role contrast, but it does not yet earn a new class.

Needle already explicitly separates **source origin** from **legal role /
recognition**, most visibly after #85. ECHA Candidate List also already appears
in the project's dynamic-reference research history.

Without a concrete current sanctions/source case where relying on the
informational representation changes the legal conclusion, naming another
source-role class would risk ontology inflation.

### Disposition

**PARK as contrast inspiration; REJECT as the #135 surviving opportunity.**

It may become useful if an independently observed research failure shows that
public-official origin is being mistaken for controlling legal authority.

---

## Candidate D — Official Journal manifestation authenticity changes over time

### Evidence

Council Regulation (EU) 2024/741 changed the contingency-publication rule for
the Official Journal.

During an exceptional EUR-Lex outage a printed edition can be authentic and
produce legal effects. Once systems are restored and the corresponding
electronic edition is published, that electronic edition becomes the only
authentic edition.

EUR-Lex also records three historical printed editions — from 2013, 2014 and
2019 — whose corresponding electronic editions became the only authentic
editions from 14 March 2024.

References:

- https://eur-lex.europa.eu/oj/all/auth-direct-access.html?locale=en
- https://eur-lex.europa.eu/eli/reg/2024/741/oj
- https://eur-lex.europa.eu/eli/reg/2013/216/2024-03-14/eng

### Potential error

A current electronic manifestation can be treated as proof that the same
manifestation carried authentic legal status at an earlier historical time.

### Taxonomy check

This is interesting source-state history but maps directly onto the logic of
`SOURCE_STATE_BACKPROJECTION`:

> current representation/source authority cannot be projected backward as proof
> of the historical source state.

It strengthens an existing class rather than exposing an orthogonal mechanism.

### Disposition

**REJECT as a new #135 opportunity.**

---

## Candidate comparison

| Candidate | Consequential? | Orthogonal to current classes? | Evidence quality | Result |
|---|---:|---:|---:|---|
| Judicial document role (AG Opinion ≠ judgment) | yes | **plausibly yes** | current official CURIA | retain |
| Delegated-act adoption ≠ entry into force | yes | no | current EUR-Lex + basic acts | reject as new class |
| Official website legal-role asymmetry | potentially | not yet | official ECHA/Council | park as inspiration |
| OJ manifestation authenticity transition | yes | no | EUR-Lex + Regulation 2024/741 | reject as new class |

## Defined opportunity

> When researching a pending EU judicial case, a researcher must preserve the
> procedural identity and authority of each CURIA document so that a proposition
> from an Advocate-General Opinion is not attributed as a Court holding before a
> judgment exists.

Current strongest baseline can do this by inspecting official document type and
case status.

The open question is whether this deserves a reusable corpus failure identity,
not whether Needle needs a judicial product feature.

## Smallest next evidence test

One bounded follow-up only:

1. find one **different judicial-document role contrast** from official sources
   where role confusion would materially alter a legal research conclusion;
2. test whether the current 14-class taxonomy already owns it;
3. if it is genuinely the same mechanism, consider whether a two-instance
   derivation family is justified;
4. if not, reject the working class and keep this as case-specific research
   hygiene.

No model run is needed for that test.

No schema/UI/judicial ingestion system is justified.

## Final disposition

**ADOPT_FOR_EXPERIMENT**

Adopt only the bounded generality test for
`JUDICIAL_DOCUMENT_ROLE_CONFUSION`.

Do **not** add the class or corpus entries yet.

Do **not** run a baseline-vs-Needle model evaluation yet.

Do **not** build CURIA ingestion, a case-law graph, procedural-state schema or
Explorer feature.

The experiment succeeds only if a second, meaningfully different judicial
document-role case demonstrates the same consequential failure mechanism. If it
does not, the opportunity is rejected as generic source-reading hygiene.

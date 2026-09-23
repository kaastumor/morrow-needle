# Issue #88 candidate discovery — pre-seal audit

**Date:** 2026-09-23  
**Status:** CANDIDATE DISCOVERY / NOT YET SEALED

This file records candidate selection before any R/M investigator run.

A candidate is not admitted because it looks likely to make R fail. It is
admitted because it independently instantiates one of the six failure strata
pre-registered in Issue #88.

Rejected and weak candidates are preserved so the case set cannot silently
drift toward examples that flatter Needle.

## Candidate 1 — source-state / ex-post back-projection

**Candidate:** Regulation (EU) 2018/1806, Polish Annex I, omitted Sudan and the
11 February 2026 Polish corrigendum.

Official evidence:

- original Polish OJ text lists Saudi Arabia followed directly by Sierra Leone;
- the Polish-only corrigendum of 11 February 2026 explicitly inserts Sudan
  between them;
- the current Polish consolidated representation is still nominally
  `02018R1806-20251230` / 30 December 2025, but records the later corrigendum
  as C1.

Candidate question family:

Can today's consolidated Polish text labelled 30 December 2025 be used to prove
that a researcher inspecting the official Polish source on 30 December 2025
would already have seen Sudan in Annex I?

**Admission assessment:** STRONG.

The wrong answer is consequential because it fabricates a historical source
state from an ex-post corrected consolidation.

Sources:

- https://eur-lex.europa.eu/eli/reg/2018/1806/oj/pol
- https://eur-lex.europa.eu/eli/reg/2018/1806/corrigendum/2026-02-11/oj
- https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:02018R1806-20251230

## Candidate 2 — authentic-language / corrigendum asymmetry

**Candidate:** NIS2 Directive (EU) 2022/2555, Italian Article 33 heading,
corrected 4 April 2025.

Official evidence:

- the authentic Italian Article 33 heading originally says supervision and
  enforcement relating to `soggetti essenziali` (essential entities);
- the body of Article 33 itself concerns `soggetto importante` / important
  entities;
- an Italian-only corrigendum published 4 April 2025 changes the heading from
  essential entities to important entities;
- the English expression already says important entities.

Candidate question family:

For a historical-source audit immediately before 4 April 2025, was it wrong to
quote the authentic Italian Article 33 heading as referring to essential
entities, and can the English wording be projected onto the Italian source
state?

**Admission assessment:** ADMISSIBLE, LOWER DISCRIMINATION.

This is a real language-state trap, but the substantive body of Article 33 makes
the intended entity class visible. A competent baseline may therefore recover
the correct legal scope despite getting the historical heading state wrong.
That is acceptable parity evidence; it is not a reason to strengthen the case.

Sources:

- https://eur-lex.europa.eu/legal-content/EN-IT/TXT/?uri=CELEX:32022L2555
- https://eur-lex.europa.eu/eli/dir/2022/2555/corrigendum/2025-04-04/oj/eng

## Candidate 3 — status/set-state != legal applicability

**Candidate:** Commission designation of ChatGPT as a VLOSE on 31 August 2026.

Official evidence:

- Commission designated ChatGPT as a VLOSE on 31 August 2026;
- the Commission states that the designated services have four months, by
  January 2027, to comply with the additional VLOP/VLOSE obligations;
- DSA Article 33 separates designation from the later application boundary.

Candidate question family:

On 23 September 2026, does ChatGPT's designation itself mean that the additional
Section 5 VLOSE obligations are already applicable to the service?

**Admission assessment:** STRONG.

The trap is live, current and operationally consequential: designated state and
additional-obligation applicability are not the same temporal fact.

Sources:

- https://digital-strategy.ec.europa.eu/en/news/commission-designates-chatgpt-reddit-roblox-under-digital-services-act
- https://eur-lex.europa.eu/eli/reg/2022/2065

## Candidate 4 — unchanged text / changed legal effect

**Candidate:** Commission Implementing Decision (EU) 2025/1457 and restricted
reference to EN 60335-1:2012.

Official evidence:

- Directive 2014/35/EU gives a presumption of conformity where the relevant
  harmonised-standard reference is published;
- Decision 2025/1457 maintains EN 60335-1:2012 in the OJ but adds a restriction;
- the specified part of clause 20.2 no longer confers presumption of conformity
  with Annex I point 2(c);
- the parent Directive did not need a textual amendment for that operative
  effect to change.

Candidate question family:

After publication of Decision 2025/1457, can a manufacturer rely on the mere
continued listing of EN 60335-1:2012 to claim the presumption of conformity for
the restricted clause-20.2 test-probe part?

**Admission assessment:** STRONG.

A yes answer confuses identifier/listing continuity with unchanged legal effect.

Source:

- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202501457

## Candidate 5 — source origin != legal authority/recognition

**Candidate:** Philips MDR conformity documentation relying on TÜV SÜD Product
Service GmbH (NB 0123).

Evidence chain:

- a Philips EU declaration identifies TÜV SÜD Product Service GmbH, NB 0123,
  and an MDR certificate for a Class II device;
- TÜV SÜD is a private conformity-assessment body, not an EU institution;
- NANDO records TÜV SÜD Product Service GmbH as notified body 0123 under
  Regulation (EU) 2017/745;
- MDR Article 56 expressly gives notified bodies the role of issuing,
  restricting, suspending and withdrawing conformity certificates;
- EUDAMED now publicly records these certificate states.

Candidate question family:

May the TÜV SÜD certification determination be discarded as legally
non-authoritative merely because its source is private rather than a public EU
authority?

**Admission assessment:** ADMISSIBLE, BUT MUST STAY NARROW.

The correct result is not that every private certificate proves EU compliance.
The legally relevant fact is the bounded notified-body role recognised by
public law. The manufacturer declaration is evidence of the claimed certificate,
while NANDO/MDR establish the public-law recognition basis. An investigator
must not silently collapse those two evidence roles.

Sources:

- https://www.documents.philips.com/assets/EU%20Declaration%20of%20conformity/20251014/7b94dbf1c0a64d588e7db37600fd16d6.pdf
- NANDO notification: Regulation (EU) 2017/745, TÜV SÜD Product Service GmbH,
  NB 0123
- https://eur-lex.europa.eu/eli/reg/2017/745/2023-03-11/eng
- https://health.ec.europa.eu/medical-devices-eudamed/notified-bodies-and-certificates-module_en

## Candidate 6 — temporal precision / boundary loss

**Candidate:** Swedish HVMFS 2025:10 real-time northern-prawn closure in
Skagerrak.

Official evidence:

- decision/publication date: 20 March 2025;
- prohibition begins 21 March 2025 at 01:00 Swedish time;
- prohibition runs through 4 April 2025 at 00:59 Swedish time.

Candidate question family:

At 00:30 Swedish time on 21 March 2025, was the closure already in force? What
about 00:30 on 4 April 2025?

**Admission assessment:** STRONG, WITH DOMAIN-SIMILARITY CAVEAT.

This is a different legal event from Issue #81 but the same fishery/real-time
closure family. It cleanly tests the pre-registered precision failure, yet it
may be easier for Method because the deriving case used the same regulatory
mechanism. Keep it only if no equally clean different-domain instant-boundary
case is found before sealing.

Source:

- https://www.havochvatten.se/download/18.6d787a77195724ae952cf116/1742461949334/HVMFS%202025-10-ev.pdf

## Rejected / deferred candidates

### Reusing the exact Issue #61, #64, #77, #78, #81, #83 or #85 cases

**REJECTED.** They created the failure strata and would test memory/replay rather
than fresh discrimination.

### Generic "is a notified body private?" question

**REJECTED.** Too semantic. Candidate 5 is admissible only because it binds a
real manufacturer/certificate claim to a concrete NANDO designation and the MDR
certificate role.

### Source reopening as the trap

**REJECTED.** #87 showed that investigators may reopen sources simply because
verification is good practice. #88 scores consequential legal conclusions and
unsupported certainty, not browsing count.

## Next pre-seal work

1. adversarially review whether Candidate 2 is consequential enough;
2. search once more for a different-domain substitute for Candidate 6;
3. pin a direct public recognition/status path for Candidate 5 if available;
4. only then freeze the six questions and answer keys;
5. commit hashes before any R/M execution.

No investigator run has occurred yet.

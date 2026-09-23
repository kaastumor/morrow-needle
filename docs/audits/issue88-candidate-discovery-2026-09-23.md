# Issue #88 candidate discovery — pre-seal audit

**Date:** 2026-09-23  
**Status:** SEALED / PHASE A EXECUTION PENDING

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

**Final candidate:** EU ETS accredited verifier opinion and Union Registry
verified-emissions/account status.

Official evidence:

- Implementing Regulation (EU) 2018/2067 defines a verifier as a legal person
  carrying out verification activities and accredited by a national
  accreditation body;
- Article 27 requires the verifier to issue a verification report and permits
  the opinion that an emissions report is verified as satisfactory;
- the Commission's EU ETS MRV guidance states that operators must have their
  annual report verified by an accredited verifier;
- Delegated Regulation (EU) 2019/1122 uses satisfactory verification/verified
  status in the Union Registry and requires blocking of a stationary
  installation account when preceding-year emissions are not entered and marked
  verified by 1 April.

Final question family:

Can an operator disregard the absence of satisfactory accredited verification
on the theory that a private verifier's opinion is legally irrelevant because
only public-authority determinations matter?

**Admission assessment:** STRONG.

This is materially better than the initial notified-body candidate because the
private-primary verification output participates in a concrete compliance and
account-state consequence while public authorities retain their own correction
and administration powers. It directly tests whether origin and legal
recognition are collapsed.

Sources:

- Regulation (EU) 2018/2067, especially Articles 3 and 27;
- Delegated Regulation (EU) 2019/1122, especially Articles 31-32;
- Commission EU ETS monitoring/reporting/verification guidance.

## Candidate 6 — temporal precision / boundary loss

**Final candidate:** licence-application 13:00 Brussels-time boundary under
current Implementing Regulation (EU) 2016/1239.

Official evidence:

- Article 3(1) provides that an application received after 13:00 Brussels time
  on a working day is deemed lodged on the first working day following actual
  receipt;
- therefore two applications received on the same calendar day at 12:59 and
  13:01 can have different legally deemed lodgement days.

Final question family:

Can a date-only case-management record safely treat otherwise valid applications
received at 12:59 and 13:01 Brussels time on the same working day as lodged on
the same day?

**Admission assessment:** STRONG.

This replaces the HVMFS candidate before sealing because it tests the same
pre-registered precision failure in a different legal domain from the fishery
case that originally exposed Temporal's sub-day limitation.

Source:

- current consolidated Commission Implementing Regulation (EU) 2016/1239,
  Article 3(1).

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

## Final pre-seal disposition

All six pre-registered strata now have one admitted fresh case.

Candidate 2 remains intentionally lower-discrimination rather than being
replaced merely to make Needle more likely to win. If R and M both recover the
Italian NIS2 history safely, that is valid parity evidence.

Candidate 5 was replaced by the EU ETS verifier/Union Registry chain because it
creates a concrete legal consequence from a bounded private-primary
determination while preserving public-authority roles.

Candidate 6 was replaced by the 13:00 Brussels-time licence boundary because it
tests temporal precision outside the fishery mechanism that originally exposed
the issue.

The exact R/M prompts and exact answer key are now sealed outside Git.

Canonical commitments:

- prompts SHA-256:
  `a8725af696f12eb286a1dec84c6e1df870a2a6ebd3409cee0db97d14f8354659`
- answer key SHA-256:
  `8c32ed2c3506b6f508a4093cba171c166b759fb3f475c4956ff84657818cfde0`
- runner ZIP SHA-256:
  `d66f9a00ab18599bb77b227eb21dd8c942d2eeea2d5c8af63b638a8ef90496bc`

Public manifest:
`fixtures/value-gates/issue88-sealed-manifest-v0.1.json`

No R/M investigator run had occurred when these commitments were fixed.

# Issue #413 — lean-team standards-maintenance job evidence

Date: 2026-09-27  
Mode: **DISCOVER / USE — CANDIDATE B**

## Result

# **LEAN_TEAM_STANDARDS_MAINTENANCE_JOB_SUPPORTED**

This result is intentionally narrower than a Candidate-B product win.

Supported:

> lean product manufacturers have a real recurring job in identifying applicable harmonised
> standards, keeping standards/legal-reference state current, anticipating already-known transitions,
> and updating conformity documentation/product work when the state changes.

Not supported:

- Candidate B is unique;
- current point products are inferior;
- the status card alone solves product conformity;
- a software status surface replaces testing, technical-standard interpretation, notified bodies,
  supplier evidence or qualified conformity judgment;
- users will pay for Needle.

The result earns one **disposable usability MVP** around the already-frozen five #411 standards-status
cases.

---

## 1. Independent public job evidence

### European Commission — Union harmonisation compliance-cost study

The Commission's 2017 staff working document on product-compliance costs describes familiarisation
with Union harmonisation legislation and standards as an **important and ongoing task for all
firms**.

The study reports, among other findings:

- familiarisation commonly represented roughly 15–20% of compliance human-resource effort in the
  studied firms;
- SMEs had proportionally more staff tied to compliance while fewer could dedicate specialised
  full-time staff;
- large firms were more likely to follow legislative and standardisation developments early and
  participate in the process;
- frequent changes to legislation and technical standards create adaptation/familiarisation costs;
- technical files and declarations must be maintained and updated when legislation/standards change;
- SMEs were more likely to rely on external laboratories / third-party conformity-assessment
  services.

The same study gives concrete examples where changes to standards drove product redesign,
retesting, documentation updates and product withdrawal/adaptation.

Source:

> https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:52017SC0466

Interpretation:

> standards-state maintenance is not an invented software problem. It is one recurring component
> of a wider manufacturer conformity job.

### European Commission — 2025 competitiveness material

Current Commission competitiveness material states that regulatory burden is especially cumbersome
for SMEs and reports that **28% of EU SMEs say more than 10% of their staff are employed to assess
and comply with regulatory requirements and standards**.

Source:

> https://single-market-economy.ec.europa.eu/document/download/e566634a-29cf-4adf-a98d-1e708c873af8_en

This supports the user segment's burden.

It does not identify Candidate B as the solution.

### Commission manufacturer / standardisation responsibilities

The Commission's CE-marking/manufacturer guidance places responsibility on manufacturers to identify
applicable legislation and applicable harmonised standards.

Current Commission standardisation policy also identifies timeliness, inclusiveness and access to
standards as live framework concerns.

Sources:

- https://single-market-economy.ec.europa.eu/single-market/goods/ce-marking/manufacturers_en
- https://single-market-economy.ec.europa.eu/single-market/goods/european-standards_en
- https://single-market-economy.ec.europa.eu/smes/growing-and-scaling-sme/improving-smes-access-marktets/standardisation-and-smes_en

---

## 2. Named small-team evidence — directional, vendor-hosted

These sources are useful because they expose concrete workflows, but they are positive customer
stories published by a standards/compliance vendor. They are **not neutral prevalence or treatment
evidence**.

### SpineWelding AG

BSI's published customer story describes a small team where standards tracking could be postponed
behind daily work and where proactive change alerts were described as avoiding substantial cost.

Source:

> https://compliancenavigator.bsigroup.com/en/community/spinewelding-ag/

### Tissue Regenix

BSI's published customer story describes fragmented standards access and value placed on upcoming
change visibility and comparison/tracked-change support.

Source:

> https://compliancenavigator.bsigroup.com/en/community/tissue-regenix/

### Smart Surgical Appliances

A BSI startup case describes the value of knowing **when standards will change** and the risk that
late discovery can force redesign/retesting.

Source:

> https://compliancenavigatorppd.bsigroup.com/en/community/single-case-study/

### Robinson Healthcare

A BSI customer story describes manually checking standards-setter websites for updated standards
and then needing to determine implications.

Source:

> https://compliancenavigator.bsigroup.com/en/community/robinson-healthcare/

Interpretation:

> there is credible workflow evidence that small teams value maintained standards-change state.

Because the evidence is vendor-hosted, it cannot establish comparative superiority or willingness
to choose Needle.

---

## 3. Strong counter-hypothesis

The **full manufacturer conformity job is much bigger than standards status**.

Depending on product/regime it can include:

- identifying applicable legislation and standards;
- interpreting the technical content of the standards;
- testing / laboratory work;
- notified-body or other third-party conformity assessment;
- supplier/component evidence;
- product design changes;
- technical-file maintenance;
- declarations/marking;
- post-market obligations.

The Commission compliance-cost study itself shows that testing, product redesign, technical-file
work and external conformity-assessment services can dominate substantial parts of the burden.

Therefore:

> Candidate B must not market an OJ-reference card as "CE compliance".

The card addresses only:

> **the maintained legal status of a harmonised-standard reference and the resulting presumption
> consequence as of a date.**

That can still matter because a wrong/current/future standards state can trigger expensive
downstream work.

But the status wedge is **one decision input**, not the whole decision.

---

## 4. Why timing is consequential

The five frozen #411 cases demonstrate three distinct kinds of state:

1. **restriction while citation remains**;
2. **formal decision not to publish**;
3. **current citation with a binding future withdrawal already scheduled**.

These distinctions can affect:

- whether reliance on a harmonised standard provides presumption of conformity;
- which scope/requirements are covered;
- when a manufacturer should prepare for an upcoming transition;
- whether an old/current status may be safely reused in a later product decision.

The LVD EN 60335-2-60 case is especially useful as a usability control:

> a 2025 decision already exists, but the reference remains cited on 26 September 2026 and is only
> withdrawn on 18 January 2027.

A simplistic "withdrawal decision exists" alert can therefore be operationally different from a
date-sensitive status view.

---

## 5. Relationship to incumbents

#411 remains binding.

Accessible products already productise substantial parts of this job.

That is evidence that the job is real, but it kills any claim that Needle invented it.

The MVP therefore asks only:

> **Can the five-case decision-ready status view make the official legal state easier to understand
> and inspect than navigating the fragmented Commission/EUR-Lex surfaces?**

It is not yet comparing against the private product view of Grecta, Certivo, ComplyMatrix, BSI or
other incumbents.

That remains a separate direct-product-access gate.

---

## 6. Phase-2 gate

All three predeclared conditions pass:

1. **Recurring job:** supported by Commission evidence and directional small-team case evidence.
2. **Timing matters:** supported by official restriction/non-publication/future-withdrawal cases.
3. **Bounded role:** the card can be explicitly constrained to harmonised-reference legal state and
   refuse full-conformity claims.

Therefore one disposable MVP surface is earned.

### Disposable MVP scope

Use exactly the five frozen #411 cases.

Provide:

- case/regime selection;
- arbitrary query date;
- current OJ-reference status at that date;
- presumption consequence;
- latest owning legal event;
- next already-fixed future event;
- scope/restriction;
- direct EUR-Lex evidence links;
- forbidden/non-implication statements.

Do not add:

- live monitoring;
- accounts;
- portfolio management;
- applicable-legislation discovery;
- standard text licensing/access;
- testing/lab workflow;
- CE-marking automation;
- notifications;
- AI advice/chat;
- database/API.

## Final disposition

# **LEAN_TEAM_STANDARDS_MAINTENANCE_JOB_SUPPORTED**

This earns **usability prototyping**, not a product/value claim.

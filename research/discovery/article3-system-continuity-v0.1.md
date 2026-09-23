# Discovery — Article 3 system identity after the 2025 rewrite

Status: **BOUNDED AUDIT FINDING**

## Question

Did Regulation 2025/905 merely rename the technical systems previously called
SANI and PKI, or did its generic wording leave technical identity open?

## Evidence

### Pre-2025 legal text

Article 3(3) explicitly named:

- State Aid Notification Interactive (**SANI**) for notifications;
- Public Key Infrastructure (**PKI**) for correspondence.

The Commission's original electronic-notification arrangements likewise
described the web application SANI and PKI encrypted e-mail for subsequent
correspondence.

### 2025 rewrite

Regulation 2025/905 says Commission practice had evolved in the use of
electronic notification systems. It replaces the named systems with:

- “the electronic application designated by the Commission”;
- “the secured electronic system designated by the Commission”.

That wording preserves the legal duties while deliberately no longer naming the
technical products.

### Current Commission operational documentation

The current State-aid forms page says the forms are for public authorities using
State-aid notification software “SANI” and repeatedly instructs users to attach
forms to the standard notification form in **SANI2**.

That is sufficient for a bounded current operational statement:

> Current Commission notification documentation identifies SANI/SANI2 as the
> State-aid notification application.

It is not sufficient to prove that today's SANI2 service is technically
identical to the 2008 SANI implementation.

### Correspondence

The audit found authoritative historical PKI evidence.

It did **not** find a post-2025 official source that identifies the generic
“secured electronic system designated by the Commission” as PKI.

Current general State-aid contact pages mention Registry email and EU Send, but
those instructions do not establish the Article 3 notification-correspondence
system and are therefore not promoted into that role.

## Result

The existing Thread unknown survives, but can be understood more precisely:

| Question | Result |
|---|---|
| Historical notification system | SANI — supported |
| Historical correspondence system | PKI — supported |
| Current operational notification application | SANI/SANI2 — supported |
| 2008 SANI → current SANI2 technical continuity | unresolved |
| Current Article 3 correspondence system | unresolved |
| 2008 PKI → current secured-system technical continuity | unresolved |
| Legal rule continuity (electronic notification / secured correspondence) | separately evidenced; does not prove technical identity |

This is a **bounded narrowing of the evidence gap, not a Thread defect**.

Pinned matrix:
`fixtures/audit/reg794-article3-system-continuity-2025-v0.1.json`.

Official sources checked 2026-09-23:

- https://eur-lex.europa.eu/eli/reg/2004/794/2016-12-22/eng
- https://eur-lex.europa.eu/eli/reg_impl/2025/905/oj/eng
- https://competition-policy.ec.europa.eu/state-aid/legislation/forms-notifications-and-reporting_en
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=oj:JOC_2005_237_R_0003_01
- https://competition-policy.ec.europa.eu/state-aid/contact_en

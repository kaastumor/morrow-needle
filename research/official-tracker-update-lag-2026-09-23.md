# Official tracker update lag versus national legal state

**Issue:** #93  
**Research cutoff:** 2026-09-23  
**Status:** CONFIRMED TWO-COUNTRY FAILURE FAMILY

## Question

Can a currently accessible official EU status tracker be treated as proof of the
current national legal state merely because the page is official and can be
opened today?

The Netherlands and Sweden provide independent counterexamples.

The safe rule is:

> current access time is not the same thing as the observation/update time of
> the status represented by the source.

## Case A — Netherlands / NIS2

### Commission tracker state

The Commission's current page titled *NIS2 Directive implementation in The
Netherlands* says that it gives the state of play and that its content will be
updated progressively as information becomes available to the Commission.

Its displayed transposition status is still:

> On 7 May 2025 the Commission sent a reasoned opinion for failure to notify
> full transposition.

That is a valid historical Commission enforcement/status fact.

The Commission later referred the Netherlands to the Court on 8 July 2026 for
then-failure to notify transposition measures. That press release is also a
time-bounded historical fact and is not treated here as erroneous.

### Newer Dutch official legal state

Dutch primary/public official sources establish later events:

- Staatsblad 2026, 187 publishes the **Cyberbeveiligingswet**, whose title
  expressly states that it implements Directive (EU) 2022/2555;
- Article 107 leaves commencement to royal decision;
- Staatsblad 2026, 189, Article 35, provides that the Cyberbeveiligingswet and
  Cyberbeveiligingsbesluit enter into force on **15 August 2026**;
- Rijksoverheid on 15 August 2026 states that the Cyberbeveiligingswet is in
  force from that day and implements the NIS2 Directive.

Therefore, on the research cutoff of 23 September 2026, the Commission country
page's visible May-2025 status cannot safely be used to infer that no Dutch NIS2
implementing law is currently in force.

### Important limit

This finding does **not** independently decide:

- whether Dutch transposition is complete in every respect;
- whether the Commission regards all notified measures as compliant;
- whether the infringement case has been formally closed;
- whether any particular entity is within the Cyberbeveiligingswet.

Those are separate propositions.

The tested proposition is only that the currently served tracker page cannot
prove the absence of later national implementing law.

## Case B — Sweden / NIS2

### Commission tracker state

The Commission's current Sweden page likewise says its content is a state of
play, progressively updated as information becomes available.

It still reports:

> On 7 May 2025 the Commission sent a reasoned opinion for failure to notify
> full transposition.

The page displays **Last update: 7 July 2025**.

### Newer Swedish official legal state

Swedish official sources establish later law:

- **Cybersäkerhetslag (2025:1506)** states that its provisions partially
  implement Directive (EU) 2022/2555;
- its transitional provisions state that the law enters into force on
  **15 January 2026**;
- the Swedish Government stated on 15 January 2026 that the new cybersecurity
  law and regulation entered into force that day.

Thus a user who opens the Commission page in September 2026 and treats the
visible May-2025 reasoned-opinion status as a current absence-of-legislation fact
would project an older tracker state forward over newer Swedish primary law.

Again, this does not independently determine whether every NIS2 requirement has
been completely or correctly transposed for Commission infringement purposes.

## Cross-case failure mechanism

### OFFICIAL_TRACKER_UPDATE_LAG

A currently accessible official summary/status tracker can lag newer primary
legal sources.

Unsafe inference:

> official + accessible today = current factual/legal coverage.

The source's role and temporal coverage must remain explicit.

This is distinct from `SOURCE_STATE_BACKPROJECTION`:

- **SOURCE_STATE_BACKPROJECTION:** a present corrected representation is
  projected backward as if it were the contemporaneous historical source state;
- **OFFICIAL_TRACKER_UPDATE_LAG:** a historically valid but stale status snapshot
  still accessible today is projected forward as if it represented the current
  legal state.

The direction of temporal error is opposite.

## Why two cases matter

One stale country page could be editorial accident.

Two independent Member States, each with newer national official implementing
law and Commission country pages still displaying the 7 May 2025 enforcement
state, support preserving this as a real source-handling failure family.

The family is about how official status-summary systems are used, not about
criticising the Commission or judging Member-State compliance.

## Source roles

### Commission

- Netherlands country tracker: official summary/status source; explicitly
  progressively updated; currently displays the May-2025 reasoned-opinion state.
- Sweden country tracker: same source role; currently displays the May-2025
  state and a 7 July 2025 last-update marker.
- 7 May 2025 reasoned-opinion release: historical enforcement event.
- 8 July 2026 Netherlands referral release: historical enforcement event at
  that later date.

### Netherlands

- Staatsblad 2026, 187: formal publication of the Cyberbeveiligingswet.
- Staatsblad 2026, 189: formal commencement rule fixing 15 August 2026.
- Rijksoverheid 15 August 2026: official current explanatory confirmation of
  entry into force and NIS2 implementation purpose.

### Sweden

- SFS 2025:1506: Swedish statutory text and commencement provision.
- Regeringen 15 January 2026: official confirmation that the new cybersecurity
  law/regulation entered into force that day.

## URLs

Commission:
- https://digital-strategy.ec.europa.eu/en/policies/nis2-directive-netherlands
- https://digital-strategy.ec.europa.eu/en/policies/nis2-directive-sweden
- https://digital-strategy.ec.europa.eu/en/news/commission-calls-19-member-states-fully-transpose-nis2-directive
- https://digital-strategy.ec.europa.eu/en/news/commission-refers-ireland-spain-france-and-netherlands-court-justice-failing-transpose-rules

Netherlands:
- https://www.officielebekendmakingen.nl/stb-2026-187.html
- https://www.officielebekendmakingen.nl/stb-2026-189.html
- https://www.rijksoverheid.nl/actueel/nieuws/2026/08/15/cyberbeveiligingswet-en-wet-weerbaarheid-kritieke-entiteiten-vanaf-vandaag-van-kracht

Sweden:
- https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/cybersakerhetslag-20251506_sfs-2025-1506/
- https://regeringen.se/pressmeddelanden/2026/01/nu-skarps-kraven-pa-svensk-cybersakerhet/

## Project consequence

No monitoring/freshness architecture is earned.

The project only needs to preserve the adversary:

- official-source origin and current URL availability are insufficient to infer
  current factual coverage;
- summary/tracker source role must be separated from primary legal publication;
- visible status must be bounded by its update/observation horizon where known;
- newer primary official sources can supersede a tracker's usefulness for a
  narrow current-state proposition without making the historical tracker event
  false.

This belongs in the corpus and protocol, not in a new service.

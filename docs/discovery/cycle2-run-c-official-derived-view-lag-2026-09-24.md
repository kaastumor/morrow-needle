# Cycle 2 Run C — official-summary / primary-source divergence scan

Issue: #158  
Parent: #155  
Date: 2026-09-24  
Disposition: **ADOPT_FOR_EXPERIMENT**

## Proven Needle anchor

Run C starts from #93:

`OFFICIAL_TRACKER_UPDATE_LAG`

Current class meaning:

> a currently accessible official summary/status tracker can lag newer primary
> legal sources, so current access time cannot be substituted for the tracker's
> observation/update horizon.

#93 proved the mechanism in Member-State NIS2 implementation tracking.

Run C asks whether the same failure mechanism transfers to other official
derived information systems.

## Candidate system 1 — EU consolidated financial sanctions list

**Retained.**

The European Commission maintains a consolidated list of persons, groups and
entities subject to EU financial sanctions.

The Commission describes that list as reflecting officially adopted texts
published in the Official Journal.

Official Commission overview:

https://finance.ec.europa.eu/eu-and-world/sanctions-restrictive-measures/overview-sanctions-and-related-resources_en

The legally authoritative state remains the Official Journal / adopted legal
acts.

A Member-State authority states this boundary even more explicitly.

Latvia's Ministry of Foreign Affairs says:

- the EU Sanctions Map and consolidated list are advisory tools;
- only publication of legal acts in the EU Official Journal is legally binding.

Reference:

https://www.mfa.gov.lv/en/sanctions

Historical/current EU consolidated-list material also carries the disclaimer
that only Official Journal information is authentic and that omissions or errors
may occur.

Example:

https://pfi.public.lu/dam-assets/pdf/blanchiment/sanctions/1811/ue-liste-consolide-des-sanctions-financires-internationales-jour-au-08032023.pdf

### Direct evidence of update lag

The Italian Financial Intelligence Unit (UIF) published a sanctions alert on
17 July 2026 after an EU listing act was published in the Official Journal.

It states that newly designated persons would be added to the EU consolidated
list **subject to the time strictly necessary for updating**.

Reference:

https://uif.bancaditalia.it/pubblicazioni/avvisi/2026/sanzioni-alert-2026.07.17/index.html

A similar 7 August 2026 alert repeats the same update-lag language.

Reference:

https://uif.bancaditalia.it/pubblicazioni/avvisi/2026/sanzioni-alert-2026.08.07/index.html

### Consequential job

A sanctions-screening / compliance user may ask:

> Is this person/entity currently subject to an EU asset freeze?

If the legal act has already taken effect but the consolidated screening list
has not yet incorporated the designation, treating the current list as the
current legal state can produce a false negative.

This is a materially consequential use case.

### Strong existing baseline

The boring baseline is strong:

- Official Journal / EUR-Lex legal act;
- Commission sanctions resources;
- consolidated list;
- explicit official warnings about authenticity.

A careful legal/compliance researcher can resolve the issue without Needle.

Potential Needle value is therefore not a sanctions product.

It is corpus/evaluation coverage for the source-role and observation-horizon
failure.

---

## Candidate system 2 — legislation.gov.uk revised legislation

**Retained as an independent structural case.**

Legislation.gov.uk publishes revised versions of UK legislation.

Its own help material states that the "latest available revised" version is the
latest version **after changes have been applied by the editorial team**.

The site explicitly warns that:

- revised legislation may not be fully up to date;
- outstanding changes can exist;
- the target is to incorporate amendments within a maximum of about three
  months after they come into force;
- outstanding changes are exposed through a "Changes to Legislation" banner.

Official guidance:

- https://www.legislation.gov.uk/help
- https://www.legislation.gov.uk/understanding-legislation

Live pages exist where "Latest available (Revised)" is displayed while
outstanding amendments remain unapplied.

Example:

https://www.legislation.gov.uk/ukpga/1981/66/section/17

### Consequential job

A user may ask:

> What does this provision currently say?

If an amending provision is already legally effective but the editorially
revised text has not yet incorporated it, copying only the visible revised text
can understate current law.

The site mitigates this strongly with an explicit red/outstanding-changes banner.

### Strong existing baseline

The official baseline is unusually good:

- revised text;
- change annotations;
- unapplied-change list;
- explicit freshness warning;
- primary amending legislation.

This makes the system both:

1. a valid structural transfer case; and
2. a strong boundary against claiming a Needle product advantage.

The failure is avoidable if the user reads the outstanding-changes signal.

---

## Candidate system 3 — Single Market / transposition scoreboards

**Boundary / control; not separately retained.**

The Commission Single Market Scoreboard explicitly declares:

- a reporting period;
- a cut-off date for notifications;
- that later verification/closure may still be pending.

Example current reporting page:

https://single-market-scoreboard.ec.europa.eu/node/1342_fi

The page states that the 2025 reporting period considers notifications made by
5 December 2025.

This is a snapshot by design, not a claim to real-time legal status.

### Boundary lesson

A summary/tracker is not defective merely because it is historical.

The dangerous condition is:

> the interface or user inference allows "accessible now" to be treated as
> "observed/legally current now" without preserving the summary's own horizon.

Where the official system clearly exposes the cut-off and the user question is
historical/performance-oriented, no failure exists.

---

## Structural correspondence

The sanctions list and UK revised-legislation examples share the #93 mechanism:

```text
primary authoritative event becomes legally effective
    ↓
official derived representation exists
    ↓
derived representation has separate update/editorial cycle
    ↓
user accesses representation later
    ↓
ACCESS_TIME is mistaken for OBSERVATION/UPDATE_HORIZON
    ↓
current legal state can be misstated
```

The derived representation may be:

- a status tracker;
- a consolidated list;
- a revised/consolidated legislative text.

The mechanism is therefore broader than "tracker lag".

## Relationship to existing taxonomy

The existing class name:

`OFFICIAL_TRACKER_UPDATE_LAG`

may be too surface-specific.

The higher-order mechanism is better described as:

`OFFICIAL_DERIVED_VIEW_LAG`

Working definition:

> an official derived representation of legal state has its own observation,
> editorial or publication horizon and can lag a newer legally operative primary
> source; current accessibility of the derived view does not prove that it
> reflects current legal state.

Do not rename the class yet.

A taxonomy change must be earned by an explicit generality test.

## One falsifiable transfer hypothesis

Hypothesis:

> `OFFICIAL_TRACKER_UPDATE_LAG` generalises into a broader
> `OFFICIAL_DERIVED_VIEW_LAG` failure family across at least two materially
> different official derived-view systems, without collapsing into generic
> "check the source date" hygiene.

## Smallest discriminating experiment

If Cycle 2 synthesis selects this candidate:

1. pre-register one fresh sanctions-list case and one fresh revised-legislation
   case;
2. freeze:
   - operative primary legal event;
   - derived-view content/state;
   - derived-view observation/update metadata;
3. prove that a realistic "current legal state" question changes depending on
   whether the derived view is treated as authoritative current state;
4. test whether existing
   `OFFICIAL_TRACKER_UPDATE_LAG` owns both cases without semantic distortion;
5. include one explicit control where the derived view's declared snapshot date
   makes the inference safe.

Success requires:

- two distinct derived-view types;
- material legal consequence in both;
- same underlying horizon-confusion mechanism;
- no need for a new product or monitoring service.

Kill if:

- both cases reduce to users ignoring prominent freshness warnings;
- no current legal conclusion changes;
- or the existing #93 class already covers both cleanly without modification.

## Relative-value check

This run does **not** establish a user-facing product opportunity.

The strongest practical alternatives already include:

- primary legal acts;
- official freshness/status warnings;
- official change lists;
- mature sanctions-screening tools.

A Needle surface would need separate evidence of meaningful relative advantage,
importance and behavioral consequence.

No such product claim is made here.

## Run C disposition

# **ADOPT_FOR_EXPERIMENT**

Retain one bounded candidate:

> test whether `OFFICIAL_TRACKER_UPDATE_LAG` should generalise to
> `OFFICIAL_DERIVED_VIEW_LAG`.

The sanctions-list and revised-legislation systems supply independent target
evidence.

Do not:

- rename the class yet;
- add corpus cases yet;
- build a sanctions monitor;
- build UK-law ingestion;
- build a generalized freshness service;
- create a source-observation database.

The next step, if selected by #160, is only the two-case generality experiment.

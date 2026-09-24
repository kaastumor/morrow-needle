# #174 pre-registration — official derived-view lag generality

Date: 2026-09-24  
Issue: #174  
Claim type: `CORRECTNESS_VALIDITY / FAILURE_FAMILY_GENERALITY`

## Question

Does the existing:

`OFFICIAL_TRACKER_UPDATE_LAG`

mechanism generalise beyond status trackers to a broader:

`OFFICIAL_DERIVED_VIEW_LAG`

family?

Provisional definition:

> An official derived representation of legal state has its own observation,
> editorial or update horizon and can lag a newer legally operative primary
> source; current accessibility of the derived view does not prove that it
> reflects current legal state.

## Existing evidence

Cycle 2 Run C used exposed examples from:

- EU consolidated sanctions resources;
- legislation.gov.uk revised legislation;
- a Single Market Scoreboard snapshot control.

Those examples are:

`DERIVATION / PUBLIC_EXPOSED`

They motivate this experiment but cannot be the two fresh generality cases.

## Frozen systems

Exactly two positive systems plus one negative control:

1. EU financial-sanctions consolidated derived view;
2. legislation.gov.uk revised legislation;
3. European Commission Single Market Scoreboard snapshot/control.

No fourth system is allowed.

## Positive case A — fresh EU sanctions-list lag

### Candidate source

Italian Financial Intelligence Unit (UIF) sanctions alerts are used only as the
candidate/event index because Run C established that they record the relation
between newly operative EU listings and the Commission consolidated list's
update cycle.

Run C already exposed:

- 17 July 2026;
- 7 August 2026.

Exclude both.

### Frozen selection rule

Select the **chronologically earliest** UIF `Sanzioni Alert` published after
7 August 2026 and no later than 23 September 2026 that satisfies all eligibility
conditions.

Do not skip an eligible alert because its legal consequence looks too easy or
too hard.

### Eligibility

The alert must:

- identify a new EU financial-sanctions listing or delisting grounded in an
  Official Journal legal act;
- state or otherwise establish that the Commission consolidated financial-
  sanctions list / derived view requires a subsequent update step;
- allow the underlying OJ act and affected person/entity to be identified;
- concern a legal-state change capable of altering a screening/compliance
  answer.

If the first post-7-August alert is ineligible, inspect later alerts
chronologically and record the exclusion reason.

### Frozen observation point

Use the publication time/date of the UIF alert as the derived-view observation
point unless the alert itself supplies a more precise update timestamp.

The positive proposition must be true at that frozen observation point:

> the legal act is operative/published while the derived list is not yet proven
> updated for the affected identity.

## Positive case B — fresh legislation.gov.uk revised-text lag

### Frozen search

Run exactly one standard web search:

`site:legislation.gov.uk/ukpga "outstanding changes not yet made" "section"`

Use the first returned result set.

Exclude the Run C exposed page:

`https://www.legislation.gov.uk/ukpga/1981/66/section/17`

### Candidate pool

For each distinct canonical `legislation.gov.uk/ukpga/.../section/...` URL
returned:

1. preserve canonical URL;
2. compute:
   `SHA256("needle174|UK_REVISED_VIEW|<canonical-url>")`;
3. sort ascending by hash;
4. inspect in that order until one is eligible.

Do not issue a second search because the first pool is inconvenient.

### Eligibility

A candidate is eligible only if:

- the page is an official revised-text view;
- it identifies at least one outstanding editorial change not yet applied to the
  displayed revised text;
- at least one outstanding change is already legally in force at experiment
  freeze;
- the underlying amending provision can be identified from official legislation;
- applying that amendment changes the answer to a realistic "what does this
  provision currently require/permit/say?" question.

If the outstanding change is wholly prospective, not yet commenced, or purely
editorial with no consequential answer change, record exclusion and continue in
hash order.

## Negative control — declared snapshot

### Frozen search

Run exactly one standard web search:

`site:single-market-scoreboard.ec.europa.eu "reporting period" "notifications" "2025"`

Exclude the Run C exposed Finland page:

`https://single-market-scoreboard.ec.europa.eu/node/1342_fi`

### Selection

Preserve distinct returned Scoreboard URLs.

Select by ascending:

`SHA256("needle174|DECLARED_SNAPSHOT_CONTROL|<canonical-url>")`

Inspect in hash order until one page:

- explicitly declares its reporting/cut-off horizon;
- presents itself as a performance/reporting snapshot rather than real-time
  current legal state.

The control passes if reading it according to its declared horizon produces no
freshness error.

## Strong baseline

The strongest boring baseline is:

- primary operative legal act;
- official derived view;
- official freshness/outstanding-change/update metadata.

A careful researcher can resolve the cases without Needle.

No product/workflow advantage is claimed.

## Materiality

A positive case is material only if using the derived view alone at the frozen
observation time can change at least one realistic answer about:

- whether a person/entity is currently subject to an EU financial restriction;
- what a statutory provision currently says/requires/permits.

A generic warning that "websites can be stale" is insufficient.

## Mechanism test

Both positive cases must instantiate:

```text
primary legal event becomes operative
    ↓
official derived representation exists
    ↓
derived representation has independent update/editorial horizon
    ↓
user observes derived representation
    ↓
ACCESS_TIME mistaken for DERIVED_VIEW_STATE_TIME
    ↓
current legal conclusion can be wrong
```

The control must demonstrate:

> a derived view with an explicit historical/reporting cutoff is not defective
> merely because it is not real-time.

## Existing class first refusal

Current class:

`OFFICIAL_TRACKER_UPDATE_LAG`

Current definition:

> A currently accessible official summary/status tracker lags newer primary
> legal sources, so current access time cannot be substituted for the tracker's
> observation or update horizon.

### SUPPORT broader family

Rename/generalise only if:

- both positive cases pass materiality;
- the same mechanism explains NIS2 tracker + sanctions list + revised
  legislation;
- "tracker" is demonstrably a surface-specific label narrower than the evidence;
- the negative snapshot control passes.

### KEEP existing class / REJECT generalisation

Keep the tracker class unchanged if:

- one positive system relies on a materially different mechanism;
- the selected cases reduce only to ignoring conspicuous warnings;
- no current legal answer changes;
- or the control shows the proposed broader definition would incorrectly flag
  ordinary historical snapshots.

### REVISE

Revise only the existing class definition/label if the mechanism generalises but
the provisional `OFFICIAL_DERIVED_VIEW_LAG` wording is too broad.

## Corpus consequence

If broader family is supported:

- rename `OFFICIAL_TRACKER_UPDATE_LAG` to the smallest defensible broader label;
- retag the two existing #93 NIS2 cases;
- add the two fresh positive cases as public DERIVATION/regression cases;
- do not count the control as a trap case;
- trap-class count should remain unchanged by a pure rename/generalisation.

No EVALUATION/model claim is created.

## No implementation

No:

- sanctions monitor;
- UK legislation ingestion;
- derived-view crawler;
- source freshness database;
- alerting;
- product surface.

## Hard stop

If the frozen searches/candidate rules cannot yield both positive cases and one
control:

`INDETERMINATE / SAMPLE_INCOMPLETE`

Do not add replacement systems or search queries after exposure.

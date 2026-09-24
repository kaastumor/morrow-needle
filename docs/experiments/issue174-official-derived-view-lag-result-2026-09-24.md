# #174 result — official derived-view lag generality

Date: 2026-09-24  
Issue: #174  
Disposition: **INDETERMINATE / SAMPLE_INCOMPLETE**

## Decision

No taxonomy conclusion is permitted.

The pre-registered sample required:

1. one fresh EU sanctions-list lag case;
2. one fresh legislation.gov.uk revised-text lag case;
3. one declared-snapshot negative control.

The negative control was available.

The hard stop fired because the **frozen UK revised-text candidate pool contained
no eligible positive case**: no selected page established an already-in-force,
editorially unapplied amendment to the displayed provision that materially
changed a current-law answer.

The preregistration prohibits a second search or replacement system after
exposure.

Therefore:

- do not rename `OFFICIAL_TRACKER_UPDATE_LAG`;
- do not add fresh corpus cases;
- do not treat sample incompleteness as evidence against
  `OFFICIAL_DERIVED_VIEW_LAG`.

## EU sanctions branch

The frozen chronological rule selected the 23 September 2026 UIF targeted-
sanctions de-listing alert as the first post-7-August candidate.

The corresponding operative event was identifiable as Council Implementing
Regulation (EU) 2026/2160 of 22 September 2026, amending Regulation
(EU) No 269/2014 and entering into force on publication.

This is structurally consistent with:

```text
binding primary legal state changes
    ↓
official derived list requires subsequent update
```

Because the full three-part sample became impossible on the UK branch, this
candidate is not admitted as a #174 positive case.

Status:

`FRESH_CANDIDATE / NOT_ADMITTED`

## UK frozen pool

Exact search, run once:

`site:legislation.gov.uk/ukpga "outstanding changes not yet made" "section"`

The Run C exposed section 17 page was excluded.

The frozen hash order was inspected without a second query.

Findings:

- Police Reform and Social Responsibility Act 2011 s.157: outstanding 2026
  changes shown on the Act page concern other provisions, not s.157;
- several 1981 Act section pages exposed wider Act-level outstanding effects but
  no eligible already-in-force unapplied textual amendment to the selected
  displayed provision;
- the Land Compensation Act section 9 result was a historical point-in-time
  view, not the required latest revised positive;
- 1981 Act section 11 directly exposed 2026 Wales amendments, but the relevant
  Schedule 2 changes were prospective / not yet in force at experiment freeze.

Thus no frozen candidate satisfied all eligibility conditions.

The preregistration says:

> do not issue a second search because the first pool is inconvenient.

Therefore:

> **UK positive case B = SAMPLE UNAVAILABLE UNDER FROZEN RULE.**

This alone triggers:

`INDETERMINATE / SAMPLE_INCOMPLETE`

## Negative control — available

Exact frozen query:

`site:single-market-scoreboard.ec.europa.eu "reporting period" "notifications" "2025"`

After excluding the Run C Finland page, the first result set still contained the
Commission page:

> **Notifications in the field of technical regulations (TRIS) and services
> (IMI)**

It explicitly declares reporting period:

`10/2024 – 09/2025`

and presents itself as a reporting/performance snapshot.

That is consistent with the pre-registered control:

> a derived view with an explicit historical/reporting cutoff is not defective
> merely because it is not real-time.

The experiment therefore did **not** fail because the control was unavailable.

## Interpretation

This is not `REJECT`.

The proposed broader mechanism was not falsified; fresh sample construction
failed first.

This is not `SUPPORT`.

Both fresh positive systems plus the control were required. Partial directional
evidence cannot waive a frozen sample requirement.

## Operational learning

#165 and #174 exposed a common execution risk:

> a sound sample-selection rule can still fail because external
> search/enumeration transport does not reliably produce the required candidate
> pool.

Future transport-sensitive experiments should perform a
**metadata-only transport smoke test before full sample preregistration**:

1. verify query/API shape;
2. verify result count/schema/pagination only;
3. do not retain candidate identities or inspect substantive candidate content;
4. then freeze the deterministic selection rule.

Cycle 3 (#177) adopts this guard.

## Consequence

H-21 remains **PARKED / UNRESOLVED**.

No corpus or taxonomy change.

Proceed to sponsor-authorised active Discovery Cycle 3 rather than repairing the
sample after exposure.

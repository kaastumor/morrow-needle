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

## Positive A — EU sanctions candidate

Frozen rule:

> select the chronologically earliest eligible UIF `Sanzioni Alert` after
> 7 August 2026 and no later than 23 September 2026.

The UIF index identifies the next targeted-sanctions alert as:

> **23 September 2026 — EU targeted financial sanctions alert — de-listing**

The corresponding legal event was identifiable as Council Implementing
Regulation (EU) 2026/2160 of 22 September 2026, which amended Regulation
(EU) No 269/2014 and entered into force on publication.

The candidate is structurally consistent with the proposed mechanism:

```text
binding primary legal state changes
    ↓
official derived list requires subsequent update
```

Because the complete three-part sample became impossible on the UK branch, the
sanctions candidate is not promoted into a #174 positive result and no
replacement/extra transport path was pursued.

Status:

`FRESH_CANDIDATE / NOT_ADMITTED`

## Positive B — UK frozen pool

Exact search, run once:

`site:legislation.gov.uk/ukpga "outstanding changes not yet made" "section"`

The Run C exposed page `/ukpga/1981/66/section/17` was excluded.

Candidates were canonicalised and sorted by:

`SHA256("needle174|UK_REVISED_VIEW|<canonical-url>")`

Frozen inspection order:

1. `/ukpga/2011/13/section/157`
2. `/ukpga/1981/66/section/10`
3. `/ukpga/1981/66/section/5B`
4. `/ukpga/1981/66/section/4`
5. `/ukpga/Eliz2/9-10/33/section/9`
6. `/ukpga/1981/66/section/8`
7. `/ukpga/1981/66/section/12`
8. `/ukpga/1981/66/section/11`
9. `/ukpga/1981/66/section/5A`
10. `/ukpga/1981/66/section/7`

### Section 157

Outstanding Crime and Policing Act 2026 changes shown on the Act page concern
other provisions, notably sections 42/43, not section 157 itself.

No selected-provision answer change.

**Ineligible.**

### 1981 Act sections 10, 5B, 4, 8, 12, 5A and 7

The pages expose wider Act-level outstanding effects, including 2026 Wales
legislation and application/modification effects, but no eligible already-in-
force unapplied textual amendment to the selected displayed provision was
established.

**Ineligible.**

### Land Compensation Act 1961 section 9

The returned result was a historical point-in-time view, not the required
current/latest revised positive candidate.

**Ineligible.**

### 1981 Act section 11

This was the strongest direct candidate because its outstanding changes include:

- words omitted from s.11(6);
- s.11(7) inserted;

by Planning (Consequential Provisions) (Wales) Act 2026 Sch.2 para.168.

However, the relevant Schedule 2 changes are prospective / not yet in force
unless commenced.

The preregistration requires the outstanding change to be **already legally in
force** at experiment freeze.

**Ineligible.**

## UK pool conclusion

No eligible positive case exists in the frozen first result set.

The preregistration explicitly says:

> do not issue a second search because the first pool is inconvenient.

Therefore:

> **UK positive case B = SAMPLE UNAVAILABLE UNDER FROZEN RULE.**

This alone triggers:

`INDETERMINATE / SAMPLE_INCOMPLETE`

## Negative control — available and valid in shape

Exact frozen query:

`site:single-market-scoreboard.ec.europa.eu "reporting period" "notifications" "2025"`

The exposed Finland Run C page was excluded.

The first result set also contained the Commission page:

> **Notifications in the field of technical regulations (TRIS) and services
> (IMI)**

It explicitly declares a reporting period:

`10/2024 – 09/2025`

and presents its figures as a reporting/performance snapshot.

This is consistent with the preregistered control proposition:

> an official derived view with an explicit historical/reporting horizon is not
> defective merely because it is not real-time.

The control was therefore **available**. The experiment did not fail on control
transport.

## Why this is not REJECT

The proposed `OFFICIAL_DERIVED_VIEW_LAG` mechanism was not falsified.

Run C still provides exposed derivation evidence from sanctions and revised
legislation.

The fresh experiment failed at deterministic positive-sample construction.

Therefore:

> sample incompleteness ≠ mechanism rejection.

## Why this is not SUPPORT

The experiment required **both** fresh positive systems plus the control.

One positive system could not be instantiated under the frozen rule.

Partial directional evidence cannot waive a pre-registered sample requirement.

## Operational learning

#165 and #174 exposed a common execution risk:

> a sound scientific selection rule can still fail because external
> search/enumeration transport does not reliably yield the required candidate
> pool.

Future transport-sensitive experiments should therefore perform a
**metadata-only transport smoke test before full sample preregistration**:

1. verify intended query/API shape;
2. verify result count/schema/pagination only;
3. do not preserve candidate identities or inspect substantive candidate content;
4. then freeze deterministic candidate selection.

This improves execution integrity without permitting post-exposure sample
tuning.

Discovery Cycle 3 (#177) already adopts this guard.

## Assumption / corpus consequence

H-21 remains **PARKED / UNRESOLVED**.

No corpus or taxonomy change.

Do not:

- rename `OFFICIAL_TRACKER_UPDATE_LAG`;
- add the sanctions candidate;
- add any UK candidate;
- count the Scoreboard control as a trap case.

## Next action

Sponsor direction remains active discovery.

The Cycle 2 reserve queue is exhausted:

- Run A was consumed successfully by #171;
- Run B remains parked behind a specific stronger trigger;
- Run C remains unresolved after #174 sample incompleteness;
- Run D remains unresolved after #165 transport blockage.

Proceed to **Discovery Cycle 3 (#177)**, which searches new source-role and
evidence-state mechanisms and includes the new metadata-only transport guard.

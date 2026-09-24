# #174 result — official derived-view lag generality

Date: 2026-09-24  
Issue: #174  
Disposition: **INDETERMINATE / SAMPLE_INCOMPLETE**

## Scientific/taxonomy result

No taxonomy conclusion is permitted.

The pre-registered sample required:

1. one fresh EU sanctions-list lag case;
2. one fresh legislation.gov.uk revised-text lag case;
3. one declared-snapshot negative control.

The frozen control search returned no usable Single Market Scoreboard candidate.

The hard stop therefore fired before the full three-part sample existed.

Do not rename `OFFICIAL_TRACKER_UPDATE_LAG`.

Do not add fresh corpus cases from this experiment.

## Positive A — sanctions candidate selection

The frozen chronological rule was:

> earliest eligible UIF Sanzioni Alert after 7 August 2026 and no later than
> 23 September 2026.

UIF's official news index shows:

- 7 August 2026 — listing;
- next displayed targeted-sanctions alert: 23 September 2026 — de-listing.

The 23 September alert was therefore the deterministic first candidate.

Official UIF evidence:
https://uif.bancaditalia.it/pubblicazioni/avvisi/2026/sanzioni-alert-2026.09.23/index.html

The alert states:

- the latest update to Regulation (EU) No 269/2014 is in the Official Journal,
  L series, 22 September 2026;
- subjects whose designation was revoked **will be removed** from the EU
  consolidated list.

That is structurally consistent with the proposed mechanism:

```text
binding primary legal state changes
    ↓
official derived list requires later update
```

However, because the complete preregistered sample failed, this candidate is
not promoted into a #174 positive-case result.

Status:

`FRESH_CANDIDATE / NOT_ADMITTED`

## Positive B — UK candidate pool

The exact frozen search was executed once:

`site:legislation.gov.uk/ukpga "outstanding changes not yet made" "section"`

The exposed Run C section 17 page was excluded.

Distinct eligible-shape URLs returned by the first result set included:

- `/ukpga/1981/66/section/10`
- `/ukpga/2011/13/section/157`
- `/ukpga/1981/66/section/4`
- `/ukpga/1981/66/section/5A`
- `/ukpga/1981/66/section/5B`
- `/ukpga/1981/66/section/7`
- `/ukpga/1981/66/section/8`
- `/ukpga/1981/66/section/11`
- `/ukpga/1981/66/section/12`

Applying the frozen hash:

`SHA256("needle174|UK_REVISED_VIEW|<canonical-url>")`

puts first:

`https://www.legislation.gov.uk/ukpga/2011/13/section/157`

hash:

`173f35adb5fd16e6e6f5beb62456bcb0773279adf4f5afd14aae8f52197060d3`

The search result itself confirms that the page is a "Latest available
(Revised)" view with outstanding changes not yet made by the editorial team.

Because the negative-control pool had already failed, #174 stopped before
substantive eligibility inspection of the hash-selected UK candidate.

Status:

`HASH_SELECTED / NOT_INSPECTED_FOR_ELIGIBILITY`

## Negative control — failed frozen pool

The exact frozen query was executed once:

`site:single-market-scoreboard.ec.europa.eu "reporting period" "notifications" "2025"`

The first returned result set contained no usable Single Market Scoreboard URL
from which the pre-registered hash-selected control could be frozen.

The preregistration states:

> if the frozen searches/candidate rules cannot yield both positive cases and
> one control: INDETERMINATE / SAMPLE_INCOMPLETE.

It also prohibits replacement systems or additional queries after exposure.

Therefore no broader/reworded Scoreboard search is allowed.

## Why this is not REJECT

The proposed `OFFICIAL_DERIVED_VIEW_LAG` mechanism was not falsified.

The experiment failed earlier at complete fresh-sample construction.

The sanctions candidate is directionally supportive and the UK pool exists, but
partial evidence cannot substitute for the required negative control.

Therefore:

> sample incompleteness ≠ taxonomy rejection.

## Why this is not SUPPORT

The negative control is part of construct validity.

Without it, a broader "derived view lag" class could accidentally label honest
historical/reporting snapshots as defective merely because they are not
real-time.

That distinction was important enough to pre-register and cannot be waived
after the search result is known.

## Operational learning

#165 and #174 both lost otherwise credible hypotheses to transport/query-shape
limitations rather than substantive evidence.

Future bounded experiments should therefore perform a **transport smoke test
before full sample preregistration**:

- test whether the runtime can execute the intended query/API shape;
- inspect only transport success/schema/count, not candidate content;
- do not preserve candidate identities from the smoke test;
- only then freeze the deterministic candidate-selection rule.

This is an execution-integrity improvement, not permission to tune samples after
seeing candidates.

## Assumption consequence

H-21 remains unresolved and should be **PARKED**.

Run C remains good DERIVATION evidence that the broader mechanism is plausible.

No new class/cases are admitted.

## Active-discovery consequence

Sponsor direction remains active discovery.

The Cycle 2 reserves are now:

- Run A — consumed successfully by #171;
- Run B — parked behind a specific compliant-yet-unreconstructable trigger;
- Run C — #174 sample-incomplete; H-21 parked;
- Run D — #165 transport-blocked; H-19 parked.

The existing reserve queue is exhausted.

The correct next action is a fresh active linked-discovery cycle, with transport
feasibility checked before any transport-sensitive experiment is frozen.

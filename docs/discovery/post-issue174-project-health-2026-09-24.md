# Post-#174 Project Health Check — 2026-09-24

Issue: #174  
Decision: **CONTINUE — CYCLE 3 ACTIVE**

## #174 result

#174 ended:

`INDETERMINATE / SAMPLE_INCOMPLETE`

The experiment did **not** fail because the negative control was unavailable.

The frozen Scoreboard search produced a usable declared-snapshot control.

The hard stop fired because the frozen legislation.gov.uk first-result pool
contained no eligible positive case with an already-in-force, editorally
unapplied change to the selected provision that materially changed a current-law
answer.

No second query or replacement system was permitted after exposure.

Consequences:

- no taxonomy change;
- `OFFICIAL_TRACKER_UPDATE_LAG` remains unchanged;
- H-21 remains PARKED / UNRESOLVED;
- no sanctions/UK corpus case is admitted.

Sample incompleteness is an execution result, not a negative mechanism result.

## Partial evidence retained without promotion

- the deterministic 23 September 2026 UIF sanctions de-listing candidate remains
  directionally consistent with legal-state-before-derived-list-update;
- the frozen UK candidate pool was real but did not contain an eligible positive;
- the Scoreboard control behaved as intended: an explicitly bounded reporting
  snapshot is not defective merely because it is not real-time.

None substitutes for the required complete fresh sample.

## Operational learning

#165 and #174 exposed the same project-level execution risk:

> a scientifically sound sample rule can fail because the external
> query/enumeration transport cannot deterministically produce the required
> candidate set.

Future transport-sensitive experiments therefore add one pre-preregistration
guard:

### Metadata-only transport smoke test

Before freezing candidate-selection rules:

- verify intended API/query/search shape;
- inspect only transport success, schema/count and pagination;
- do not retain candidate identities;
- do not inspect candidate content;
- discard the smoke-test result;
- then preregister and rerun under the frozen rule.

This is not permission to tune samples after exposure.

## Active-discovery state

Sponsor direction remains explicit active discovery.

Cycle 2 reserves are now exhausted or parked behind stronger triggers:

- Run A → #171 SUPPORT;
- Run B → PARK behind compliant-yet-unreconstructable evidence;
- Run C → #174 INDETERMINATE / SAMPLE_INCOMPLETE;
- Run D → #165 INDETERMINATE / TRANSPORT_BLOCKED.

The correct response is not to repair #174 until it yields a positive.

It is to move to a fresh active linked-discovery cycle with the transport lesson
embedded.

## Cycle 3

Parent: #177

WIP=1:

- #178 — official guidance/Q&A promoted into binding law;
- #179 — registry/list absence promoted into proof of legal non-existence;
- #180 — machine-readable official derivative diverges from authoritative state;
- #181 — expert/recommendation stage promoted into final authorization/decision;
- #183 — synthesis.

No feature implementation is authorised.

## Direction

# **CONTINUE**

Next: **#178**.

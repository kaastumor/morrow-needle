# Issue #407 — longitudinal operational value probe

Date: 2026-09-26  
Mode: **USE / REASSESS — LONGITUDINAL OPERATIONAL VALUE PROBE**

## Result

# **LIGHTWEIGHT_BASELINE_SUFFICIENT**

The historical operational machinery does **not** earn reactivation from this frozen workload.

This is a bounded retrospective result. It does not show that persistent legal state can never be
useful. It shows that, on the chronology-selected historical cycles, the incremental work actually
performed by Needle was reproducible by a much smaller maintained source/hash ledger, while the
richer legal-analysis layer established no legal outcomes.

---

## 1. Why this experiment was run

#406 and an independent Astra construct-validity review agreed on two points:

1. the historical contraction remains broadly justified;
2. one residual construct was incompletely tested: longitudinal operational value across sequential
   updates, persistent state and repeated resource encounters.

The sponsor explicitly authorised one bounded shot.

The experiment did **not** reopen:

- #97 Method latent-detection value;
- #214 corpus-assisted diagnostic value;
- Full Needle as a default architecture;
- the old public-feed product thesis.

---

## 2. Frozen workload selection

The workload was selected by chronology before reading the selected reports.

Anchor:

> `38717205d65c07ea435c294250c91f31968935c4` — Complete product checkpoint and activate
> adversarial gate.

Rule:

- first `Advance operational Needle pilot state` commit at least four hours after the checkpoint;
- thereafter first state-promotion at least three hours after the prior selected promotion;
- continue to the final preserved promotion before monitor freeze;
- no replacement because a cycle is boring, incomplete or negative.

Frozen cycles:

| Commit | Window end (UTC) |
| --- | --- |
| `29d58f24fc` | 2026-09-22 04:58:27 |
| `872692f001` | 2026-09-22 08:35:32 |
| `910281c06d` | 2026-09-22 11:40:04 |
| `d13f464f89` | 2026-09-22 16:58:30 |
| `8cb344bfd7` | 2026-09-22 21:20:20 |
| `c2ae524d55` | 2026-09-23 00:24:58 |
| `b832e07ad9` | 2026-09-23 04:46:23 |

The final cycle had been partially inspected during historical archaeology, but it entered the
workload by the chronology rule, not because of its outcome.

---

## 3. Workload scale

Across the seven frozen cycles:

| Measure | Observed |
| --- | ---: |
| Feed events reported | 69,643 |
| New feed events | 67,911 |
| Root groups | 5,877 |
| Eligible maintained-resource observations | 264 |
| Unique eligible roots | 217 |
| Repeated eligible roots | 42 |
| Feed notifications represented inside eligible groups | 13,632 |
| Metadata-only observations | 135 |
| Content-changed observations | 99 |
| Unresolved source observations | 30 |
| Legal-analysis attempts on content changes | 99 |
| Legal candidates / established legal outcomes | **0** |

The first selected cycle contained no eligible maintained resource. It remains part of the result.

Most of the official feed was therefore not a usable maintained legal-resource comparison. The
operational system's dominant behavior was filtering, grouping or abstaining.

---

## 4. Strong lightweight baseline

The predeclared comparator was deliberately strong:

> **HASH-AWARE MAINTAINED BASELINE**

It may retain:

- stable resource/root identifier;
- previous/current source snapshot references;
- content hash;
- metadata hash;
- observation time;
- ordinary notes;
- duplicate-event grouping by root/work;
- official-source access;
- capable source-grounded review when content actually changes.

This deliberately gives generic monitoring/state bookkeeping full credit. The experiment asks
whether the **richer Needle state/legal machinery** adds consequential value beyond that layer.

### Mechanical baseline classifier

Using only the permitted previous/current snapshot fields:

- missing content snapshot -> `UNRESOLVED`;
- changed content hash -> `CONTENT_CHANGED`;
- unchanged content + changed metadata hash -> `METADATA_ONLY`;
- unchanged content + unchanged metadata -> `NO_CHANGE`.

Result:

> **264 / 264 classifications matched Needle exactly.**

Confusion map:

| Lightweight baseline | Needle | Count |
| --- | --- | ---: |
| `UNRESOLVED` | `UNRESOLVED` | 30 |
| `METADATA_ONLY` | `METADATA_ONLY` | 135 |
| `CONTENT_CHANGED` | `CONTENT_CHANGED` | 99 |

There were **zero mismatches**.

Therefore Needle receives no incremental credit for source-change triage on this workload.

---

## 5. Longitudinal persistence check

The strongest remaining rescue hypothesis was that Needle's maintained state creates longitudinal
continuity that a lightweight ledger cannot reproduce.

Across the 42 repeated eligible roots there were 47 cross-cycle transitions.

For the 43 transitions where content state existed on both sides:

> **43 / 43 next-cycle previous-content hashes exactly matched the prior cycle's current-content hash.**

That continuity is valuable operational bookkeeping, but the permitted lightweight ledger can
preserve the same chain directly.

Four repeated transitions involved resources with no supported content representation. Needle
remained source-unresolved there; metadata changed but no richer legal state was established.

No repeated-resource example showed a historical-state fact, legal-state owner or dependency
consequence that existed in Needle but could not be represented by the lightweight maintained
snapshot ledger.

---

## 6. Legal-analysis layer

This is the most damaging result for a reactivation claim.

Needle detected 99 content-changing maintained-resource observations and attempted legal analysis
on all 99.

Result:

> **0 legal candidates / 0 established legal outcomes / 0 CHANGE_FEED items.**

Many selected records were court/judicial documents for which the historical operational version
sealed official bytes but lacked a deterministic visible-text projection or otherwise could not
establish a unique legal result.

This limitation is real treatment evidence.

The experiment does not repair it after seeing the result. The guardrail was to test the old
machinery actually present in the frozen cycles, not a hypothetical improved Full Needle.

A capable ordinary reviewer could still open a changed official source and analyse it manually;
the historical Needle treatment did not demonstrate a reduction in that legal-review step.

---

## 7. Noise reduction is real but not distinctive here

The operational system did substantial engineering work:

- event clustering;
- prospective baseline tracking;
- immutable source observations;
- content-versus-metadata comparison;
- fail-closed abstention;
- preservation of uncertainty.

The selected eligible groups alone represented 13,632 feed notifications collapsed into 264
maintained-resource observations.

That is a real capability.

But under this experiment's strong comparator, root grouping + source snapshots + hash comparison
are ordinary monitoring primitives, not Needle-specific legal-state value.

The richer layer did not add a consequential state/change result beyond them.

Therefore the correct interpretation is:

> **generic maintained-source monitoring survived; richer historical Needle Core value did not.**

---

## 8. Operational overhead proxy

The frozen reports also expose non-user timing overhead proxies.

Across the selected period:

- prospective baselines grew from **854** to **1,130**;
- source observations grew from **1,445** to **2,599**;
- the operational state JSON grew from about **1.52 MB** to **2.54 MB**.

The wider historical monitor also produced many state-promotion commits before it was frozen.

These numbers are not a cost model and are not criticised merely for being large. They matter
because additional state/operations only earn themselves if they produce consequential value over
the lightweight comparator.

This replay did not observe such a value delta.

---

## 9. Known positive historical case does not rescue the result

The old operational programme contains a known successful 2026/2104 vertical slice where a real
official update was processed through the source/time/provenance pipeline and a meaningful card
was produced.

That capability remains historically valid.

But #407 precommitted to chronology-selected cycles and forbids replacing a null with a known
friendly case.

The correct synthesis is:

- operational Needle **could** work on selected supported routes;
- the broader frozen workload did not show robust incremental value over a strong lightweight
  monitoring/state baseline.

---

## 10. Source-reopening / repeated-query question

No qualified-lawyer time is inferred.

Structurally:

- metadata-only observations require no legal-source reopening under either arm once hashes are
  maintained;
- content-changing observations require substantive legal inspection unless a deterministic
  analyzer establishes the consequence;
- Needle established none in the 99 content-changing observations;
- repeated hash/state chains were equally representable by the lightweight ledger.

Therefore this replay provides **no observed source-reopening or repeated-query advantage** for the
richer historical Core.

This does not prove such an advantage is impossible on a different job. It means this bounded
workload does not earn a stronger prospective Core experiment.

---

## 11. Important limitation: comparator intentionally abstracts source-monitor construction

The lightweight arm is allowed maintained source snapshots and automatic root/hash comparison.

Therefore #407 does **not** answer:

> is it valuable to build an EU official-source monitor at all?

Needle clearly built one.

It answers the narrower and more relevant reactivation question:

> once a competent monitoring/state layer exists, does Needle's richer persistent legal-state
> machinery add enough operational value to justify re-entry?

On this workload:

> **No demonstrated incremental value.**

That is also consistent with today's incumbent environment, where source/change monitoring is a
well-occupied capability rather than a distinctive Needle product gap.

---

## 12. Relationship to historical gates

#407 does not alter:

- #97 — Method latent-detection null;
- #214 — corpus-assisted diagnostic null;
- #327 — generic Reference Pack post-answer null;
- #366 — standing artifact-value proof retired.

It does add a missing piece to the historical contraction story:

> a real sequential operational workload was inspected, not another one-shot legal QA task.

The result supports rather than reverses the contraction.

---

## 13. Relationship to current MVP candidates

### Candidate A — evaluation/oracle maintenance

Unchanged.

Candidate A's Maintenance Delta core is much smaller than the historical operational stack and
targets an evaluator-owned maintenance decision. #407 does not test its external burden hypothesis.

### Candidate B — EU operative-state reconstruction

Still live as a secondary candidate.

#407 weakens any argument that Candidate B should simply revive the old generic live-monitoring
stack. A Candidate-B MVP still needs a practitioner-owned cross-owner operative-state job and must
use only the smallest state machinery required by that job.

### Candidate C — failure/postmortem -> regression/oracle

Unchanged.

#407 does not test failure-to-regression conversion.

---

## Final disposition

# **LIGHTWEIGHT_BASELINE_SUFFICIENT**

The historical operational Core remains **parked**.

No fresh prospective operational experiment is earned from this replay.

Preserve the old source-monitoring, provenance, temporal and state machinery as technical capital,
but reactivate components only when a concrete current job requires them.

Do not revive Full Needle or a general EU monitoring product from historical capability alone.
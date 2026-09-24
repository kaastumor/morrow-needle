# Red-team — Issue #136 Explorer observed-use protocol

Date: 2026-09-24  
Parent: #134  
Issue: #136  
Claim type: `PRODUCT_WORKFLOW`

## Decision

**PROCEED — HARDENED.**

#136 is still the highest-information next task before #139, but the original
session design had three evidence risks that must be bounded.

## Attack 1 — self-report is mislabeled as direct observation

The current chat cannot see the sponsor's screen or clickstream.

A post-task narrative is useful evidence, but it is not equivalent to direct
moderated observation.

### Guard

This session is labelled:

`SPONSOR_DOGFOOD / CONCURRENT_SELF_REPORT`

The participant reports actions and hesitation in chat as they happen. Morrow
records them without coaching.

Evidence strength:

1. direct/repeated real-world choice remains stronger;
2. direct moderated observation remains stronger;
3. concurrent self-report during a real task is useful but weaker;
4. retrospective summary alone is weaker still.

This session may expose concrete defects and relative-friction signals. It cannot
by itself establish general external-user value.

## Attack 2 — the previously revealed NIS2 task is contaminated

The NIS2 task has already been shown repeatedly in chat. Reusing it as the first
task can create familiarity and expectancy effects.

### Guard

Do not use NIS2 as the first discriminating task.

Use a fresh task whose answer has not been revealed or hinted in the current
session.

The old NIS2 task may later be used only as a non-blind regression/usability
check, clearly labelled.

## Attack 3 — same-case Explorer-vs-repository comparison creates carryover

If the participant solves one exact case in the Explorer and then repeats the
same case in the repository, the second route benefits from learned case identity
and answer.

### Guard

Use **matched but different tasks** for route comparison.

- Task A: Explorer route.
- Task B: direct repository/corpus route.
- Match them on job family and approximate information complexity.
- Do not reuse the same case or decisive trap wording.
- Treat the comparison as qualitative, not a timed benchmark.

The purpose is to compare friction patterns, not claim a precise speed ratio.

## Attack 4 — task wording teaches the answer

A prompt can over-cue the exact trap class or case title.

### Guard

State the practical research problem, not the answer, trap-class name or exact
search term.

The task may describe the risk the researcher is investigating, because that is
the user job, but should not reveal the matching corpus title.

## Attack 5 — Morrow coaches after seeing participant behavior

Interactive chat makes it easy to accidentally help after a hesitation.

### Guard

During an active task Morrow may only:

- acknowledge receipt;
- ask the participant to continue;
- clarify the reporting format if needed.

No hints, suggested search terms, case names, trap classes, navigation advice or
correctness feedback until the task is explicitly finished.

If the participant gets stuck, preserve the stopping point as evidence.

## Attack 6 — stated preference is treated as adoption

"I would use this again" is useful but not observed repeated choice.

### Guard

Record separately:

- observed task friction;
- stated preference;
- actual later repeated choice, if it ever occurs.

Only the last is strong behavioral adoption evidence.

## Attack 7 — a smoother Explorer hides evidence loss

A thin UI can feel easier while making provenance or evidence ownership harder to
verify.

### Guard

Every task includes a validity-floor check:

- can the participant identify the provenance role;
- can they reach or identify the durable evidence owner;
- do they preserve the decisive trap accurately;
- is uncertainty/evaluation mode retained where relevant.

A usability gain that materially weakens these fails the product/workflow claim.

## Session protocol

### Task A — Explorer

Fresh case-finding task using the isolated Explorer snapshot.

The participant should report **concurrently** after each meaningful action:

- what they did;
- what they expected;
- any hesitation/confusion.

Do not ask for feature ideas.

### Task B — direct baseline

A different matched research task using the strongest realistic direct
repository/corpus route the participant would actually use.

Do not force raw JSON if the participant would realistically use GitHub search or
repository navigation.

### Task C — relation/provenance check

Only if Tasks A/B leave material uncertainty, use one small follow-up focused on
related-case interpretation or evidence ownership.

No fourth task without new information.

## Decision boundary

#136 can conclude:

- `ADOPT_FOR_EXPERIMENT` — concrete relative-value hypothesis survives;
- `REVISE` — useful signal exists but task/surface/claim must narrow;
- `REJECT` — no meaningful relative advantage or validity floor fails;
- `PARK` — session is too weak/limited to discriminate.

A sponsor-only concurrent-self-report session cannot fully resolve general H-16.
It can, however, materially change confidence and justify the next evidence step.

## Red-team verdict

Proceed with #136 before #139.

The test is worthwhile only under the bounded evidence label above; do not call
this direct observation and do not reuse the already-exposed NIS2 task as the
first discriminating task.

# #494 bounded reading pilot runbook — frozen before participants

Status: **PRE-RUN OPERATIONAL FREEZE — RECRUITMENT/EXECUTION NOT AUTHORISED**

This runbook operationalises the diagnostic presentation comparison in [protocol.md](protocol.md). It does not authorise recruitment, participant contact, public release, or merge. Do not change these rules after observing a participant unless the run is stopped and the change is recorded as a new experiment version.

## 1. Purpose and arms

Question under test:

> What did the European Parliament record on the selected package decisions concerning consumer-facing environmental claims, and how are the two legislative files related?

Compare exactly two frozen presentations of the same evidence:

- **A — Linked specimen:** `specimen.html`
- **B — Competent handoff:** `baseline.html`

The factual content, qualifications, source destinations and eight scored questions remain identical. Do not add a source, explanation, political cue, result or hint to only one arm after the first participant starts.

## 2. Eligibility and recruitment boundary

Target for this diagnostic pilot: **16 adults who can read English comfortably**.

Include only people who:
- are age 18 or older;
- self-report that they can read the English pages and questions without translation assistance;
- have not previously seen the #494 specimen, baseline, answer key or development discussion.

Exclude:
- anyone who worked on Morrow // Needle or reviewed #494;
- anyone who has already completed either arm;
- anyone who cannot use the test browser/source links independently enough to attempt the task.

Legal or EU-policy expertise is **not** an automatic exclusion. Record it only as a coarse yes/no prior-familiarity field; do not select participants based on political views or party affiliation.

Do **not** collect political preference, ideology, party support, vote intention, support/opposition to the legislation, or persuasion outcomes.

Recruitment source and contact method require separate sponsor authorisation before use. The authorised recruiter must not target people based on politics.

## 3. Allocation

Assign anonymous IDs in arrival order: `P01` through `P16`.

Use this frozen balanced sequence:

| Participant | Arm |
| --- | --- |
| P01 | A |
| P02 | B |
| P03 | B |
| P04 | A |
| P05 | B |
| P06 | A |
| P07 | A |
| P08 | B |
| P09 | A |
| P10 | B |
| P11 | A |
| P12 | B |
| P13 | B |
| P14 | A |
| P15 | B |
| P16 | A |

Do not swap assignments because of expertise, apparent politics, early scores, device, availability or operator preference. If a participant withdraws before seeing the page, keep the ID/arm as a non-start and recruit a replacement under a new ID after the original P16 only if separately authorised; do not refill the old slot silently.

There is **no crossover** in the scored pilot. Exposure to one arm teaches the shared factual answers.

## 4. Test environment

Use desktop/laptop only for the scored pilot.

Minimum environment:
- viewport width at least **1024 CSS px**;
- normal browser zoom at **100%** at task start;
- JavaScript is not required by these static pages;
- source links are allowed to open in the same browser;
- network/source failures are recorded, not repaired by giving an answer verbally.

Record browser name/version, viewport width/height and whether any source destination failed. Assignment is not conditioned on browser family.

Before participant execution, both arms must pass the separate browser gate for rendering, keyboard/focus, narrow/reflow checks and source-link activation. A browser-gate failure pauses participant execution.

## 5. Participant instruction

Give every participant exactly this instruction:

> You are looking at a historical European Parliament voting-information page. Use the page and, if useful, its linked sources to answer eight factual questions. This is not a test of your political views. If the page does not establish an answer, say “unresolved” rather than guessing. You may open source links. Work at your normal pace. You have up to 15 minutes.

Do not explain the package-versus-clause distinction, the related-file rationale, the correct text identity, the group rows or the coverage limits before the task.

## 6. Timing and navigation

Start timing when the assigned page is fully visible. Stop timing when the participant submits all eight responses or at **15:00 minutes**, whichever comes first.

At 15:00:
- do not permit further scored edits;
- unanswered questions become `UNRESOLVED_TIMEOUT`;
- source pages already open may not be used to revise scored responses.

Record:
- total elapsed seconds;
- number of source-link openings;
- number of observable navigation errors (wrong page/section opened and then corrected);
- source destination failures separately from participant navigation errors.

Do not turn these fields into a single composite score.

## 7. Eight scored questions

Use the eight questions and answer key in [protocol.md](protocol.md) verbatim.

Critical items:
- **Q1:** exact voted text for 17 January 2024;
- **Q7:** package vote versus clause attribution;
- **Q8:** within-file ballot coverage.

For each question record one of:
- `CORRECT`
- `INCORRECT`
- `UNRESOLVED`
- `UNRESOLVED_TIMEOUT`

Record a short literal answer or coding note sufficient for later audit. Do not infer what the participant “meant” to rescue a wrong answer.

## 8. Hard-stop errors

Immediately flag `HARD_STOP=YES` if the interface causes or materially contributes to:
- wrong ballot identity;
- wrong legislative stage;
- wrong voted-text identity.

Do not average a hard-stop error away with faster timing or other correct responses. Preserve the exact response and navigation state for review.

## 9. Analysis frozen before observation

Report arms descriptively. Do not claim statistical significance from this pilot.

For each arm report:
- correct count for each Q1–Q8;
- unresolved count for each question;
- total correct critical-item responses out of 24 opportunities;
- median and range of elapsed seconds;
- source openings and navigation errors separately;
- hard-stop incidents;
- source destination failures.

Pre-specified continuation rule from [protocol.md](protocol.md):

1. Arm A must not have fewer correct responses than Arm B on **any** critical item Q1, Q7 or Q8.
2. Arm A must have at least **3 more correct critical-item responses in total** than Arm B across the 24 critical-item opportunities per arm.
3. There must be **no interface-caused hard-stop attribution error** in Arm A.

If all three hold, the presentation signal is sufficient to justify a larger or more realistic follow-up; it does **not** prove population benefit.

If any fails, disposition is `PARITY_OR_INSUFFICIENT` unless a documented execution defect invalidated the run. Prefer the simpler handoff rather than post-hoc changing the threshold, questions or sample.

Timing/navigation may describe usability but cannot rescue a failed critical factual criterion.

## 10. Missing data, withdrawals and invalid runs

A participant who sees the assigned page and then withdraws remains in the execution record; do not replace their results in the primary descriptive table.

Mark a run `EXECUTION_INVALID` only for a concrete external failure that prevents the assigned treatment from being delivered as frozen, such as:
- wrong arm served;
- page/source assets differ from the frozen head;
- browser failure prevents the page from rendering;
- operator reveals an answer before completion.

Record the reason. Do not classify poor comprehension, slow reading or refusal to guess as invalid execution.

## 11. Version and provenance freeze

Before the first participant, record:
- exact PR/head commit;
- hashes or Git blob SHAs of `specimen.html`, `baseline.html`, `protocol.md`, `evidence.md`, this runbook and the observation template;
- preview/build identifier actually used;
- observation date;
- browser build.

No content change is permitted mid-run. If any content must change, stop, version the experiment, preserve the partial run separately and restart only under a new authorisation.

## 12. Authority boundary

This file prepares execution only.

Still requires separate sponsor authorisation:
- recruitment or participant contact;
- execution of the 16-reader pilot;
- incentives/purchases;
- public sharing outside the existing protected/research boundary;
- merge or production deployment.

No stronger model is required to execute this protocol. A model may help audit coding after results, but it must not replace the frozen answer key or silently infer political attitudes.

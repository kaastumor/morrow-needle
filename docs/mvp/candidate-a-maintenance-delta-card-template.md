# Maintenance Delta Card

Status: **Candidate A pre-partner template — not proof of value**

Use one card per maintenance event.

The card sits beside the evaluator's existing task/rubric estate. It does not replace it.

---

## Subject

**Task / evaluation item:**  
`<task-id>`

**Baseline contract:**  
`<immutable version / commit / release>`

**Candidate contract:**  
`<immutable revised version / pending>`

**Change status:**  
`OBSERVED | ADOPTED_BY_OWNER | SUPERSEDED`

---

## Trigger

**Kind:**  
`<law/source change | wrong/stale proposition | criterion ambiguity | coverage gap | inconsistency | acceptance-boundary change | revision | postmortem | other>`

**Reference:**  
`<source / issue / incident / adjudication>`

**Why this contract was reopened:**  
<one concise paragraph>

---

## Changed score-bearing state

| Unit | Before | After | Affected contract | Evidence owner | Governing time | Risk |
| --- | --- | --- | --- | --- | --- | --- |
| `D-01` | <prior state> | <revised / unresolved state> | <criterion / answer-key / task refs> | <authority / task / adjudication> | <event/date/period/N/A> | <false reject / false accept / ambiguous grading / non-comparable / none / unknown> |

Add rows only for genuinely changed score-bearing state.

Do not copy unaffected rubric/source material into this card.

---

## Repair status

`NOT_REQUIRED | PROPOSED | ACCEPTED | REJECTED | PARTIAL`

If accepted, the candidate contract above must identify the owner-adopted revised state.

---

## Existing results

**Comparability:**  
`COMPARABLE | NOT_COMPARABLE | UNKNOWN`

**Action:**  
`NONE | REJUDGE_EXISTING_OUTPUTS | RERUN_SUBJECTS | REVIEW_SAMPLE | HUMAN_DECISION_REQUIRED`

**Affected result scope:**  
<which runs/results may be affected>

**Reason:**  
<why the selected action follows from the delta>

---

## Adjudication

**Status:**  
`NOT_REQUIRED | PENDING | ACCEPTED | REJECTED | SPLIT`

**Owner / note:**  
<qualified reviewer / maintainer decision if needed>

---

## Completion rule

The card is complete when a maintainer can answer, without reopening unrelated task material:

1. what changed;
2. why;
3. what score-bearing contract is affected;
4. what the proposed/current repaired state is;
5. what happens to existing results;
6. what remains subject to human adjudication.

A longer card is not a better card.

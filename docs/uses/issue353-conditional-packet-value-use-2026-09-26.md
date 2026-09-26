# Issue #353 — complexity-stratified packet-value test on case-treatment failures

Date: 2026-09-26  
Primary outcome: **CONDITIONAL_PACKET_VALUE_SUPPORTED**  
v0.2 navigation: **SUCCESS**  
Structured-layer signal: **INDETERMINATE**

## Question

Does Needle's observed failure-analysis packet value depend on a consequential complexity
boundary rather than applying uniformly to every known legal hallucination?

The candidate boundary entering #353 was:

> Needle may add material value when a strong ordinary postmortem still leaves non-trivial
> legal-state, authority-relationship, boundary, provenance/reuse or regression-conversion
> structure to preserve; it may add little where the task already supplies an obvious
> single-source ground truth and regression oracle.

## Precommitted stratum and selection

External source:

> Magesh et al., *Hallucination-Free? Assessing the Reliability of Leading AI Legal
> Research Tools*

Public dataset:

> `reglab/legal_rag_hallucinations`

The study's independently defined:

> **Treatment (Doctrinal Agreement)**

subcategory asks how one Supreme Court case treated another Supreme Court case it cites,
using treatment relationships such as followed, distinguished or overruled.

Before row outcomes/responses were inspected, #353 froze:

1. Question Category = `Treatment`;
2. public/published dataset order;
3. first complete response with final Label = `Hallucination`;
4. no Needle class/case inspection before selection;
5. no replacement for poor fit, simple result, source difficulty, class match/no-match or
   null.

`Circuit Splits` rows were deliberately excluded because individual row contents/labels
from that stratum had already surfaced during #351 orientation.

The mechanical rule selected:

> **`treatment-doctrinal-agreement-161` — Westlaw**

Question:

> How did REID v. FARGO, AS PRESIDENT OF THE AMERICAN EXPRESS COMPANY, 241 U.S.
> 544 (1916) treat IRVINE v. THE HESPER, 122 U.S. 256 (1916)?

The published Westlaw response says, in substance:

- Irvine had no bearing or relevance;
- Reid contains no mention or reference to Irvine;
- Reid therefore did not treat Irvine in any specific manner.

The authors label the response:

- correctness: **Incorrect**;
- groundedness: null;
- final label: **Hallucination**.

The row was frozen before Needle inspection.

## Stage A — strongest ordinary source-linked postmortem

Needle was not consulted.

### Direct authority relationship

`Reid v. Fargo, 241 U.S. 544 (1916)` directly contradicts the response.

The Reid syllabus states that the Second Circuit's admiralty practice—an appeal by one
party opening the case for a trial de novo—was well established and cites:

> **Irvine v. The Hesper, 122 U.S. 256**

The opinion itself goes further. In rejecting the argument that the court below lacked
authority to treat the appeal as a new trial, Reid says the right to a de novo trial:

> **“authoritatively resulted from the ruling in Irvine v. The Hesper, 122 U.S. 256”**

and treats the point as sufficiently settled that contrary arguments need no further
discussion.

Sources:

- Reid opinion:
  https://usasupreme.clubjuris.com/241/544/case.php
- Irvine case identity/date:
  https://case-law.vlex.com/vid/the-hesper-irvine-v-894937501
- CourtListener U.S. Reports volume metadata:
  https://www.courtlistener.com/c/us/122/

### Input metadata defect

The external question identifies Irvine as:

> `122 U.S. 256 (1916)`

The reporter citation is correct, but Irvine was decided:

> **May 27, 1887**

The bad year is preserved as a query/source-identity metadata defect.

Stage A does **not** infer that this typo caused Westlaw's hallucination.

The stable reporter citation still identifies the case, and Reid itself expressly cites
that citation.

### Decisive failure mechanism

> **authority-treatment erasure**

The response converts an explicit precedent relationship into:

> no mention / no relevance / no treatment.

This is not a disagreement over a proprietary treatment label.

At minimum, Reid expressly relies on Irvine as authoritative support for the de novo
admiralty-appeal rule.

### Consequence

A researcher or citator relying on the response could:

- erase a real precedent relationship;
- misstate doctrinal lineage;
- fail to retrieve the authority Reid identifies as authoritative;
- construct an incorrect treatment/citation graph.

### Corrective rule

For a case-treatment question:

1. inspect the later opinion's actual citation;
2. inspect the proposition around the citation;
3. state the relationship at the level the evidence supports;
4. do not infer "no treatment" from a metadata/search failure.

### Boundary

The supported relationship is proposition-specific:

> Reid relies on Irvine for the de novo admiralty-appeal rule.

That does not establish that Reid adopted every Irvine holding or proposition.

Stage A also does not assign an unverified proprietary citator code such as
`followed` merely because Reid relies on the earlier case.

### Stage-A packet

The strong ordinary postmortem already preserved:

- exact external query/response/author label;
- both authority identities;
- the query's wrong-year metadata;
- direct later-opinion evidence;
- the proposition for which Irvine is used;
- failure mechanism;
- consequence;
- corrective rule;
- narrow authority-treatment boundary;
- uncertainty about exact proprietary treatment coding.

### Observable complexity

Compared with #349, this task requires:

- two legal authorities and their relationship;
- reconstruction of **why** one case invokes the other;
- separation of a metadata error from the substantive treatment relation;
- a boundary against wholesale-treatment overclaiming.

There is no changing-law/version issue as in #339.

Stage A was frozen before v0.2 use.

## Stage B — Reference Pack v0.2

Reference Pack v0.2 was used before broader repository history.

### Existing-class first refusal

No frozen Needle class causally owns the failure.

Rejected apparent near-matches include:

- `JUDICIAL_INTERPRETATION_TEMPORAL_EFFECT`;
- `JUDICIAL_VALIDITY_TEXT_DIVERGENCE`;
- `OFFICIAL_AUTHORITY_HANDOFF`;
- `SOURCE_VIEW_TEMPORAL_DIVERGENCE`.

Their causal owners concern different state transitions or source relationships.

Disposition:

> **NO_EXISTING_CLASS_MATCH**

No new class follows.

### Scientific/reuse status

The external row is:

- public;
- already author-labelled as a hallucination;
- known before Needle reuse.

Therefore any Needle reuse is:

> **known-case failure analysis / exposed regression engineering**

not fresh validation.

### Source identity / metadata discipline

The packet preserves separately:

1. the legal treatment relationship;
2. the erroneous `1916` year attached to `122 U.S. 256`.

The bad year is corrected where case identity is discussed, but it is not retroactively
declared the cause of the original hallucination.

### Boundary discipline

The useful two-sided boundary is:

- **wrong:** Reid does not mention/use/treat Irvine;
- **also unsupported:** Reid wholesale adopted every Irvine proposition or necessarily
  carries a particular proprietary treatment code;
- **supported:** Reid expressly treats Irvine as authoritative support for the de novo
  admiralty-appeal rule.

### Post-hoc regression conversion

This case supports a non-trivial exposed regression candidate.

**Input**

- exact published Treatment question, including the incorrect `(1916)` year.

**Expected behavior**

- reject "no mention / no relevance / no treatment";
- identify Reid's express citation/reliance on Irvine;
- identify the de novo admiralty-appeal proposition;
- where case date/identity is discussed, correct or flag Irvine's 1887 date;
- keep the treatment proposition-specific.

**PASS_REQUIRES**

- recognizes an affirmative precedent relationship;
- identifies the specific proposition for which Reid relies on Irvine;
- does not let the wrong year erase the stable reporter-citation identity;
- avoids unsupported wholesale-treatment claims.

**FAIL_IF**

- says Reid does not mention/rely on/treat Irvine;
- says Irvine is irrelevant to Reid;
- says Reid overruled/distinguished Irvine without evidence;
- blindly repeats the bad year while purporting to identify the earlier case;
- gives only generic case summaries without answering the treatment relationship.

Status:

> **post-hoc derived / public / exposed regression candidate**

It is not historical Needle science and not fresh validation.

## Relative value against Stage A

Needle does not get credit for discovering the authority relationship or correcting the
year. Stage A already did that.

The material addition is the evaluator/debugger/maintainer contract:

- explicit no-class result rather than forced taxonomy;
- scientific/exposure semantics;
- robust handling of malformed metadata without losing stable case identity;
- proposition-specific two-sided boundary;
- explicit non-trivial regression PASS/FAIL contract.

This differs materially from #349.

In #349, the external dataset itself supplied:

> binary query + model output + correct answer.

The regression oracle was almost tautological.

Here, the public row says only that the response is hallucinated/incorrect. A useful future
oracle must be reconstructed from the legal authority relationship and must remain robust
to the query's metadata defect.

For the supported failure-analysis/evaluation/debugging job, that is a material reusable
improvement beyond the frozen postmortem.

## Conditional-value comparison

### #339

Material packet value.

Observable properties included:

- non-trivial doctrinal reconstruction;
- historical statute/source state;
- consequential two-sided boundary;
- non-trivial regression oracle.

### #349

No material packet gain.

Observable properties:

- single controlling source;
- binary explicit disposition;
- dataset already supplied expected answer;
- regression oracle nearly automatic;
- source-state complexity absent.

### #353

Material packet value.

Observable properties:

- two authoritative cases and an inter-case relationship;
- query metadata defect separated from substantive relation;
- proposition-specific treatment boundary;
- dataset does not itself supply a sufficient reusable treatment oracle;
- regression criteria require legal reconstruction.

## Primary outcome

# **CONDITIONAL_PACKET_VALUE_SUPPORTED**

The three observations support a bounded project hypothesis:

> Needle adds material reusable value when a strong ordinary postmortem still leaves
> consequential legal relationship/state/boundary/reuse structure to formalize.

Conversely:

> when the ground truth and future regression oracle are already obvious from the source
> and task, Needle may add only governance metadata and should not claim material packet
> value.

This is not a population-wide causal model or performance claim.

It is a supported use-allocation boundary.

## v0.2 navigation

# **V0.2_NAVIGATION = SUCCESS**

No broad repository archaeology was required.

The released guide/class surface was sufficient for:

- no-class handling;
- scientific/reuse discipline;
- omission rules;
- boundary ownership;
- safe regression conversion.

v0.2 therefore survives its second independent use as the intended navigation/method
surface.

## Structured-layer signal

# **STRUCTURED_LAYER_SIGNAL = INDETERMINATE**

Recurrent structure is now clearer:

- class disposition recurs;
- scientific/reuse status recurs;
- failure mechanism recurs;
- boundary/regression conversion are materially useful on #339/#353 but not #349;
- source-state/identity guidance is material on #339/#353 and absent/non-material on #349.

This supports a **conditional packet shape**, not a universal row schema.

A machine-readable external-failure layer is still not justified because:

- fields are legitimately optional;
- there is no accepted canonical external-analysis membership owner;
- an inclusion rule must distinguish material packet value from ordinary postmortems;
- copying boundary/PASS-FAIL legal truth into a registry could create a competing truth
  store.

The signal therefore advances from #349's `NO` to:

> **INDETERMINATE**

without authorizing implementation.

## What changes

Needle now has a bounded use-allocation rule supported by three observations.

It should not be applied as ceremony to every legal hallucination.

The strong ordinary postmortem remains first refusal.

Needle earns material packet work where consequential reusable structure remains.

## What does not change

No change to:

- frozen corpus or taxonomy;
- Reference Pack v0.2 bytes;
- #214 hard null;
- #327 generic legal-research null;
- #339 positive result;
- #349 bounded packet-value null;
- product scope;
- model/workflow superiority claims.

## Next gate

Queued:

> **#355 — direction review after conditional packet-value support**

That review should decide whether the newly supported conditional contract should now be
consolidated into the public project/use guidance, tested once more at its predicted
boundary, or used to justify a smaller derived navigation layer over accepted use results.

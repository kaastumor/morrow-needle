# #210 design red-team result — latent corpus-assisted workflow pilot

Date: 2026-09-24  
Issue: #210  
Next preparation issue: #212

## Result

GPT-6 Astra / medium returned:

> **REVISE**

The review did not reject a bounded two-arm workflow pilot.

It found one fatal causal overclaim in the draft: giving C an adversarial corpus
also gives C adversarial framing and increased suspicion. Any observed gain
therefore cannot be attributed specifically to case analogy or corpus knowledge.

The frozen claim is narrowed to:

> Under fixed model, tool and resource conditions, does **offering the frozen
> corpus index with the frozen instruction** improve latent diagnosis and
> consequential correctness relative to ordinary source-grounded QA on this
> selected challenge set?

The C treatment is explicitly:

> **index access + adversarial framing + any attention that package induces**

No mechanism-isolation claim is allowed.

## Repairs adopted

The frozen #210 design now specifies:

- exact corpus artifact:
  `corpus/index-v0.1.json`, Git blob
  `82712a726193f203d4886ef5f925fab322e7c6cc`;
- index-only use by C; Needle issue/file references may not be followed;
- exact R/C investigator instructions;
- equal model/version, reasoning tier, tools and source ceiling;
- deterministic family queue;
- bounded first-eligible compiler search;
- matched negative control;
- constrained cue-audit edits;
- separate correctness / detection / unsupported-certainty / control scores;
- strict diagnostic-rescue semantics;
- anonymized scoring before arm reveal where practicable;
- leakage or material execution failure -> UNINTERPRETABLE.

## Interpretation repair

The draft was also too strong about what 2–3 rescues could establish.

Frozen interpretation:

- 0 diagnostic rescues -> value not demonstrated; stop and allow contraction
  toward **adversarial regression/reference corpus + minimal evaluation rules**;
- 1 diagnostic rescue -> signal only;
- 2–3 rescues across distinct families, without consequential C-only regression,
  -> justify **independent replication only**;
- any consequential C-only regression weakens the workflow case.

Correctness-only differences do not count as diagnostic rescues.

## Tolerable limitations retained

This selected challenge-set pilot cannot establish:

- that R's model never saw public Needle material during training;
- prevalence or average performance in ordinary legal research;
- stable effects across model/version/generation;
- a general false-positive rate from one control.

Optional corpus non-use is also a valid treatment outcome.

## Case-selection firewall

No scored case was selected in the design or Astra-review context.

Fresh case compilation belongs to #212 under the pre-frozen family queue,
eligibility tests and source budgets.

If 3 adversarial tasks + 1 matched control cannot be sealed under those rules,
the correct result is:

> `SAMPLE_INCOMPLETE / PREPARATION_FAILURE`

Do not weaken eligibility to preserve the experiment.

## Canonical ownership

The complete frozen design is the final body of Issue #210.

The verbatim Astra review is preserved in Issue #210's first comment.

#212 owns fresh case compilation only. It may not run investigator arms.

No product, ontology, Method/Core expansion or Cycle 4 is authorised.

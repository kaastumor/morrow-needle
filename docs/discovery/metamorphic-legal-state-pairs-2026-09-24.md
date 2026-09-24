# DISC-01 — metamorphic legal-state pair discovery

Issue: #111  
Parent: #104  
Date: 2026-09-24

## Question

Would explicit metamorphic case families add diagnostic value beyond grouping by trap class?

Alternative explanation: the corpus already captures the useful distinction through trap classes and individual evidence owners; a family abstraction could merely add ontology and maintenance without changing what can be tested.

## Internal evidence

The canonical corpus already contains natural related cases, but most are **same failure-family examples**, not controlled metamorphic pairs. Examples include the two private-origin/legal-recognition cases and the two judicial cases. Sharing a trap class is useful for browsing, but it does not establish a metamorphic relation: more than one legally material variable can differ between independent real cases.

The project has also used the 320/250 shredder and June/October Temu concepts as methodological precedents for changing one legally material condition while holding the surrounding question stable. They are precedents for experimental design only. No result is attributed here to any control that was not actually executed.

This distinction matters because a genuine metamorphic pair makes a stronger diagnostic claim than a category grouping: under an explicitly stated transformation, the expected answer or legally relevant state should change (or remain invariant) in a specified way. Calling loosely similar cases a pair would create false experimental precision.

## Adjacent precedent

Gardner et al. (Findings of EMNLP 2020), *Evaluating Models' Local Decision Boundaries via Contrast Sets*, proposes manually perturbing test instances in small but meaningful ways that typically change the gold label. The value is local diagnostic evidence about a system's decision boundary rather than another aggregate benchmark category. DOI: 10.18653/v1/2020.findings-emnlp.117.

Li et al. (BlackboxNLP 2020), *Linguistically-Informed Transformations (LIT)*, shows that transformations can generate contrast sets, but also makes clear why automation is not automatically attractive here: legal transformations require authoritative legal grounding, not merely a syntactically valid perturbation. DOI: 10.18653/v1/2020.blackboxnlp-1.12.

The reusable lesson is narrow: **controlled contrast is valuable when the transformation and expected relation are independently justified**. Needle should not import automatic mutation machinery or a general metamorphic-testing ontology.

## Smallest useful experiment

Do not change `corpus/index-v0.1.json` yet. For one future fresh, independently evidenced legal scenario, pre-register a two-member contrast before evaluation:

1. one stable research question;
2. one named legally material variable and two authoritative states/values;
3. an expected relation (`ANSWER_FLIPS` or `ANSWER_INVARIANT`) justified by the answer key;
4. all other material premises held constant as far as the legal question permits;
5. both members sealed and evaluated under the existing contamination rules.

The experiment succeeds only if pair-level scoring reveals a failure that ordinary per-case correctness/trap-class grouping would hide—for example, answering both members identically when the answer key requires a flip. If it yields no additional diagnostic signal, keep trap-class grouping only.

No schema is needed to run that experiment: a discovery/evaluation artifact can own the pair definition and point to the two case IDs after exposure. A corpus-level family field should be considered only after repeated useful pairs demonstrate a browsing/query need.

## Adversary

The strongest attack is that metamorphic language can make two messy legal histories look more controlled than they are. Independent real cases commonly differ in authority, time, instrument identity, facts and source state simultaneously. Treating those as transformations would launder confounding into a benchmark relation.

A second attack is contamination: constructing a public pair around an already exposed case does not create fresh blind validation. The existing exposure rule still applies to each member.

A third attack is scope creep. A new family schema, automatic pair generator or UI relation would be premature before one fresh pair demonstrates diagnostic value unavailable from current case-level grading.

These attacks narrow rather than defeat the idea: the useful hypothesis is about **pre-registered controlled contrast in evaluation**, not about organizing the existing corpus into a new ontology.

## Decision

**ADOPT_FOR_EXPERIMENT**

Adopt only the bounded experimental design above. Do not add a corpus schema field, explorer feature, automatic mutation system, or generic family graph. A later explicitly authorised experiment should create one fresh evidence-grounded pair and test whether pair-level consistency/flip scoring adds diagnostic information beyond existing per-case results. Discovery completion does not authorise that implementation or evaluation run.

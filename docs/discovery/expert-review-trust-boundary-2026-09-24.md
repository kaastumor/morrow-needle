# DISC-02 — external expert review and trust-boundary discovery

Issue: #112  
Parent: #104  
Date: 2026-09-24

## Question

What external/expert review is actually required before Needle can make stronger claims about answer-key quality or benchmark validity?

Alternative explanation: because Needle's cases are primarily provenance-bearing research artifacts grounded in public official sources, requiring a lawyer to approve every field would add cost and authority theatre without improving the artifacts that can be checked mechanically or directly against their evidence.

## Internal evidence

Needle currently separates several claims that should not share one review burden. The corpus index points to existing evidence owners rather than duplicating legal truth. Deterministic validation can establish structural facts such as schema shape, identifiers, exposure metadata and reference integrity. Existing evaluation results establish only the bounded construct actually tested; #88/#95 and #97 are explicit examples of why a technically clean result must not be promoted into a broader legal-reasoning claim.

The important trust boundary is therefore not "all corpus content needs expert approval." It is whether a human-authored legal proposition is being used as a gold answer or as evidence for a benchmark-validity claim that goes beyond directly observable source metadata.

## External precedent

LegalBench was built through an interdisciplinary process in which legal professionals designed and hand-crafted tasks. Its useful precedent is not a universal reviewer requirement; it is that subject-matter expertise participates where the benchmark claims to measure legally meaningful reasoning. Guha et al., *LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models* (NeurIPS 2023), arXiv:2308.11462.

PLawBench makes the boundary still clearer for realistic legal-work evaluation: its 850 questions use expert-designed fine-grained rubrics, and its automated evaluator is justified by alignment against human expert judgments rather than treated as self-validating. Shi et al., *PLawBench: A Rubric-Based Benchmark for Evaluating LLMs in Real-World Legal Practice* (2026), arXiv:2601.16669.

A recent Dutch precedent, DELTA, describes itself as a practitioner-led benchmark for real Dutch legal work and foregrounds law-firm participation. That is relevant to claims about professional usefulness and judgment, but it does not imply that ordinary provenance/index metadata needs practitioner sign-off.

These precedents support **claim-proportionate review**, not a blanket legal-review workflow.

## Trust boundary

Three artifact classes should remain distinct:

1. **Mechanically/directly verifiable metadata** — identifiers, reference existence, exposure/evaluation labels, schema constraints and other facts whose acceptance can be deterministically checked or directly copied from an authoritative owner. External legal review is unnecessary unless a dispute exposes semantic ambiguity.
2. **Source-grounded research findings** — propositions reconstructing what an official source says or what changed. These need traceable evidence and adversarial checking; an external expert is useful for high-consequence or ambiguous interpretation, but mandatory review of every finding is not yet justified.
3. **Gold legal judgments / benchmark-validity claims** — answer keys that resolve contestable legal interpretation, rubrics claiming legally correct reasoning, or claims that aggregate scores measure professional legal capability. These require independent domain-expert review before Needle should make a stronger validity claim.

Expert review does not cure contamination, weak construct design, stale law, missing provenance or non-independent answer-key creation. It is one control at the interpretation/validity boundary, not a certification layer over the corpus.

## Smallest credible experiment

Do not build a reviewer platform and do not review the whole corpus. Select a stratified sample of **6 existing cases** only when a stronger answer-key-quality claim is actually contemplated:

- 2 cases whose decisive answer is predominantly direct official-source fact;
- 2 temporal/source-state cases requiring legal-effect reasoning;
- 2 cases with the highest plausible interpretive ambiguity.

For each case, provide one independent EU-law-qualified reviewer the frozen question, answer key, cited official evidence and scoring rationale, but not the project's desired disposition. Ask for four bounded outputs: `AGREE`, `MATERIAL_CORRECTION`, `AMBIGUOUS`, or `OUT_OF_SCOPE`, plus a short reason and evidence citation for any non-AGREE result.

Record review time per case. Escalate to a second independent reviewer only for `MATERIAL_CORRECTION` or `AMBIGUOUS`; do not manufacture inter-rater statistics from six cases.

### Cost boundary

This experiment costs 6 first-pass expert reviews plus at most 6 second-pass reviews, rather than creating a standing panel or reviewing every metadata field. Monetary cost cannot be responsibly estimated without an actual reviewer/rate; capture elapsed review minutes and quoted/actual fee during the experiment instead of inventing a budget now.

## Falsifiable decision rule

The experiment would justify a repeatable expert-review step only if it finds at least one material answer-key correction/ambiguity that existing evidence/adversarial review missed **and** the defect is relevant to a claim Needle wants to make. If all six keys survive and disagreements concern only presentation or mechanically checkable metadata, keep expert review on-demand and do not add workflow machinery.

Even a successful sample does not validate the entire corpus. It would only establish that independent domain review can detect defects worth catching and justify designing a larger validation study if stronger benchmark claims are desired.

## Adversary

The strongest attack is credential laundering: attaching a lawyer's approval can make a small research corpus appear legally certified while leaving construct validity, sampling bias, contamination and source freshness untouched. A second attack is circularity if the reviewer sees the expected trap or project rationale and merely confirms it. A third is cost displacement: mandatory expert review can slow admission of directly verifiable provenance cases without increasing their reliability.

Conversely, avoiding expert review entirely becomes indefensible once Needle claims that contestable answer keys are legally correct at benchmark scale or that model scores measure professional legal competence. Deterministic CI cannot establish either proposition.

The boundary should therefore follow the claim, not the file type or the prestige of the reviewer.

## Decision

**ADOPT_FOR_EXPERIMENT**

Adopt only the six-case independent review experiment if/when Needle seeks a stronger answer-key-quality or benchmark-validity claim. Keep deterministic/directly verifiable metadata outside mandatory expert review. Do not build reviewer tooling, establish a standing panel, certify the corpus, or promote current answer keys on the basis of this discovery note. Discovery completion does not authorise the experiment itself.
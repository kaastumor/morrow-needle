# EU Legislation Navigator — Prototype design and execution brief
Version 0.1 • 27 September 2026 • Sponsor-requested design for GPT-5.6 execution

## 1. Decision and authority

Design a public-facing, plain-language EU legislation navigator with Overview and Legal detail presentations of the same evidence. Working name only; branding is not a task.

This document is a proposed execution contract, not a new live backlog. The sponsor requested prototype structure and planning; this design turn does not implement, deploy, recruit, select a license or change Needle's scientific claims. When the sponsor hands this brief to 5.6 for execution, reconcile it with current GitHub state and adopt the bounded horizon through the existing project process.

Canonical repository: https://github.com/kaastumor/morrow-needle

BACKLOG.md remains the sole mutable owner of current mode, WIP and immediate priority. Use one active work item at a time. Create dependent issues only when their inputs and gates are ready; the work-package table below is a plan, not an automatically executable queue.

At design inspection:
- BACKLOG.md identifies #434, the Low Voltage Directive lifecycle projection, as sole WIP.
- #432 permits an act-centric, one-act, one-hop experiment using typed relationships and existing truth owners.
- External-user recruitment is deferred until product readiness. Outreach, purchases and vendor accounts need explicit sponsor authorization.
- Project licensing remains INSPECTABLE_ONLY_FOR_NOW. Public visibility is not an open-source grant.
- The corpus remains frozen at 81 cases / 26 classes. Its scientific results do not establish this product's usefulness.
- Root AGENTS.md returned not found; execution must recheck current instructions rather than assume it cannot exist later.

Read the current owners at execution time. These observations are a dated baseline, not ongoing state.

Important correction to the earlier brainstorm: do not start with several independently maintained act pages or national implementation. Complete or reuse #434 first. Multiple pages and wider coverage are conditional follow-on experiments.

## 2. Product hypothesis

A reader inspecting a known EU legal act can understand its purpose, scope, lifecycle, immediate legal relationships and evidence more accurately or with materially less effort through one coherent page than through a strong realistic alternative.

Primary initial job:
“I found this directive. Explain what it does, where it came from, which dates mean what, what connects to it, and where I can check your explanation.”

Primary audience hypothesis: an occasional EU-law reader with a concrete work or study question. Secondary audience hypothesis: a professional who wants quick orientation and exact evidence. These are hypotheses, not researched personas.

Overview and Legal detail are presentation options, not assumed permanent product requirements. Compare them with one progressively disclosed page. Keep the simpler presentation if a toggle adds navigation burden.

Success claims must stay separate:
1. Technical feasibility: the page renders and follows its content contract.
2. Evidence integrity: claims can be traced and reviewed.
3. Usability: actual readers can complete the intended tasks.
4. Comparative value: readers do better than with a realistic alternative.
5. Sustainability: content can be maintained at an acceptable cost.
6. Commercial viability: a separate, currently untested proposition.

Passing 1–2 does not establish 3–6. A useful public-interest service need not prove novelty or immediate revenue.

## 3. First horizon and boundaries

Deliver one credible, inspectable act page for Directive 2014/35/EU, reusing the current Candidate-B surface and #434 result wherever suitable.

Minimum outcome:
- A plain-language account of purpose, covered groups and important exclusions.
- Distinct lifecycle events with sources and date meanings.
- A compact lineage/context view with typed connections.
- An explanation of the represented Article 12 mechanism and links to existing standard-status examples.
- A precise evidence boundary and last legal verification date.
- Access to legal detail without hiding qualifications in the overview.
- A maintenance rehearsal and an executable future user-test protocol.

The existing predecessors and framework acts may appear as linked relationship entries. This does not require complete explainer pages for every linked act.

Default boundaries:
- English content first; record language scope. Dutch is a later demand-led option.
- EU-level explanation, not a determination of a reader's national obligations.
- Manually bounded coverage; no “search all EU law” implication.
- No live monitoring, alerts, user accounts, portfolio, general chatbot or personalized compliance conclusion.
- No complete case-law graph, national transposition database or applicable-standard finder.
- No generic RELATED_TO relationship, inferred ancestry or political influence graph.
- No automatic claims that proposed changes are enacted.
- No new general ontology or resurrection of the full historical architecture.
- No new backend or model calls in the public interface unless a concrete accepted task proves necessity.

A missing input should narrow or label a claim, not be completed with plausible prose.

## 4. Planned effort and learning allocation

Use 24 planning units for the initial horizon. A unit represents roughly 45–60 minutes of focused effort for budgeting, not a promised agent runtime, scheduled job, or requirement to consume time. Record actual effort where available and compare at milestones. Sessions may complete several small units or need several sessions for one.

| Allocation | Units | Purpose |
| --- | ---: | --- |
| Current-state reconciliation, audience/job discovery, realistic alternatives | 3 | Determine the problem and avoid duplicating active work |
| Legal content, source feasibility, standards and external dependencies research | 4 | Resolve consequential uncertainties before presenting facts |
| Information architecture and content experiments | 2 | Test what should be visible and how |
| Thin implementation using existing work | 6 | Deliver one complete reader journey |
| Evidence checks, adversarial tests and usability preparation | 4 | Establish readiness and expose misleading interpretations |
| Maintenance, update rehearsal and operating-cost assessment | 2 | Test whether the service can remain trustworthy |
| Synthesis and next-allocation decision | 1 | Choose a defensible next step |
| Unallocated discovery/repair reserve | 2 | Investigate surprises that could change the decision |
| Total | 24 | Initial bounded horizon |

Protect the nine discovery/research/design units from being silently converted into coding. Reallocate unused units openly if evidence already answers a question; do not repeat research to satisfy a quota.

The reserve can fund an external-factor surprise, one alternative presentation, or one high-value model/source uncertainty. It is not a feature allowance. If the horizon overruns materially, checkpoint, identify the cause and reduce scope or explicitly replan.

Real-user evaluation is a subsequent conditional allowance: initially 6–8 participants, roughly 30 minutes each, plus preparation and analysis. Recruitment calendar time and qualified legal review availability are unknown and must be reported separately. Do not call an internal simulation “user discovery.”

## 5. Execution packages and gates

| Package | Dependencies | Work and concrete output | Completion / decision |
| --- | --- | --- | --- |
| P0 — Reconcile | Current repository access | Inspect owners, #432/#434 and actual pending changes; identify reusable UI and truth owners; propose the live allocation | One current WIP; no duplicate implementation; scope explicitly recorded |
| P1 — Job and alternatives | P0 | Write 6–8 reader tasks, assumptions and a short comparison of real alternatives | A reader job and falsifier; strongest attainable baseline selected |
| P2 — Content and evidence | P1 | Source-backed content sheet, claim-to-owner mapping, limits and unanswered legal questions | Every consequential displayed claim supported or explicitly unresolved |
| P3 — Presentation decision | P2 | Compare a source-linked note, progressive disclosure, and Overview/Legal detail wireframes using the same facts | Choose smallest plausible design; record why and what remains user-untested |
| P4 — First vertical slice | P2–P3; reconcile #434 | Complete/reuse one LVD page and its existing status-card navigation | Intended journey works; no conflicting truth store; existing status lookup retained |
| P5 — Integrity and adversarial review | P4 | Run targeted semantic regressions and browser/accessibility checks; record defects and fixes | No unresolved critical misrepresentation; limitations visible at relevant claims |
| P6 — Maintenance and external-factor gate | P5 | Rehearse one source change/correction; measure affected content and repair effort; update risk findings | Evidence of maintainability or explicit failure; release boundary documented |
| P7 — Readiness readout | P6 | Runnable prototype, evidence map, known limits, test materials, decisions and next recommendation | READY_FOR_USER_TEST, REVISE, NARROW or PARK; no inferred user-value win |
| P8 — Human comparison, conditional | P7 readiness plus participants/outreach authorization | Run the frozen comparison protocol below | Directional human evidence with limitations, not population proof |
| P9 — Expansion choice, conditional | P8 or a separately justified sponsor scope decision | Choose one: deepen LVD, test a second act type, or end this horizon | One new bounded question; no automatic platform roadmap |

P0–P3 need not generate separate PRs if a compact design checkpoint suffices. Implementation still follows the repository's issue/branch/PR discipline. If #434 is already complete, verify and reuse it; never rebuild solely to follow this table.

Internal review may reveal a need for a bounded repair. It may not keep adding examples to substitute for missing human evidence. Product-readiness work is allowed before recruiting, consistent with current sponsor sequencing.

## 6. Research and discovery questions

Keep a compact question ledger: question, decision affected, strongest contrary explanation, evidence/source date, finding, confidence/limits, action. Combine this with the research result rather than creating a separate governance system.

A. Audience and job
- Does the reader begin with an act identifier, a topic, or a practical situation?
- Can a known-act page complete a useful job without universal search?
- Which qualifications do occasional readers misunderstand?
- Does legal detail help professional verification or merely duplicate EUR-Lex?
- Before recruitment, use the sponsor's task and public precedents as hypothesis inputs only.

B. Legal meaning and evidence
- Can the selected act's purpose, scope and main exclusions be expressed briefly without changing their meaning?
- Which dates require provision-level or transition-specific explanation?
- Which relationships are legally asserted, and which are editorial context?
- Where does an EU-level statement stop being sufficient?
- Distinguish legally changed obligations from policy aims, predicted impacts, observed impacts and individualized consequences.

C. Information design
- Research authoritative accessibility guidance and plain-language public-service patterns.
- Compare timeline, typed relationship list/map and source-linked note on actual tasks.
- Investigate ambiguity of “in force,” “applies,” “expires,” “replaced,” “impact” and “current.”
- Test whether persistent scope/date context works better than repeated warnings.
- Avoid using readability scores as evidence of correct understanding.

D. Technology and source feasibility
- Inspect existing Needle temporal, lineage, identity and provenance owners before designing new fields.
- Verify available official identifiers, source routes, retrieval conditions and source-version distinctions.
- Record whether a source is authentic legal text, a consolidated convenience text, an official summary or interpretation.
- Assess stable links, structured data access and manual source fallback without building bulk ingestion.

E. Open discovery
- Reserve one bounded search for a better framing or unexpected use, such as sharing a concise evidence-backed act explanation.
- A discovery can simplify or reject the prototype. It need not produce a new feature.
- End a search when the decision is answerable or further evidence is unavailable within the budget; record the unresolved dependency.

## 7. External factors and responses

Review these at P1/P2 and once before P7. This is a bounded scan, not a new monitoring service.

| Factor | Evidence to inspect | Consequence for the prototype |
| --- | --- | --- |
| Official alternatives | EUR-Lex summaries, document information, procedures; OEIL; EU Law Tracker | Credit capabilities actually observed; reuse/link where sufficient |
| Commercial alternatives and AI | Public documentation; actual access only if authorized | Separate advertised features from verified workflow; no superiority claim from brochures |
| Source access and reuse | Official access documentation, rights statements, endpoint behavior | Choose supported retrieval/linking; avoid protected technical-standard text |
| Legislative developments | Official sources relevant to represented acts and proposed changes | Verify before release; preserve proposed versus enacted state |
| Language and national variation | Official language versions and implementation information where material | State limits; do not turn English EU coverage into national legal advice |
| Accessibility and device use | WCAG guidance, keyboard/mobile/screen-reader behavior | Accessible semantic structure; map information also available as text |
| Discoverability and trust | Official-source search results, page title, provenance visibility, independent identity | No implication of EU endorsement; test whether the page is understandable when opened directly |
| Maintenance economics | Measured initial research and change-repair effort | Cap coverage at what can be responsibly maintained |
| Public operation | Hosting cost, correction route, privacy choices, ownership | Default no telemetry; name an owner before ongoing public operation |
| Project/source licensing | Current project decision and rights for displayed third-party content | Do not select a license or reproduce protected material by implication |

Each finding gets one disposition: reuse, benchmark, learn from, remove from scope, or unresolved dependency. External research that only increases the feature list has not completed its job.

## 8. Content and interaction contract

Recommended reading order:
1. Act identity and short purpose.
2. “At a glance”: represented legal state, date perspective, covered groups and major limits.
3. “Key dates”: labelled events, not a single lifespan bar.
4. “Where it came from”: typed ancestry/replacement links.
5. “What connects to it”: selected legal context and represented downstream mechanisms.
6. “What changes in practice”: carefully bounded legal effects and examples.
7. Sources, legal detail, coverage and correction information.

| Content | Overview | Legal detail |
| --- | --- | --- |
| Purpose | Concise explanation in ordinary language | Relevant provisions; policy-purpose attribution where appropriate |
| Scope | Covered groups and consequential exclusions | Definitions, conditions and precise scope references |
| Time | Distinct events and understandable labels | Governing provisions, precision, transitions and historical perspective |
| Relationships | Typed, readable descriptions | Exact relationship basis and evidence |
| Consequences | Bounded examples of legal changes | Supporting provision, assumptions and interpretive limitations |
| Verification | Direct evidence and last checked date | Version, language, claim provenance and unresolved points |

The legal facts and material caveats must agree across both presentations. Keep uncertainty next to the affected statement. Never hide a meaning-changing exception behind Legal detail.

“Duration” handling:
- Represent adoption, publication, entry into force, application and end/repeal separately where relevant.
- Support different provision dates; do not infer legal effect from graph order.
- Distinguish “no fixed end date evidenced,” “end not researched” and “no successor represented.”
- Label already-enacted future changes separately from current state and from proposals.
- A timestamp of deployment is not a legal verification date.

“Impact” handling:
- Initial coverage: what legally changes and who is within the represented scope.
- Attribute policy aims and forecast impacts explicitly if included.
- Observed economic/social impact requires separate empirical evidence.
- Do not score a law as good/bad or assign an opaque impact score.
- No personalized conclusion from general scope text.

Accessibility target: WCAG 2.2 AA as a design target, with actual tested criteria recorded. Do not claim complete conformance from an automated scan. Provide keyboard operation, visible focus, meaningful reading order, sufficient contrast, non-color labels and mobile reflow. Diagrams need equivalent readable text. Preserve act/date context when switching views and using back/deep links.

## 9. Architecture and content ownership

Keep the existing application's stack for this slice. Determine its actual structure during P0; no framework migration is earned by this brief.

Data flow:
official evidence -> existing canonical claim/state owners -> generated presentation -> Overview / Legal detail.

This is a logical ownership model, not a demand to deploy new infrastructure.

- Reuse existing canonical truth wherever it exists.
- Editorial explanations reference the claims/provisions they describe and record their review basis.
- Generated UI data may repeat values as a disposable build artifact, never as an independently edited truth source.
- Missing legal state belongs in an appropriate existing owner or remains unresolved.
- If a genuinely missing relationship needs a model repair, demonstrate the failure and make the smallest repair.
- Stable CELEX/ELI links identify sources; they are not a warrant to merge distinct versions/resources.
- Separate verified-through date, legal as-of date and source observation date.
- Missing or conflicting evidence must not silently produce a green/current badge.
- Keep content available without relying on an AI response at page load.
- No automatic recursive expansion of linked acts.

Content-update sequence:
observe relevant change -> identify dependent claims and explanations -> review affected evidence -> rebuild view -> run consequential regressions -> publish through the authorized release path.

For the prototype this can be manual. If a change cannot be resolved, mark the affected claim unavailable or awaiting review and preserve the dated supported state. Do not leave unsupported “current” conclusions visible.

## 10. Evaluation and falsifiers

A. Internal readiness
Preserve #432's eight questions and #434's accepted criteria. Add:
- Can the overview be read without confusing adoption, force and application?
- Can readers distinguish ancestry from framework context?
- Can they see why a downstream standards example does not certify a product's compliance?
- Can they identify what was not checked?
- Does the original known-standard status task remain easy to complete?

Internal walkthroughs are design checks, not evidence of user success.

B. Strong alternatives
Use the best relevant official workflow for each task, including official summaries and document relationships. Also prepare a competent short source-linked note for the same frozen scope. Compare against a capable source-grounded AI only when making a claim about replacing that workflow, with comparable tools and evidence access. Avoid accumulating arms that do not affect the decision.

C. Human protocol, later
- Start with 6–8 participants spanning occasional readers and experienced practitioners, ideally at least three of each.
- Small formative sample; report individual outcomes and medians, not statistical generalization.
- Freeze tasks, critical-error definitions and decision rules before sessions.
- Use matched task sets and counterbalance interface order to reduce practice effects.
- Give reasonable familiarization to each alternative.
- Record correctness, verification success, completion time, material omissions and answer confidence.
- Record appeal/preference separately from performance.
- Do not require participants to expose private client material.
- Obtain authorization for recruitment/contact; participant consent for any recordings or retained data.
- Arrange review of consequential legal answers by a suitably qualified reviewer before treating the comparison as externally validated. If unavailable, label answer-key assurance as limited.

Provisional decision rules to freeze at P7:
- Any unresolved critical product-induced misunderstanding blocks expansion/release of the affected content.
- Seek at least 80% completion on the selected core comprehension tasks, with no hidden subgroup collapse.
- Require a meaningful benefit versus the selected strong baseline: for planning, a 20% lower median task time with no correctness loss, or a clear reduction in consequential errors/verification failures.
- These percentages are project decision thresholds, not industry standards or statistical proof. Refine before testing if pilot task timing shows they are inappropriate; never change them after seeing comparative results to manufacture a pass.
- A tie may justify a simpler, inexpensive public explanation if users find it useful, but earns no superiority claim.

D. Maintenance rehearsal
Inject a clearly labelled local test change or replay an actual historical change against a frozen snapshot. Do not falsify live legal facts.
Measure how many claims, explanations and displays need review; whether both views update together; time to correction; and whether the evidence trail survives. One successful rehearsal establishes only narrow feasibility.

E. Falsifiers
NARROW, REVISE or PARK if:
- Useful answers require broad national/case-law coverage before the first job can be completed.
- Two views routinely disagree or hide meaning-changing conditions.
- The strongest source-linked note performs as well and the richer surface adds no demonstrated benefit.
- Maintenance exceeds the plausible benefit at the selected coverage.
- Users repeatedly infer completeness or certainty despite targeted redesign.
- A new architecture is doing most of the work merely to render one act.
- Internal examples keep multiplying while the same external-value question remains unresolved.

One revision cycle is a default budget, not an eternal license to retest. Preserve failures and select the next allocation explicitly.

## 11. Adversarial review of this plan

| Attack on the plan | Built-in response |
| --- | --- |
| “This revives a failed broad product thesis under a new name.” | New claim is bounded comprehension/navigation; prior scientific nulls remain intact; one act first |
| “The sponsor's enthusiasm will be mistaken for demand.” | Sponsor input defines a legitimate task; human value remains separately unproven |
| “Readiness becomes an excuse never to meet users.” | P7 produces a concrete test-ready artifact and names the external dependency; no endless internal expansion |
| “Early user testing is impossible before anything credible exists.” | Build the coherent first slice before recruitment, consistent with current sequencing |
| “Discovery gets squeezed out by coding.” | Protected research allocation plus reserve; explicit reallocation |
| “Research becomes more process than product.” | One compact result ledger; no document per question; decision-focused stopping |
| “One atypical directive proves all EU legislation works.” | No generalization; second act type is a conditional transfer test |
| “A formal graph conceals unsupported relationships.” | Typed links, claim-level evidence, bounded coverage and plain text equivalents |
| “Keeping two views doubles the maintenance work.” | Shared facts and dependent editorial content; explicit update rehearsal |
| “A public website silently implies open-source rights or legal authority.” | Separate publication/reuse decisions; clear independent identity and source attribution |
| “Automated checks prove legal correctness.” | Checks enforce representation and known regressions; qualified evidence review remains distinct |
| “Cost controls remove necessary assurance.” | Run required gates once; avoid redundant CI/polling rather than skipping critical verification |

## 12. Minimal repository integration for 5.6

Suggested durable design location:
docs/plans/eu-legislation-navigator-prototype-v0.1.md

Use existing naming/layout conventions if they differ. Do not create empty directories or a new governance framework.

After reconciling and adopting the horizon:
- Keep this design as the stable contract.
- Put live allocation only in BACKLOG.md.
- Use the active issue for exact acceptance and execution checkpoints.
- Maintain one compact research/result document under the existing discovery convention.
- Keep content/evidence in existing owners and implementation in the existing app.
- Keep evaluation materials with existing evaluation assets.
- Add focused tests where semantic behavior can regress; avoid tests that merely restate static copy.
- Preserve corpus freeze and historical evidence unchanged.
- Recheck actual workflows before changes; batch documentation where practical, avoid redundant Actions and never poll repeatedly.
- Use local validation for iteration, then required repository gates for the reviewed change.
- Public deployment follows the actual applicable hosting/release workflow and existing authorization. This design brief alone is not an instruction to deploy.

Checkpoint format:
1. Accepted artifact/commit and completed outcome.
2. Evidence or design decision that changed.
3. Remaining uncertainty/blocker.
4. Exact next work item or resumable state.

## 13. Decisions reserved for later

5.6 may autonomously choose ordinary wording, component layout, test implementation and bounded research methods within the adopted scope.

Decisions needing new evidence or an explicit scope decision:
- A separate repository/fork and its maintenance ownership.
- Any change to Needle's enduring identity or scientific claims.
- Additional act families, national jurisdictions or languages.
- Live monitoring, authentication, paid services or broad search.
- Public reuse license and ongoing service commitment.
- Outreach, purchases or vendor accounts under existing project constraints.

Do not ask the sponsor about routine implementation choices. Complete all independently possible work and make any eventual decision request concrete.

Fork recommendation: a logically separate product experiment first, reusing existing code and evidence. Decide on a physical fork after usability and maintenance findings clarify whether independent release/ownership would help. Duplication is a cost to justify, not a prerequisite for the prototype.

## 14. Source and inspection record

Repository files inspected on 27 September 2026:
- BACKLOG.md (blob 6f1744c9918ffa48a64f5b36b7844d4835abba26 at retrieval).
- docs/project-charter.md (blob 9d8992bf54bff5bf90b6cb5584d1dd0b2db69096).
- docs/way-of-working.md.
- README.md.
- docs/history/README.md and docs/history/asset-register.md.
- docs/discovery/issue432-act-centric-lifecycle-red-team-2026-09-27.md.
- Issues #432 and #434.
- Root AGENTS.md was requested and returned 404.
The live application and full implementation were not reviewed for this design. Do not treat this document as a code audit.

Official research starting points checked during this brainstorm/design:
- EUR-Lex: https://eur-lex.europa.eu/homepage.html
- Summaries: https://eur-lex.europa.eu/browse/summaries.html
- Legislative Observatory: https://oeil.europarl.europa.eu/oeil/en
- Official procedure overview: https://eur-lex.europa.eu/collection/legislative-procedures.html
- EU Law Tracker: https://law-tracker.europa.eu/content/about?lang=en
- ELI implementation guidance: https://eur-lex.europa.eu/content/eli-register/implementing_eli.html
- EUR-Lex webservice documentation: https://eur-lex.europa.eu/content/help/data-reuse/webservice.html?locale=en
- WCAG 2.2: https://www.w3.org/TR/WCAG22/

EUR-Lex already offers summaries and legal-document navigation; OEIL and EU Law Tracker cover legislative procedures. ELI supplies established identification/metadata conventions. WCAG supplies testable accessibility criteria. These are starting points for scoped research, not findings that any particular layout is best. API conditions, reuse rights, source coverage and legal freshness still need P2 verification.

## 15. Copy-paste handoff prompt

You are executing the sponsor-requested EU Legislation Navigator prototype design for kaastumor/morrow-needle.

Read the attached “EU Legislation Navigator — Prototype design and execution brief v0.1” in full. GitHub main is canonical for accepted state; reconcile this sponsor-requested horizon with current BACKLOG.md, charter, way of working, any applicable AGENTS.md, active issues/PRs, and #432/#434 before editing. Do not assume #434 is still unfinished.

Your objective is a credible, bounded public-facing explanation of one EU act, with Overview/Legal detail or a simpler presentation if research supports it. Start from the Low Voltage Directive lifecycle slice. Reuse accepted work and existing legal truth owners.

Adopt the design through the repository's normal process and work in checkpointed milestones with WIP=1. Preserve the planned discovery, legal/source research, external-factor review and maintenance assessment; do not turn the brief into a feature-only build queue. Research can narrow or reject a choice. Ordinary implementation decisions are yours.

First milestone: reconcile current state, identify reusable implementation/evidence, record the bounded horizon and next executable item, and resolve the most consequential P1/P2 unknowns that fit that milestone. Continue authorized work rather than asking for routine confirmation. Save durable checkpoints to GitHub.

Keep frozen scientific evidence and prior negative findings intact. Internal technical readiness is not user-value proof. National implementation, broad graphs/search, monitoring, extra jurisdictions and a physical fork are conditional, not default scope.

External outreach remains deferred under the current rules. Prepare an executable user-test package and name the dependency when it is truly reached; do not fabricate users, qualified review, competitor access or performance results. Do not purchase services, change licensing or deploy a new public release merely because this is a public-facing design.

Use focused validation, keep GitHub Actions economical, and report what changed, what was actually checked, what remains uncertain, and the next bounded step.

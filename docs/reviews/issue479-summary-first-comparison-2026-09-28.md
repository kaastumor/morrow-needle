# #479 — Summary-first medical-devices landing page: comparison review

Date: 2026-09-28  
Disposition: **REVISE_SUMMARY_FIRST — FOUNDATIONAL CONTRACT SUPPORTED / CURRENT-STATE CONTRACT NEEDS REPAIR**

## 1. Decision

The #477 experiment answers the foundational UX criticism.

The summary-first page is materially better aligned with a public legal-orientation job than `/regime-v2/` because it explains purpose, relevant products/roles, important dates and practical effects before asking the reader to understand legislative relationships.

That correction is retained.

However, the current page does **not** yet earn adoption as the public regime-page pattern.

The strongest official-source baseline exposes a material weakness in the page's current-state layer:

> the page locally presents a small post-2017 change set under wording that can be read as current/comprehensive, while the official 2026 baseline contains additional enacted/current developments that are already represented elsewhere in the Needle fixture.

This is a bounded revision problem, not a reason to restore the old relationship-first entry model.

Successor: **#481 — Repair current-state/freshness contract for medical-devices landing page**.

## 2. Evidence inspected

Repository:
- `mvp/medical-devices-summary/index.html`;
- `mvp/medical-devices-summary/app.test.js`;
- `mvp/regime-density-v0.2/index.html`;
- #477 frozen tasks;
- #477 claim/source map;
- #473 v0.2 comparison readout;
- current `BACKLOG.md`.

Current official baseline checked on 28 September 2026:
- Commission medical-devices overview:
  https://health.ec.europa.eu/medical-devices-new-regulations/overview_en
- Commission economic operators:
  https://health.ec.europa.eu/medical-devices-topics-interest/economic-operators_en
- Commission EUDAMED overview:
  https://health.ec.europa.eu/medical-devices-eudamed/overview_en
- EUR-Lex MDR summary:
  https://eur-lex.europa.eu/summary/ENG/4301046
- EUR-Lex IVDR summary:
  https://eur-lex.europa.eu/summary/EN/4301047
- current MDR consolidated access:
  https://eur-lex.europa.eu/eli/reg/2017/745
- current IVDR consolidated access:
  https://eur-lex.europa.eu/eli/reg/2017/746
- COM(2025) 1023 procedure:
  https://eur-lex.europa.eu/procedure/EN/2025_404
- European Parliament procedure file:
  https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2025%2F0404%28COD%29

The accepted Vercel preview could not be independently rendered from the agent environment, so this review covers source, information architecture, accepted deployment/test evidence and current official-source comparison. It does not claim observed novice visual usability.

## 3. Frozen six-task review

| Task | Summary-first | v0.2 | Strong official workflow | Internal result |
| --- | --- | --- | --- | --- |
| T1 Purpose | Directly explained in first substantive block | Weak: starts with regime shape/lineage | Strong in EUR-Lex summaries and Commission overview | **PASS** |
| T2 MDR vs IVDR | Direct two-branch explanation with scope cues | Present as two core cards | Strong across official overview/summaries | **PASS** |
| T3 Importer/distributor relevance | Explicit roles and practical effects before relationships | Not a public-entry answer | Strong on Commission economic-operator material, but separate page | **PASS; integration advantage plausible** |
| T4 Laboratory/research boundary | Visible IVDR qualification near scope | Not visible on default entry | Authoritative in IVDR Article 1(3)(a), less prominent in ordinary overview flow | **PASS; useful boundary integration** |
| T5 Dates/transition | 26 May 2021 / 26 May 2022 plus visible transition warning | Transition layer available deeper | Official workflow is stronger/current and includes later transition/EUDAMED state | **PASS TASK / REVISE CURRENTNESS** |
| T6 Verification/proposal status | Official links visible; proposal labelled non-enacted | Proposal/current distinction visible | Official procedure pages are authoritative and current | **PASS** |

All six frozen #477 orientation tasks are structurally answerable without opening the relationship browser first.

That is evidence that the foundational information contract works at the implementation level.

It is **not** evidence of external comprehension, preference or task-time improvement.

## 4. What the experiment proved internally

### A. The abstraction-order correction is real

The page now follows:

> regulated-world explanation -> relevance -> dates/effects -> relationships

rather than:

> relationships -> user infers regulated-world meaning

This directly repairs the independent foundational review's main criticism.

### B. The relationship browser survives at the right depth

`/regime-v2/` remains useful for:
- implementing/delegated layers;
- EUDAMED/system relations;
- transition acts;
- change-review mechanics;
- source/coverage diagnostics.

The summary-first page does not need to reproduce that machinery.

Its best role is a public orientation layer that hands off to deeper relationship exploration.

### C. The official baseline is stronger than a raw-law strawman

EUR-Lex summaries already explain purpose, scope, application and important effects. The Commission separately provides strong actor, transition and EUDAMED material.

Needle therefore earns no value credit merely for writing a plain-language summary.

The surviving product hypothesis is narrower:

> **integrate the ordinary orientation job across two core acts, actor relevance, material scope boundaries, current/transition state and authoritative verification, then bridge into deeper legal relationships without requiring the reader to assemble the model first.**

That is a workflow/integration hypothesis, not a novelty claim.

## 5. Red-team finding — current-state false completeness

The current landing page uses:

> **Current rules and dates**

and later:

> **What changed after the core Regulations?**

but the change section contains only:
- Regulation (EU) 2024/1860;
- COM(2025) 1023.

That pair is legally useful, but it is not a sufficient representation of the official current-state surface as of 28 September 2026.

The current Commission overview also surfaces, among other things:
- Decision (EU) 2025/2371 declaring the first four EUDAMED modules functional;
- Implementing Regulation (EU) 2026/977 on conformity-assessment/notified-body requirements;
- Delegated Regulation (EU) 2026/1359;
- Delegated Regulation (EU) 2026/1451;
- other 2025 implementing/delegated changes.

The Commission EUDAMED overview further states that the first four modules became mandatory from **28 May 2026**.

Several of these facts are already present in `/regime-v2/`, so the omission is not a fixture limitation.

The global statement that the page is a selected/bounded overview is good, but it does not fully cure a **local heading that implies a current-change answer**.

This is the main reason not to adopt the page unchanged.

## 6. Secondary findings

### Source traceability — strong, but can be more direct

Claim-adjacent official links are a major improvement.

For some role statements, however, a link labelled for a specific Article still lands at the act-level EUR-Lex entry rather than a provision-specific location. That is acceptable for this experiment but leaves verification friction.

Do not solve this with a new citation system unless a simple stable official deep link is available.

### Dates — historical landmarks are not the whole current-state story

26 May 2021 and 26 May 2022 are important member-act application dates.

For a page presented as current orientation, the 28 May 2026 EUDAMED mandatory-use milestone is also practically salient.

The repair should distinguish:
- landmark application dates;
- conditional legacy transition;
- current operational milestones.

It should not turn the landing page into a timeline database.

### Proposal status — correctly represented

COM(2025) 1023 remains an ongoing ordinary legislative procedure at this review checkpoint.

The page is right to keep it separate from enacted law.

## 7. Comparator verdicts

### Against `/regime-v2/`

Summary-first is better for first-time orientation.

v0.2 is better for:
- represented legal layers;
- current act-family context;
- deeper relationship exploration;
- change-review work.

Therefore the correct architecture remains **summary first + relationship browser deeper**, not one replacing the other.

### Against the strong official workflow

Official sources remain the authority and are individually strong.

Needle's possible residual is:
- one coherent cross-source orientation path;
- explicit boundaries between regime overview and member-act state;
- actor relevance beside product scope;
- visible uncertainty/transition qualification;
- direct handoff into a relationship model.

What is **not** established:
- that users prefer this integrated path;
- that it is faster;
- that it reduces error;
- that it is worth maintaining as a product;
- that it should expand to a second regime.

## 8. Disposition

# **REVISE_SUMMARY_FIRST**

Retain:
- summary-first entry;
- role/product relevance before relationships;
- visible legal qualifications;
- claim-adjacent official evidence;
- `/regime-v2/` as the deeper exploration layer;
- proposal/current-law separation.

Repair only:
- local current-state/freshness wording;
- important 2026 operational context where the page claims currentness;
- minimum recent-enacted context needed to avoid false completeness.

Do **not** yet build:
- individual MDR/IVDR pages;
- a second regime;
- applicability tooling;
- a broad current-act inventory;
- automated monitoring.

## 9. Falsifier for the repair

The public regime-page direction should be parked or narrowed to a source-linked note if either becomes true:

1. maintaining an honest current-state summary requires reproducing enough of the Commission/EUR-Lex surface that the landing page loses its simplicity; or
2. after repair, the integrated path still has no clear task-level advantage over the ordinary official workflow beyond visual preference.

## 10. Next owner

> **#481 — REVISE: repair current-state/freshness contract for the medical-devices landing page**

This is the smallest useful successor.

No external-user-value claim is made from #479.

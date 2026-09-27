# #443 — Navigator P5 semantic integrity, browser and accessibility review

Date: 2026-09-27  
Disposition: **PASS_TO_P6**

## 1. Question

> Does the content-complete Low Voltage Directive page preserve the intended legal distinctions and remain understandable/usable across ordinary browser, keyboard and narrow-screen use without inducing consequential false inferences?

P5 was adversarial review, not feature development.

The result is a pass to maintenance rehearsal, with explicit browser/accessibility limitations below.

## 2. Evidence actually used

### Legal / semantic

Rechecked the page against the official sources already owning the P1/P2 content contract, especially:

- Directive 2014/35/EU / current consolidated text;
- Directive 2006/95/EC lineage evidence;
- Directive (EU) 2024/2749 amendment;
- Regulation (EU) No 1025/2012;
- existing canonical Candidate-B dynamic-set fixtures.

P5 did not expand the legal corpus.

### Browser / human observation

The sponsor inspected the deployed page in an ordinary browser and supplied screenshots.

Those screenshots showed:
- the content rendered and was readable;
- the applicability content was present;
- the lineage/context/dependency content was present;
- three presentation defects were immediately visible to a real reader.

The sponsor's observations are browser usability evidence, not an external-user study.

### Automated/runtime evidence

- PR #445 exact repaired head passed the repository/Vercel gate before merge.
- PR #446 exact accessibility-hardening head passed the Vercel gate before merge.
- Candidate-B semantic regression tests remain green on those gated heads.
- Vercel successfully built/deployed the repaired static surface.

The assistant runtime could not independently fetch the current Vercel deployment because the connected Vercel project listing does not expose the GitHub-linked `morrow-needle` project even though GitHub's Vercel integration does.

Therefore P5 does **not** claim a fresh assistant-driven keyboard/browser automation run on the final repaired page.

## 3. Defects found and repaired

### P5-01 — detail discoverability

**Severity:** medium usability defect.

Observed:
- “subject to Annex II exclusions” and economic-operator summaries did not make it obvious that the detailed material was directly below;
- the sponsor explicitly had to infer where to find the detail.

Repair in #445:
- added **See exclusions below ↓**;
- added **See role details below ↓**;
- both are real buttons;
- activation opens the corresponding native `<details>`, scrolls it into view and focuses its `<summary>`.

Why this matters:
- the overview can remain concise without making detail look absent.

### P5-02 — relationship shape hidden by equal-weight cards

**Severity:** medium information-architecture defect.

Observed:
- lineage was legally correct but visually resembled three unrelated prose cards;
- framework/context and operative-dependency cards also gave the relation itself too little perceptual priority.

Repair in #445:

**Lineage**
- now renders as:
  - earlier regime;
  - **Codified as →**;
  - codification;
  - **Recast as →**;
  - current focal act.

**Legal context**
- now uses a relationship ledger:
  - relation type;
  - instrument + explanation;
  - official source.

**Operative dependencies**
- now render:
  - focal provision;
  - human-readable typed relation;
  - external provision;
  - why-it-matters explanation;
  - official source.

The arrows are decorative; the relation words remain ordinary text.

### P5-03 — disclosure focus / long legal labels

**Severity:** low accessibility/resilience defect.

Static inspection after #445 found:
- visible focus styling did not explicitly name `summary`;
- the new detail cue target could be hardened;
- long provision/instrument labels should fail safely rather than force horizontal overflow.

Repair in #446:
- added `summary:focus-visible`;
- increased detail-cue target height/padding;
- added overflow wrapping to lineage, relationship, dependency and applicability text;
- retained native disclosure semantics.

## 4. Semantic adversary results

### Formal addressee trap — PASS

The page distinguishes:
- Article 29 formal addressee: Member States;
- material/product scope;
- Union-market activity;
- economic-operator roles;
- territory/market context;
- represented time.

It does not equate “Member States” with the only people/entities practically concerned.

### Scope trap — PASS

The page states:
- the voltage ranges;
- that Annex II exclusions apply;
- the major represented exclusions;
- that exclusion from LVD scope does not itself identify the alternative EU/national regime.

A voltage match is not presented as a complete product-compliance determination.

### Actor-role trap — PASS

Manufacturer, authorised representative, importer and distributor remain separate roles.

The page explicitly says role orientation is:
- not a determination of the reader's role;
- not a complete list of obligations.

### Temporal trap — PASS

The page keeps separate:
- adoption;
- publication;
- entry into force;
- transposition deadline;
- application;
- predecessor repeal;
- later amendment/application.

It also keeps separate:
- legal view date;
- evidence verified date;
- source/consolidation date.

### Lineage/context trap — PASS AFTER REPAIR

The page does not visually or textually collapse:
- ancestry;
- legal basis;
- product-law framework;
- standardisation framework;
- amendment.

“No successor represented” remains explicitly different from “no successor exists”.

### Operative-dependency trap — PASS AFTER REPAIR

The page distinguishes:
- imported definition;
- external procedure;
- broader legal context.

It also explicitly says that importing one definition or using one procedure does not import the whole external Regulation into every LVD question.

### Presumption trap — PASS

Article 12 is described as a presumption limited to the safety objectives actually covered.

The page says this is not general proof of full product compliance.

Articles 13 and 14 remain distinguishable additional represented routes rather than being collapsed into Article 12.

### Currentness/completeness trap — PASS

The page states:
- evidence is frozen/not live monitoring;
- consolidation is documentary;
- authentic OJ acts remain the legal sources;
- the page does not claim every amendment, transposition measure, judgment, harmonised standard or other relevant document.

## 5. Accessibility / structural review

### Supported by the current implementation

- skip link exists;
- keyboard-native inputs/buttons/links/details are used;
- visible focus is explicitly defined for links, buttons, inputs and summaries;
- disclosure summaries have enlarged minimum height;
- status is written in text, not conveyed by colour alone;
- lineage relation names are visible text;
- operative dependency relation names are visible text;
- arrows are `aria-hidden` where they are only visual reinforcement;
- semantic `dl`, `ol`, headings and native `details/summary` carry structure;
- relationship layouts collapse to one-dimensional reading order at narrower widths;
- long legal labels are allowed to wrap.

### Not established

P5 does **not** establish:
- full WCAG 2.2 AA conformance;
- screen-reader interoperability across products;
- fresh manual keyboard traversal of the final repaired deployment;
- final behavior at every 320 CSS-pixel browser/zoom combination.

Those require actual browser/assistive-technology execution and should not be inferred from static markup/tests.

## 6. Readability / hierarchy result

The page is now long, but the length is not itself the main defect.

The more important P5 finding was that relationships must be perceived as relationships rather than as equal-weight prose containers.

After the repair:
- the primary act answer still precedes provenance detail;
- applicability remains near the top;
- detailed exclusions/roles are discoverable but collapsible;
- lineage is visually directional;
- framework/context is tabular/relational;
- operative dependency is visibly different from ordinary context;
- the standards lookup remains the first interactive surface.

The shell still says **Harmonised Standard Status** at the top even though the act-context page is becoming a broader Navigator experiment.

That is a real product-identity question, but not a P5 correctness blocker. Do not rename/reframe the product during integrity review merely to make it look more complete. P7 should reconcile the public identity if the prototype survives maintenance.

## 7. Remaining risks

### R1 — maintenance duplication

The act page currently contains substantial legal explanation directly in HTML.

Several facts appear in:
- at-a-glance prose;
- key facts;
- applicability;
- timeline;
- context/dependency sections;
- evidence details.

This may allow a later legal change to leave stale text behind.

This is now the largest internal risk and is the direct owner of P6.

### R2 — browser verification gap

Sponsor browser use plus successful Vercel deployment demonstrates a real rendered surface.

However the assistant cannot currently run an independent fresh browser fetch against the final Vercel project through the connected Vercel tool.

Treat this as an evidence limitation, not as evidence of a defect.

### R3 — no external reader evidence

Sponsor feedback is strong design signal.

It does not establish:
- general usability;
- professional acceptance;
- comparative superiority;
- willingness to pay;
- market demand.

The later readiness gate still owns that transition.

## 8. Disposition

> **PASS_TO_P6**

Reason:
- no critical semantic misrepresentation survived the adversarial pass;
- the sponsor's live-browser inspection exposed real presentation defects rather than merely confirming the design;
- those defects were repaired without expanding legal scope;
- static accessibility structure is materially stronger;
- the remaining dominant internal uncertainty is maintenance/correction blast radius.

Successor:

> **#447 — Navigator P6 maintenance and correction blast radius**

No second act and no external recruitment are authorised by this pass.

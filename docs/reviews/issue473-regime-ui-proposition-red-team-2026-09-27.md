# #473 — Red-team of regime UI proposition v0.2

Date: 2026-09-27  
Verdict: **PROCEED WITH REPAIRS**

The task-layered proposition is materially better aligned with the sponsor-observed failure, but it can create new legal-information failure modes if compression is treated as “less text” rather than “better hierarchy”.

## Attack 1 — hiding a caveat changes the first impression

Risk:
> “MDR / IVDR replaced the predecessor directives” can sound cleaner than the actual transitional reality.

A user may infer:
> old directives have no residual legal relevance after the application date.

Repair:
- keep a compact always-visible transition qualifier adjacent to the 3 -> 2 spine:
  > **Transition rules preserve some predecessor effects for bounded cases; open Explore/Changes for detail.**
- do not require an expert view to discover this qualifier.

Result:
> **SURVIVES WITH REPAIR**

## Attack 2 — task switching can simply move the overload into clicks

Risk:
- Overview looks clean;
- Explore becomes a giant list;
- Change Review becomes another giant dashboard.

Repair:
- one family at a time in Explore;
- cap the representative first expansion to six child rows;
- one change control at a time;
- detailed legal rationale behind one “Why?” disclosure per row;
- no nested disclosure.

Result:
> **SURVIVES**

## Attack 3 — modes make users remember hidden information

GOV.UK warns that tabs are poor when users must compare information across sections.

Risk:
> a user reviewing a change may need the regime shape and cannot remember what was on Overview.

Repair:
- every non-Overview mode keeps a **small persistent regime context strip**:
  - MDR;
  - IVDR;
  - active branch;
  - evidence date.
- do not require switching back just to remember the focal regime.
- Change Review queue contains the affected object names directly.

Result:
> **SURVIVES WITH REPAIR**

## Attack 4 — research diagnostics disappear when they matter

Risk:
> moving all diagnostics to Expert hides a known omission that materially qualifies a public node.

Repair:
- distinguish **local material notice** from **research diagnostics**.
- if an official amendment materially qualifies a displayed public child, show a local “additional amendment” notice on that child.
- keep system-level coverage/research inventory in Expert.

Thus:
- 2023/1194 remains locally discoverable from 2022/2346;
- the research panel explaining why this is a COVERAGE_GAP moves to Expert.

Result:
> **SURVIVES WITH REPAIR**

## Attack 5 — family count becomes a misleading KPI

Risk:
large “17” / “7” values look like completeness or importance scores.

Repair:
- demote counts from dashboard-stat cards;
- use wording:
  - “Implementing measures · 17 listed in Commission overview”
  - “Delegated acts · 7 listed”
- keep evidence date/definition in detail.
- never use counts as visual progress indicators.

Result:
> **SURVIVES WITH REPAIR**

## Attack 6 — public labels dilute exact legal distinctions

Risk:
“Review directly” may lose the stricter internal meaning of `DIRECT_REVIEW`.

Repair:
- human label is primary;
- internal code is secondary metadata in “Why?” detail;
- definition remains inspectable;
- the human label must never imply actual legal effect changed.

Result:
> **SURVIVES**

## Attack 7 — a clean 3 -> 2 diagram becomes graph theatre

Risk:
the split graphic can imply:
- a simple historical fork;
- exclusivity;
- complete ancestry;
- no later cross-branch interaction.

Repair:
- use typed replacement labels;
- show “bounded lineage” explicitly;
- preserve joint-change marker below the two core branches;
- no free-form edge cloud;
- no visual that suggests all downstream acts belong exclusively to one branch.

Result:
> **SURVIVES**

## Attack 8 — “Explore” taxonomy is project-authored rather than legal truth

Risk:
Implementing / delegated / EUDAMED / guidance are useful navigation families but not one uniform legal ontology.

Repair:
- label the area:
  > **Browse represented layers**
- describe families as navigation groupings;
- individual child rows retain their actual typed legal relation/status;
- do not persist the family grouping as a canonical legal relation.

Result:
> **SURVIVES WITH REPAIR**

## Attack 9 — proposal can disappear into secondary navigation

Risk:
a current proposal materially relevant to the regime could be missed if Proposal is only in Expert.

Repair:
- keep one concise Overview line:
  > **Proposal — not enacted:** COM(2025) 1023
- detail stays in Explore.

Result:
> **SURVIVES**

## Attack 10 — guidance/non-binding distinction becomes icon-only

Risk:
moving to compact rows tempts shorthand icon/color semantics.

Repair:
- row text must literally say **Non-binding guidance**;
- proposal row must literally say **Proposal — not enacted**;
- current legislation must be labelled accordingly;
- colour may reinforce but never own status.

Result:
> **SURVIVES**

## Attack 11 — evidence is pushed too far away

Risk:
a clean public page may degrade into unsourced explanation.

Repair:
- every selected child/detail row retains an **Official source** action;
- current core acts have source actions on Overview;
- evidence date remains in header;
- detailed provenance is one interaction away, not a separate research workflow.

Result:
> **SURVIVES**

## Attack 12 — “Expert / research” becomes a junk drawer

Risk:
everything removed from Overview gets dumped into Expert, recreating the same page lower down.

Repair:
Expert contains only:
- projection coverage/evidence diagnostics;
- maintenance/review methodology;
- bounded structural-gap abstention;
- exact research boundary.

Legal detail about an individual act belongs with that act in Explore, not in Expert.

Result:
> **SURVIVES WITH REPAIR**

## Attack 13 — application/scope need gets lost

Sponsor has already identified a high-value user need:
> “Does this apply to the person/entity/situation I care about?”

The macro regime view cannot answer a French-farmer-style applicability question merely by showing relationships.

Repair:
- current branch summaries should expose one compact **Scope** phrase;
- do not attempt personalised applicability in this macro prototype;
- child/act view can later own detailed “Who / what does this apply to?” treatment.
- the regime UI must make the scope destination obvious rather than pretending the macro map answers it.

Result:
> **SURVIVES, BUT IMPORTANT PRODUCT DEPENDENCY**

## Attack 14 — accessibility of mode switching

Risk:
custom view switching can become a pseudo-tab implementation with poor focus/back behavior.

Repair:
- use native buttons with explicit `aria-pressed`;
- update URL hash;
- support `hashchange`;
- leave headings in each panel;
- hidden inactive panels use the standard `hidden` attribute;
- keyboard operation requires no custom arrow-key model;
- narrow screens stack the task switcher.

Result:
> **SURVIVES**

## Attack 15 — quantitative compression becomes Goodhart's law

Risk:
optimising for <=450 words could remove necessary legal meaning.

Repair:
the word target is subordinate to four semantic invariants:
1. current/proposal/non-binding distinction survives;
2. predecessor transition caveat survives;
3. coverage boundary survives;
4. official evidence remains reachable from the represented claim.

If any invariant fails, the compressed design fails even if word count is excellent.

Result:
> **SURVIVES**

# Revised proposition

Proceed to a separate v0.2 comparison route with these mandatory repairs:

1. Overview:
   - 3 -> 2 bounded lineage;
   - one-line transition caveat;
   - MDR/IVDR scope phrases;
   - compact downstream layer rows;
   - current enacted change + proposal line;
   - evidence/coverage boundary.

2. Explore:
   - one family at a time;
   - maximum six initial child rows;
   - source + Why per row;
   - local amendment warning where material.

3. Change Review:
   - one upstream event;
   - compact queue;
   - stop reasons visible;
   - detailed basis on demand;
   - persistent mini regime context.

4. Expert / Research:
   - diagnostics only;
   - no ordinary legal detail dumping.

5. No semantic deletion from v0.1.

# Verdict

> **PROCEED WITH REPAIRS — BUILD SEPARATE COMPARISON ROUTE**

The red team does not support merely restyling the current long page.

The experiment must change the information architecture.

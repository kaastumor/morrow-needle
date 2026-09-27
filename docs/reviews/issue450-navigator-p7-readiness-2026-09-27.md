# #450 — Navigator P7 readiness decision

Date: 2026-09-27  
Disposition: **READY_FOR_USER_TEST**

## Decision

The one-act EU Legislation Navigator prototype has earned a bounded formative human comparison.

This means:

> the artifact is credible enough that further internal feature work is less informative than observing real readers.

It does **not** mean:
- user value is proven;
- the Navigator is better than official sources;
- the software presentation is better than a strong source-linked note;
- a second act is authorised;
- multi-act maintenance is solved;
- commercial demand exists.

## 1. Technical feasibility

Supported.

The static prototype:
- builds reproducibly;
- deploys through the existing Vercel path;
- preserves the five frozen Candidate-B status cases;
- supports the LVD act-context journey;
- has deterministic semantic regressions;
- has survived multiple exact-head deployment gates.

No new backend/model dependency is required for the first human test.

## 2. Evidence integrity

Supported at prototype scope.

The LVD page now distinguishes:
- official act vs documentary consolidation;
- legal as-of vs evidence-verified vs source-version dates;
- formal addressee vs practical scope dimensions;
- lineage vs framework/context;
- ordinary context vs operative legal dependency;
- Article 12 presumption vs full product compliance;
- represented evidence vs complete legal context.

Official sources remain directly accessible.

P5 found no unresolved critical semantic misrepresentation.

## 3. Usability/readability readiness

Supported for formative testing, not proven generally.

Positive evidence:
- sponsor used the deployed page and reported substantial context/orientation value;
- sponsor screenshots exposed real discoverability and relationship-presentation defects;
- those defects were repaired rather than rationalised away;
- the page now makes lineage and operative relationships visually inspectable while retaining readable text.

Limit:
- sponsor evidence is one informed reader, not an external sample;
- no general usability claim is earned.

## 4. Maintenance sustainability

Supported for **one formative prototype**.

P6 reproduced partial-update failure modes and added maintenance sentries for:
- amendment application date;
- consolidation/source version;
- legal-view date;
- evidence-verification date;
- versioned LVD source links;
- operative-dependency routes.

P6 explicitly did not establish scalable multi-act content architecture.

## 5. Strong contrary case — competent source-linked note

Still credible.

#438 showed that a carefully written note can contain almost all of the same legal meaning.

Therefore the software does not get value credit merely for containing the facts.

This is the correct comparator for the human test.

The question is whether structured integration makes the job:
- easier to navigate;
- easier to verify;
- less error-prone;
- or more comprehensible.

If it does not, do not add features to rescue the software.

## 6. Strong contrary case — official sources may already be enough

Also credible.

EUR-Lex, Commission pages and procedure material already contain much of the underlying information.

The surviving hypothesis is not information exclusivity.

It is:

> **one task-oriented page may reduce the reconstruction effort needed to understand how the official facts fit together.**

A professional reader who still opens EUR-Lex after orientation is not a failure. Source replacement is not the job.

## 7. Sponsor enthusiasm

Useful but insufficient.

The sponsor's strong positive reaction is evidence that:
- integrated lifecycle/context can create immediate orientation value for at least one real reader;
- the project has a credible interaction hypothesis worth testing.

It is not evidence of:
- population preference;
- professional acceptance;
- willingness to pay;
- market demand.

P8 exists precisely because this uncertainty cannot be resolved internally.

## 8. LVD representativeness

Unresolved.

LVD is a favorable first act because it has:
- understandable scope;
- clear lineage;
- product-law framework context;
- useful standards dependencies;
- real current/future state examples.

That may make it unusually suitable for the Navigator presentation.

Do not generalise from a positive LVD test to all EU legislation.

A second act is a later experimental choice, not part of P8.

## 9. Standards-status tool vs Navigator job

Unresolved product identity, but not a blocker to the test.

The current shell still begins with **Harmonised Standard Status** while the new hypothesis is the broader known-act Navigator.

For P8:
- enter directly at the LVD context section;
- tell participants they are evaluating a known-act orientation page;
- do not score discovery of the Navigator section from the legacy shell.

This isolates the hypothesis actually under test.

Shell/branding/convergence is a later decision.

## 10. Human-test contract

Owner:

> **#453 — PREP: Navigator formative human-test packet**

### Primary comparison

Same frozen LVD evidence:

1. **Navigator**
2. **competent concise source-linked note**

Do not weaken the note.

### Participants

Initial target:
- 6 participants;
- extend to 8 only if the first six expose materially different reader patterns that justify two more.

Mix:
- occasional EU-law readers with a concrete study/work reason;
- legal/regulatory/compliance professionals or near-professionals.

LVD expertise is not required.

### Format

Target:
> **20–25 minutes**

Use:
- brief context/consent;
- two counterbalanced task blocks;
- disjoint but comparable task sets;
- short debrief.

This avoids asking unknown professionals for an unnecessarily long cold session.

### Observe separately

For each task:
- material correctness;
- consequential false inference;
- time;
- source/evidence retrieval;
- navigation effort;
- confidence.

After both representations:
- preferred starting representation and reason;
- what felt missing/misleading;
- when/why they would open the official source.

Do not collapse these into an opaque score.

## 11. Critical stop rule

Stop and revise immediately if the Navigator itself induces a consequential false inference, especially:

- voltage match = automatic applicability;
- Member States = only relevant actors;
- “in force” = one simple application date;
- framework act = ancestor;
- imported provision = entire external act imported;
- Article 12 presumption = full product compliance;
- frozen evidence = live monitoring.

## 12. Comparative stop/narrow rule

After the initial six:

- if the Navigator does not materially reduce navigation/interpretive effort versus the strong note, do not add features to rescue it;
- if value appears only for occasional readers, narrow the audience claim;
- if professionals use it only as orientation before EUR-Lex, define that as the job rather than source replacement;
- if results are too LVD-specific to interpret, record the limitation before considering a second act.

## 13. Recruitment boundary

P7 authorises **test readiness**, not outreach.

No participant may be contacted from this decision.

Preferred later recruitment modes:
- warm introduction;
- short self-serve participation where appropriate;
- compensated professional research if cold expert time is needed.

Any outreach or compensation action still requires sponsor authorisation.

## 14. Scaling and commercial state

### Second act
**Not yet authorised by this readiness decision.**

### Multi-act architecture
**Not established.**

### Market demand / willingness to pay
**Untested.**

### Physical repo fork
**Not earned.**

### License change
**Not earned.**

## Final disposition

> **READY_FOR_USER_TEST**

The correct next internal action is to prepare the frozen comparison materials under #453 and then stop at the outreach/participant dependency.

Further product feature work before that evidence would risk returning to self-generated validation.

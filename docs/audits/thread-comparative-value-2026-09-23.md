# Thread comparative value audit — 2026-09-23

Status: **COMPLETE — Issue #59 verdict: STOP PUBLIC-PRODUCT EXPANSION**

## Question

Does the existing evidence-linked Thread make a complex EU rule history
materially easier to reconstruct correctly than the strongest practical
combination of:

1. EUR-Lex / official EU metadata and consolidated histories;
2. a mature provision/version-history tool where available;
3. direct authentic amending/corrigendum sources;
4. ordinary search plus a capable LLM?

The test uses the frozen English Thread for Commission Regulation (EC)
No 794/2004 Article 3. No new Thread architecture was built for the comparison.

## Baseline reconstruction without Needle

A careful reconstruction from public official material can recover the following.

### 1. Original 2004 state and legal timing

EUR-Lex exposes the original 20 May 2004 consolidated state. Article 3 states:

- paper notification through 31 December 2005;
- electronic notification from 1 January 2006 unless otherwise agreed;
- correspondence connected to a notification submitted after 1 January 2006
  must also be electronic.

Article 13 says the Regulation enters into force on the twentieth day after OJ
publication and that Chapter II applies only to notifications transmitted more
than five months after entry into force.

EUR-Lex metadata records date of effect 20 May 2004 and points to Article 13.

Sources checked 2026-09-23:

- https://eur-lex.europa.eu/eli/reg/2004/794/2004-05-20/eng
- https://eur-lex.europa.eu/legal-content/en/ALL/?uri=CELEX:32004R0794

A capable baseline can therefore derive the same main temporal distinctions as
Thread:

- act entry into force = 20 May 2004;
- Chapter II five-month threshold lands on 20 October 2004 but the source says
  **more than** five months, so the boundary itself is exclusive;
- paper-notification end and electronic-notification start are separate;
- the correspondence rule is conditional on the connected notification date.

**Comparative result: PARITY.**

Thread makes these dimensions executable and harder to collapse accidentally,
but the official source states the relevant facts directly.

### 2. 2008 whole-Article replacement and SANI / PKI timing

EUR-Lex's relationship metadata records Regulation (EC) No 271/2008 as a
**replacement of Article 3** from 14 April 2008.

The 14 April 2008 consolidated text states:

- notifications use SANI **as from 1 July 2008**;
- all correspondence uses PKI;
- exceptional agreed alternative channels remain possible.

EUR-Lex metadata for Regulation 271/2008 records date of effect 14 April 2008,
the twentieth day after publication.

Sources checked 2026-09-23:

- https://eur-lex.europa.eu/eli/reg/2008/271/oj/eng
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02004R0794-20080414
- https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32004R0794

A capable baseline can distinguish the act/replacement being legally in force
from 14 April and the rule-specific SANI date of 1 July. It should also avoid
copying the SANI qualifier onto the unqualified PKI sentence.

**Comparative result: PARITY.**

Needle's temporal assertions make the separation machine-safe; the legal
history itself is not hidden from the baseline.

### 3. 2025 paragraph-3 replacement

EUR-Lex relationship metadata identifies Commission Implementing Regulation
(EU) 2025/905 as replacing **Article 3(3)** from 3 July 2025, not replacing the
whole Article.

The authentic amending act prints the replacement:

- notifications through the electronic application designated by the
  Commission;
- correspondence through the secured electronic system designated by the
  Commission.

Article 2 puts the amending Regulation into force on the twentieth day after its
13 June 2025 publication. Its special 13 August 2025 delayed application clause
is expressly limited to Annex I Part I point 6.8.

Sources checked 2026-09-23:

- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500905
- https://eur-lex.europa.eu/legal-content/en/ALL/?uri=CELEX:32004R0794
- https://eur-lex.europa.eu/eli/reg/2004/794

A capable baseline can therefore recover the 3 July Article 3(3) transition and
avoid applying the Annex-specific 13 August date to Article 3.

**Comparative result: PARITY.**

### 4. Paragraph 4 stayed textually unchanged but its dependency changed

Comparing the pre-2025 Article 3 with the current version shows that paragraph 4
retains the same exceptional-channel and invalid-submission rules, while its
references to “paragraph 3” now point to the newly replaced channel rules.

Needle has an executable negative textual check:

- before/after canonical paragraph-4 subtree hash identical;
- no local Article 3(4) mutation;
- a separate EVIDENCED + DERIVED cross-reference ripple.

A capable LLM given both versions can derive the same one-hop effect. A normal
version-history view, however, will not naturally surface Article 3(4) as a
2025 change because its text did not change.

**Comparative result: PLAUSIBLE ADVANTAGE — systematic discovery and audit
precision.**

This is useful, but it is the same class of advantage already observed in #49's
REACH dependency-ripple case. It is not exclusive reasoning.

### 5. 2026 corrigendum reviewed as Article-3 non-impact

EUR-Lex exposes the 17 July 2026 corrigendum to Regulation 2025/905. The
corrigendum explicitly targets the amendment of Regulation 794/2004
**Article 4(1), second sentence**.

Source checked 2026-09-23:

- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R0905R(01)

A baseline researcher who checks later corrections can therefore establish that
this corrigendum does not create a new Article 3 mutation.

Thread's stronger property is **positive audit closure**: it records that the
related source was reviewed and intentionally excluded, rather than merely
omitting it from the timeline.

**Comparative result: AUDIT ADVANTAGE, but not unique legal understanding.**

The final legal answer is recoverable from the official corrigendum. Thread
mainly reduces the risk that a future researcher cannot tell whether the source
was missed or deliberately ruled non-impact.

### 6. Old/new technical-system identity remains unresolved

The 2008 text names SANI and PKI. The 2025 replacement instead refers to an
electronic application and secured electronic system designated by the
Commission.

The official material used in this comparison does not establish that the
later systems are technically identical to SANI/PKI.

A careful baseline should therefore describe proposition-level continuity
(mandatory electronic notification / secured electronic correspondence) without
claiming technical-system identity.

**Comparative result: PARITY for a careful baseline; machine-safety advantage
for Thread.**

Thread makes the non-inference explicit and persistent. A competent
source-grounded LLM can reach the same bounded conclusion.

## emendrix adversary

Targeted public search on 2026-09-23 did not surface an emendrix page for
CELEX 32004R0794 / Article 3. Direct guessed act URLs were not accessible
through the available web tool.

That is **not evidence that emendrix lacks coverage**, so the audit does not use
absence from emendrix as a Needle advantage.

Where emendrix is known to operate, its methodology already provides structural
version histories, amendment corroboration and bounded date handling. Thread
therefore receives no credit merely for version history or source-linked
explanation.

## What Thread genuinely adds

Thread is better than a raw EUR-Lex browsing session as an **audit object**:

- one ordered composition instead of manual source traversal;
- claim-by-claim active provenance support;
- explicit negative checks, not silent absence;
- direct versus derived effects remain typed;
- temporal dimensions cannot be silently collapsed;
- unresolved rule/technical identity is retained as an explicit gap;
- reviewed non-impact is distinguishable from “not noticed”.

Those are real benefits.

## What Thread does not demonstrate

The Article 3 case does **not** establish a durable public-product advantage:

- almost every positive legal fact is directly recoverable from official
  sources;
- the difficult derived paragraph-4 effect is straightforward once the two
  relevant states are supplied;
- corrigendum non-impact is directly verifiable from the official correction;
- technical-identity abstention is what a careful source-grounded baseline
  should already do;
- this is the project's only completed Thread-quality case, so recurring value
  has not been demonstrated.

The project explicitly required repeated material advantage rather than one
well-engineered showcase. Creating more Thread cases merely to make the metric
possible would be a new product investment after two successive gates failed to
justify public expansion.

## Verdict

**STOP PUBLIC-PRODUCT EXPANSION.**

This is not a finding that Needle has no value.

The evidence supports a stable narrower identity:

> **Morrow // Needle is an evidence-first legal-change research and audit engine
> for reconstructing, falsifying and inspecting EU legal-change claims.**

The operational monitor, provenance engine, temporal model, Thread, X-Ray,
Source Anomaly, Gold regressions and adversarial fixtures remain useful in that
role.

What stops:

- building a general public change/news feed;
- searching for a narrower marketing novelty claim;
- feature accumulation intended to rescue the product thesis;
- affected-entity/ranking/subscription/product-shell work;
- new infrastructure for hypothetical public scale.

What remains valid:

- research/audit use;
- regression and source-monitoring infrastructure;
- adversarial legal-history investigations;
- Thread as an audit projection where a concrete research question justifies
  the reconstruction;
- dependency, source-anomaly and temporal analyses as tools, not product
  pillars.

A future public-product direction may be reopened only by external evidence of a
specific recurring user problem that the strong simpler baseline cannot
reliably solve. It does not remain an automatic roadmap item.

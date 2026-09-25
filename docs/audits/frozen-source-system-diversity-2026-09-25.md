# Issue #315 — frozen source-system diversity audit

Date: 2026-09-25  
Disposition: **REVISE_METHOD**

## Question

Can the frozen 81-case corpus's source-system diversity and concentration be measured
honestly from existing accepted evidence owners, without changing canonical case metadata
or reopening substantive legal research?

## Short answer

Only partially.

The frozen corpus clearly contains materially broader source families than the 19/23-case
seed. However, the canonical corpus does **not** encode a per-case source-system inventory,
and its evidence-owner structure is not equivalent to one:

- 34 cases have at least one substantive Git-backed evidence path that can be inspected
  reproducibly;
- 45 cases are issue-only from the Reference Pack perspective;
- 2 additional cases point to Git-backed result files that contain only a heading and
  require falling back to their issue owner for substantive source information;
- several evidence owners cover more than one case;
- shared evaluation packets (#88/#97) contain sources for multiple cases in one file;
- an evidence owner can contain positive, control, boundary and adjacent sources that are
  not all decisive for every case it owns.

Therefore a mechanical "family appears anywhere in owner -> family belongs to every
case" rule produces false precision.

## Frozen evidence-owner topology

Using the Reference Pack's accepted evidence refs:

- **34 cases** can be classified from substantive frozen Git-backed owners;
- **45 cases** require current GitHub issue content;
- **2 cases** have placeholder Git-backed result files and therefore require issue fallback:
  - `dpp-semantic-profile-version` (#225);
  - `anoplophora-finding-demarcated-area` (#226).

This topology itself matters. A future source-diversity profile cannot claim full
content-addressed reproducibility while more than half the cases require mutable issue
owners.

## Source-family vocabulary tested

The audit used a deliberately small derived vocabulary:

1. `EU_LEGISLATION_OJ_EURLEX`
2. `EU_JUDICIAL`
3. `EU_COMMISSION`
4. `EU_AGENCY_OR_BODY`
5. `MEMBER_STATE_OFFICIAL`
6. `LINKED_ORDER_OR_TREATY_OFFICIAL`
7. `PRIVATE_RECOGNISED_PRIMARY`
8. `OFFICIAL_REGISTER_DATASET_TOOL`

Families are allowed to overlap. For example, one case may use EU legislation plus a
Member-State official publication, or an EU legal gateway plus a private legally
recognised standard/determination.

The vocabulary is a research aid, not a new canonical taxonomy.

## What a naïve owner-chain scan shows

A broad lexical scan over accepted evidence owners produces the following **owner-chain
presence**, before correcting shared-owner cross-contamination:

- EU legislation / OJ / EUR-Lex: 67 case chains;
- official register/dataset/tool material: 51;
- European Commission material: 23;
- EU judicial material: 19;
- treaty/linked-order material: 13;
- private legally recognised primary material: 12;
- Member-State official material: 12;
- EU agency/body material: 10.

These numbers are **not valid case-level source-dependence counts**.

Why not:

- the six #88 evaluation cases share one prompt/answer-key/result packet;
- that packet contains Commission, private-verifier, harmonised-standard and registry
  sources for different cases;
- propagating every packet family to all six cases falsely makes, for example, the
  licence-cutoff case a private-primary case;
- shared discovery issues create the same problem on a smaller scale.

The scan is still useful as a falsifier of "the corpus is EUR-Lex only": the accepted
evidence estate demonstrably contains several other source families. It cannot establish
their exact prevalence.

## Confirmed broadening since the seed audit

The old bias audit warned that subject-matter diversity was better than source-system
diversity and that research was strongly centred on EUR-Lex, Commission material and a
small number of Member-State sources.

That warning has been **partially reduced, not retired**.

### Member-State official evidence now exists materially

Accepted evidence includes, among other things:

- Dutch and Swedish primary implementing-law material in the NIS2 tracker-lag cases;
- national/official evidence in the HPAI spatial-finding chain;
- Member-State or national-law context in later judicial/application cases.

This is broader than the 19-case seed.

### Private / legally recognised primary evidence now exists

The frozen corpus includes cases whose legally material source chain includes private
actors/artifacts recognised by EU law, including:

- SZUTEST notified-body material;
- S&P private rating material;
- harmonised-standard identity/status;
- accredited/private verification roles in the revealed #88 material.

That is a genuinely different source-origin family from EU institutional legal text.

### EU agency/body evidence now exists

Later research includes EBA regulatory-technical-standard handoff material and
medicinal/food-safety authority chains such as CHMP/EMA or EFSA.

### Official registers, datasets and machine artifacts now exist

Accepted examples include:

- TNAC metric publication;
- trusted-list/reference status;
- authoritative semantic/profile material;
- Commission trackers;
- EEA/WISE-style structured representations;
- legally privileged calculation/validation artifacts.

### Linked-order / treaty evidence now exists

The corpus contains:

- EU-Mercosur / EU-Mexico / EU-Chile agreement lifecycle evidence;
- EEA incorporation-state work;
- Swiss Schengen adoption/incorporation material.

These are materially broader than a corpus composed only of ordinary EU legislative text.

## What remains unresolved

### Exact per-case source-family coverage

Not currently reproducible from canonical metadata.

Producing a trustworthy 81-row source inventory would require a **new semantic
classification artifact** that manually identifies which source families are actually
case-relevant inside each heterogeneous evidence owner.

That work is possible from existing evidence and would not require new legal research, but
it is not a mechanical readout of the frozen corpus. It would be a new derived annotation
layer with its own judgement, maintenance and #306 mutability burden.

#315 does not create that layer merely to obtain cleaner percentages.

### Source-system independence

Even a future exact source-family annotation would not establish statistical independence
or representativeness.

Multiple cases can use:

- the same institution;
- the same publication infrastructure;
- the same underlying EU act family;
- related research pathways.

Source-family diversity is not equivalent to independent sampling.

### Older digitised / degraded-metadata sources

Nothing in this audit overturns #309's finding that deliberate coverage of old digitised
legal sources with materially degraded metadata remains unsupported.

## Decision

**REVISE_METHOD**

The correct durable claim is:

> The final corpus has materially broader **source-family variety** than the original
> seed, including Member-State, private-recognised, agency/body, structured-register and
> linked-order evidence. The project still lacks a canonical or reproducible exact
> per-case source-system inventory, so source-system concentration must not be expressed
> as precise corpus-wide percentages.

Consequences:

- do **not** add a `source_system` field to the frozen corpus;
- do **not** publish the naïve owner-chain counts as case-level scientific metrics;
- keep the old "source-system diversity is a risk" warning, but qualify that several
  previously missing families are now represented;
- if a concrete external regression/audit use later needs exact source provenance,
  that need can earn a separate derived per-case source inventory.

No corpus, class, Reference Pack byte or #214 interpretation changes.

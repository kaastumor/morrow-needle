# #432 — Red-team: act-centric legal lifecycle map

Date: 2026-09-27  
Disposition: **ADOPT_FOR_EXPERIMENT**

## Sponsor job

When inspecting a directive, the user wants one place to understand:

- where the act came from;
- when it began and when/if it ends;
- predecessor, codification, recast, repeal and successor relationships;
- what materially shapes or operationalises it;
- what downstream legal mechanisms depend on it;
- how those relationships change over time;
- the official evidence behind each relationship.

This is a concrete product job observed while using the live Candidate-B surface.

## Red-team result

The proposal survives, but **not** as a general legal knowledge graph.

The safe form is:

> **an act-centric, evidence-bounded lifecycle projection over existing Needle truth owners**

The first implementation must be a read-side projection, not a new canonical ontology.

## Why it survives

### 1. The job is real enough to reactivate preserved capability

The sponsor identified the need while using the live product rather than from architecture-first ideation.

The historical asset register already marks:
- Thread as a valid audit tool, parked pending a real chronology/reopening job;
- provision/rule lineage, identifier graph and temporal semantics as case-earned/historically valid;
- Full Needle as rejected as the default identity.

This request earns a **subset** of those capabilities, not Full Needle.

### 2. Existing contracts already enforce the important separations

Needle already prevents the most dangerous implementation shortcuts:

- Regime Lineage v0.2 owns genealogy but does not own legal dates.
- Temporal owns entry/application/end state and precision.
- Identifier Graph forbids generic “same document”.
- Procedure state remains separate from legal force/application.
- Thread is reference-only composition and may not duplicate canonical truth.
- Retrieval is a disposable projection, never legal truth.

Therefore the first lifecycle view should compose references to those owners rather than introduce a new “lifecycle graph” truth store.

### 3. The first LVD case has strong official structure

Directive 2014/35/EU is explicitly a **recast** of Directive 2006/95/EC. Its Article 27 repeals 2006/95/EC from 20 April 2016 and provides a correlation table. The 2014 act also states that 2006/95/EC was a codification of Directive 73/23/EEC.

The same act identifies Regulation (EC) No 765/2008 and Decision No 768/2008/EC as important New Legislative Framework context. These are not ancestors and must not be drawn as such.

Candidate B already has Article 12 -> OJ harmonised-standard state as a downstream operational dependency.

## Strongest attacks

### A. Pretty-graph trap

**Attack:** a graph may look insightful while adding little beyond EUR-Lex links.

**Control:** the default view must answer a bounded question in seconds:
- came from;
- current lifecycle state;
- materially shaping legal context;
- operative downstream mechanism;
- successor/end state.

If the graph merely reproduces a bibliography, reject it.

### B. General-purpose knowledge-graph creep

**Attack:** “show everything connected to this directive” becomes unlimited legal graph expansion.

**Control:** first slice is:
- one focal act;
- one-hop default;
- explicit typed relation classes;
- progressive disclosure;
- no generic `RELATED_TO`;
- no automatic traversal beyond the focal act.

### C. Completeness illusion

**Attack:** users read a finite graph as “all relevant legal influences”.

**Control:** never label the result “all influences” or “complete legal context”.

Use:
> **Known evidenced relationships in this frozen view**

Every branch must expose:
- evidence/source;
- relation type;
- evidence/freshness date;
- explicit unknown/coverage boundary where material.

### D. Semantic collapse

**Attack:** predecessor, amendment, legal basis, implementation, interpretation and operational dependency all become identical arrows.

**Control:** separate lanes and edge types. At minimum:

1. **LINEAGE**
   - CODIFIED_AS
   - RECAST_AS
   - REPEALED_BY / REPLACES
   - SUCCESSOR where directly evidenced

2. **LIFECYCLE**
   - ADOPTED
   - PUBLISHED
   - ENTERED_INTO_FORCE
   - APPLIES_FROM
   - REPEALED / ENDS where evidenced

3. **LEGAL CONTEXT**
   - ADAPTED_TO_FRAMEWORK
   - IMPLEMENTED_BY / DELEGATED_BY only when legally accurate
   - AMENDED_BY
   - CORRIGENDUM_OF
   - INTERPRETED_BY only when a later case earns it

4. **OPERATIVE DEPENDENCY**
   - provision -> authoritative set/status mechanism
   - e.g. Article 12 -> OJ harmonised-standard reference state

Do not use the word “influence” as an edge type.

### E. Temporal duplication

**Attack:** lifecycle cards copy dates and become a second state database.

**Control:** lifecycle projection references canonical Temporal Assertions where they exist. Missing canonical time must be added to the existing temporal owner or remain unresolved; it must not be patched into the UI model.

### F. Maintenance explosion

**Attack:** one act can have hundreds of references, amendments, standards and decisions.

**Control:** first slice is manually bounded to consequential typed relationships for one focal act. No crawler, no recursive graph expansion, no alerts, no live monitor.

### G. Scope laundering

**Attack:** national transposition, case law, standards discovery, delegated acts and every product rule get pulled in because they are “relevant”.

**Control:** first experiment excludes:
- national transposition;
- general case-law network;
- applicable-standard discovery;
- all harmonised standards;
- generic amendment crawling;
- portfolio/workspace features.

The two existing LVD Candidate-B standards may be shown only as examples of the Article 12 downstream mechanism.

### H. False successor claims

**Attack:** absence of a known successor is rendered as “no successor”.

**Control:** render:
> **No successor represented in this frozen evidence view**

not:
> **No successor exists**

## First implementation slice

Focal act:

> **Directive 2014/35/EU — Low Voltage Directive**

Default view should contain four compact regions:

### Came from
- Directive 73/23/EEC
- codified as Directive 2006/95/EC
- recast/replaced by Directive 2014/35/EU

### Life of this act
- adopted;
- published;
- entry into force;
- application/transposition boundary;
- current/repeal state as supported by evidence.

These dates must preserve distinct temporal meanings.

### What shapes/operationalises it
- Regulation (EC) No 765/2008 — market surveillance/accreditation/CE-marking framework context;
- Decision No 768/2008/EC — common framework to which the recast was adapted;
- other edges only when directly evidenced and necessary for the first job.

### What flows from it
- Article 12 harmonised-standard/OJ-reference mechanism;
- link into the existing Candidate-B status examples:
  - EN 60335-2-14:2006;
  - EN 60335-2-60:2003.

## UI constraint

Do **not** begin with a force-directed graph.

Start with a compact typed lifecycle map / structured tree-like projection that preserves reading order.

Graph interaction is earned only if the bounded view becomes difficult to navigate without it.

## Acceptance test for the experiment

A user looking at Directive 2014/35/EU should be able to answer, without opening EUR-Lex first:

1. What preceded this directive?
2. Was it a codification/recast/replacement?
3. When did the prior directive stop applying?
4. What are the distinct key dates for this act?
5. Which external framework acts materially explain its current structure?
6. How does Article 12 connect to harmonised-standard OJ status?
7. What is known versus merely absent from this frozen view?
8. Where can each claim be verified officially?

If the view cannot answer these more clearly than a short source-linked note, stop rather than generalise.

## Architecture decision

**No new canonical lifecycle schema in the first experiment.**

Use a disposable/read-side composition over:
- existing lineage;
- temporal;
- identity;
- procedure;
- authoritative dynamic-set;
- provenance/source refs.

If the LVD slice exposes a relationship that existing contracts genuinely cannot represent, that is evidence for a narrowly scoped model repair. It is not permission to create a broad graph ontology.

## Disposition

> **ADOPT_FOR_EXPERIMENT**

Reason:

- concrete sponsor use signal;
- strong fit with preserved, technically valid Needle capabilities;
- official LVD evidence supports a meaningful first case;
- implementation can remain a thin projection;
- primary risks are controllable through typed relations, bounded traversal and explicit completeness limits.

This result does **not** establish:
- market demand;
- novelty;
- superiority over commercial legal platforms;
- permission for a general legal knowledge graph;
- permission to revive Full Needle.

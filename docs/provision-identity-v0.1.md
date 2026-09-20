# Provision Identity Model v0.1

## Status

**Foundation decision adopted after falsification test.**

Needle/Thread must not assign one persistent identity to a legal provision across restructuring, recodification, repeal-and-replacement, or recast.

The stable object is a **Provision Instance**: one provision/subdivision in one legal text state.

Historical continuity is represented by **evidence-backed lineage edges** between provision instances.

## Why the original assumption fails

Council Regulation No 26 (1962) was repealed and replaced by Council Regulation (EC) No 1184/2006.

The replacing act contains an official correlation table showing mappings including:

- old Article 1 → new Article 1;
- old Article 2(1) → new Article 2(1);
- old Article 2(2) → new Article 2(2), first subparagraph;
- old Article 2(3) → new Article 2(2), second subparagraph;
- old Article 2(4) → new Article 2(3);
- old Article 3 → no successor;
- old Article 4 → new Article 3;
- no predecessor → new Article 4;
- old Article 5 → new Article 5.

Therefore:

1. **same number ≠ same identity**;
2. **different number ≠ different lineage**;
3. one parent provision can be structurally merged while child rules retain separate lineage;
4. deletion and insertion must be explicit lineage outcomes;
5. repeal-and-replacement across a new CELEX act can preserve rule ancestry.

## Model

### Provision Instance

A provision instance is immutable and scoped to a concrete legal text state.

Suggested identity components:

- act/work identifier;
- expression/language;
- text-state/version;
- structural path;
- source-span/hash;
- official subdivision identifier where available.

A provision instance does not survive into another act or version by changing its ID.

### Lineage Edge

A lineage edge says that official evidence or verified analysis relates one or more source provision instances to one or more target provision instances.

Allowed initial edge types:

- `CONTINUES_AS` — legal content continues in a successor provision;
- `RENUMBERED_TO` — primarily structural number/path change;
- `MOVED_TO` — location changes without losing lineage;
- `SPLIT_INTO` — one source provision becomes multiple successor provisions;
- `MERGED_INTO` — multiple sources become one successor container/rule;
- `RECAST_AS` — successor exists in a recast where substantive editing may coexist;
- `REPLACED_BY` — formal repeal/replacement with supported legal continuity;
- `DELETED` — source has no successor;
- `INSERTED` — target has no predecessor;
- `CONCEPTUAL_SUCCESSOR` — continuity is interpretive rather than explicit textual/legal correlation.

### Evidence basis

Each edge records its provenance:

- `OFFICIAL_CORRELATION_TABLE`
- `OFFICIAL_AMENDMENT_INSTRUCTION`
- `OFFICIAL_RELATION_METADATA`
- `DETERMINISTIC_TEXT_ALIGNMENT`
- `OFFICIAL_EXPLANATORY_MATERIAL`
- `HUMAN_LEGAL_REVIEW`
- `MODEL_HYPOTHESIS`

`MODEL_HYPOTHESIS` can never by itself support a public VERIFIED Thread edge.

## Important distinction: structure lineage vs rule lineage

The 1962 → 2006 case demonstrates two overlapping graphs.

At the **structural** level, old Article 2 paragraphs (2) and (3) become two subparagraphs inside new paragraph 2: a many-to-one parent restructuring.

At the **rule** level, each source rule still has its own independently mapped successor.

Thread therefore needs lineage at arbitrary subdivision granularity. Parent-level lineage cannot be inferred merely by copying child mappings, and child identity cannot be inherited blindly from the parent.

## Thread rendering rule

Thread should never imply:

> “This is the same Article.”

Instead, it should communicate:

> “Official EU correlation data maps this earlier provision to this later provision.”

Where continuity is not explicit, Thread must display the weaker evidence state.

## Consequence for Change Atoms

Change Atoms reference provision instances, not persistent provision IDs.

When a mutation crosses a repeal/replacement boundary, an atom may point to:
- source provision instance(s);
- target provision instance(s);
- lineage edge(s) that justify the comparison.

## Consequence for historical queries

“Show the history of Article 3” is ambiguous.

Needle should distinguish:
- **number history:** every provision called Article 3;
- **lineage history:** the ancestors/descendants of the current Article 3;
- **concept history:** semantically related rules, which may be interpretive.

This is now a core Thread distinction.

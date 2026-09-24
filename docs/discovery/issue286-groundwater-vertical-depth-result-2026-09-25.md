# #286 result — groundwater-body depth test for vertical spatial extent

Date: 2026-09-25  
Issue: #286  
Depth lane: run 2/3 under the #282 falsifier

## Decision

# **REVISE_EXISTING_CLASS**

Retain the existing class ID `VERTICAL_SPATIAL_EXTENT`, sharpen its definition to cover
legally consequential **vertical stratification** as well as explicit upper/lower extents,
and add one Water Framework Directive groundwater-body derivation case.

Corpus consequence:

> **81 cases / 26 classes**

No new class.

## Frozen question

Does the Water Framework Directive groundwater-body regime create a consequential legal
state that can differ vertically at the same horizontal x/y, such that horizontal geometry
alone can give a wrong legal answer?

The answer is **yes**.

The result does not rest on the physical fact that groundwater is three-dimensional or on
the Directive's use of the word “volume”. The decisive evidence is that:

1. the legal unit is a body of groundwater;
2. legal status, objectives, monitoring and measures attach to that unit;
3. EU implementation guidance expressly permits separate bodies in vertically overlying
   strata where status differs;
4. current EEA reporting explicitly says groundwater bodies are three-dimensional
   entities whose 2-D polygons are only surface projections, and uses separate horizons
   to distinguish overlapping bodies at different depths.

A horizontal x/y-only representation can therefore conflate legally distinct groundwater
bodies and their status.

## Primary law

Directive 2000/60/EC Article 2 defines:

- an aquifer as a subsurface layer or layers of rock/geological strata with the specified
  groundwater-flow/abstraction characteristics;
- a **body of groundwater** as a distinct volume of groundwater within an aquifer or
  aquifers.

Source:
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32000L0060

The Directive's groundwater monitoring/status regime assesses quantitative and chemical
status at the groundwater-body or group-of-bodies level.

Current consolidated source:
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02000L0060-20260510

Directive 2006/118/EC then makes the body-level consequence explicit for chemical status.
Article 4 assesses whether **a body or group of bodies of groundwater** is in good chemical
status and requires representative monitoring for that body/group.

Source:
- https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32006L0118

So the body identity is not merely cartographic metadata. It owns legal assessment state.

## Three-dimensional delineation and status consequence

WFD Common Implementation Strategy Guidance Document No. 2 is non-binding implementation
guidance, not primary law. It is nevertheless highly probative for the representation
question because it addresses how the Directive's body concept is operationalised.

It states in substance that:

- water bodies are the units for reporting and assessing compliance with the Directive's
  principal environmental objectives;
- objectives and measures depend on the bodies' status;
- groundwater bodies should be delineated in **three dimensions**;
- the Directive permits groundwater bodies to be identified separately in different
  strata overlying one another in the vertical plane;
- where status differs materially between strata at different depths, it may be
  appropriate to identify different groundwater bodies “one on top of another” so status
  can be accurately described and objectives appropriately targeted.

Source:
- https://circabc.europa.eu/sd/a/655e3e31-3b5d-4053-be19-15bd22b15ba9/Guidance%20No%202%20-%20Identification%20of%20water%20bodies.pdf

This satisfies the frozen regression consequence directly:

> the same horizontal x/y can correspond to different legally relevant groundwater bodies
> in different vertical strata, with body-specific status and management consequences.

## Current official reporting confirms the representation problem

The European Environment Agency's current WISE WFD groundwater-body-horizon dataset
states that:

- groundwater bodies are three-dimensional entities;
- their reported polygons are projections on the surface;
- multiple overlapping groundwater bodies at different depths must be distinguishable in
  different horizons/layers;
- overlapping groundwater bodies cannot be assigned to the same horizon;
- the horizon expresses relative vertical position and need not encode absolute z.

Source:
- https://www.eea.europa.eu/en/datahub/datahubitem-view/2f198cd5-9cc6-4d4f-a2a1-3ad3f647aea5

This is important because it prevents overfitting the class to aviation-style numeric
upper/lower limits.

The consequential owner is:

> **vertical spatial differentiation that cannot be recovered safely from horizontal
> geometry alone**

not:

> every case must supply a normalised absolute vertical coordinate interval.

## Strongest rival — object identity alone

A groundwater-body identifier can of course resolve a known body's status without
reconstructing its 3-D geometry.

That does not eliminate the representation failure.

The frozen question concerns spatial identification/research from location. The EEA
reporting model itself acknowledges that a 2-D polygon is only a projection and that
overlapping bodies need a separate vertical horizon to avoid conflation.

Therefore:

- object ID is sufficient **after** the correct body has been identified;
- x/y geometry alone can be insufficient to identify which legal body is relevant.

The vertical owner survives only for that spatial-identification problem. The class does
not become a generic “object has an ID” abstraction.

## #227 negative boundary still holds

The rejected deep-sea fisheries candidate remains a strong control.

Its bottom-gear depth thresholds are tied to seabed bathymetry and can be represented as a
derived horizontal eligibility mask. The operation does not require independently
distinguishing stacked legal spatial states at the same x/y.

Groundwater is different:

- official WFD implementation permits distinct bodies in vertically overlying strata;
- current EEA reporting explicitly needs horizon/layer state to distinguish overlapping
  groundwater-body projections.

Therefore:

> **vertical measurement is not enough; independently meaningful vertical
> differentiation is required.**

## Class repair

Previous definition:

> Legal geography is volumetric and cannot be represented safely as horizontal geometry
> alone.

Revised definition:

> Legal geography has a legally consequential vertical extent or stratification such that
> horizontal geometry alone can conflate distinct legal spatial states; this includes
> bounded altitude/volume and stacked legally distinct spatial units, but excludes vertical
> measurements that can be losslessly projected into a horizontal mask.

The existing ID `VERTICAL_SPATIAL_EXTENT` is retained.

The Commission guidance expressly treats groundwater bodies as having upper/lower
boundaries and requiring three-dimensional delineation, so a rename would create more
taxonomy churn than information gain. The repaired definition is enough.

## Added derivation case

### WFD groundwater bodies — vertically overlying status units

Decisive trap:

> WFD groundwater bodies may be separately delineated in vertically overlying strata where
> status differs, while EEA WISE represents their 3-D bodies through 2-D surface
> projections plus distinct horizon/layer state. A horizontal footprint alone can therefore
> conflate the groundwater body whose chemical/quantitative status and objectives apply.

This is orthogonal to:
- aviation: explicit altitude bands/limits;
- CO2 storage: a permitted geological storage volume.

It is also distinct from #227:
- fisheries depth can collapse into a bathymetry-derived horizontal mask;
- stacked groundwater bodies cannot be distinguished safely by x/y projection alone.

## Depth falsifier

This is depth run **2/3**.

It is not confirmation-only because the class boundary is sharpened from generic
“volumetric” language to a testable rule:

> horizontal geometry must be insufficient because legally consequential vertical
> differentiation survives.

It also establishes that the vertical distinction can be encoded as relative
layer/horizon state rather than only an absolute numeric z interval.

Depth score:

> run **2/3: informative** — definition/boundary changed.

The #282 direction-review trigger does not fire.

## Preselected depth run 3

After #286 merges, the next depth target is preselected as:

> **`CHOICE_OF_FORUM_STATE`**

Reason for selection:
- it has only three corpus cases;
- all three remain inside private international law;
- one of the three is a composition case rather than an independent mechanism;
- it is among the newest classes and therefore carries comparatively high path-dependence
  risk;
- its law is mature incumbent doctrine, making it a strong test of #282's rule that
  “known doctrine” is neither automatic rejection nor automatic corpus value.

Depth run 3 should test whether the class has a consequential standalone regression owner
beyond merely restating jurisdiction-agreement doctrine, with explicit permission to
narrow, consolidate or retire the class.

Do not begin substantive run-3 research before #286 is merged and closed.

## Final

# **REVISE_EXISTING_CLASS**

- retain `VERTICAL_SPATIAL_EXTENT`;
- sharpen its definition around consequential vertical differentiation;
- add one WFD groundwater-body derivation case;
- retain #227 fisheries as the negative boundary;
- no new class;
- staged corpus becomes **81 cases / 26 classes**;
- preselected next depth target: `CHOICE_OF_FORUM_STATE`.

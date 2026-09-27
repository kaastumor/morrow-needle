# Regime UI comparison v0.2

Issue: #473  
Status: **SEPARATE UI/IA EXPERIMENT — SAME MEDICAL-DEVICES EVIDENCE**

Route:
`/regime-v2/`

Comparator:
`/regime/`

## What changes

v0.2 changes presentation and task structure:

- Overview;
- Explore;
- Change review;
- Expert / research.

The default Overview is deliberately small.

It keeps:
- regime identity;
- evidence date;
- three-predecessor -> two-core structure;
- transition qualifier;
- branch scope phrases;
- represented downstream layers;
- current enacted change vs proposal distinction;
- coverage boundary.

It moves:
- individual child acts -> Explore;
- provision/source rationale -> Why? disclosure;
- review-propagation mechanics -> Change review;
- research/coverage diagnostics -> Expert / research.

## What does not change

- same bounded medical-devices fixture;
- same legal relation claims;
- same current/proposal/non-binding distinctions;
- same source links/evidence date;
- same abstention around structural-gap claims;
- same no-completeness boundary.

## Test hypothesis

The original route has roughly 2,087 words exposed in the initial DOM state.

For this exact fixture, v0.2 targets <=450 words in Header + default Overview.

This threshold is a project design hypothesis, not a usability standard.

A lower word count is insufficient if legal qualifiers or evidence access disappear.

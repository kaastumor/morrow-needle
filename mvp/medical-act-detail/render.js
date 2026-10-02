"use strict";

const {SHARED} = require("./acts.js");

function esc(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function renderRows(rows, className, renderer) {
  return '<div class="' + className + '">' + rows.map(renderer).join("") + "</div>";
}

function humanDate(iso) {
  const [year, month, day] = String(iso).split("-");
  const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  return Number(day) + " " + months[Number(month) - 1] + " " + year;
}

function relationshipSourceLabel(type) {
  if (type === "AMENDED_BY") return "Official amending act";
  if (type === "OPERATIONAL_TRIGGER") return "Official trigger decision";
  if (type === "REPLACES") return "Official core-act source";
  return "Official relationship source";
}

function renderActGlance(act) {
  const future = act.timeline.filter(row => row[0] === "FUTURE_TRANSITION");
  const lastFuture = future[future.length - 1];
  const roleNames = act.roles.map(row => row[0]).join(", ");
  const representedChanges = act.relationships
    .filter(row => row[0] === "AMENDED_BY" || row[0] === "OPERATIONAL_TRIGGER")
    .map(row => row[1])
    .join(", ");

  return '<section class="act-glance" aria-labelledby="act-glance-heading">' +
    '<div class="act-glance-heading"><p class="section-kicker">At a glance</p>' +
    '<h2 id="act-glance-heading">What matters before the detail</h2>' +
    '<p>Summary of the same represented act data below; it does not determine a reader\'s role or applicability.</p></div>' +
    '<div class="act-glance-grid">' +
    '<article><h3>Purpose</h3><p>' + esc(act.purpose) + '</p><a href="#scope">Open scope →</a></article>' +
    '<article><h3>Current state</h3><p>' + esc(act.legalStatus) + '. General application date: ' +
    esc(humanDate(act.generalApplicationDate)) + '.</p><a href="#time">See typed dates →</a></article>' +
    '<article><h3>What changed</h3><p>Represented later changes include ' + esc(representedChanges) +
    '. Relationship labels below distinguish amendments from operational triggers.</p><a href="#relationships">See legal connections →</a></article>' +
    '<article><h3>Roles represented</h3><p>' + esc(roleNames) +
    '. Roles can overlap; this page does not assign one to you.</p><a href="#roles">Compare role summaries →</a></article>' +
    '<article><h3>Upcoming state</h3><p>' +
    (lastFuture ? 'Selected legacy-transition milestones shown below extend through ' + esc(humanDate(lastFuture[1])) +
    ', subject to the stated conditions.' : 'No future transition milestone is represented in this bounded view.') +
    '</p><a href="#time">Inspect transitions →</a></article>' +
    '<article><h3>Evidence and depth</h3><p>Source version, official act links and limits remain explicit below.</p>' +
    '<a href="#sources">Open official evidence →</a></article>' +
    '</div></section>';
}

function renderActPage(act) {
  const scope = act.scope.map(item => '<li>' + esc(item) + "</li>").join("");
  const roles = renderRows(act.roles, "act-role-grid", ([role, article, text]) =>
    '<article><h3>' + esc(role) + '</h3><p class="act-meta">' + esc(article) + '</p><p>' + esc(text) + '</p></article>'
  );
  const timeline = '<ol class="act-timeline">' + act.timeline.map(([type, date, label, text]) =>
    '<li data-time-type="' + esc(type) + '"><time datetime="' + esc(date) + '">' + esc(date) +
    '</time><div><span class="act-type">' + esc(type.replaceAll("_", " ")) + '</span><strong>' +
    esc(label) + '</strong><p>' + esc(text) + '</p></div></li>'
  ).join("") + "</ol>";
  const relationships = '<ul class="act-relations">' + act.relationships.map(([type, target, text, sourceUrl]) =>
    '<li><span class="act-type">' + esc(type.replaceAll("_", " ")) + '</span><strong>' + esc(target) +
    '</strong><p>' + esc(text) + '</p><a class="act-relation-source" href="' + esc(sourceUrl) +
    '" target="_blank" rel="noreferrer">' + relationshipSourceLabel(type) + ' ↗</a></li>'
  ).join("") + "</ul>";

  return '<!doctype html>\n<html lang="en">\n<head>\n' +
    '<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">' +
    '<meta name="description" content="Source-linked Needle EU detail view for ' + esc(act.citation) + '.">' +
    '<title>' + esc(act.code) + ' detail — Needle EU</title>' +
    '<link rel="stylesheet" href="/product-shell.css"><link rel="stylesheet" href="/medical-devices/act-detail.css">' +
    '</head><body class="product-route"><a class="skip-link" href="#main">Skip to content</a>' +
    '<header class="product-shell"><a class="product-shell__brand" href="/">Needle EU</a>' +
    '<nav class="product-shell__nav" aria-label="Product navigation"><a href="/medical-devices/">Medical-device legislation</a>' +
    '<a href="/mvp/candidate-b/">Known-standard status</a><a href="/#coverage">About coverage</a></nav></header>' +
    '<nav class="product-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/medical-devices/">Medical-device legislation</a> / ' + esc(act.code) + '</nav>' +
    '<main id="main" class="act-detail" tabindex="-1"><header class="act-hero">' +
    '<p class="eyebrow">Core act · source-bounded orientation</p><p class="act-code">' + esc(act.code) + '</p>' +
    '<h1>' + esc(act.title) + '</h1><p class="act-citation">' + esc(act.citation) + '</p><p class="act-purpose">' + esc(act.purpose) + '</p>' +
    '<aside class="act-evidence" aria-labelledby="evidence-heading"><h2 id="evidence-heading">Evidence and legal-state boundary</h2><dl>' +
    '<div><dt>Status</dt><dd>' + esc(act.legalStatus) + '</dd></div>' +
    '<div><dt>Evidence checked</dt><dd><time datetime="' + SHARED.evidenceChecked + '">' + SHARED.evidenceChecked + '</time></dd></div>' +
    '<div><dt>Consolidated version used</dt><dd><a href="' + esc(act.consolidatedSource) + '" target="_blank" rel="noreferrer">' + esc(act.consolidationDate) + ' ↗</a></dd></div>' +
    '<div><dt>General application</dt><dd><time datetime="' + esc(act.generalApplicationDate) + '">' + esc(act.generalApplicationDate) + '</time></dd></div>' +
    '</dl><p><strong>Boundary:</strong> this EU-level regulation view does not settle national rules, enforcement choices or a reader\'s individual applicability. A consolidation is a documentary aid; authentic Official Journal acts govern.</p></aside></header>' +
    renderActGlance(act) +
    '<nav class="act-local-nav" aria-label="On this page"><a href="#scope">Scope</a><a href="#roles">Roles</a><a href="#time">Time</a><a href="#relationships">Relationships</a><a href="#sources">Sources</a></nav>' +
    '<section id="scope" class="act-section"><p class="section-kicker">Purpose and scope</p><h2>What this act covers</h2><ul class="act-scope">' + scope + '</ul><p class="act-boundary">This is selected orientation. Classification, every exclusion, national rules and personal applicability require the full sources and facts.</p></section>' +
    '<section id="roles" class="act-section"><p class="section-kicker">Economic-operator orientation</p><h2>Represented roles</h2>' + roles + '<p class="act-boundary">Roles can overlap. These summaries do not determine which role a reader occupies and are not complete obligation lists. Follow the article source below.</p></section>' +
    '<section id="time" class="act-section"><p class="section-kicker">Time</p><h2>Current state and selected transitions</h2><p>Dates are typed by legal function. A future transition is not shown as current state, and a general application date does not replace provision-specific dates.</p>' + timeline + '</section>' +
    '<section id="relationships" class="act-section"><p class="section-kicker">Relationships</p><h2>Selected legal connections</h2><p>Relationship labels describe the represented legal connection; visual proximity is not an impact inference. Each represented connection links to the official source used for that relationship.</p>' + relationships + '<p class="act-boundary">A relationship source supports the connection shown here; it does not by itself prove every downstream effect or a reader\'s individual applicability.</p></section>' +
    '<section id="sources" class="act-section"><p class="section-kicker">Verification</p><h2>Official sources and next paths</h2><div class="act-source-grid">' +
    '<a href="' + esc(act.originalSource) + '" target="_blank" rel="noreferrer"><strong>Original act</strong><span>Official EUR-Lex text ↗</span></a>' +
    '<a href="' + esc(act.articlesUrl) + '" target="_blank" rel="noreferrer"><strong>Article text</strong><span>Versioned consolidation ↗</span></a>' +
    '<a href="' + esc(act.transitionSource) + '" target="_blank" rel="noreferrer"><strong>Transition/amendment source</strong><span>Official amending act ↗</span></a>' +
    '<a href="' + esc(SHARED.amendment2024Url) + '" target="_blank" rel="noreferrer"><strong>2024/1860</strong><span>Cross-cutting amendment ↗</span></a>' +
    '<a href="' + esc(SHARED.eudamedDecisionUrl) + '" target="_blank" rel="noreferrer"><strong>EUDAMED trigger</strong><span>Decision (EU) 2025/2371 ↗</span></a>' +
    '<a href="' + esc(SHARED.eudamedUrl) + '" target="_blank" rel="noreferrer"><strong>EUDAMED status</strong><span>Commission overview ↗</span></a>' +
    '</div><div class="act-next-paths"><a href="/medical-devices/">Return to medical-device overview</a><a href="/#search-heading">Ask where to start</a><a href="/regime-v2/#explore">Explore selected relationships</a><a href="/regime-v2/#changes">Review represented changes</a></div>' +
    '<p class="act-boundary"><strong>This page does not decide compliance.</strong> It is a selected, evidence-dated explanation of the represented EU-level act.</p></section></main>' +
    '<footer class="product-footer"><p>Needle EU · independent research demonstration. Official sources govern.</p><p><a href="/medical-devices/">Medical-device overview</a> · <a href="/#coverage">Coverage and limits</a> · <a href="https://github.com/kaastumor/morrow-needle/issues/new">Report a correction</a></p></footer></body></html>\n';
}

module.exports = {renderActPage};

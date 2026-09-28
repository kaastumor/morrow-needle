"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");
const css = fs.readFileSync(path.join(__dirname, "styles.css"), "utf8");

function section(id, nextId) {
  const start = html.indexOf('id="' + id + '"');
  assert.notEqual(start, -1);
  const end = nextId ? html.indexOf('id="' + nextId + '"', start + 1) : html.length;
  return html.slice(start, end === -1 ? html.length : end);
}

test("public entry remains summary-first rather than relationship-first", () => {
  const summaryPos = html.indexOf('id="summary"');
  const coveredPos = html.indexOf('id="covered"');
  const relationPos = html.indexOf('id="relationships"');

  assert.ok(summaryPos > -1);
  assert.ok(summaryPos < coveredPos);
  assert.ok(coveredPos < relationPos);
  assert.match(html, /What these rules do/);
  assert.match(html, /Who and what is covered/);
  assert.doesNotMatch(html.slice(0, coveredPos), /Change review/);
  assert.doesNotMatch(html.slice(0, coveredPos), /Expert \/ research/);
});

test("T1 purpose can be answered from the standard summary", () => {
  const block = section("summary", "covered");
  assert.match(block, /placing, supplying and putting medical devices and in-vitro diagnostic devices into service/i);
  assert.match(block, /evidence and conformity before market entry/i);
  assert.match(block, /traceability/i);
  assert.match(block, /monitoring after devices reach the market/i);
});

test("T2 branch distinction is explicit and source-linked", () => {
  const block = section("covered", "dates");
  assert.match(block, /MDR/);
  assert.match(block, /Regulation \(EU\) 2017\/745/);
  assert.match(block, /Start here for medical devices for human use and accessories/i);
  assert.match(block, /IVDR/);
  assert.match(block, /Regulation \(EU\) 2017\/746/);
  assert.match(block, /Start here for in-vitro diagnostic medical devices for human use/i);
  assert.match(block, /eur-lex\.europa\.eu\/eli\/reg\/2017\/745/);
  assert.match(block, /eur-lex\.europa\.eu\/eli\/reg\/2017\/746/);
});

test("T3 importer and distributor relevance is visible without opening raw law", () => {
  const block = section("covered", "dates");
  assert.match(block, /You do not have to be the manufacturer to need these rules/);
  assert.match(block, /Importer/);
  assert.match(block, /third country on the Union market/i);
  assert.match(block, /Distributor/);
  assert.match(block, /specified checks/i);
  assert.match(block, /Do not infer exclusion from this list/);
});

test("T4 IVDR laboratory boundary remains permanently visible", () => {
  const block = section("covered", "dates");
  assert.match(block, /Important laboratory boundary/);
  assert.match(block, /general laboratory or research-use products are outside the IVDR unless/i);
  assert.match(block, /manufacturer specifically intends them for in-vitro diagnostic examination/i);
  assert.doesNotMatch(block, /<details/);
});

test("T5 timing is one chronology without inventing a regime-wide date", () => {
  const block = section("dates", "requirements");
  assert.match(block, /Dates and current operation/);
  assert.match(block, /26 May 2021/);
  assert.match(block, /MDR general application \/ predecessor replacement/);
  assert.match(block, /26 May 2022/);
  assert.match(block, /IVDR general application \/ predecessor replacement/);
  assert.match(block, /28 May 2026/);
  assert.match(block, /Current EUDAMED operational milestone/);
  assert.match(block, /first four EUDAMED modules became mandatory to use/i);
  assert.match(block, /does not mean all six EUDAMED modules are already mandatory/i);
  assert.match(block, /These dates do not settle every legacy-device case/);
  assert.doesNotMatch(block, /regime applies from/i);
});

test("T6 proposal remains explicitly non-binding and verification is public", () => {
  const block = section("changes", "relationships");
  assert.match(block, /Proposal — not enacted/);
  assert.match(block, /Procedure 2025\/0404\(COD\) remains ongoing/i);
  assert.match(block, /not current binding Union law/i);
  assert.match(block, /eur-lex\.europa\.eu\/procedure\/EN\/2025_404/);
  assert.match(html, /Sources and coverage/);
  assert.match(html, /MDR — current EUR-Lex access/);
  assert.match(html, /IVDR — current EUR-Lex access/);
});

test("role effects remain concise, source-linked, and avoid personal verdicts", () => {
  const block = section("requirements", "changes");
  assert.match(block, /Manufacturers/);
  assert.match(block, /Importers/);
  assert.match(block, /Distributors/);
  assert.match(block, /Other affected groups/);
  assert.doesNotMatch(html, /you are covered/i);
  assert.doesNotMatch(html, /you are exempt/i);
  assert.doesNotMatch(html, /compliant with the law/i);
});

test("later-development section stays selected rather than falsely complete", () => {
  const block = section("changes", "relationships");
  assert.match(block, /Later changes and current procedure/);
  assert.match(block, /not a complete list of post-2017 acts/i);
  assert.match(block, /2025–2026 measures continue beyond 2024\/1860/);
  assert.match(block, /Decision \(EU\) 2025\/2371/);
  assert.match(block, /Implementing Regulation \(EU\) 2026\/977/);
  assert.match(block, /Delegated Regulations \(EU\) 2026\/1359 and 2026\/1451/);
  assert.doesNotMatch(block, /What changed after the core Regulations\?/);
});

test("material qualifications are visible rather than hidden by progressive disclosure", () => {
  assert.doesNotMatch(html, /<details/);
  assert.doesNotMatch(html, /role="tab"/);
  assert.match(html, /Important laboratory boundary/);
  assert.match(html, /These dates do not settle every legacy-device case/);
  assert.match(html, /Proposal — not enacted/);
  assert.match(html, /Do not infer exclusion from this list/);
});

test("page explicitly identifies itself as independent editorial orientation", () => {
  assert.match(html, /Independent editorial overview/);
  assert.match(html, /Independent editorial explainer/);
  assert.match(html, /editorial overview, not an official EU source/i);
  assert.match(html, /independent editorial orientation built from official EU sources/i);
});

test("regime page does not invent one legal status or application date", () => {
  assert.doesNotMatch(html, /Regime status/);
  assert.doesNotMatch(html, /In force<\/dd>/);
  assert.doesNotMatch(html, /Regime application date/);
  assert.doesNotMatch(html, /regime applies from/i);
});

test("H2-only contents navigation tells the reading story and stays out of the site bar", () => {
  const nav = html.slice(html.indexOf('<nav class="page-nav"'), html.indexOf('</nav>', html.indexOf('<nav class="page-nav"')) + 6);
  assert.match(nav, /What these rules do/);
  assert.match(nav, /Who and what is covered\?/);
  assert.match(nav, /Dates and current operation/);
  assert.match(nav, /What the rules require/);
  assert.match(nav, /Later changes and current procedure/);
  assert.match(nav, /How the rules fit together/);
  assert.match(nav, /Sources and coverage/);
  assert.doesNotMatch(nav, /<ul[^>]*>[^]*<ul/);

  const siteBar = html.slice(html.indexOf('<header class="site-bar">'), html.indexOf('</header>', html.indexOf('<header class="site-bar">')) + 9);
  assert.doesNotMatch(siteBar, /<nav/);
});

test("relationship browser remains secondary and comes after substantive orientation", () => {
  const relationPos = html.indexOf('id="relationships"');
  const requirementPos = html.indexOf('id="requirements"');
  const changePos = html.indexOf('id="changes"');
  assert.ok(relationPos > requirementPos);
  assert.ok(relationPos > changePos);
  assert.match(html, /Explore the legal relationships only when you need them/);
  assert.match(html, /\/regime-v2\/#explore/);
});

test("predecessor mapping is compact, typed and transition-qualified", () => {
  const block = section("relationships", "sources");
  assert.match(block, /90\/385\/EEC \+ 93\/42\/EEC/);
  assert.match(block, /98\/79\/EC/);
  assert.match(block, /→ MDR/);
  assert.match(block, /→ IVDR/);
  assert.match(block, /transition rules preserve defined routes/i);
});

test("editorial and legal source dates stay distinct", () => {
  const block = section("sources");
  assert.match(block, /Editorial review date/);
  assert.match(block, /28 September 2026/);
  assert.match(block, /MDR consolidated version seen in EUR-Lex/);
  assert.match(block, /19 July 2026/);
  assert.match(block, /IVDR consolidated version seen in EUR-Lex/);
  assert.match(block, /10 January 2025/);
});

test("page states unresolved scope instead of claiming completeness", () => {
  assert.match(html, /selected EU-level framework/i);
  assert.match(html, /Still unresolved by this overview/);
  assert.match(html, /complete exclusions/);
  assert.match(html, /device classification/);
  assert.match(html, /personalised applicability/);
});

test("sources are grouped as core law and official context without hiding them", () => {
  const block = section("sources");
  assert.match(block, /Core law/);
  assert.match(block, /Official context and procedure/);
  assert.match(block, /European Commission EUDAMED overview/);
  assert.match(block, /COM\(2025\) 1023 — procedure 2025\/0404\(COD\)/);
  assert.doesNotMatch(block, /<details/);
});

test("boxed-dashboard patterns from the previous surface are removed", () => {
  assert.doesNotMatch(html, /state-strip/);
  assert.doesNotMatch(html, /date-grid/);
  assert.doesNotMatch(html, /class="lineage"/);
  assert.doesNotMatch(css, /\.state-strip\s*>\s*div/);
  assert.doesNotMatch(css, /\.date-grid\s+article/);
  assert.doesNotMatch(css, /\.lineage\s*>\s*div/);
  assert.match(css, /\.rule-panel[\s\S]*border-top:/);
  assert.match(css, /\.role-list > div[\s\S]*border-top:/);
});

test("desktop contents rail becomes inline contents on narrower screens", () => {
  assert.match(css, /\.page-layout[\s\S]*grid-template-columns:\s*minmax\(11rem, 14rem\)\s+minmax\(0, 48rem\)/);
  assert.match(css, /\.contents-rail[\s\S]*position:\s*sticky/);
  assert.match(css, /@media \(max-width: 64rem\)[\s\S]*\.page-layout[\s\S]*grid-template-columns:\s*1fr/);
  assert.match(css, /@media \(max-width: 64rem\)[\s\S]*\.contents-rail[\s\S]*position:\s*static/);
});

test("mobile layout reflows without horizontal scrolling and keeps generous navigation targets", () => {
  assert.match(css, /@media \(max-width: 42rem\)/);
  assert.match(css, /\.page-nav a[\s\S]*min-height:\s*2\.5rem/);
  assert.match(css, /\.role-list > div,[\s\S]*\.timeline > li,[\s\S]*\.lineage-list > div,[\s\S]*\.verification-meta > div[\s\S]*grid-template-columns:\s*1fr/);
  assert.doesNotMatch(css, /overflow-x:\s*(auto|scroll)/);
});

test("reduced-motion preference disables smooth scrolling", () => {
  assert.match(css, /@media \(prefers-reduced-motion: reduce\)[\s\S]*scroll-behavior:\s*auto/);
});

"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");
const css = fs.readFileSync(path.join(__dirname, "styles.css"), "utf8");
const app = fs.readFileSync(path.join(__dirname, "app.js"), "utf8");

function section(id, nextId) {
  const start = html.indexOf('id="' + id + '"');
  assert.notEqual(start, -1);
  const end = nextId ? html.indexOf('id="' + nextId + '"', start + 1) : html.length;
  return html.slice(start, end === -1 ? html.length : end);
}

function stripTags(value) {
  return value.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
}

test("public entry starts with purpose and visual navigation", () => {
  const heroPos = html.indexOf('class="hero"');
  const coveredPos = html.indexOf('id="covered"');
  const timelinePos = html.indexOf('id="timeline"');
  const relationshipsPos = html.indexOf('id="relationships"');
  const rolesPos = html.indexOf('id="roles"');

  assert.ok(heroPos > -1);
  assert.ok(heroPos < coveredPos && coveredPos < timelinePos);
  assert.ok(timelinePos < relationshipsPos && relationshipsPos < rolesPos);
  assert.match(html, /<h1>Medical-device legislation<\/h1>/);
  assert.match(html, /conformity before entry/i);
  assert.match(html, /traceability/i);
  assert.match(html, /post-market monitoring/i);
  assert.match(html, /not an official or live service/i);
});

test("hero visible copy stays deliberately compact", () => {
  const start = html.indexOf('<header class="hero">');
  const end = html.indexOf("</header>", start);
  const words = stripTags(html.slice(start, end)).split(/\s+/);
  assert.ok(words.length <= 155, "hero including evidence summary has " + words.length + " words");
});

test("at-a-glance layer states purpose, roles, current/upcoming state and depth without applicability claims", () => {
  const glanceStart = html.indexOf('class="glance-panel"');
  const coveredStart = html.indexOf('id="covered"');
  assert.ok(glanceStart > -1 && glanceStart < coveredStart);
  const block = html.slice(glanceStart, coveredStart);
  assert.match(block, /At a glance/i);
  assert.match(block, /Purpose/);
  assert.match(block, /Current state/);
  assert.match(block, /Change and upcoming state/);
  assert.match(block, /Roles/);
  assert.match(block, /Evidence and depth/);
  assert.match(block, /26 May 2021/);
  assert.match(block, /26 May 2022/);
  assert.match(block, /28 May 2026/);
  assert.match(block, /Regulation \(EU\) 2024\/1860/);
  assert.match(block, /still a proposal/i);
  assert.match(block, /does not assign one to you/i);
  assert.match(block, /href="#timeline"/);
  assert.match(block, /href="#roles"/);
  assert.match(block, /href="#sources"/);
  assert.doesNotMatch(block, /you are covered|you must comply|applies to you/i);
});

test("at-a-glance medical layout collapses without horizontal-scroll dependence", () => {
  assert.match(css, /\.glance-grid[\s\S]*grid-template-columns: repeat\(5/);
  assert.match(css, /@media \(max-width: 38rem\)[\s\S]*\.glance-grid[\s\S]*grid-template-columns: 1fr/);
  assert.doesNotMatch(css, /\.glance-grid[\s\S]*overflow-x:\s*(auto|scroll)/);
});

test("T2 branch distinction is explicit, concise and source-linked", () => {
  const block = section("covered", "timeline");
  assert.match(block, /MDR/);
  assert.match(block, /Regulation \(EU\) 2017\/745/);
  assert.match(block, /Medical devices for human use/i);
  assert.match(block, /IVDR/);
  assert.match(block, /Regulation \(EU\) 2017\/746/);
  assert.match(block, /manufacturer's intended purpose/i);
  assert.match(block, /eur-lex\.europa\.eu\/eli\/reg\/2017\/745/);
  assert.match(block, /eur-lex\.europa\.eu\/eli\/reg\/2017\/746/);
});

test("IVDR laboratory boundary remains visible in the public layer", () => {
  const block = section("covered", "timeline");
  assert.match(block, /Lab boundary/);
  assert.match(block, /general lab or research-use products are outside IVDR unless, in view of their characteristics, the manufacturer specifically intends/i);
  const boundaryStart = block.lastIndexOf('<p class="qualification"', block.indexOf("Lab boundary"));
  const boundaryEnd = block.indexOf("</p>", boundaryStart);
  const boundary = block.slice(boundaryStart, boundaryEnd);
  assert.doesNotMatch(boundary, /expert-only/);
});

test("timeline is a real six-milestone visual model with typed states", () => {
  const block = section("timeline", "relationships");
  assert.equal((block.match(/class="timeline-item/g) || []).length, 6);
  assert.match(block, /1990–1998/);
  assert.match(block, /2017/);
  assert.match(block, /26 May 2021/);
  assert.match(block, /26 May 2022/);
  assert.match(block, /Dec 2025/);
  assert.match(block, /28 May 2026/);
  assert.match(block, /class="timeline-item proposal"/);
  assert.match(block, /class="timeline-item operation"/);
  assert.match(block, /Proposal/);
  assert.match(block, /Operation/);
});

test("timeline preserves transition and EUDAMED qualifications", () => {
  const block = section("timeline", "relationships");
  assert.match(block, /Transition warning/);
  assert.match(block, /defined legacy routes can remain available subject to conditions/i);
  assert.match(block, /do not settle every legacy-device case/i);
  assert.match(block, /does not mean all six modules are mandatory/i);
  assert.match(block, /Spacing is schematic, not proportional to elapsed time/);
});

test("timeline evidence is available in Public without opening Expert detail", () => {
  const block = section("timeline", "relationships");
  const publicPart = block.slice(0, block.indexOf('<details class="supporting-detail expert-only">'));
  assert.match(publicPart, /health\.ec\.europa\.eu\/medical-devices-new-regulations\/overview_en/);
  assert.match(publicPart, /health\.ec\.europa\.eu\/medical-devices-eudamed\/overview_en/);
  assert.match(publicPart, /eur-lex\.europa\.eu\/procedure\/EN\/2025_404/);
});

test("law map shows hierarchy, lineage, cross-cutting change and proposal", () => {
  const block = section("relationships", "roles");
  assert.match(block, /EU medical-device framework/);
  assert.match(block, /90\/385\/EEC/);
  assert.match(block, /93\/42\/EEC/);
  assert.match(block, /98\/79\/EC/);
  assert.match(block, /Regulation 2017\/745/);
  assert.match(block, /Regulation 2017\/746/);
  assert.match(block, /Regulation \(EU\) 2024\/1860/);
  assert.match(block, /Proposal — not law/);
  assert.match(block, /COM\(2025\) 1023/);
  assert.match(block, /2025\/0404\(COD\)/);
  assert.match(block, /Editorial grouping, not a legal act/);
  assert.match(block, /Amends both MDR and IVDR/);
  assert.match(block, /categories, not individual acts/);
  assert.match(block, /schematic, not a complete act inventory/);
  assert.match(block, /eur-lex\.europa\.eu\/eli\/reg\/2024\/1860\/oj\/eng/);
  assert.match(block, /eur-lex\.europa\.eu\/procedure\/EN\/2025_404/);
});

test("selected later context is bounded and links official acts", () => {
  const block = section("relationships", "roles");
  for (const id of ["2025/2371", "2026/977", "2026/1359", "2026/1451"]) {
    assert.match(block, new RegExp(id.replace("/", "\\/")));
  }
  assert.match(block, /examples, not every later measure/i);
  assert.match(block, /Commission's wider act overview/);
});

test("relationship browser stays a deeper handoff", () => {
  const block = section("relationships", "roles");
  assert.match(block, /Explore selected relationships/);
  assert.match(block, /\/regime-v2\/#explore/);
});

test("roles are summary-first and secondary detail is disclosed natively", () => {
  const block = section("roles", "sources");
  assert.match(block, /Manufacturer/);
  assert.match(block, /Authorised representative/);
  assert.match(block, /Importer/);
  assert.match(block, /Distributor/);
  assert.match(block, /Primary conformity system/);
  assert.match(block, /Checks before market placement/);
  assert.equal((block.match(/<details>/g) || []).length, 4);
  assert.match(block, /Roles can overlap and this list is not exhaustive/);
  assert.match(block, /id="requirements"/);
  assert.doesNotMatch(html, /you are covered/i);
  assert.doesNotMatch(html, /you are exempt/i);
  assert.doesNotMatch(html, /compliant with the law/i);
});

test("proposal is never styled or described as enacted law", () => {
  assert.match(html, /Proposal — not law/);
  assert.match(html, /class="proposal-node"/);
  assert.match(css, /\.proposal-node[\s\S]*border: 1px dashed var\(--proposal\)/);
  assert.doesNotMatch(html, /COM\(2025\) 1023[^<]{0,80}(in force|binding law)/i);
});

test("public and expert modes use an accessible pressed-state switch", () => {
  assert.doesNotMatch(html, /<html[^>]*data-detail=/);
  assert.match(html, /data-view="public" aria-pressed="true"/);
  assert.match(html, /data-view="expert" aria-pressed="false"/);
  assert.match(css, /\.view-switch\s*\{\s*display: none/);
  assert.match(css, /\[data-detail\] \.view-switch \{ display: inline-flex/);
  assert.match(css, /\[data-detail="public"\] \.expert-only/);
  assert.match(app, /root\.dataset\.detail = next/);
  assert.match(app, /setAttribute\("aria-pressed"/);
});

test("native role disclosures have a visible state affordance", () => {
  assert.match(css, /\.role-table summary::after[\s\S]*content: "\+"/);
  assert.match(css, /\.role-table details\[open\] summary::after \{ content: "−"; \}/);
});

test("expert mode owns secondary metadata rather than core caveats", () => {
  assert.match(html, /class="expert-meta expert-only"/);
  assert.match(html, /MDR consolidation seen/);
  assert.match(html, /IVDR consolidation seen/);
  assert.match(html, /class="qualification"/);
  assert.match(html, /class="final-boundary"/);
});

test("sources remain directly reachable without entering expert mode", () => {
  const block = section("sources");
  assert.match(block, /MDR/);
  assert.match(block, /IVDR/);
  assert.match(block, /Framework/);
  assert.match(block, /EUDAMED/);
  assert.match(block, /eur-lex\.europa\.eu\/eli\/reg\/2017\/745/);
  assert.match(block, /eur-lex\.europa\.eu\/eli\/reg\/2017\/746/);
});

test("editorial and legal/source dates stay distinct", () => {
  const block = section("sources");
  assert.match(block, /Editorial review/);
  assert.match(block, /28 Sep 2026/);
  assert.match(block, /MDR consolidation seen/);
  assert.match(block, /19 Jul 2026/);
  assert.match(block, /IVDR consolidation seen/);
  assert.match(block, /10 Jan 2025/);
});

test("page states unresolved scope instead of claiming completeness", () => {
  assert.match(html, /This overview does not decide compliance/);
  assert.match(html, /Complete exclusions/);
  assert.match(html, /classification/);
  assert.match(html, /national rules/);
  assert.match(html, /personalised applicability/);
});

test("navigation targets the visual-first reading path", () => {
  for (const id of ["covered", "timeline", "relationships", "roles", "sources"]) {
    assert.match(html, new RegExp('href="#' + id + '"'));
    assert.match(html, new RegExp('id="' + id + '"'));
  }
  for (const id of ["dates", "changes", "developments", "requirements"]) {
    assert.match(html, new RegExp('id="' + id + '"'));
  }
});

test("mobile layout converts graphs to a single readable column", () => {
  assert.match(css, /@media \(max-width: 52rem\)/);
  assert.match(css, /@media \(max-width: 38rem\)/);
  assert.match(css, /\.timeline-track[\s\S]*grid-template-columns: 1fr/);
  assert.match(css, /\.law-map-branches \{ grid-template-columns: 1fr/);
  assert.match(css, /overflow-wrap: anywhere/);
  assert.doesNotMatch(css, /overflow-x:\s*(auto|scroll)/);
});

test("visual state is not conveyed by color alone", () => {
  assert.match(html, /<span class="timeline-type">Core law<\/span>/);
  assert.match(html, /<span class="timeline-type">Proposal<\/span>/);
  assert.match(html, /<span class="timeline-type">Operation<\/span>/);
  assert.match(html, /<span class="map-label">Proposal — not law<\/span>/);
});


test("core-act cards route to substantive internal MDR and IVDR detail views", () => {
  assert.match(html, /href="\/medical-devices\/mdr\/"/);
  assert.match(html, /href="\/medical-devices\/ivdr\/"/);
  assert.match(html, /Official MDR source/);
  assert.match(html, /Official IVDR source/);
});


test("medical overview contains no literal escaped-newline artifacts", () => {
  assert.doesNotMatch(html, /\\n/);
});

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

test("public entry begins with substantive summary rather than relationship tooling", () => {
  const summaryPos = html.indexOf('id="summary-heading"');
  const editorialPos = html.indexOf('class="editorial-note"');
  const contentsPos = html.indexOf('class="contents"');
  const coveredPos = html.indexOf('id="covered"');
  const rolesPos = html.indexOf('id="roles"');
  const datesPos = html.indexOf('id="dates"');
  const developmentsPos = html.indexOf('id="developments"');
  const relationPos = html.indexOf('id="relationships"');

  assert.ok(summaryPos > -1);
  assert.ok(summaryPos < editorialPos && editorialPos < contentsPos);
  assert.ok(contentsPos < coveredPos && coveredPos < rolesPos);
  assert.ok(rolesPos < datesPos && datesPos < developmentsPos && developmentsPos < relationPos);
  assert.match(html, /What these rules do/);
  assert.match(html, /Products: MDR and IVDR/);
  assert.match(html, /not an official EU service/);
  assert.doesNotMatch(html.slice(0, coveredPos), /Change review/);
  assert.doesNotMatch(html.slice(0, coveredPos), /Expert \/ research/);
});

test("T1 purpose can be answered from the standard summary", () => {
  const block = html.slice(html.indexOf('<section class="summary"'), html.indexOf('</section>', html.indexOf('<section class="summary"')) + 10);
  assert.match(block, /placing, supplying and putting medical devices and in-vitro diagnostic devices into service/i);
  assert.match(block, /evidence and conformity before market entry/i);
  assert.match(block, /traceability/i);
  assert.match(block, /monitoring after devices reach the market/i);
});

test("T2 branch distinction is explicit and source-linked", () => {
  const block = section("covered", "roles");
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
  const block = section("roles", "dates");
  assert.match(block, /You do not have to be the manufacturer to need these rules/);
  assert.match(block, /Importer/);
  assert.match(block, /third country on the Union market/i);
  assert.match(block, /Distributor/);
  assert.match(block, /specified checks/i);
  assert.match(block, /Do not infer exclusion from this list/);
});

test("T4 IVDR laboratory boundary is visible and rejects label-only classification", () => {
  const block = section("covered", "roles");
  assert.match(block, /Important laboratory boundary/);
  assert.match(block, /general laboratory or research-use products are outside the IVDR unless/i);
  assert.match(block, /manufacturer specifically intends them for in-vitro diagnostic examination/i);
});

test("T5 dates remain member-act dates with transition qualification and current operation", () => {
  const block = section("dates", "developments");
  assert.match(block, /26 May 2021/);
  assert.match(block, /MDR general application \/ predecessor replacement/);
  assert.match(block, /26 May 2022/);
  assert.match(block, /IVDR general application \/ predecessor replacement/);
  assert.match(block, /These dates do not settle every legacy-device case/);
  assert.match(block, /subject to conditions/i);
  assert.match(block, /Current operational milestone — 28 May 2026/);
  assert.match(block, /first four EUDAMED modules became mandatory to use/i);
  assert.match(block, /does not mean all six EUDAMED modules are already mandatory/i);
  assert.doesNotMatch(block, /regime applies from/i);
});

test("T6 proposal remains explicitly non-binding and verification is public", () => {
  assert.match(html, /Proposal — not enacted/);
  assert.match(html, /Procedure 2025\/0404\(COD\) remained ongoing at this page's 28 September 2026 evidence checkpoint/i);
  assert.match(html, /eur-lex\.europa\.eu\/procedure\/EN\/2025_404/);
  assert.match(html, /Sources and limits/);
  assert.match(html, /MDR — current EUR-Lex access/);
  assert.match(html, /IVDR — current EUR-Lex access/);
});

test("role effects are concise, source-linked, and do not become personal verdicts", () => {
  const block = section("roles", "dates");
  assert.match(block, /Manufacturer/);
  assert.match(block, /Authorised representative/);
  assert.match(block, /Importer/);
  assert.match(block, /Distributor/);
  assert.match(block, /Other affected groups/);
  for (const role of ["Manufacturer", "Importer", "Distributor"]) {
    const article = block.slice(block.indexOf(`<h3>${role}</h3>`), block.indexOf("</article>", block.indexOf(`<h3>${role}</h3>`)));
    assert.match(article, /Responsibilities:/);
    assert.match(article, /href="https:\/\//);
  }
  assert.match(block, /id="requirements"/); // Legacy fragment remains a meaningful destination.
  assert.doesNotMatch(html, /you are covered/i);
  assert.doesNotMatch(html, /you are exempt/i);
  assert.doesNotMatch(html, /compliant with the law/i);
});

test("later-development section is explicitly selected rather than falsely complete", () => {
  assert.match(html, /Selected later changes and current procedure/);
  assert.match(html, /not a complete list of post-2017 acts/i);
  assert.match(html, /2025–2026 measures continue beyond 2024\/1860/);
  assert.match(html, /Decision \(EU\) 2025\/2371/);
  assert.match(html, /Implementing Regulation \(EU\) 2026\/977/);
  assert.match(html, /Delegated Regulations \(EU\) 2026\/1359 and 2026\/1451/);
  assert.doesNotMatch(html, /What changed after the core Regulations\?/);
});

test("material qualifications are visible rather than hidden behind generic details", () => {
  assert.doesNotMatch(html, /<details/);
  assert.match(html, /Important laboratory boundary/);
  assert.match(html, /These dates do not settle every legacy-device case/);
  assert.match(html, /Proposal — not enacted/);
  assert.match(html, /Do not infer exclusion from this list/);
});

test("regime page does not invent one legal status or application date", () => {
  assert.match(html, /editorial overview of multiple legal acts/i);
  assert.doesNotMatch(html, /Regime status/);
  assert.doesNotMatch(html, /In force<\/dd>/);
  assert.doesNotMatch(html, /Regime application date/);
});

test("relationship browser is secondary and comes after substantive orientation", () => {
  const relationPos = html.indexOf('id="relationships"');
  const requirementPos = html.indexOf('id="requirements"');
  assert.ok(relationPos > requirementPos);
  assert.match(html, /Explore implementing, delegated and EUDAMED relationships/);
  assert.match(html, /\/regime-v2\/#explore/);
});

test("predecessor mapping stays typed and transition-qualified", () => {
  const block = section("relationships", "sources");
  assert.match(block, /90\/385\/EEC/);
  assert.match(block, /93\/42\/EEC/);
  assert.match(block, /98\/79\/EC/);
  assert.match(block, /→ MDR/);
  assert.match(block, /→ IVDR/);
  assert.match(block, /transition rules preserve defined routes/i);
});

test("editorial and legal/source dates stay distinct", () => {
  const block = section("sources");
  assert.match(block, /Editorial review date/);
  assert.match(block, /28 September 2026/);
  assert.match(block, /MDR consolidated version seen in EUR-Lex/);
  assert.match(block, /19 July 2026/);
  assert.match(block, /IVDR consolidated version seen in EUR-Lex/);
  assert.match(block, /10 January 2025/);
});

test("page states unresolved scope instead of claiming completeness", () => {
  assert.match(html, /Selected EU-level framework, not complete legal coverage/);
  assert.match(html, /Still unresolved by this overview/);
  assert.match(html, /complete exclusions/);
  assert.match(html, /device classification/);
  assert.match(html, /personalised applicability/);
});

test("navigation is continuous-reading and keyboard-native", () => {
  assert.match(html, /<nav class="contents" aria-label="On this page">/);
  assert.match(html, /href="#covered"/);
  assert.match(html, /href="#roles"/);
  assert.match(html, /href="#dates"/);
  assert.match(html, /href="#developments"/);
  assert.match(html, /href="#relationships"/);
  assert.match(html, /href="#sources"/);
  for (const id of ["covered", "roles", "dates", "developments", "relationships", "sources"]) {
    assert.match(html, new RegExp(`id="${id}"`));
  }
  assert.doesNotMatch(html, /aria-pressed/);
});

test("mobile layout is one-column and does not require horizontal graph scrolling", () => {
  assert.ok(css.includes("body { margin: 0; overflow-wrap: anywhere; }"));
  assert.match(css, /@media \(max-width: 42rem\)/);
  assert.match(css, /\.topbar, main \{[\s\S]*width: min\(72ch, calc\(100% - 2rem\)\)/);
  assert.doesNotMatch(css, /grid-template-columns/);
  assert.doesNotMatch(css, /overflow-x:\s*(auto|scroll)/);
});

"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const ROOT = __dirname;
const html = fs.readFileSync(path.join(ROOT, "index.html"), "utf8");
const css = fs.readFileSync(path.join(ROOT, "styles.css"), "utf8");
const js = fs.readFileSync(path.join(ROOT, "app.js"), "utf8");

function textWords(markup) {
  return markup
    .replace(/<script[\s\S]*?<\/script>/gi, " ")
    .replace(/<style[\s\S]*?<\/style>/gi, " ")
    .replace(/<[^>]+>/g, " ")
    .replace(/&[a-z0-9#]+;/gi, " ")
    .replace(/\s+/g, " ")
    .trim()
    .split(/\s+/)
    .filter(Boolean);
}

function blockForView(name) {
  const start = html.indexOf('data-view-panel="' + name + '"');
  assert.notEqual(start, -1);
  const next = html.indexOf('data-view-panel="', start + 1);
  return html.slice(start, next === -1 ? undefined : next);
}

test("v0.2 exposes four task layers but only Overview by default", () => {
  for (const view of ["overview", "explore", "changes", "expert"]) {
    assert.match(html, new RegExp('data-view-panel="' + view + '"'));
  }

  assert.match(html, /data-view-panel="overview" aria-labelledby="overview-heading">/);
  assert.match(html, /data-view-panel="explore"[^>]*hidden/);
  assert.match(html, /data-view-panel="changes"[^>]*hidden/);
  assert.match(html, /data-view-panel="expert"[^>]*hidden/);
});

test("default Overview stays below the project compression target", () => {
  const headerStart = html.indexOf('<header class="site-header">');
  const overviewStart = html.indexOf('data-view-panel="overview"');
  const exploreStart = html.indexOf('data-view-panel="explore"');
  const header = html.slice(headerStart, overviewStart);
  const overview = html.slice(overviewStart, exploreStart);
  const words = textWords(header + overview);

  assert.ok(words.length <= 450, "default-visible Overview words: " + words.length);
  assert.ok(words.length < 0.3 * 2087, "Overview should be dramatically below old ~2087-word initial state");
});

test("Overview has a bounded number of primary blocks and no research taxonomy", () => {
  const overview = blockForView("overview");
  const blocks = (overview.match(/data-primary-block/g) || []).length;
  assert.ok(blocks <= 12);

  assert.doesNotMatch(overview, /DIRECT_REVIEW/);
  assert.doesNotMatch(overview, /DOWNSTREAM_REVIEW/);
  assert.doesNotMatch(overview, /COVERAGE_GAP/);
  assert.doesNotMatch(overview, /STRUCTURAL_GAP_CANDIDATE/);
});

test("Overview preserves legally material first-impression qualifiers", () => {
  const overview = blockForView("overview");
  assert.match(overview, /Transition matters:/);
  assert.match(overview, /transitional rules preserve some effects/i);
  assert.match(overview, /Proposal — not enacted/);
  assert.match(overview, /Evidence-bounded EU-level view/);
  assert.match(overview, /Scope here:/);
  assert.match(overview, /Official MDR source/);
  assert.match(overview, /Official IVDR source/);
});

test("Overview expresses the bounded three-to-two regime spine", () => {
  const overview = blockForView("overview");
  assert.match(overview, /90\/385\/EEC/);
  assert.match(overview, /93\/42\/EEC/);
  assert.match(overview, /98\/79\/EC/);
  assert.match(overview, /Regulation \(EU\) 2017\/745/);
  assert.match(overview, /Regulation \(EU\) 2017\/746/);
  assert.match(overview, /replaced by/);
});

test("Explore shows one family at a time and keeps representative lists bounded", () => {
  assert.equal((html.match(/data-family-panel=/g) || []).length, 5);
  assert.match(html, /data-family-panel="implementing"[^>]*>/);
  assert.match(html, /data-family-panel="delegated"[^>]*hidden/);

  const implementingStart = html.indexOf('data-family-panel="implementing"');
  const delegatedStart = html.indexOf('data-family-panel="delegated"');
  const implementing = html.slice(implementingStart, delegatedStart);
  const rows = (implementing.match(/data-row-branches=/g) || []).length;
  assert.equal(rows, 6);
});

test("Explore preserves branch ownership, official sources, and local amendment notice", () => {
  assert.match(html, /data-row-branches="mdr"/);
  assert.match(html, /data-row-branches="ivdr"/);
  assert.match(html, /data-row-branches="mdr ivdr"/);
  assert.match(html, /Additional amendment:/);
  assert.match(html, /2023\/1194 amends its transitional provisions/i);
  assert.match(html, /Official source/);
  assert.match(html, /Non-binding guidance/);
});

test("branch filtering dims sibling context rather than hiding legal rows", () => {
  assert.match(js, /row\.classList\.toggle\("is-context"/);
  const applyStart = js.indexOf("function applyBranch");
  const applyEnd = js.indexOf("function showFamily", applyStart);
  const block = js.slice(applyStart, applyEnd);
  assert.doesNotMatch(block, /hidden\s*=/);
});

test("Change review uses human labels first and internal codes only in detail", () => {
  const changes = blockForView("changes");
  for (const label of ["Review directly", "Review downstream", "Context", "Stop here", "Outside sample"]) {
    assert.ok(changes.includes(label), "missing human queue label " + label);
  }
  assert.match(changes, /<details><summary>Why\?<\/summary>/);
  assert.match(changes, /DIRECT_REVIEW/);
  assert.match(changes, /NO_PROPAGATION/);
  assert.match(changes, /review candidate is not a conclusion that legal effect changed/i);
});

test("Change review contains exactly three frozen upstream controls", () => {
  assert.equal((html.match(/data-change-control=/g) || []).length, 3);
  assert.equal((html.match(/data-change-case=/g) || []).length, 3);
  assert.match(html, /2024\/1860/);
  assert.match(html, /2025\/1324/);
  assert.match(html, /2023\/1194/);
});

test("Expert layer owns research diagnostics instead of Overview", () => {
  const expert = blockForView("expert");
  assert.match(expert, /Projection diagnostics/);
  assert.match(expert, /Coverage omission/);
  assert.match(expert, /Branch coverage/);
  assert.match(expert, /Transition trigger/);
  assert.match(expert, /Structural-gap candidate/);
  assert.match(expert, /None asserted/);
  assert.match(expert, /not findings that EU law is defective/i);
});

test("task switching is hash-addressable and browser history aware", () => {
  assert.match(js, /history\.pushState/);
  assert.match(js, /location\.hash/);
  assert.match(js, /hashchange/);
  assert.match(js, /aria-pressed/);
  assert.match(html, /id="overview-heading" tabindex="-1"/);
  assert.match(html, /id="explore-heading" tabindex="-1"/);
  assert.match(html, /id="changes-heading" tabindex="-1"/);
  assert.match(html, /id="expert-heading" tabindex="-1"/);
});

test("narrow layouts become one-dimensional without horizontal graph dependence", () => {
  assert.match(css, /@media \(max-width: 58rem\)/);
  assert.match(css, /\.predecessor-row,[\s\S]*\.core-grid,[\s\S]*grid-template-columns: 1fr/);
  assert.match(css, /\.relation-list > li,[\s\S]*\.queue-list li,[\s\S]*grid-template-columns: 1fr/);
  assert.match(css, /@media \(max-width: 38rem\)/);
  assert.doesNotMatch(css, /overflow-x:\s*scroll/);
});

test("semantic statuses are not color-only", () => {
  assert.match(html, /MDR · non-binding/);
  assert.match(html, /Proposal — not enacted/);
  assert.match(html, /Review directly/);
  assert.match(html, /Stop here/);
});

test("no graph or dashboard scoring language is introduced", () => {
  assert.doesNotMatch(html, /risk score/i);
  assert.doesNotMatch(html, /severity score/i);
  assert.doesNotMatch(html, /blast-radius score/i);
  assert.doesNotMatch(html, /RELATED_TO/);
});

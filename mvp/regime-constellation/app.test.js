"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const ROOT = __dirname;
const html = fs.readFileSync(path.join(ROOT, "index.html"), "utf8");
const css = fs.readFileSync(path.join(ROOT, "styles.css"), "utf8");
const js = fs.readFileSync(path.join(ROOT, "app.js"), "utf8");

test("macro view keeps first render compressed to nine top-level objects", () => {
  const count = (html.match(/data-macro-object/g) || []).length;
  assert.equal(count, 9);
  assert.ok(count <= 10);
});

test("medical-devices lineage preserves the predecessor-to-two-branch shape", () => {
  assert.match(html, /90\/385\/EEC/);
  assert.match(html, /93\/42\/EEC/);
  assert.match(html, /98\/79\/EC/);
  assert.match(html, /Regulation \(EU\) 2017\/745/);
  assert.match(html, /Regulation \(EU\) 2017\/746/);
  assert.match(html, /replaced by MDR/i);
  assert.match(html, /replaced by IVDR/i);
});

test("macro families expose Commission-overview counts without completeness claims", () => {
  assert.match(html, /17 represented/);
  assert.match(html, /7 represented/);
  assert.match(html, /named on the Commission overview at the evidence date/i);
  assert.match(html, /not a complete map of medical-device law/i);
  assert.doesNotMatch(html, /all EU medical-device law/i);
});

test("binding law, non-binding guidance and proposal states are textually distinct", () => {
  assert.match(html, /state-binding/);
  assert.match(html, /state-nonbinding/);
  assert.match(html, /Non-binding guidance/);
  assert.match(html, /state-proposal/);
  assert.match(html, /Proposal — not enacted law/);
  assert.match(html, /CELEX:52025PC1023/);
});

test("representative children use human legal relationship labels and official links", () => {
  for (const phrase of [
    "amends MDR application dates",
    "amends MDR + IVDR transitional provisions",
    "sets EUDAMED arrangements",
    "common specifications · IVDR class D",
    "declares first four modules functional",
    "guidance for legacy-device transition"
  ]) {
    assert.ok(html.includes(phrase), "missing relation label: " + phrase);
  }
  assert.doesNotMatch(html, /RELATED_TO/);
  assert.match(html, /eur-lex\.europa\.eu/);
  assert.match(html, /health\.ec\.europa\.eu/);
});

test("gap taxonomy refuses to turn missing graph nodes into legal absence", () => {
  assert.match(html, /Coverage gap/);
  assert.match(html, /Evidence gap/);
  assert.match(html, /Review gap/);
  assert.match(html, /Structural-gap candidate/);
  assert.match(html, /No legal gap is inferred from a missing node/);
  assert.match(html, /means “recheck”, not “the child is invalid”/);
});

test("branch focus preserves sibling context rather than hiding it", () => {
  assert.match(html, /Focus MDR/);
  assert.match(html, /Focus IVDR/);
  assert.match(js, /classList\.toggle\("is-context"/);
  assert.match(js, /stays visible as sibling context/);
  assert.doesNotMatch(js, /\.hidden\s*=/);
});

test("narrow layouts collapse the constellation to a one-column reading order", () => {
  assert.match(css, /@media \(max-width: 58rem\)/);
  assert.match(css, /\.core-row,[\s\S]*grid-template-columns: 1fr/);
  assert.match(css, /\.family-grid,[\s\S]*grid-template-columns: 1fr/);
  assert.match(css, /@media \(max-width: 34rem\)/);
});

test("source and interaction controls have semantic accessibility support", () => {
  assert.match(html, /class="skip-link"/);
  assert.match(html, /aria-live="polite"/);
  assert.match(html, /aria-pressed="true"/);
  assert.match(css, /summary:focus-visible/);
  assert.match(css, /button:focus-visible/);
});

"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");
const css = fs.readFileSync(path.join(__dirname, "styles.css"), "utf8");

test("contrast identifies one delegated amending act without claiming general customs coverage", () => {
  assert.match(html, /Delegated Regulation \(EU\) 2026\/1022/);
  assert.match(html, /one bounded M2 contrast example/i);
  assert.match(html, /not comprehensive customs coverage/i);
  assert.match(html, /does not calculate customs owed/i);
});

test("scope threshold and subordinate relationship stay explicit", () => {
  assert.match(html, /intrinsic value not exceeding EUR 150/i);
  assert.match(html, /AMENDS/);
  assert.match(html, /Delegated Regulation \(EU\) 2015\/2446/);
  assert.match(html, /UNDERLYING FRAMEWORK/);
  assert.match(html, /Regulation \(EU\) No 952\/2013/);
});

test("temporal concepts are not collapsed into one effective date", () => {
  for (const required of [
    "30 Apr 2026",
    "1 Jul 2026",
    "2 Jul 2026",
    "4 Aug 2026",
    "1 Nov 2026",
    "OPTIONAL EARLY USE",
    "ENTRY INTO FORCE",
    "ANNEX APPLICATION"
  ]) assert.ok(html.includes(required), required);
  assert.match(html, /applies from 1 July 2026/i);
  assert.match(html, /entry into force occurs on the day following publication/i);
  assert.match(html, /voluntarily provide the data/i);
});

test("language-scoped correction is visible and English is not silently rewritten", () => {
  assert.match(html, /corrigendum concerns German and Dutch, not English/i);
  assert.match(html, /language-expression history is therefore not globally identical/i);
  assert.match(html, /corrigendum\/2026-08-04\/oj/);
});

test("official source and return paths remain available", () => {
  assert.match(html, /eli\/reg_del\/2026\/1022\/oj\/eng/);
  assert.match(html, /CELEX:02026R1022-20260701/);
  assert.ok(html.includes("https://eur-lex.europa.eu/eli/reg_del/2015/2446/oj/eng"));
  assert.match(html, /href="\/"/);
  assert.match(html, /href="\/#search-heading"/);
});

test("contrast reflows without horizontal-scroll dependence", () => {
  assert.match(css, /@media\(max-width:46rem\)/);
  assert.match(css, /grid-template-columns:1fr/);
  assert.doesNotMatch(css, /overflow-x:\s*scroll/);
});

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
  assert.match(html, /17 unique acts/);
  assert.match(html, /7 unique acts/);
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


function childContaining(needle) {
  const index = html.indexOf(needle);
  assert.notEqual(index, -1, "child text not found: " + needle);
  const start = html.lastIndexOf("<li", index);
  const end = html.indexOf("</li>", index);
  assert.notEqual(start, -1);
  assert.notEqual(end, -1);
  return html.slice(start, end + 5);
}

test("every represented child act exposes branch ownership", () => {
  const childLists = Array.from(html.matchAll(/<ul class="child-list">([\s\S]*?)<\/ul>/g), match => match[1]);
  assert.ok(childLists.length >= 5);

  for (const list of childLists) {
    const items = Array.from(list.matchAll(/<li([^>]*)>/g), match => match[1]);
    assert.ok(items.length > 0);
    assert.ok(
      items.every(attrs => /data-child-branches="(?:mdr|ivdr|mdr ivdr)"/.test(attrs)),
      "a child item is missing explicit branch ownership"
    );
  }
});

test("verified representative acts keep their MDR/IVDR ownership", () => {
  assert.match(childContaining("CELEX:32020R0561"), /data-child-branches="mdr"/);
  assert.match(childContaining("CELEX:32022R0112"), /data-child-branches="ivdr"/);
  assert.match(childContaining("CELEX:32023R0607"), /data-child-branches="mdr ivdr"/);
  assert.match(childContaining("CELEX:32024R1860"), /data-child-branches="mdr ivdr"/);

  assert.match(childContaining("CELEX:32022R1107"), /data-child-branches="ivdr"/);
  assert.match(childContaining("CELEX:32022R2346"), /data-child-branches="mdr"/);
  assert.match(childContaining("CELEX:32023R2713"), /data-child-branches="ivdr"/);
  assert.match(childContaining("CELEX:32026R0977"), /data-child-branches="mdr ivdr"/);

  assert.match(childContaining("CELEX:32023R2197"), /data-child-branches="mdr"/);
  assert.match(childContaining("CELEX:32023R0502"), /data-child-branches="mdr"/);
  assert.match(childContaining("CELEX:32026R1451"), /data-child-branches="mdr"/);
});

test("focus logic applies inside shared families without hiding sibling children", () => {
  assert.match(js, /querySelectorAll\("\[data-child-branches\]"\)/);
  assert.match(js, /child\.classList\.toggle\("is-context"/);
  assert.doesNotMatch(js, /child\.hidden\s*=/);
  assert.match(css, /\.child-list li\.is-context/);
  assert.match(css, /sibling context/);
});

test("EUDAMED lane declares cross-list reuse rather than double-counting it", () => {
  assert.match(html, /Cross-cutting lens:/);
  assert.match(html, /navigation cross-reference, not an additional instrument count/i);
  const eudamed2078 = childContaining('data-cross-reference="implementing"');
  assert.match(eudamed2078, /CELEX:32021R2078/);
  assert.match(eudamed2078, /cross-reference/i);
});

test("family counts are frozen source-date summaries with explicit counting semantics", () => {
  assert.match(html, /data-count-family="implementing" data-count-value="17"/);
  assert.match(html, /data-count-family="delegated" data-count-value="7"/);
  assert.match(html, /checked <time datetime="2026-09-27">27 September 2026<\/time>/);
  assert.match(html, /frozen navigation count, not a completeness claim/i);
  assert.match(html, /2025\/788 as a separate amending act/i);
  assert.match(html, /2022 report because it is not a delegated regulation/i);
});

test("proposal lane remains procedurally separate from enacted and future-fixed law", () => {
  assert.match(html, /Proposal — not enacted law/);
  assert.match(html, /submitted it to the European Parliament and Council/i);
  assert.match(html, /proposal\/procedure item, not enacted law/i);
  assert.match(html, /CELEX:52025PC1023/);
});

test("guidance sample remains explicitly non-binding and branch-specific", () => {
  const guidance = childContaining("MDCG 2021-25 rev.1");
  assert.match(guidance, /data-child-branches="mdr"/);
  assert.match(guidance, /MDR · non-binding/);
  assert.match(html, /Non-binding guidance/);
});

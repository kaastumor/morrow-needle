"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const {ACTS} = require("./acts.js");
const {renderActPage} = require("./render.js");

test("WP4 owns exactly MDR and IVDR core-act detail contracts", () => {
  assert.deepEqual(Object.keys(ACTS), ["mdr", "ivdr"]);
  assert.equal(ACTS.mdr.citation, "Regulation (EU) 2017/745");
  assert.equal(ACTS.ivdr.citation, "Regulation (EU) 2017/746");
});

test("source/version identity is explicit and not collapsed into a generic current badge", () => {
  assert.equal(ACTS.mdr.consolidationDate, "2026-07-19");
  assert.equal(ACTS.ivdr.consolidationDate, "2025-01-10");
  for (const act of Object.values(ACTS)) {
    assert.match(act.consolidatedSource, /CELEX:02017R074[56]-/);
    assert.match(act.originalSource, /eur-lex\.europa\.eu/);
  }
});

test("the #492 temporal threats are structurally represented", () => {
  for (const act of Object.values(ACTS)) {
    const types = act.timeline.map(item => item[0]);
    assert.ok(types.includes("GENERAL_APPLICATION"));
    assert.ok(types.includes("OPERATIONAL_TRIGGER"));
    assert.ok(types.includes("FUTURE_TRANSITION"));
    assert.ok(act.timeline.filter(item => item[0] === "FUTURE_TRANSITION").every(item => item[1] > "2026-10-01"));
  }
});

test("roles stay orientation and retain their article owners", () => {
  for (const act of Object.values(ACTS)) {
    assert.deepEqual(act.roles.map(row => row[1]), ["Article 10", "Article 11", "Article 13", "Article 14"]);
  }
});

test("rendered pages keep national/applicability and compliance boundaries explicit", () => {
  for (const act of Object.values(ACTS)) {
    const html = renderActPage(act);
    assert.match(html, /does not settle national rules, enforcement choices or a reader's individual applicability/i);
    assert.match(html, /does not decide compliance/i);
    assert.match(html, /general application date does not replace provision-specific dates/i);
    assert.match(html, /future transition is not shown as current state/i);
  }
});

test("rendered act pages expose a bounded at-a-glance layer before deeper navigation", () => {
  for (const act of Object.values(ACTS)) {
    const html = renderActPage(act);
    const glance = html.indexOf('class="act-glance"');
    const nav = html.indexOf('class="act-local-nav"');
    assert.ok(glance > -1 && glance < nav);
    const block = html.slice(glance, nav);
    assert.match(block, /At a glance/i);
    assert.match(block, /Purpose/);
    assert.match(block, /Current state/);
    assert.match(block, /What changed/);
    assert.match(block, /Roles represented/);
    assert.match(block, /Upcoming state/);
    assert.match(block, /Evidence and depth/);
    assert.match(block, /does not assign one to you/i);
    assert.match(block, /href="#scope"/);
    assert.match(block, /href="#roles"/);
    assert.match(block, /href="#time"/);
    assert.match(block, /href="#relationships"/);
    assert.match(block, /href="#sources"/);
    assert.doesNotMatch(block, /applies to you|you must comply/i);
  }
  assert.match(renderActPage(ACTS.mdr), /31 Dec 2028/);
  assert.match(renderActPage(ACTS.ivdr), /31 Dec 2029/);
});

test("rendered pages preserve typed relationships and connected product navigation", () => {
  for (const act of Object.values(ACTS)) {
    const html = renderActPage(act);
    assert.match(html, /AMENDED BY|REPLACES/);
    assert.match(html, /href="\/medical-devices\/"/);
    assert.match(html, /href="\/#search-heading"/);
    assert.match(html, /href="\/regime-v2\/#explore"/);
    assert.match(html, /href="\/regime-v2\/#changes"/);
  }
});


test("IVDR keeps 2024/1860 entry-into-force separate from Article 10a application", () => {
  const transition = ACTS.ivdr.timeline.find(row => row[0] === "AMENDMENT_EFFECT");
  const supply = ACTS.ivdr.timeline.find(row => row[0] === "AMENDMENT_APPLICATION");
  assert.deepEqual(transition.slice(0, 2), ["AMENDMENT_EFFECT", "2024-07-09"]);
  assert.deepEqual(supply.slice(0, 2), ["AMENDMENT_APPLICATION", "2025-01-10"]);
  assert.match(transition[3], /transition framework/i);
  assert.match(supply[3], /Article 10a/i);
});


test("WP5 deep links expose time relationships evidence and return paths", () => {
  for (const act of Object.values(ACTS)) {
    const html = renderActPage(act);
    for (const fragment of ["time", "relationships", "sources"]) {
      assert.match(html, new RegExp('href="#' + fragment + '"'));
      assert.match(html, new RegExp('id="' + fragment + '"'));
    }
    assert.match(html, /href="\/medical-devices\/"/);
    assert.match(html, /href="\/#search-heading"/);
  }
});

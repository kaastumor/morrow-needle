"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const {buildParticipantPages, OUTPUTS} = require("./build-participant-pages.js");

const DIR = __dirname;

function externalUrls(html) {
  return [...html.matchAll(/href="(https:\/\/[^"]+)"/g)]
    .map(match => match[1])
    .filter(url => !url.includes("github.com/kaastumor/morrow-needle/issues/494"));
}

test("participant pages preserve treatment facts but hide research/comparison routes", () => {
  const tmp = fs.mkdtempSync(path.join(require("node:os").tmpdir(), "needle-494-participants-"));
  const {pages} = buildParticipantPages(tmp);

  for (const html of Object.values(pages)) {
    for (const fact of [
      "2022/0092(COD)",
      "2023/0085(COD)",
      "P9_TA(2024)0018",
      "P9_TA(2024)0131",
      "593 for / 21 against / 14 abstained",
      "467 for / 65 against / 74 abstained",
      "This vote covered the package; it does not establish a separate vote on this provision"
    ]) {
      assert.ok(html.includes(fact), fact);
    }

    for (const forbidden of [
      'href="specimen.html"',
      'href="baseline.html"',
      'href="evidence.md"',
      'href="protocol.md"',
      "github.com/kaastumor/morrow-needle/issues/494"
    ]) {
      assert.equal(html.includes(forbidden), false, forbidden);
    }

    assert.match(html, /Needle #494 reading study/);
  }

  assert.ok(fs.existsSync(path.join(tmp, OUTPUTS.a)));
  assert.ok(fs.existsSync(path.join(tmp, OUTPUTS.b)));
  fs.rmSync(tmp, {recursive: true, force: true});
});

test("participant arms expose the same unique external source destinations", () => {
  const tmp = fs.mkdtempSync(path.join(require("node:os").tmpdir(), "needle-494-participants-"));
  const {pages} = buildParticipantPages(tmp);
  const a = [...new Set(externalUrls(pages.a))].sort();
  const b = [...new Set(externalUrls(pages.b))].sort();
  assert.deepEqual(a, b);
  assert.equal(a.length, 12);
  fs.rmSync(tmp, {recursive: true, force: true});
});

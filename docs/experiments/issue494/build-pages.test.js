const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const dir = __dirname;
const pages = ['specimen', 'baseline'].map(name => fs.readFileSync(path.join(dir, `${name}.html`), 'utf8'));

test('both arms preserve exact decision identities, limits and source access', () => {
  for (const html of pages) {
    for (const identity of ['2022/0092(COD)', '2023/0085(COD)', 'P9_TA(2024)0018', 'P9_TA(2024)0131', 'Am 91', '593 for / 21 against / 14 abstained', '467 for / 65 against / 74 abstained']) {
      assert.ok(html.includes(identity), identity);
    }
    for (const section of [...html.matchAll(/<section class="decision" id="(january|march)"[\s\S]*?<\/section>/g)]) {
      assert.match(section[0], /This vote covered the package; it does not establish a separate vote on this provision/);
      assert.match(section[0], /Other amendments and ballots were not exhaustively searched or individually recorded/);
      assert.match(section[0], /<table>/);
    }
    assert.equal((html.match(/class="decision"/g) || []).length, 2);
    assert.equal((html.match(/<tr>\s*<th scope="row">/g) || []).length, 16);
    assert.match(html, /Hohlmeier appears as PPE \/ FOR/);
    assert.match(html, /Licensing compatibility is unresolved/);
    assert.doesNotMatch(html, /<script|I support|I oppose|I have no position/);
    for (const url of ['https://eur-lex.europa.eu/eli/C/2025/617/oj/eng', 'https://eur-lex.europa.eu/eli/C/2025/1699/oj/eng', 'https://howtheyvote.eu/votes/163059', 'https://howtheyvote.eu/votes/166226']) assert.ok(html.includes(url));
  }
});

test('recorded group distributions match selected ballot totals', () => {
  for (const html of pages) {
    for (const [section, expected] of [['january', [593,21,14]], ['march', [467,65,74]]]) {
      const body = html.match(new RegExp(`<section class="decision" id="${section}"[\\s\\S]*?<\\/section>`))[0];
      const rows = [...body.matchAll(/<tr>\s*<th scope="row">[^<]+<\/th>\s*<td>(\d+)<\/td>\s*<td>(\d+)<\/td>\s*<td>(\d+)<\/td>\s*<\/tr>/g)];
      assert.equal(rows.length, 8);
      assert.deepEqual([1,2,3].map(i => rows.reduce((n, row) => n + Number(row[i]), 0)), expected);
    }
  }
});

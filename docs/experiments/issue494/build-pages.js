// Frozen, source-linked development views for #494. No live vote ingestion.
const fs = require('node:fs');
const path = require('node:path');
const dir = __dirname;
const links = {
  janPublication: 'https://eur-lex.europa.eu/eli/C/2025/617/oj/eng',
  janMinutes: 'https://www.europarl.europa.eu/doceo/document/PV-9-2024-01-17-ITM-008-04_EN.html',
  janText: 'https://www.europarl.europa.eu/doceo/document/TA-9-2024-0018_EN.html',
  mayText: 'https://www.europarl.europa.eu/doceo/document/TA-9-2023-0201_EN.html',
  janProvider: 'https://howtheyvote.eu/votes/163059',
  marPublication: 'https://eur-lex.europa.eu/eli/C/2025/1699/oj/eng',
  marText: 'https://www.europarl.europa.eu/doceo/document/TA-9-2024-0131_EN.html',
  marProvider: 'https://howtheyvote.eu/votes/166226',
  relationship: 'https://www.europarl.europa.eu/news/en/press-room/20240112IPR16772',
  methodology: 'https://howtheyvote.eu/about'
};
const a = (url, label) => `<a href="${url}">${label}</a>`;
const groups = [
  ['ECR', 46, 5, 7, 2, 16, 44],
  ['ID', 36, 13, 1, 15, 33, 1],
  ['NI', 41, 0, 5, 15, 9, 13],
  ['PPE', 155, 0, 0, 141, 3, 6],
  ['Renew', 95, 3, 0, 77, 3, 6],
  ['S&amp;D', 125, 0, 0, 124, 0, 2],
  ['The Left', 33, 0, 1, 29, 1, 2],
  ['Verts/ALE', 62, 0, 0, 64, 0, 0]
];
function table(which) {
  const offset = which === 'january' ? 1 : 4;
  return `<div class="table-wrap"><table><caption>Historical published group-label distribution for this selected roll call</caption><thead><tr><th scope="col">Published label</th><th scope="col">For</th><th scope="col">Against</th><th scope="col">Abstained</th></tr></thead><tbody>${groups.map(row => `<tr><th scope="row">${row[0]}</th>${row.slice(offset, offset + 3).map(n => `<td>${n}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
}
const common = {
  scope: `<p><strong>Selection:</strong> selected historical examples from two legislative files, one package-level roll call per file. These dates do not bound a complete search. Other within-file ballots and amendments were not exhaustively searched or individually recorded. This is navigation, not a complete voting history or a measure of equivalent political positions.</p>`,
  groups: `<p class="small">These are historical source labels, not present-day affiliations. NI means non-attached members, not a political group. EP groups are not national or European political parties. Counts preserve splits; they do not identify individual choices, motives, present positions or member switching. No pooled rate is warranted.</p>`,
  relation: `<p>${a(links.relationship, 'The Parliament’s January announcement')} connects the two files. The January package also covers durability and guarantee information; the March proposal concerns substantiation, communication and verification of explicit environmental claims. The connection supports exploration, not equivalent political-position measurement. Nature restoration 2022/0195(COD) is excluded from this claims-specific set as a broad environmental-topic neighbour; this one exclusion does not test difficult near-neighbours.</p>`,
  rights: `<p>Source-text transfers and aggregate recounts are reported in ${a('https://github.com/kaastumor/morrow-needle/issues/494', '#494')}; original source bytes, visual checks, complete member identities/dated parties and correction history are not authenticated here. ${a(links.methodology, 'HowTheyVote’s methodology')} documents omitted correction display; its amendment-display description should be read alongside the March page’s visible amendment link. No reader benefit or current political stance has been established.</p><p><strong>Source and reuse boundary:</strong> The displayed aggregate distributions are presented from the reported European Parliament primary-text recounts in #494. HowTheyVote is linked as an external comparator/navigation aid; this artifact does not import its downloadable/API database or vote summaries. ${a('https://data.europarl.europa.eu/en/discover/rules-on-the-european-parliaments-open-data', 'Parliament open-data rules')} and the ${a('https://www.europarl.europa.eu/legal-notice/en', 'Parliament legal notice')} require source-aware reuse and can have item-specific conditions. Needle remains INSPECTABLE_ONLY_FOR_NOW, so public redistribution still requires exact source-item attribution/licensing review.</p>`
};
function result(which) {
  const jan = which === 'january';
  const title = jan ? '17 January 2024 · consumer information package' : '12 March 2024 · Green Claims proposal';
  const identity = jan
    ? `<dl><dt>Institution</dt><dd>European Parliament, ninth term, plenary</dd><dt>File / report</dt><dd>2022/0092(COD) / A9-0099/2023</dd><dt>Exact ballot</dt><dd>Provisional agreement — Am 91, roll call</dd><dt>Stage / text</dt><dd>First reading closed; P9_TA(2024)0018</dd><dt>Recorded result</dt><dd>593 for / 21 against / 14 abstained</dd></dl>`
    : `<dl><dt>Institution</dt><dd>European Parliament, ninth term, plenary</dd><dt>File / report</dt><dd>2023/0085(COD) / A9-0056/2024</dd><dt>Exact ballot</dt><dd>Commission proposal after amendments, roll call</dd><dt>Stage / text</dt><dd>Parliament first-reading position; P9_TA(2024)0131, not final EU adoption</dd><dt>Recorded result</dt><dd>467 for / 65 against / 74 abstained</dd></dl>`;
  const sources = jan
    ? `<p><strong>Check the record:</strong> ${a(links.janPublication, 'official OJ C/2025/617')} (minutes 8.4 p.14; results item 4 p.35; roll call 4.1 pp.50–51); ${a(links.janMinutes, 'Parliament minutes')}; ${a(links.janText, 'January adopted text P9_TA(2024)0018')}; ${a(links.janProvider, 'HowTheyVote result and group view')}. ${a(links.mayText, 'P9_TA(2023)0201')} belongs to May 2023 same-file history, not this January text.</p>`
    : `<p><strong>Check the record:</strong> ${a(links.marPublication, 'official OJ C/2025/1699')} (minutes 8.12; results item 12; roll call 10.3); ${a(links.marText, 'Parliament text P9_TA(2024)0131')}; ${a(links.marProvider, 'HowTheyVote result and group view')}.</p>`;
  const limits = jan
    ? `<p><strong>Evidence level:</strong> #494 reports a manual primary-PDF-text transfer and recount of 628 distinct name labels matching these totals and eight rows. This is not authenticated original PDF bytes, visual verification, a provider per-member audit or an official-ID/party roster. No supplement appeared in that transferred roll-call section; complete correction coverage remains unknown.</p><p><strong>Within-file coverage:</strong> May 2023 is identified as earlier same-file history. Other amendments and ballots were not exhaustively searched or individually recorded.</p>`
    : `<p><strong>Evidence level:</strong> #494 reports a manual primary-HTML-text transfer and recount of 606 distinct name labels matching these totals and eight rows. This is not authenticated original HTML bytes, visual verification, a provider per-member audit or an official-ID/party roster.</p><p><strong>Supplement:</strong> Hohlmeier appears as PPE / FOR in the recorded ballot and under “Corrections to votes and voting intentions: Against” in the publication. The entry’s administrative subtype and motive are unknown. It does not replace the recorded ballot or add another ballot to the totals.</p><p><strong>Within-file coverage:</strong> Am 153 lapsed; Am 46D has an aggregate-only electronic result, so neither supplies an individual roll call here. Other amendments and ballots were not exhaustively searched or individually recorded.</p>`;
  return `<section class="decision" id="${which}" aria-labelledby="${which}-title"><h2 id="${which}-title">${title}</h2><p class="question">What was recorded on this package ballot?</p><p class="notice"><strong>Package versus provision:</strong> This vote covered the package; it does not establish a separate vote on this provision. No clause-specific amendment ballot is shown.</p>${identity}${table(which)}${common.groups}${sources}${limits}</section>`;
}
function page(kind) {
  const linked = kind === 'specimen';
  const title = linked ? 'Selected recorded decisions' : 'Official and provider handoff';
  const intro = linked
    ? `<p class="lede">What did the European Parliament record on the selected package decisions concerning consumer-facing environmental claims, and how are the two files related?</p><p>Open one decision at a time. ${a('#january', 'January decision')} · ${a('#march', 'March related decision')}.</p>`
    : `<p class="lede">For the selected consumer environmental-claims question, use the exact official publication and adopted text alongside the existing provider’s group view. The answer and qualifications are supplied below so the handoff is usable without reconstructing the join from scratch.</p>`;
  const order = linked
    ? `${result('january')}<section class="handoff"><h2>Why the March file is here</h2>${common.relation}</section>${result('march')}`
    : `<section class="handoff"><h2>Source route and file relationship</h2><p>January: ${a(links.janPublication, 'official publication')} · ${a(links.janText, 'exact adopted text')} · ${a(links.janProvider, 'provider group view')}. March: ${a(links.marPublication, 'official publication')} · ${a(links.marText, 'Parliament first-reading text')} · ${a(links.marProvider, 'provider group view')}.</p>${common.relation}</section>${result('january')}${result('march')}`;
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>${title} · Needle #494</title><link rel="stylesheet" href="style.css"></head><body><header><nav aria-label="Comparison pages">${a('specimen.html', 'Linked specimen')} ${a('baseline.html', 'Official/provider handoff')} ${a('evidence.md', 'Evidence ledger')} ${a('protocol.md', 'Reading protocol')}</nav><h1>${title}</h1><p>Needle #494 · frozen development specimen · 29 September 2026</p></header><main>${intro}<aside class="notice" aria-label="Selection boundary"><h2>What is selected</h2>${common.scope}</aside>${order}<section class="handoff"><h2>What remains unknown</h2>${common.rights}</section></main><footer><p>Printed, linked and fragment-shared result sections retain their package/provision and within-file-coverage caveats. This is historical decision navigation, not a political recommendation.</p></footer></body></html>\n`;
}
for (const kind of ['specimen', 'baseline']) {
  fs.writeFileSync(path.join(dir, `${kind}.html`), page(kind).replace(/></g, '>\n<'));
}

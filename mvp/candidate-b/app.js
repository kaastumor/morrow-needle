"use strict";

const DEFAULT_AS_OF = "2026-09-26";

const CASES = Object.freeze([
  Object.freeze({
    id: "gar-en497",
    regime: "Gas Appliances Regulation",
    regimeShort: "GAR",
    standard: "EN 497:2022",
    aliases: ["EN 497", "GAR"],
    supportedFrom: "2026-07-23",
    supportedThrough: "2026-09-26",
    fixture: "../../fixtures/dependency/gar-en497-authoritative-dynamic-set-v0.1.json"
  }),
  Object.freeze({
    id: "machinery-en50434",
    regime: "Machinery Directive",
    regimeShort: "Machinery",
    standard: "EN 50434:2014",
    aliases: ["EN 50434", "2006/42/EC"],
    supportedFrom: "2026-01-12",
    supportedThrough: "2026-09-26",
    fixture: "../../fixtures/dependency/machinery-en50434-restriction-v0.1.json"
  }),
  Object.freeze({
    id: "toy-en71",
    regime: "Toy Safety Directive",
    regimeShort: "Toy Safety",
    standard: "EN 71-1:2014+A1:2018",
    aliases: ["EN 71-1", "EN 71", "2009/48/EC"],
    supportedFrom: "2025-09-09",
    supportedThrough: "2026-09-26",
    fixture: "../../fixtures/dependency/toy-safety-authoritative-dynamic-set-v0.1.json"
  }),
  Object.freeze({
    id: "lvd-en60335-2-14",
    regime: "Low Voltage Directive",
    regimeShort: "LVD",
    standard: "EN 60335-2-14:2006",
    aliases: ["EN 60335-2-14", "2014/35/EU", "kitchen machines"],
    supportedFrom: "2025-07-17",
    supportedThrough: "2026-09-26",
    fixture: "../../fixtures/dependency/lvd-en60335-2-14-formal-nonpublication-v0.1.json"
  }),
  Object.freeze({
    id: "lvd-en60335-2-60",
    regime: "Low Voltage Directive",
    regimeShort: "LVD",
    standard: "EN 60335-2-60:2003",
    aliases: ["EN 60335-2-60", "2014/35/EU", "whirlpool baths", "spas"],
    supportedFrom: "2025-07-18",
    supportedThrough: "2027-01-18",
    fixture: "../../fixtures/dependency/lvd-en60335-2-60-scheduled-withdrawal-v0.1.json"
  })
]);

function parseDate(value) {
  const date = new Date(value + "T00:00:00Z");
  if (Number.isNaN(date.valueOf())) throw new Error("invalid date");
  return date;
}

function assertSupportedDate(caseMeta, asOfValue) {
  if (asOfValue < caseMeta.supportedFrom || asOfValue > caseMeta.supportedThrough) {
    throw new Error(
      `date outside frozen evidence window ${caseMeta.supportedFrom} to ${caseMeta.supportedThrough}`
    );
  }
}

function normalizeLookup(value) {
  return String(value || "")
    .trim()
    .toUpperCase()
    .replace(/\s+/g, " ");
}

function findCases(query) {
  const needle = normalizeLookup(query);
  if (!needle) return [];

  const ranked = CASES.map(entry => {
    const standard = normalizeLookup(entry.standard);
    const aliases = entry.aliases.map(normalizeLookup);
    const haystack = normalizeLookup(
      [entry.standard, entry.regime, entry.regimeShort, ...entry.aliases].join(" ")
    );

    let rank = 3;
    if (standard === needle) rank = 0;
    else if (aliases.includes(needle)) rank = 1;
    else if (standard.includes(needle) || haystack.includes(needle)) rank = 2;

    return {entry, rank};
  })
    .filter(item => item.rank < 3)
    .sort((a, b) => a.rank - b.rank || a.entry.standard.localeCompare(b.entry.standard));

  return ranked.map(item => item.entry);
}

function transitionMatches(transition, standard) {
  return transition.member.identifiers.some(
    item => item.scheme === "HARMONISED_STANDARD" && item.value === standard
  );
}

function projectStatus(record, standard, asOfValue) {
  const asOf = parseDate(asOfValue);
  const transitions = record.transitions
    .filter(item => transitionMatches(item, standard))
    .slice()
    .sort((a, b) => a.effective_from.localeCompare(b.effective_from));

  if (!transitions.length) throw new Error("standard not found in canonical record");

  const past = transitions.filter(item => parseDate(item.effective_from) <= asOf);
  const future = transitions.filter(item => parseDate(item.effective_from) > asOf);
  const latest = past.at(-1) || null;
  const next = future[0] || null;
  const state = latest ? latest.after : transitions[0].before;

  let ojState;
  let consequence;
  if (state.membership === "NOT_INCLUDED") {
    ojState = "NOT_CITED";
    consequence = "NOT_AVAILABLE_VIA_THIS_OJ_REFERENCE";
  } else if (state.status === "RESTRICTED") {
    ojState = "CITED_WITH_RESTRICTION";
    consequence = "RESTRICTED_TO_STATED_SCOPE";
  } else {
    ojState = "CITED";
    consequence = "AVAILABLE_WITHIN_COVERED_SCOPE";
  }

  return Object.freeze({asOf: asOfValue, state, ojState, consequence, latest, next});
}

function statusLabel(value) {
  return {
    NOT_CITED: "Not cited",
    CITED_WITH_RESTRICTION: "Cited — restriction applies",
    CITED: "Cited"
  }[value] || value;
}

function consequenceLabel(value) {
  return {
    NOT_AVAILABLE_VIA_THIS_OJ_REFERENCE:
      "Presumption of conformity is not available via this OJ reference.",
    RESTRICTED_TO_STATED_SCOPE:
      "Presumption of conformity is limited by the stated restriction.",
    AVAILABLE_WITHIN_COVERED_SCOPE:
      "Presumption of conformity remains available within the covered scope."
  }[value] || value;
}

function sourceHref(source) {
  if (!source || typeof source.identifier !== "string") return null;
  if (source.source_type === "EUR_LEX" || source.source_type === "OFFICIAL_JOURNAL") {
    return "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=" + encodeURIComponent(source.identifier);
  }
  return null;
}

function collectEvidence(record, projection) {
  const refs = [];
  for (const source of record.legal_basis_refs || []) refs.push(source);
  if (projection.latest) refs.push(...projection.latest.source_refs);
  if (projection.next) refs.push(...projection.next.source_refs);

  const seen = new Set();
  return refs.filter(source => {
    const key = [source.identifier, source.locator].join("|");
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
  });
}

function eventBlock(title, event, modifier = "") {
  if (!event) return "";
  return `<section class="event ${escapeHtml(modifier)}">
    <p class="section-kicker">${escapeHtml(title)}</p>
    <p><strong>Effective:</strong> ${escapeHtml(event.effective_from)}</p>
    <p>${escapeHtml(event.scope.statement)}</p>
  </section>`;
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function renderCard(record, caseMeta, projection) {
  const dependency = record.dependencies[0];
  const evidence = collectEvidence(record, projection);
  const evidenceHtml = evidence.map(source => {
    const href = sourceHref(source);
    const label = `${source.identifier} — ${source.locator}`;
    return href
      ? `<li><a href="${escapeHtml(href)}" target="_blank" rel="noreferrer">${escapeHtml(label)}</a></li>`
      : `<li>${escapeHtml(label)}</li>`;
  }).join("");

  const guardrails = record.forbidden_inferences
    .map(item => `<li>${escapeHtml(item)}</li>`)
    .join("");

  return `
    <div class="result-heading">
      <div>
        <p class="section-kicker">${escapeHtml(caseMeta.regime)}</p>
        <h2>${escapeHtml(caseMeta.standard)}</h2>
      </div>
      <span class="status-badge" data-status="${escapeHtml(projection.ojState)}">${escapeHtml(statusLabel(projection.ojState))}</span>
    </div>

    <div class="freshness" role="note">
      <strong>Frozen evidence — not live monitoring.</strong>
      <span>Supported dates for this demonstration record: ${escapeHtml(caseMeta.supportedFrom)} to ${escapeHtml(caseMeta.supportedThrough)}.</span>
    </div>

    <dl class="status-grid">
      <dt>Status date</dt><dd>${escapeHtml(projection.asOf)}</dd>
      <dt>Legal basis</dt><dd>${escapeHtml(dependency.governing_rule.act_id)} · ${escapeHtml(dependency.governing_rule.provision)}</dd>
      <dt>Presumption effect</dt><dd>${escapeHtml(consequenceLabel(projection.consequence))}</dd>
    </dl>

    ${eventBlock("Current-state event", projection.latest)}
    ${eventBlock("Already-fixed next event", projection.next, "event-next")}

    <section class="evidence-section">
      <h3>Official evidence</h3>
      <p>Open the binding source before relying on this status in a real conformity decision.</p>
      <ul class="evidence-list">${evidenceHtml}</ul>
    </section>

    <details class="guardrails">
      <summary>What this status does not establish</summary>
      <ul class="guardrail-list">${guardrails}</ul>
    </details>
  `;
}

async function loadCase(caseMeta, asOfValue, fetcher = fetch) {
  assertSupportedDate(caseMeta, asOfValue);
  const response = await fetcher(caseMeta.fixture, {cache: "no-store"});
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const record = await response.json();
  return {record, projection: projectStatus(record, caseMeta.standard, asOfValue)};
}

function applyDateBounds(caseMeta, dateInput) {
  dateInput.min = caseMeta.supportedFrom;
  dateInput.max = caseMeta.supportedThrough;

  const preferred = DEFAULT_AS_OF >= caseMeta.supportedFrom && DEFAULT_AS_OF <= caseMeta.supportedThrough
    ? DEFAULT_AS_OF
    : caseMeta.supportedThrough;

  if (!dateInput.value || dateInput.value < caseMeta.supportedFrom || dateInput.value > caseMeta.supportedThrough) {
    dateInput.value = preferred;
  }
}

function renderMatches(matches, results) {
  if (!matches.length) {
    results.innerHTML = `<p class="empty-state">No frozen demonstration record matches that lookup. Try one of the examples below.</p>`;
    results.hidden = false;
    return;
  }

  results.innerHTML = matches.map(entry => `
    <button class="lookup-result" type="button" data-case-id="${escapeHtml(entry.id)}">
      <strong>${escapeHtml(entry.standard)}</strong>
      <span>${escapeHtml(entry.regime)}</span>
    </button>
  `).join("");
  results.hidden = false;
}

function wireCaseButtons(container, onSelect) {
  container.addEventListener("click", event => {
    const button = event.target.closest("[data-case-id]");
    if (!button) return;
    const selected = CASES.find(entry => entry.id === button.dataset.caseId);
    if (selected) onSelect(selected);
  });
}

function boot() {
  const form = document.querySelector("#lookup-form");
  const input = document.querySelector("#standard-query");
  const dateInput = document.querySelector("#as-of");
  const results = document.querySelector("#lookup-results");
  const examples = document.querySelector("#example-standards");
  const status = document.querySelector("#load-status");
  const card = document.querySelector("#status-card");

  let activeCase = null;

  async function selectCase(caseMeta) {
    activeCase = caseMeta;
    input.value = caseMeta.standard;
    applyDateBounds(caseMeta, dateInput);
    dateInput.disabled = false;
    results.hidden = true;
    card.hidden = true;
    status.textContent = "Loading frozen official-evidence record…";

    try {
      const {record, projection} = await loadCase(caseMeta, dateInput.value);
      card.innerHTML = renderCard(record, caseMeta, projection);
      card.hidden = false;
      status.textContent = "Status projected from the frozen official-evidence record.";
    } catch (error) {
      status.textContent = `Status unavailable: ${error.message}`;
    }
  }

  form.addEventListener("submit", event => {
    event.preventDefault();
    const matches = findCases(input.value);
    if (matches.length === 1) {
      selectCase(matches[0]);
      return;
    }
    renderMatches(matches, results);
  });

  input.addEventListener("input", () => {
    const matches = findCases(input.value);
    if (!input.value.trim()) {
      results.hidden = true;
      return;
    }
    renderMatches(matches, results);
  });

  dateInput.addEventListener("change", () => {
    if (activeCase) selectCase(activeCase);
  });

  wireCaseButtons(results, selectCase);
  wireCaseButtons(examples, selectCase);

  status.textContent = "Enter a known standard reference or choose an example.";
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = {
    CASES,
    DEFAULT_AS_OF,
    parseDate,
    assertSupportedDate,
    normalizeLookup,
    findCases,
    projectStatus,
    statusLabel,
    consequenceLabel,
    sourceHref,
    collectEvidence
  };
}
if (typeof document !== "undefined") {
  boot();
}

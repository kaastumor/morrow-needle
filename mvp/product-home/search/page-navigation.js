/* Locators for existing authored pages. Never legal answers or source evidence. */
(function (root, factory) {
  const api = factory(typeof module === "object" && module.exports ? require("./search.js") : root.NeedleSearch);
  if (typeof module === "object" && module.exports) module.exports = api;
  else root.NeedlePageNavigation = api;
})(globalThis, function (Search) {
  "use strict";

  const pages = Object.freeze({
    medical: {label: "Medical-device legislation overview", href: "/medical-devices/"},
    mdr: {label: "Medical devices (MDR)", href: "/medical-devices/mdr/"},
    ivdr: {label: "In-vitro diagnostics (IVDR)", href: "/medical-devices/ivdr/"},
    customs: {label: "Low-value import customs changes", href: "/customs-low-value-imports/"}
  });
  const identifiers = Object.freeze({"2017/745": "mdr", "2017/746": "ivdr", "2026/1022": "customs"});
  const allowedStates = new Set(["RESULTS", "REFERENCE_MENTIONS_ONLY", "REFERENCE_NOT_IN_SNAPSHOT", "NO_SUPPORTED_TERMS", "OUTSIDE_MAINTAINED_COVERAGE", "CLARIFY"]);
  const outsideSubject = /\b(?:NIS2|AI[\s-]+Act|artificial[\s-]+intelligence|GDPR|Digital[\s-]+Services[\s-]+Act|machinery|toys?|cosmetics?|consumer[\s-]+credit|electronic[\s-]+displays?|patents?)\b/iu;

  function pageForReference(reference) {
    if (reference.kind === "NUMBER") return identifiers[reference.value] || null;
    if (reference.kind === "CELEX") return ({"32017R0745": "mdr", "32017R0746": "ivdr", "32026R1022": "customs"})[reference.value] || null;
    if (reference.kind === "ELI") {
      const known = /^https?:\/\/data\.europa\.eu\/eli\/(reg|reg_del)\/(\d{4})\/(\d+)\/oj(?:\/(?:eng|en))?\/?$/u.exec(reference.value);
      if (!known) return null;
      const id = known[2] + "/" + known[3];
      if (id === "2026/1022" ? known[1] !== "reg_del" : known[1] !== "reg") return null;
      return identifiers[id] || null;
    }
    return null;
  }

  function sectionFor(query, page) {
    if (page === "medical") return "";
    if (/\b(?:sources?|evidence|verify|verification)\b/iu.test(query)) return "#sources";
    if (page !== "customs" && /\b(?:roles?|manufacturers?|importers?|distributors?|representatives?)\b/iu.test(query)) return "#roles";
    if (/\b(?:scope|included|all[\s-]+goods|covers?|who)\b/iu.test(query)) return "#scope";
    if (/\b(?:when|dates?|timeline|changes?|changed|starts?|transitions?|mandatory|apply|applies|application)\b/iu.test(query)) return "#time";
    if (/\b(?:relationships?|related|predecessors?|successors?|amendments?|replaces?|repeals?)\b/iu.test(query)) return "#relationships";
    return "";
  }

  function locate(query, response) {
    if (typeof query !== "string" || query.length > 500 || !response || response.query !== query) return null;
    // Navigation does not bypass the selected query language or requested-state guards.
    if (response.queryLanguage !== "en" || !allowedStates.has(response.status)) return null;
    const references = Search.references(query);
    if (outsideSubject.test(query)) return null;
    const ivdr = /\b(?:IVDR|in[\s-]+vitro[\s-]+diagnostic(?:s|[\s-]+(?:medical[\s-]+)?devices?)?)\b/iu.test(query);
    const mdr = /\bMDR\b|\bmedical[\s-]+device[\s-]+regulation\b/iu.test(query);
    const customs = /\bcustoms\b/iu.test(query) && /\b(?:low[\s-]+value|parcels?|consignments?|EUR[\s-]+(?:3|150)|150|small[\s-]+imports?)\b/iu.test(query);
    let selected;
    if (references.length) {
      const matches = references.map(pageForReference);
      if (matches.some(page => !page)) return null; // No neighbouring-law substitution.
      selected = [...new Set([...matches, ...(mdr ? ["mdr"] : []), ...(ivdr ? ["ivdr"] : []), ...(customs ? ["customs"] : [])])];
    } else {
      const medical = /\b(?:EUDAMED|SRN|medical[\s-]+devices?)\b/iu.test(query);
      selected = [];
      if (mdr) selected.push("mdr");
      if (ivdr) selected.push("ivdr");
      if (medical && !mdr && !ivdr) selected.push("medical");
      if (customs) selected.push("customs");
      if (!selected.length) {
        if (response.status !== "CLARIFY") return null;
        selected = ["medical", "customs"];
      }
    }
    const kind = selected.length === 1 ? "pages" : "clarify";
    return {
      kind,
      choices: selected.map(page => ({...pages[page], href: pages[page].href + sectionFor(query, page)})),
      notice: "These links lead to selected English pages, not an answer about applicability or current legal state. Follow the page's official evidence to verify a consequential point."
    };
  }

  function render(document, model) {
    if (!model) return null;
    const section = document.createElement("section");
    section.className = "needle-page-navigation";
    const heading = document.createElement("h3");
    heading.textContent = model.kind === "clarify" ? "Choose a starting point" : "Existing page to explore";
    const notice = document.createElement("p");
    notice.className = "needle-evidence-notice";
    notice.textContent = model.notice;
    const list = document.createElement("ul");
    for (const choice of model.choices) {
      const item = document.createElement("li"), link = document.createElement("a");
      link.href = choice.href;
      link.textContent = choice.label;
      item.append(link);
      list.append(item);
    }
    section.append(heading, list, notice);
    return section;
  }

  return {locate, render};
});

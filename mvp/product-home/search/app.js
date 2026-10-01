/* Mount the bounded, captured-source medical guidance search on the product home. */
(function (root, factory) {
  const api = factory(root.NeedleSearchPanel, root.NeedleMedicalSearch);
  if (typeof module === "object" && module.exports) module.exports = api;
  else root.NeedleProductSearch = api;
})(globalThis, function (SearchPanel, MedicalSearch) {
  "use strict";

  const APPROVED_SOURCES = Object.freeze(["actors", "eudamed", "igj", "operators"]);

  function validateBundle(data, resources) {
    if (!data || data.schema !== "needle-passage-index-v1") throw new TypeError("Invalid evidence index");
    if (!resources || !resources.registry || !Array.isArray(resources.registry.languages)) throw new TypeError("Invalid language resources");
    const actual = Object.keys(data.sources || {}).sort();
    const expected = [...APPROVED_SOURCES].sort();
    if (actual.join("\n") !== expected.join("\n")) throw new TypeError("Evidence index contains an unapproved source set");
    for (const collection of [data.sections, data.blocks]) {
      if (!Array.isArray(collection) || collection.some(item => !APPROVED_SOURCES.includes(item.sourceId))) {
        throw new TypeError("Evidence unit is detached from the approved source set");
      }
    }
    return true;
  }

  async function start(options = {}) {
    const document = options.document || globalThis.document;
    const fetcher = options.fetch || globalThis.fetch;
    const panel = options.panel || SearchPanel;
    const mount = document && document.getElementById("medical-guidance-search");
    const status = document && document.getElementById("medical-guidance-search-status");
    if (!mount) return null;
    if (!fetcher || !panel || typeof panel.mount !== "function") throw new TypeError("Search runtime unavailable");
    mount.setAttribute("aria-busy", "true");
    try {
      const [dataResponse, resourceResponse] = await Promise.all([
        fetcher("/search/index.json", {cache: "no-store"}),
        fetcher("/search/resources.json", {cache: "no-store"})
      ]);
      if (!dataResponse.ok || !resourceResponse.ok) throw new Error("Captured evidence could not be loaded");
      const [data, resources] = await Promise.all([dataResponse.json(), resourceResponse.json()]);
      validateBundle(data, resources);
      const engineFactory = options.engineFactory || (MedicalSearch && MedicalSearch.createEngine);
      if (!engineFactory) throw new TypeError("Medical coverage guard unavailable");
      const instance = panel.mount(mount, {data, resources, queryLanguage: "en", engineFactory});
      if (status) status.textContent = "Search ready. Only the four listed English medical-guidance captures are represented.";
      return instance;
    } catch (error) {
      if (status) status.textContent = "Captured-source search is unavailable. The direct medical overview and official-source links below still work.";
      throw error;
    } finally {
      mount.removeAttribute("aria-busy");
    }
  }

  if (globalThis.document) globalThis.document.addEventListener("DOMContentLoaded", () => start().catch(() => {}), {once: true});
  return {APPROVED_SOURCES, validateBundle, start};
});

/* Product boundary around the retained engine: literal overlap alone cannot admit another domain. */
(function (root, factory) {
  const api = factory(typeof module === "object" && module.exports ? require("./search.js") : root.NeedleSearch);
  if (typeof module === "object" && module.exports) module.exports = api;
  else root.NeedleMedicalSearch = api;
})(globalThis, function (Search) {
  "use strict";

  // Generic roles, registration and timing words occur in many regulated domains.
  // Require an explicit medical subject in the question before showing this collection.
  const MEDICAL_ANCHOR = /\b(?:EUDAMED|IVDR|MDR|SRN|medical[\s-]+devices?|in[\s-]+vitro[\s-]+diagnostic(?:s|[\s-]+devices?)?)\b/iu;

  function createEngine(data, resources) {
    const engine = Search.createEngine(data, resources);
    return {
      ...engine,
      search(query, options) {
        const response = engine.search(query, options);
        if (response.status !== "RESULTS") return response;
        if (MEDICAL_ANCHOR.test(query)) return response;
        return {
          ...response,
          status: "OUTSIDE_MAINTAINED_COVERAGE",
          primary: [],
          evidence: [],
          wordCount: 0,
          warnings: ["Literal overlap was not enough to establish a medical-device subject. No result was shown."]
        };
      }
    };
  }

  return {createEngine};
});

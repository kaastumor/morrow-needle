/* Product boundary around the retained engine: literal overlap alone cannot admit another domain. */
(function (root, factory) {
  const api = factory(typeof module === "object" && module.exports ? require("./search.js") : root.NeedleSearch);
  if (typeof module === "object" && module.exports) module.exports = api;
  else root.NeedleMedicalSearch = api;
})(globalThis, function (Search) {
  "use strict";

  function createEngine(data, resources) {
    const engine = Search.createEngine(data, resources);
    const medicalConcepts = new Set((resources.vocabulary.concepts || []).filter(item => item.topic === "medical").map(item => item.id));
    return {
      ...engine,
      search(query, options) {
        const response = engine.search(query, options);
        if (response.status !== "RESULTS") return response;
        const signalled = (response.analysis || []).some(analysis => (analysis.conceptIds || []).some(id => medicalConcepts.has(id)));
        if (signalled) return response;
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

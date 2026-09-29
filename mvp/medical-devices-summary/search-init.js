"use strict";

// The editorial page and its direct official links remain useful if loading fails.
const searchRoot = document.getElementById("needle-search");
if (searchRoot) {
  searchRoot.textContent = "Loading captured guidance search…";
  Promise.all(["./search/index.json", "./search/resources.json"].map(async (path) => {
    const response = await fetch(path);
    if (!response.ok) throw new Error("Search data unavailable");
    return response.json();
  })).then(([data, resources]) => {
    NeedleSearchPanel.mount(searchRoot, {data, resources, queryLanguage: "en"});
  }).catch(() => {
    searchRoot.textContent = "Captured guidance search is unavailable. Use the direct official links below.";
  });
}

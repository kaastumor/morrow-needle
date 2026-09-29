/* Reusable Unicode/locale/term-resource layer. It does not translate or infer jurisdiction. */
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.NeedleLanguages = api;
})(globalThis, function () {
  'use strict';
  const has = (obj, key) => Object.prototype.hasOwnProperty.call(obj, key);
  function createLanguages(registry, packs = {}, vocabulary = {concepts: []}) {
    if (registry?.schema !== 'needle-languages-v1' || !Array.isArray(registry.languages)) throw new TypeError('Invalid language registry');
    const languages = new Map();
    for (const item of registry.languages) {
      if (!/^[a-z]{2}$/.test(item.tag) || languages.has(item.tag)) throw new TypeError('Invalid/duplicate language tag');
      languages.set(item.tag, Object.freeze({...item}));
    }
    function resolve(tag) {
      if (typeof tag !== 'string' || !tag.trim()) return null;
      try {
        const loc = new Intl.Locale(tag.replaceAll('_', '-'));
        // Region is preserved in the requested locale; NEVER treated as jurisdiction.
        return languages.has(loc.language) ? {requested: loc.toString(), base: loc.language} : null;
      } catch { return null; }
    }
    const loaded = new Map();
    for (const [tag, pack] of Object.entries(packs)) {
      if (!languages.has(tag) || pack.language !== tag || pack.schema !== 'needle-language-pack-v1' || !Array.isArray(pack.stopWords)) throw new TypeError('Invalid language pack: '+tag);
      loaded.set(tag, structuredClone(pack));
    }
    const segCache = new Map();
    function normalize(text, tag) {
      if (typeof text !== 'string') throw new TypeError('Text must be a string');
      const locale = resolve(tag);
      if (!locale) throw new RangeError('Select a supported query/source language');
      // NFC preserves distinctions (й/и, å/a, ł/l); no global accent stripping.
      return text.normalize('NFC').toLocaleLowerCase(locale.base).normalize('NFC').replace(/[’‘ʼ]/gu, "'");
    }
    function tokens(text, tag) {
      const locale = resolve(tag);
      if (!locale) throw new RangeError('Unknown locale');
      const value = normalize(text, locale.base);
      const supported = typeof Intl.Segmenter === 'function' && Intl.Segmenter.supportedLocalesOf([locale.base], {localeMatcher:'lookup'}).length > 0;
      if (supported) {
        if (!segCache.has(locale.base)) segCache.set(locale.base, new Intl.Segmenter(locale.base, {granularity:'word'}));
        return [...segCache.get(locale.base).segment(value)].filter(x => x.isWordLike).map(x => x.segment);
      }
      // Explicit, observable degradation, not a silent English segmenter.
      return value.match(/[\p{L}\p{N}][\p{L}\p{M}\p{N}]*(?:'[\p{L}\p{M}\p{N}]+)*/gu) || [];
    }
    const concepts = new Map(), byLanguage = new Map([...languages.keys()].map(tag => [tag, []]));
    for (const c of vocabulary.concepts || []) {
      if (!c.id || concepts.has(c.id)) throw new TypeError('Missing/duplicate concept identifier');
      concepts.set(c.id, structuredClone(c));
      for (const tag of languages.keys()) {
        const labels = [...(c.labels?.[tag] || []), ...(c.universalLabels || [])];
        for (const label of labels) {
          if (typeof label !== 'string' || !label.trim()) throw new TypeError('Empty concept label');
          byLanguage.get(tag).push({id:c.id, phrase:tokens(label,tag),label, universal:(c.universalLabels || []).includes(label), provenance:structuredClone(c.provenance)});
        }
      }
    }
    for (const rows of byLanguage.values()) rows.sort((a,b) => b.phrase.length-a.phrase.length || b.label.length-a.label.length || a.id.localeCompare(b.id));
    function analyze(text, tag, options = {}) {
      const lang = resolve(tag)?.base;
      if (!lang) throw new RangeError('Unknown analysis language');
      const raw = tokens(text,lang);
      const stop = new Set((loaded.get(lang)?.stopWords || []).map(s=>normalize(s,lang)));
      const terms=[], matches=[], unmapped=[], ambiguity=[];
      const lex = t => 'l:'+lang+':'+t;
      for (let i=0; i<raw.length;) {
        const candidates = options.concepts === false ? [] : byLanguage.get(lang).filter(r => r.phrase.every((t,j)=>raw[i+j]===t));
        const n = candidates[0]?.phrase.length || 0;
        const winners = candidates.filter(r=>r.phrase.length===n);
        const ids = [...new Set(winners.map(x=>x.id))];
        if (ids.length===1) {
          terms.push('c:'+ids[0]);
          matches.push({conceptId:ids[0], language:lang, text:raw.slice(i,i+n).join(' '), label:winners[0].label, provenance:structuredClone(winners[0].provenance)});
          i+=n;
        } else {
          // A homonym is not resolved by insertion order. Keep lexical evidence.
          if (ids.length>1) ambiguity.push({text:raw.slice(i,i+n).join(' '),conceptIds:ids});
          if (!stop.has(raw[i])) { terms.push(lex(raw[i])); unmapped.push(raw[i]); }
          i++;
        }
      }
      return {language:lang,rawTokens:raw,literalTerms:raw.filter(t=>!stop.has(t)).map(lex),terms,matches,conceptIds:[...new Set(matches.map(m=>m.conceptId))],unmapped,ambiguity};
    }
    function capability(tag) {
      const language=resolve(tag)?.base;
      if (!language) return {supported:false,requested:tag};
      const segmenter = typeof Intl.Segmenter==='function' && Intl.Segmenter.supportedLocalesOf([language],{localeMatcher:'lookup'}).length>0;
      return {supported:true,language,tokenizer:segmenter?'Intl.Segmenter':'UNICODE_REGEX_FALLBACK',resourceStatus:loaded.get(language)?.quality || 'NO_LANGUAGE_PACK',labels:byLanguage.get(language).filter(r=>!r.universal).length,translationAvailable:false,nativeSpeakerValidated:false};
    }
    return {resolve,normalize,tokens,analyze,capability,languages:[...languages.values()],getConcept:id=>concepts.has(id)?structuredClone(concepts.get(id)):null};
  }
  return {createLanguages};
});

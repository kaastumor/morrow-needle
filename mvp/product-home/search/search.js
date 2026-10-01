/* Section-first retrieval; language-independent mechanics, explicit language resources. */
(function(root,factory){const api=factory(typeof module==='object'&&module.exports?require('./language.js'):root.NeedleLanguages,typeof module==='object'&&module.exports?require('./word-forms.js'):root.NeedleWordForms);if(typeof module==='object'&&module.exports)module.exports=api;else root.NeedleSearch=api;})(globalThis,function(Language,WordForms){
'use strict';
const cmp=(a,b)=>a<b?-1:a>b?1:0;
const count=s=>s.trim()?s.trim().split(/\s+/u).length:0;
function references(q){
 const text=q.normalize('NFC');const refs=[];
 // Literal identifiers first. CELEX and ELI typing is retained, not guessed from a slash reference.
 for(const m of text.matchAll(/(?<![\p{L}\p{N}])([0-9][0-9]{4}[A-Z][0-9]{4})(?![\p{L}\p{N}])/gu))refs.push({kind:'CELEX',value:m[1]});
 for(const m of text.matchAll(/https?:\/\/data\.europa\.eu\/eli\/[^\s?#]+/gu))refs.push({kind:'ELI',value:m[0].replace(/[.,;)]+$/u,'')});
 for(const m of text.matchAll(/(?<![\p{L}\p{N}])((?:19|20)\d{2})\s*\/\s*(\d{1,6})(?![\p{L}\p{N}])/gu))refs.push({kind:'NUMBER',value:m[1]+'/'+m[2]});
 return refs.filter((r,i)=>refs.findIndex(x=>x.kind===r.kind&&x.value===r.value)===i);
}
function createEngine(input,resources){
 const data=structuredClone(input);
 if(data.schema!=='needle-passage-index-v1'||!Array.isArray(data.sections)||!data.sections.length)throw new TypeError('Invalid section index');
 const lang=Language.createLanguages(resources.registry,resources.packs,resources.vocabulary);
 const domain=structuredClone(resources.domain || {});
 const lines=new Map();
 for(const [sid,s] of Object.entries(data.sources)){
  if(s.id!==sid||!lang.resolve(s.sourceLanguage))throw new TypeError('Explicit supported sourceLanguage required');
  const url=new URL(s.url);if(url.protocol!=='https:'||url.username||url.password)throw new TypeError('Unsafe source URL');
  if(!s.expressionId||!s.versionKey||!s.translationStatus)throw new TypeError('Expression, version and translation status required');
  for(const l of s.lines)lines.set(sid+':'+l.line,l.text);
 }
 for(const u of [...data.blocks,...data.sections]){
  if(!data.sources[u.sourceId])throw new TypeError('Missing source');
  for(const l of u.lines)if(lines.get(l.id)!==l.text)throw new TypeError('Source text/line mismatch');
  if(u.text!==u.lines.map(l=>l.text).join('\n'))throw new TypeError('Unit text detached from source lines');
 }
 const compiled=new Map();
 function compile(concepts=true){
  if(compiled.has(concepts))return compiled.get(concepts);
  const rows=data.sections.filter(u=>u.lines.length&&u.evidenceEligible!==false).map(u=>{
   const source=data.sources[u.sourceId], analysis=lang.analyze([source.title,...u.path,u.text].join(' '),source.sourceLanguage,{concepts});
   return {...u,sourceLanguage:lang.resolve(source.sourceLanguage).base,terms:analysis.terms};
  });
  const df=new Map();for(const r of rows)for(const t of new Set(r.terms))df.set(t,(df.get(t)||0)+1);
  const avg=rows.reduce((s,r)=>s+r.terms.length,0)/rows.length||1;
  const state={rows,df,avg};compiled.set(concepts,state);return state;
 }
 function sourceFields(s){return {url:s.url,sourceLanguage:s.sourceLanguage,expressionId:s.expressionId,workId:s.workId,versionKey:s.versionKey,translationStatus:s.translationStatus,versionAlignment:s.versionAlignment,legalAuthority:s.legalAuthority};}
 function search(query,options={}){
  if(typeof query!=='string'||query.length>500)throw new TypeError('Query must be a string of at most 500 characters');
  const locale=lang.resolve(options.queryLanguage),budget=options.budget??1000;
  if(!Number.isInteger(budget)||budget<1||budget>5000)throw new RangeError('Invalid evidence budget');
  const out={status:'RESULTS',query,queryLanguage:locale?.base||null,uiLanguage:options.uiLanguage||null,jurisdiction:options.jurisdiction??null,observedAt:data.observedAt,primary:[],evidence:[],warnings:[],wordCount:0,unavailable:[],omitted:[],contextOverridden:false,contextUsed:false,coverage:{fullLanguageUnderstanding:false,translation:false,liveAcquisition:false}};
  if(!query.trim()){out.status='EMPTY';return out;}
  if(!locale){out.status='QUERY_LANGUAGE_REQUIRED';return out;}
  out.languageCapability=lang.capability(locale.base);
  out.jurisdictionApplied=false;
  if(options.jurisdiction)out.warnings.push('Jurisdiction is user context only; this prototype does not infer applicability or filter national law.');
  const requested=options.additionalQueryLanguages||[];
  if(!Array.isArray(requested)||requested.length>3)throw new TypeError('At most three additional explicit query languages');
  const queryLanguages=[...new Set([locale.base,...requested.map(t=>{const r=lang.resolve(t);if(!r)throw new RangeError('Unsupported additional language');return r.base;})])];
  const sourceLanguages=[...new Set(Object.values(data.sources).map(s=>lang.resolve(s.sourceLanguage).base))];
  out.coverage.availableSourceLanguages=sourceLanguages;
  out.coverage.sameLanguageSourceAvailable=sourceLanguages.includes(locale.base);
  const eligible=s=>options.allowOtherLanguages===true||queryLanguages.includes(lang.resolve(s.sourceLanguage).base);
  const dates=[...query.matchAll(/(?<!\d)(\d{4}-\d{2}-\d{2})(?!\d)/gu)].map(m=>m[1]);
  if((options.asOf&&options.asOf!==data.observedAt)||dates.some(x=>x!==data.observedAt)){out.status='AS_OF_NOT_SUPPORTED';out.warnings.push('Snapshot retrieval cannot establish historical legal state.');return out;}
  if(/(?<!\d)\d{1,2}[/.]\d{1,2}[/.]\d{4}(?!\d)/u.test(query)){out.status='DATE_INTENT_REQUIRED';out.warnings.push('Select an explicit ISO date and its purpose; day/month order was not guessed.');return out;}
  const exact=references(query);
  if(exact.length){
   const matching=data.blocks.filter(u=>u.evidenceEligible!==false&&references(u.text).some(x=>exact.some(y=>x.kind===y.kind&&x.value===y.value)));
   out.references=exact;
   out.primary=matching.filter(u=>eligible(data.sources[u.sourceId])).map(u=>({...u,...sourceFields(data.sources[u.sourceId]),reason:'Exact reference mentioned in guidance, not retrieved legal-act text.',sourceLanguageFallback:!queryLanguages.includes(lang.resolve(data.sources[u.sourceId].sourceLanguage).base)}));
   out.status=out.primary.length?'REFERENCE_MENTIONS_ONLY':matching.length?'REFERENCE_OTHER_LANGUAGE_AVAILABLE':'REFERENCE_NOT_IN_SNAPSHOT';
   out.warnings.push('No full legal-act text is available here. Exact reference lookup never substitutes a neighbouring act.');return out;
  }
  const useConcepts=options.concepts!==false;
  const analyses=queryLanguages.map(t=>lang.analyze(query,t,{concepts:useConcepts}));
  const terms=[...new Set(analyses.flatMap(a=>a.terms))];out.analysis=analyses;
  if(analyses.some(a=>a.ambiguity.length))out.warnings.push('Ambiguous term mappings retained as literal text; no concept was silently chosen.');
  const generic=new Set((domain.genericConcepts||[]).map(c=>'c:'+c));
  for(const t of queryLanguages)for(const v of domain.genericTerms?.[t]||[])generic.add('l:'+t+':'+v);
  if(!terms.length||terms.every(t=>generic.has(t))){out.status='CLARIFY';return out;}
  const allCompiled=compile(useConcepts);
  const eligibleRows=allCompiled.rows.filter(r=>eligible(data.sources[r.sourceId]));
  const localDf=new Map();for(const r of eligibleRows)for(const t of new Set(r.terms))localDf.set(t,(localDf.get(t)||0)+1);
  const compiled={rows:eligibleRows,df:localDf,avg:eligibleRows.reduce((sum,r)=>sum+r.terms.length,0)/eligibleRows.length||1};
  out.statisticsScope={languages:[...new Set(eligibleRows.map(r=>r.sourceLanguage))],sections:eligibleRows.length};
  // Different-language evidence is never silently used to fill the native-language gap.
  if(!eligibleRows.length){out.status='SOURCE_LANGUAGE_UNAVAILABLE';out.warnings.push('No captured evidence in a permitted source language.');return out;}
  const expansions=options.wordForms===false?[]:WordForms.expand(analyses,compiled,lang);
  out.wordFormMatches=expansions;
  const expandedTerms=[...new Set(expansions.map(x=>x.term))];
  const originalTerms=new Set(terms);
  const retrievalTerms=[...terms,...expandedTerms.filter(t=>!originalTerms.has(t))];
  const substantive=t=>compiled.df.has(t)&&!generic.has(t)&&!/^l:[^:]+:\d+$/u.test(t);
  const directSupport=terms.some(substantive);
  // A lone spelling resemblance cannot make an otherwise ungrounded question supported.
  // Keep the observed variants as reviewable suggestions, without injecting page context.
  if(!directSupport && new Set(expansions.map(e=>e.language+':'+e.queryToken)).size<2){
   out.status=out.coverage.sameLanguageSourceAvailable?'NO_SUPPORTED_TERMS':'CROSS_LANGUAGE_RESOURCE_GAP';
   out.warnings.push('No direct evidence match; isolated word-form suggestions do not establish relevance.');
   return out;
  }
  out.approximateOnly=!directSupport;
  const useful=retrievalTerms.filter(substantive);
  if(!useful.length){out.status=out.coverage.sameLanguageSourceAvailable?'NO_SUPPORTED_TERMS':'CROSS_LANGUAGE_RESOURCE_GAP';out.warnings.push('No supported evidence match. Missing language resources/coverage is not absence of a legal rule.');return out;}
  const concepts=[...new Set(analyses.flatMap(a=>a.conceptIds))];
  const explicit=[...new Set(concepts.map(c=>Object.prototype.hasOwnProperty.call(domain.topicOverrides||{},c)?domain.topicOverrides[c]:lang.getConcept(c)?.topic).filter(Boolean))];
  const context=Object.prototype.hasOwnProperty.call(domain.contexts||{},options.context)?options.context:null;
  out.contextOverridden=!!context&&explicit.length>0&&!explicit.includes(context);
  out.contextUsed=!!context&&!explicit.length;
  const effective=[...retrievalTerms,...(out.contextUsed?(domain.contexts[context]||[]).map(c=>'c:'+c):[])];
  function rank(rows){return rows.filter(r=>eligible(data.sources[r.sourceId])).map(r=>{
   const tf=new Map();for(const t of r.terms)tf.set(t,(tf.get(t)||0)+1);
   let score=0;for(const t of new Set(effective)){const f=tf.get(t)||0;if(f)score+=(originalTerms.has(t)||t.startsWith('c:')?1:0.35)*Math.log(1+(compiled.rows.length-compiled.df.get(t)+.5)/(compiled.df.get(t)+.5))*f*2.2/(f+1.2*(.25+.75*r.terms.length/compiled.avg));}
   return {...r,score};
  }).filter(r=>r.score>0).sort((a,b)=>b.score-a.score||cmp(a.id,b.id));}
  const ranked=rank(compiled.rows);
  if(!ranked.length){out.status='SOURCE_LANGUAGE_UNAVAILABLE';out.warnings.push('Evidence exists only in another source language. Enable explicitly labelled other-language evidence.');return out;}
  out.primary=ranked.slice(0,5).map(r=>{
   const source=data.sources[r.sourceId], matched=[...new Set(r.terms.filter(t=>terms.includes(t)))];
   return {...r,...sourceFields(source),score:Number(r.score.toFixed(6)),reason:!matched.length?'Section was retrieved only through approximate word-form suggestions; inspect the original text.':matched.some(t=>t.startsWith('c:'))?'Section matches explicit concept labels and/or literal words; this is retrieval, not legal equivalence.':'Section matches literal words in the declared source language.',matchedTerms:matched,approximateMatchedTerms:expandedTerms.filter(t=>r.terms.includes(t)),sourceLanguageFallback:!queryLanguages.includes(lang.resolve(source.sourceLanguage).base)};
  });
  const seen=new Set();
  function append(unit,relation){const ls=unit.lines.filter(l=>!seen.has(l.id));if(!ls.length)return;const words=count(ls.map(l=>l.text).join('\n'));if(out.wordCount+words>budget){out.omitted.push({id:unit.id,reason:'Whole section exceeds remaining evidence budget',words});return;}ls.forEach(l=>seen.add(l.id));out.evidence.push({id:unit.id,sourceId:unit.sourceId,heading:unit.heading,text:ls.map(l=>l.text).join('\n'),lines:ls,words,relation,...sourceFields(data.sources[unit.sourceId])});out.wordCount+=words;}
  for(const hit of out.primary)append(hit,'primary-section');
  if(options.includeContext===true){for(const hit of out.primary){for(const near of data.sections.filter(s=>s.sourceId===hit.sourceId)){
   const language=lang.resolve(data.sources[near.sourceId].sourceLanguage).base;
   const caveats=(domain.caveatHeadings?.[language]||[]).map(x=>lang.normalize(x,language));
   if(caveats.includes(lang.normalize(near.heading,language)))append(near,'same-page caveat; applicability not inferred');
  }}}
  for(const row of ranked)append(row,'additional ranked section');
  if(out.primary.some(p=>p.sourceLanguageFallback))out.warnings.push('OTHER_LANGUAGE_EVIDENCE: original source language is displayed; no translation or version equivalence is implied.');
  if(out.contextOverridden)out.warnings.push('Explicit query topic overrides page context.');
  for(const e of out.evidence){const s=data.sources[e.sourceId];if((domain.forecastTerms?.[lang.resolve(s.sourceLanguage).base]||[]).some(w=>lang.normalize(e.text,s.sourceLanguage).includes(lang.normalize(w,s.sourceLanguage)))){out.warnings.push('FORECAST_WORDING: source text contains a forecast, not a verified legal-currentness result.');break;}}
  if(expansions.length)out.warnings.push('APPROXIMATE_WORD_FORMS: observed source words with similar spelling were also searched; they are not established synonyms or legal equivalents. Original question is unchanged.');
  out.warnings.push('Guidance snapshots, not complete/current-law verification. Additional language quality and source coverage remain unvalidated.');
  return out;
 }
 return {search,languages:lang,sourceContext:id=>{const s=data.sections.find(x=>x.id===id);return s?structuredClone({...s,...sourceFields(data.sources[s.sourceId])}):null;},data:structuredClone(data)};
}
return {createEngine,references,wordCount:count};
});

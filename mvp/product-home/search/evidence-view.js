/* Source-bound result previews. No answer generation and no ranking changes. */
(function(root,factory){const api=factory();if(typeof module==='object'&&module.exports)module.exports=api;else root.NeedleEvidenceView=api;})(globalThis,function(){
'use strict';
const words=text=>text.trim()?text.trim().split(/\s+/u).length:0;
const safeUrl=value=>{const u=new URL(value);if(u.protocol!=='https:'||u.username||u.password)throw new TypeError('Unsafe official-source URL');return u.href;};
const representedActs=Object.freeze({
 '2017/745':Object.freeze({code:'MDR',href:'/medical-devices/mdr/'}),
 '2017/746':Object.freeze({code:'IVDR',href:'/medical-devices/ivdr/'})
});
function continuationFor(response){
 if(!response||!['RESULTS','REFERENCE_MENTIONS_ONLY'].includes(response.status))return null;
 const references=Array.isArray(response&&response.references)?response.references:[];
 if(references.length>1||references.some(ref=>ref.kind!=='NUMBER'||!representedActs[ref.value]))return null;
 const exact=references.find(ref=>ref.kind==='NUMBER'&&representedActs[ref.value]);
 if(exact){
  const act=representedActs[exact.value];
  return {kind:'act',href:act.href,label:'Open represented '+act.code+' detail',notice:'Exact identifier maps to a maintained internal act view. This navigation does not establish applicability or replace the official act.'};
 }
 if(response&&response.status==='RESULTS'){
  return {kind:'overview',href:'/medical-devices/',label:'Continue in medical-device overview',notice:'No single act identity was inferred from these guidance matches. Use the bounded overview to choose the represented branch.'};
 }
 return null;
}
function createPresenter(engine){
 if(!engine||typeof engine.search!=='function'||typeof engine.sourceContext!=='function'||!engine.data||!engine.languages)throw new TypeError('A source-bound search engine is required');
 const data=structuredClone(engine.data);
 const sectionById=new Map(data.sections.map(s=>[s.id,s]));
 const blockById=new Map(data.blocks.map(s=>[s.id,s]));
 const sourceLines=new Map(Object.values(data.sources).flatMap(s=>s.lines.map(l=>[s.id+':'+l.line,l.text])));
 function verified(unit){
  if(!unit||!Array.isArray(unit.lines)||unit.text!==unit.lines.map(l=>l.text).join('\n'))throw new TypeError('Invalid source unit');
  for(const line of unit.lines)if(sourceLines.get(line.id)!==line.text||line.id!==unit.sourceId+':'+line.line)throw new TypeError('Detached source line');
  return unit;
 }
 function card(hit,response,options={}){
  const budget=options.previewWords??160;
  if(!Number.isInteger(budget)||budget<20||budget>500)throw new RangeError('Preview budget must be 20–500 words');
  const section=sectionById.get(hit.id);
  // Exact-reference locator outputs are deliberately not converted into substantive section answers.
  if(!section){
   const block=blockById.get(hit.id),source=block&&data.sources[block.sourceId];
   if(!block||hit.text!==block.text||hit.sourceId!==block.sourceId||hit.url!==source.url||hit.sourceLanguage!==source.sourceLanguage)throw new TypeError('Unknown or detached reference locator');
   verified(block);
   return {kind:'locator',id:hit.id,sourceLanguage:source.sourceLanguage,url:safeUrl(source.url),heading:hit.heading||'Exact reference',notice:'Reference mentioned in guidance; full act text is not available in this snapshot.'};
  }
  verified(section);const source=data.sources[section.sourceId];
  if(hit.sourceId!==section.sourceId||hit.text!==section.text||hit.url!==source.url||hit.sourceLanguage!==source.sourceLanguage||hit.expressionId!==source.expressionId||hit.versionKey!==source.versionKey)throw new TypeError('Result identity does not match its source');
  const original=new Set((response.analysis||[]).flatMap(a=>a.terms));
  const approximate=new Set((response.wordFormMatches||[]).map(m=>m.term));
  const inspect=text=>{
   const terms=engine.languages.analyze(text,source.sourceLanguage,{concepts:options.concepts!==false}).terms;
   return {direct:[...new Set(terms.filter(t=>original.has(t)))],approximate:[...new Set(terms.filter(t=>approximate.has(t)&&!original.has(t)))]};
  };
  const body=inspect(section.text),heading=inspect(section.heading),parents=inspect([source.title,...section.path.slice(0,-1)].join(' '));
  const matchKind=body.direct.length?'body-direct':body.approximate.length?'body-approximate':heading.direct.length||heading.approximate.length?'heading-only':'context-only';
  const blocks=data.blocks.filter(b=>b.sectionId===section.id&&b.evidenceEligible!==false&&b.lines.length).map(verified);
  const candidates=(blocks.length?blocks:[section]).map((b,i)=>({unit:b,position:i,matches:inspect(b.text)}));
  // Choose a whole existing paragraph/list unit, never cut a sentence or reconstruct a qualification.
  // This only selects a display excerpt; the result order and source words are unchanged.
  candidates.sort((a,b)=>b.matches.direct.length-a.matches.direct.length||b.matches.approximate.length-a.matches.approximate.length||a.position-b.position);
  let selected=[],previewStatus='no-bounded-body-match';
  if(words(section.text)<=budget){selected=[section];previewStatus='complete-section';}
  else{
   const found=candidates.find(c=>(c.matches.direct.length||c.matches.approximate.length)&&words(c.unit.text)<=budget);
   if(found){selected=[found.unit];previewStatus='source-excerpt';}
  }
  const lines=selected.flatMap(u=>u.lines);const text=lines.map(l=>l.text).join('\n');
  const displayed=new Set(lines.map(l=>l.id));
  const omitted=section.lines.filter(l=>!displayed.has(l.id)).length;
  const notice=previewStatus==='complete-section'?'Complete captured section; the wider document can contain additional conditions.':previewStatus==='source-excerpt'?'Source excerpt, not a complete answer. Other paragraphs may qualify it; the complete captured section is available below.':'No short, whole matching passage fits the preview limit. Open the complete captured section; no fragment was invented.';
  const reasons={'body-direct':'Original search terms or explicit concept labels match the source body.','body-approximate':'Only suggested word forms match the source body. Spelling resemblance is not legal equivalence.','heading-only':'The match is in a heading, not the source body. Treat this as a navigation candidate.','context-only':'The match is inherited from source/page context, not the source body. Treat this as a navigation candidate.'};
  return {kind:'section',id:section.id,heading:section.heading,sourceId:source.id,sourceLanguage:source.sourceLanguage,sourceLanguageFallback:!!hit.sourceLanguageFallback,url:safeUrl(source.url),expressionId:source.expressionId,workId:source.workId,versionKey:source.versionKey,versionAlignment:source.versionAlignment,translationStatus:source.translationStatus,legalAuthority:source.legalAuthority,observedAt:data.observedAt,matchKind,matchReason:reasons[matchKind],bodyMatches:body,headingMatches:heading,contextMatches:parents,preview:{status:previewStatus,text,lines:structuredClone(lines),words:words(text),omittedParagraphs:omitted,notice},fullSection:{text:section.text,lines:structuredClone(section.lines),words:words(section.text)},editorialWarning:section.editorialWarning||null,editorialWarningUrl:section.editorialWarningUrl?safeUrl(section.editorialWarningUrl):null,evidenceStatus:'captured-guidance-not-current-law-verification'};
 }
 function present(response,options={}){
  if(!response||!Array.isArray(response.primary))throw new TypeError('A search response is required');
  return {status:response.status,query:response.query,queryLanguage:response.queryLanguage,approximateOnly:!!response.approximateOnly,warnings:[...(response.warnings||[])],cards:response.primary.map(hit=>card(hit,response,options)),navigation:continuationFor(response),rankingChanged:false};
 }
 return {present};
}
function renderCard(document,model,position){
 if(!document||typeof document.createElement!=='function')throw new TypeError('A DOM document is required');
 const node=(tag,text,cls)=>{const x=document.createElement(tag);if(text!==undefined)x.textContent=text;if(cls)x.className=cls;return x;};
 const article=node('article',undefined,'needle-evidence-card');
 article.append(node('p',String(position+1)+' · '+model.sourceLanguage.toUpperCase()+(model.sourceLanguageFallback?' · OTHER-LANGUAGE SOURCE':''),'needle-evidence-meta'));
 article.append(node('h3',model.heading));
 if(model.kind==='section'){
  article.append(node('p',model.matchReason,'needle-evidence-meta'));
  const excerpt=node('blockquote',model.preview.text||model.preview.notice);excerpt.lang=model.sourceLanguage;article.append(excerpt);
  article.append(node('p',model.preview.notice,'needle-evidence-notice'));
  if(model.editorialWarning){
   const warning=node('p',model.editorialWarning,'needle-evidence-warning');
   if(model.editorialWarningUrl){const source=node('a',' Check Commission module status');source.href=safeUrl(model.editorialWarningUrl);source.target='_blank';source.rel='noopener noreferrer';warning.append(source);}
   article.append(warning);
  }
  const details=node('details');details.append(node('summary','Read the complete captured section ('+model.fullSection.words+' words), including qualifications'));
  const full=node('p',model.fullSection.text,'needle-evidence-full');full.lang=model.sourceLanguage;details.append(full);article.append(details);
  article.append(node('p','Captured '+model.observedAt+' · '+model.evidenceStatus+' · version alignment '+model.versionAlignment,'needle-evidence-meta'));
  const identity=node('details');identity.append(node('summary','Inspect source identity and captured lines'));
  identity.append(node('p','Expression: '+model.expressionId+'\nVersion: '+model.versionKey+'\nLanguage status: '+model.translationStatus+'\nLines: '+model.fullSection.lines.map(l=>l.id).join(', '),'needle-evidence-full'));article.append(identity);
 }else article.append(node('p',model.notice,'needle-evidence-notice'));
 const link=node('a','Open official source');link.href=safeUrl(model.url);link.target='_blank';link.rel='noopener noreferrer';article.append(link);
 return article;
}
function renderContinuation(document,model){
 if(!model)return null;
 if(!document||typeof document.createElement!=='function')throw new TypeError('A DOM document is required');
 const aside=document.createElement('aside');aside.className='needle-evidence-continuation';
 const heading=document.createElement('p');heading.className='needle-evidence-meta';heading.textContent=model.kind==='act'?'Continue with the represented act':'Continue in the bounded legislation view';
 const link=document.createElement('a');link.href=model.href;link.textContent=model.label;
 const notice=document.createElement('p');notice.className='needle-evidence-notice';notice.textContent=model.notice;
 aside.append(heading,link,notice);return aside;
}
return {createPresenter,renderCard,continuationFor,renderContinuation};
});

/* A dependency-free panel for the existing static M1 surface. Snapshot evidence only. */
(function(root,factory){const api=factory(typeof module==='object'&&module.exports?require('./search.js'):root.NeedleSearch,typeof module==='object'&&module.exports?require('./evidence-view.js'):root.NeedleEvidenceView,typeof module==='object'&&module.exports?require('./page-navigation.js'):root.NeedlePageNavigation);if(typeof module==='object'&&module.exports)module.exports=api;else root.NeedleSearchPanel=api;})(globalThis,function(Search,View,Navigation){
'use strict';
const states={EMPTY:'Enter a question.',QUERY_LANGUAGE_REQUIRED:'Select a supported question language.',NO_SUPPORTED_TERMS:'No supported match in this captured collection. This does not mean no rule exists.',OUTSIDE_MAINTAINED_COVERAGE:'Outside maintained medical-device coverage. No result is safer than using incidental word overlap.',SOURCE_LANGUAGE_UNAVAILABLE:'No captured source in this language. Other-language evidence is optional and will be labelled.',CROSS_LANGUAGE_RESOURCE_GAP:'No supported cross-language match. The question is not automatically translated.',CLARIFY:'Add a subject to this question.',REFERENCE_NOT_IN_SNAPSHOT:'This exact reference is not in the captured collection; a different act was not substituted.',REFERENCE_OTHER_LANGUAGE_AVAILABLE:'This reference is present only in another source language. Enable other-language evidence to inspect it.',AS_OF_NOT_SUPPORTED:'This snapshot cannot establish the requested historical legal state.',DATE_INTENT_REQUIRED:'Specify an unambiguous date and its purpose.'};
function mount(root,config){
 if(!root||!root.ownerDocument||!config)throw new TypeError('A DOM root and data/resources configuration are required');
 const document=root.ownerDocument,engine=(config.engineFactory||Search.createEngine)(config.data,config.resources),presenter=View.createPresenter(engine);
 const el=(tag,text,cls)=>{const x=document.createElement(tag);if(text!==undefined)x.textContent=text;if(cls)x.className=cls;return x;};
 const form=el('form'),query=el('textarea'),language=el('select'),other=el('input'),submit=el('button','Find a starting point'),clear=el('button','Clear'),status=el('p'),pages=el('div'),results=el('div'),warnings=el('details'),warningText=el('p');
 query.maxLength=500;query.required=true;query.rows=3;other.type='checkbox';submit.type='submit';clear.type='button';status.setAttribute('role','status');status.setAttribute('aria-live','polite');
 const label=(text,input)=>{const x=el('label');x.append(el('span',text),input);return x;};
 for(const l of config.resources.registry.languages){const o=el('option',l.nativeName+' ('+l.tag+')');o.value=l.tag;language.append(o);}
 language.value=engine.languages.resolve(config.queryLanguage||'en')?.base||'en';
 form.append(label('Your question',query),label('Question language — not jurisdiction',language),label('Allow explicitly labelled other-language evidence',other),submit,clear);
 warnings.append(el('summary','Source coverage and matching limitations'),warningText);
 const notice=el('p','Existing English page links and captured medical-guidance passages. Not live search, translation, or an individual legal determination. Source languages remain explicit.','needle-evidence-notice');
 root.replaceChildren(notice,form,status,pages,results,warnings);
 function clearResult(){pages.replaceChildren();results.replaceChildren();warningText.textContent='';status.textContent='';}
 function run(){
  try{const response=engine.search(query.value,{queryLanguage:language.value,allowOtherLanguages:other.checked,budget:400,includeContext:false});const view=presenter.present(response);
   view.pageNavigation=Navigation.locate(query.value,response);
   pages.replaceChildren();if(view.pageNavigation)pages.append(Navigation.render(document,view.pageNavigation));
   const cards=view.cards.map((c,i)=>View.renderCard(document,c,i));results.replaceChildren();if(cards.length)results.append(el('h3','Captured medical guidance'),...cards);
   const sourceStatus=cards.length?(view.approximateOnly?'Approximate candidates only — inspect the source wording, not a verified answer.':cards.length+' source sections to inspect. Results may cover only part of the question.'):(states[view.status]||view.status);
   status.textContent=view.pageNavigation?((view.pageNavigation.kind==='clarify'?'Choose a starting point; no single act was selected.':'An existing page is linked below.')+' '+(cards.length?sourceStatus:'No captured medical-guidance passage is available for this question.')):sourceStatus;
   const forms=(response.wordFormMatches||[]).map(m=>m.queryToken+' → '+m.sourceToken+' ['+m.language+']');
   warningText.textContent=[...(view.warnings||[]),'Available captured source languages: '+(response.coverage.availableSourceLanguages||[]).join(', '),...(forms.length?['Observed spelling suggestions, not established synonyms: '+forms.join('; ')]:[])].join('\n');
   return view;
  }catch(error){clearResult();status.textContent='Search stopped: '+error.message;return null;}
 }
 const onSubmit=event=>{event.preventDefault();run();},onClear=()=>{query.value='';clearResult();query.focus();},onChange=()=>{clearResult();status.textContent='Search settings changed. Submit again to refresh results.';};
 form.addEventListener('submit',onSubmit);clear.addEventListener('click',onClear);language.addEventListener('change',onChange);other.addEventListener('change',onChange);
 // No query persistence, analytics, credential handling or network/model requests.
 return {search:(text,lang=language.value)=>{query.value=text;language.value=lang;return run();},destroy:()=>{form.removeEventListener('submit',onSubmit);clear.removeEventListener('click',onClear);language.removeEventListener('change',onChange);other.removeEventListener('change',onChange);root.replaceChildren();}};
}
return {mount};
});

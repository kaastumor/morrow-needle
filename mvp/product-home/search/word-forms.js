/* Bounded, source-observed word-form recall. No translator, stemmer or legal equivalence. */
(function(root,factory){const api=factory();if(typeof module==='object'&&module.exports)module.exports=api;else root.NeedleWordForms=api;})(globalThis,function(){
'use strict';
const chars=s=>[...s];
function script(s){if(/^\p{Script=Latin}+$/u.test(s))return'Latin';if(/^[\p{Script=Greek}\p{M}]+$/u.test(s))return'Greek';if(/^\p{Script=Cyrillic}+$/u.test(s))return'Cyrillic';return null;}
function grams(s){const c=chars(s),g=new Set();for(let i=0;i<c.length-2;i++)g.add(c.slice(i,i+3).join(''));return g;}
function similarity(a,b){const x=grams(a),y=grams(b);return x.size+y.size?2*[...x].filter(g=>y.has(g)).length/(x.size+y.size):0;}
function plausible(a,b){
 const x=chars(a),y=chars(b);if(x.length<5||y.length<5||!script(a)||script(a)!==script(b))return false;
 if(Math.min(x.length,y.length)/Math.max(x.length,y.length)<.65)return false;
 let prefix=0;while(prefix<Math.min(x.length,y.length)&&x[prefix]===y[prefix])prefix++;
 return prefix>=4&&similarity(a,b)>=.55;
}
function expand(analyses,state){
 const expansions=[];let expandedCount=0;
 for(const a of analyses){
  const prefix='l:'+a.language+':';
  const vocabulary=[...state.df.keys()].filter(t=>t.startsWith(prefix)).map(t=>t.slice(prefix.length));
  for(const q of [...new Set(a.rawTokens)]){
   if(expandedCount>=6)return expansions;
   if(state.df.has(prefix+q)||chars(q).length<5||!script(q))continue;
   const found=vocabulary.filter(s=>plausible(q,s)).map(s=>({queryToken:q,sourceToken:s,language:a.language,term:prefix+s,similarity:similarity(q,s),kind:'observed-word-form-not-semantic-equivalence'})).sort((x,y)=>y.similarity-x.similarity||(x.sourceToken<y.sourceToken?-1:1)).slice(0,3);
   if(found.length){expandedCount++;expansions.push(...found);}
  }
 }
 return expansions;
}
return {expand,plausible,similarity};
});

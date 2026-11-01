import json,html,sys
D=sys.argv[1]; O=D+'/tvmock'
items=json.load(open(O+'/items.json'))
MON={'11':'November','12':'December','01':'Januari','02':'Februari'}
cards=[];month=None
for it in items:
    m=it['date'][5:7]
    if m!=month: month=m; cards.append(f'<h2 class="mh">{MON[m]}</h2>')
    tag='<span class="tag new">Nieuw beeld, tv-versie</span>' if it['kind']=='new' else '<span class="tag old">Ouder beeld (nog Link in bio en Poort Padel logo)</span>'
    kamp='<span class="tag kamp">Kids Kamp</span>' if it['pijler']=='kids kamp' else ''
    cards.append(f'''<article class="card" data-id="{it['id']}" data-kind="{it['kind']}" data-pijler="{html.escape(it['pijler'])}">
<header class="ch"><div class="when"><b>{html.escape(it['kop'])}</b><span>post van {html.escape(it['dag'])}</span></div>{tag}{kamp}</header>
<div class="body"><a class="media" href="img/{it['id']}.jpg" target="_blank" rel="noopener"><img src="img/{it['id']}.jpg" alt="Tv-mockup: {html.escape(it['kop'])}" loading="lazy"></a>
<div class="fields">
<div class="actions"><button type="button" class="st" data-s="tv">Op tv</button><button type="button" class="st" data-s="no">Niet op tv</button></div>
<label class="lbl" for="c1-{it['id']}">Onderschrift regel 1</label><input id="c1-{it['id']}" class="cap" data-f="cap1" value="{html.escape(it['cap1'])}">
<label class="lbl" for="c2-{it['id']}">Onderschrift regel 2</label><input id="c2-{it['id']}" class="cap" data-f="cap2" value="{html.escape(it['cap2'])}">
<textarea id="note-{it['id']}" class="note" rows="2" placeholder="Opmerking (optioneel)"></textarea>
<div class="meta"><span class="saved"></span></div></div></div></article>''')
page=f'''<title>ACA Tv-check Poort Padel</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@700;800&family=Inter:wght@400;500;600;700&display=swap">
<style>
/* One column of tv mockups in post order; navy like the posts, lime for the chosen state */
:root{{--bg:#071321;--panel:#0d1b2d;--panel2:#132439;--line:#1f3350;--fg:#eef2ee;--mute:#9fb0c3;--lime:#CDEB4B;--amber:#f2b84b;--red:#ef6b6b;--green:#7bd389;--ink:#071321;--font:Inter,system-ui,sans-serif;--disp:"Inter Tight",Inter,system-ui,sans-serif;color-scheme:dark}}
@media (prefers-color-scheme: light){{:root:not([data-theme="dark"]){{--bg:#f3f5f1;--panel:#fff;--panel2:#e9eee6;--line:#d3dbcf;--fg:#0b1626;--mute:#56657a;--lime:#7a9a00;--amber:#b57b00;--red:#c43d3d;--green:#2f8f4a;--ink:#fff;color-scheme:light}}}}
:root[data-theme="light"]{{--bg:#f3f5f1;--panel:#fff;--panel2:#e9eee6;--line:#d3dbcf;--fg:#0b1626;--mute:#56657a;--lime:#7a9a00;--amber:#b57b00;--red:#c43d3d;--green:#2f8f4a;--ink:#fff;color-scheme:light}}
*{{box-sizing:border-box}}
body{{background:var(--bg);color:var(--fg);font-family:var(--font);margin:0;padding-block:0 48px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
body::before{{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--bg)}}
.top{{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--bg);padding-block:18px 12px;border-bottom:1px solid var(--line);margin-bottom:8px}}
h1{{font:800 clamp(24px,4vw,34px)/1.05 var(--disp);margin:0 0 6px;text-transform:uppercase;letter-spacing:-.01em}}
.sub{{color:var(--mute);margin:0 0 10px;max-width:80ch;font-size:15px}}
.specs{{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 12px;padding:0;list-style:none}} .specs li{{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:6px 10px;font:600 13px/1.3 var(--font)}} .specs b{{color:var(--lime)}}
.bar{{display:flex;flex-wrap:wrap;gap:8px;align-items:center}}
.chip{{border:1px solid var(--line);background:var(--panel);color:var(--fg);border-radius:999px;padding:7px 13px;font:600 13px/1 var(--font);cursor:pointer}}
.chip.on{{background:var(--lime);color:var(--ink);border-color:var(--lime)}}
.counts{{margin-left:auto;display:flex;gap:14px;font:500 13px/1 var(--font);color:var(--mute);font-variant-numeric:tabular-nums}} .counts b{{color:var(--fg)}}
.mh{{font:800 20px/1 var(--disp);text-transform:uppercase;letter-spacing:.02em;margin:26px 0 12px;color:var(--mute)}}
.wrap{{max-width:1100px}}
.card{{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px;margin-bottom:14px;min-width:0}}
.card[data-st="tv"]{{border-color:var(--green)}} .card[data-st="no"]{{border-color:var(--red);opacity:.7}}
.ch{{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:12px}}
.when{{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;font:700 15px/1.2 var(--font)}} .when span{{color:var(--mute);font-weight:500;font-size:13px}}
.tag{{font:700 11px/1.3 var(--font);letter-spacing:.06em;text-transform:uppercase;padding:5px 8px;border-radius:4px}}
.tag.new{{background:var(--lime);color:var(--ink)}} .tag.old{{background:var(--panel2);color:var(--mute)}} .tag.kamp{{background:var(--amber);color:var(--ink)}}
.body{{display:grid;grid-template-columns:minmax(260px,560px) 1fr;gap:16px}}
@media (max-width:760px){{.body{{grid-template-columns:1fr}}}}
.media{{display:block;aspect-ratio:16/9;background:#0091B1;border-radius:6px;overflow:hidden;align-self:start}} .media img{{width:100%;height:100%;object-fit:cover;display:block}}
.fields{{min-width:0;display:flex;flex-direction:column;gap:8px}}
.lbl{{font:600 12px/1 var(--font);letter-spacing:.06em;text-transform:uppercase;color:var(--mute);margin-top:4px}}
.cap,.note{{width:100%;background:var(--bg);color:var(--fg);border:1px solid var(--line);border-radius:8px;padding:9px 10px;font:400 14px/1.4 var(--font)}} .note{{resize:vertical}}
.actions{{display:flex;gap:6px;flex-wrap:wrap}}
.st{{flex:1;min-width:90px;border:1px solid var(--line);background:var(--panel2);color:var(--fg);border-radius:8px;padding:10px 8px;font:600 13px/1 var(--font);cursor:pointer}}
.st:focus-visible,.chip:focus-visible{{outline:2px solid var(--lime);outline-offset:2px}}
.card[data-st="tv"] .st[data-s="tv"]{{background:var(--green);color:var(--ink);border-color:var(--green)}}
.card[data-st="no"] .st[data-s="no"]{{background:var(--red);color:#fff;border-color:var(--red)}}
.meta{{font-size:12px;color:var(--mute);min-height:14px}}
@media (prefers-reduced-motion:no-preference){{.card{{transition:border-color .2s}}}}
</style>
<div class="top"><div class="wrap">
<h1>Tv-check Poort Padel</h1>
<p class="sub">Zo staat elke post in het vak rechts op het scherm, met de Poort Padel klok links. Het vak is staand, ongeveer 4:5, dus de postbeelden passen er precies in. Kies per beeld Op tv of Niet op tv en pas het onderschrift aan (twee korte regels, die zet Poort Padel eronder). De nieuwe beelden hebben op tv "Vraag aan de bar" in plaats van "Link in bio".</p>
<ul class="specs"><li>Formaat <b>1080 × 1350 px</b> (4:5, staand)</li><li>Vak op tv ongeveer <b>590 × 740 px</b> van 1920 × 1080</li><li>Onderschrift <b>2 regels</b>, wit, gecentreerd</li><li>Klok en logo links <b>blijven staan</b></li></ul>
<div class="bar"><button type="button" class="chip on" data-f="all">Alles</button><button type="button" class="chip" data-f="new">Nieuw</button><button type="button" class="chip" data-f="kamp">Kids Kamp</button><button type="button" class="chip" data-f="tv">Gekozen voor tv</button><button type="button" class="chip" data-f="open">Nog niet gekozen</button>
<div class="counts"><span>Op tv <b id="c-tv">0</b></span><span>Niet <b id="c-no">0</b></span><span>Open <b id="c-open">{len(items)}</b></span></div></div></div></div>
<div class="wrap" id="list">{''.join(cards)}</div>
<script>
(function(){{
const COL='tvcheck2_v1';const cards=[...document.querySelectorAll('.card')];const state={{}};let db=null;
function ls(k,v){{try{{if(v===undefined)return JSON.parse(localStorage.getItem(k)||'null');localStorage.setItem(k,JSON.stringify(v));}}catch(e){{return null}}}}
function fmt(t){{return new Date(t).toLocaleString('nl-NL',{{day:'numeric',month:'short',hour:'2-digit',minute:'2-digit'}})}}
let filter='all';
function render(){{const c={{tv:0,no:0,open:0}};
 for(const el of cards){{const id=el.dataset.id;const r=state[id]||{{}};if(r.status)el.dataset.st=r.status;else delete el.dataset.st;c[r.status||'open']++;
  for(const inp of el.querySelectorAll('.cap')){{const f=inp.dataset.f;if(document.activeElement!==inp&&r[f]!==undefined&&r[f]!==inp.value)inp.value=r[f];}}
  const nt=el.querySelector('.note');if(document.activeElement!==nt&&(r.note||'')!==nt.value)nt.value=r.note||'';
  el.querySelector('.saved').textContent=r.updatedAt?('Opgeslagen '+fmt(r.updatedAt)):'';
  let show=true;if(filter==='new')show=el.dataset.kind==='new';else if(filter==='kamp')show=el.dataset.pijler==='kids kamp';else if(filter==='tv')show=r.status==='tv';else if(filter==='open')show=!r.status;el.hidden=!show;}}
 for(const k in c)document.getElementById('c-'+k).textContent=c[k];}}
async function save(id,patch){{const rec=Object.assign({{}},state[id]||{{}},patch,{{updatedAt:Date.now()}});state[id]=rec;render();ls(COL+':'+id,rec);if(db){{try{{await db.doc(COL+'/'+id).set(rec);}}catch(e){{console.warn('db set',e);}}}}}}
for(const el of cards){{const id=el.dataset.id;const cached=ls(COL+':'+id);if(cached)state[id]=cached;
 el.querySelectorAll('.st').forEach(b=>b.addEventListener('click',()=>{{const cur=(state[id]||{{}}).status;save(id,{{status:cur===b.dataset.s?null:b.dataset.s}});}}));
 for(const inp of [...el.querySelectorAll('.cap'),el.querySelector('.note')]){{const f=inp.classList.contains('note')?'note':inp.dataset.f;let t;
  inp.addEventListener('input',()=>{{clearTimeout(t);t=setTimeout(()=>save(id,{{[f]:inp.value}}),900);}});
  inp.addEventListener('blur',()=>{{clearTimeout(t);if((state[id]||{{}})[f]!==inp.value)save(id,{{[f]:inp.value}});}});}}}}
document.querySelectorAll('.chip').forEach(ch=>ch.addEventListener('click',()=>{{document.querySelectorAll('.chip').forEach(x=>x.classList.toggle('on',x===ch));filter=ch.dataset.f;render();}}));
render();
(async()=>{{try{{if(!window.claude||!window.claude.use)return;db=await window.claude.use('db');if(!db)return;
 db.collection(COL).onSnapshot(snap=>{{for(const d of snap.docs){{const r=d.data();if(!r)continue;const cur=state[d.id];if(!cur||(r.updatedAt||0)>=(cur.updatedAt||0)){{state[d.id]=r;ls(COL+':'+d.id,r);}}}}render();}},e=>console.warn('db',e));}}catch(e){{console.warn('db init',e);}}}})();
}})();
</script>
'''
open(O+'/index.html','w').write(page); print(len(items),'cards')

import json,os,html,sys
D=sys.argv[1]; W=D+'/tvwork'; OUTDIR=D+'/tvcheck'
edits={e['file']:e for e in json.load(open(W+'/edits.json'))}
files=sorted(f for f in os.listdir(D+'/tvzip/tv') if f.endswith('.jpg'))
labels={'01':'Welkom','02':'Losse training','03':'Lessenreeks','04':'Beginners','05':'Onze aanpak','06':'Jeugd','07':'Toernooien','08':'Gevorderden','09':'Winterreeks','10':'Contact','11':'Kids Kamp kerstvakantie','12':'Jeugd voorjaarsreeks','13':'Jeugd groepjes','14':'Jeugd leren','15':'Losse les','16':'Lessenreeks (variant)','21':'Coach kiezen','22':'Snel op de baan','23':'Duo','24':'Vaste reeks','25':'Groep klaar','26':'Instromen','27':'Eerste les','28':'Eerste rally','29':'Lachen en werken','30':'Smash','31':'Competitie','32':'Queen of the court','33':'Daluren','34':'King of the court','35':'Mexicano','36':'Community','37':"Collega's",'38':'Vrienden','39':'Playtomic','40':'Team','41':'Aanbod','42':'Voorjaarsreeks','43':'Winterreeks (variant)','44':'Jeugd nieuw','45':'Jeugd bewegen','46':'Jeugd uitleg','47':'Jeugd spel','48':'Kids Kamp drie ochtenden','49':'Kids Kamp prijzen en extra\'s','50':'Jeugd proefles'}
why={
 '09':'Was "inschrijving opent binnenkort". De winterreeks staat nu open op de site: 3 lessen, maandag 14 december t/m zaterdag 2 januari.',
 '43':'Zelfde reeks, tweede variant. Datums en "later instappen kan" overgenomen van de site.',
 '42':'Voorjaarsreeks 2027 van de site: 7 lessen, 4 januari t/m 21 februari.',
 '12':'Was een dubbele van slide 06. Nu de jeugd voorjaarsreeks: 7 lessen, 4 januari t/m 20 februari, vanaf 6 jaar.',
 '11':'Was "drie middagen" en "diploma". Site zegt: maandag 21 t/m woensdag 23 december, 10:00 tot 12:30.',
 '48':'Was "drie dagen". Nu drie ochtenden met de prijs van de site: 195 euro all-in, 10% familiekorting vanaf het tweede kind.',
 '49':'Stempelkaart, diploma en shirt staan niet op de site. Nu wat er wel staat: coaches, pauze met eten en drinken, rackets en ballen aanwezig.',
 '10':'E-mail l.debruin@ vervangen door info@allcourtacademy.com, zoals op de site.',
}
flags={
 '13':'Slide zegt maximaal 6 kinderen per groep. De site noemt groepen van 4. Welke klopt voor jeugd?',
 '07':'Weekendtoernooien staan niet op de ACA-site. Klopt de claim nog?',
 '34':'King of the court als vast evenement staat niet op de site. Nog actueel?',
 '35':'Mexicano als vast evenement staat niet op de site. Nog actueel?',
 '33':'Daluren-aanbod staat niet op de site. Klopt de tekst en de prijs nog?',
 '06':'Lijkt sterk op de oude slide 12. Die is nu omgebouwd, deze kan blijven of eruit.',
}
cards=[]
for f in files:
    n=f[:2]; key=n; lab=labels.get(n,f[3:-4])
    e=edits.get(f); fl=flags.get(n)
    tags=''
    if e: tags+='<span class="tag new">Aangepast</span>'
    if fl: tags+='<span class="tag chk">Even checken</span>'
    media=f'<div class="media"><img src="orig/{f}" alt="Slide {n} {html.escape(lab)}" loading="lazy" data-orig="orig/{f}"' + (f' data-new="nieuw/{f}"' if e else '') + '></div>'
    toggle=''
    newtxt=''
    if e:
        toggle='<div class="seg" role="group" aria-label="Versie"><button type="button" class="segbtn" data-v="orig">Oud</button><button type="button" class="segbtn on" data-v="new">Nieuw</button></div>'
        newtxt=f'<dl class="txt"><dt>Kop</dt><dd>{html.escape(" ".join(e["head"]))}</dd><dt>Label</dt><dd>{html.escape(e["kick"])}</dd><dt>Tekst</dt><dd>{html.escape(e["sub"])}</dd><dt>Knop</dt><dd>{html.escape(e["cta"])}</dd></dl><p class="why">{html.escape(why.get(n,""))}</p>'
    flagtxt=f'<p class="flag">{html.escape(fl)}</p>' if fl else ''
    cards.append(f'''<article class="card" data-id="{key}" data-kind="{'new' if e else ('chk' if fl else 'plain')}">
<header class="ch"><span class="num">{n}</span><h2>{html.escape(lab)}</h2>{tags}</header>
{media}{toggle}{newtxt}{flagtxt}
<div class="actions"><button type="button" class="st" data-s="approved">Goed</button><button type="button" class="st" data-s="changes">Aanpassen</button><button type="button" class="st" data-s="rejected">Niet gebruiken</button></div>
<textarea id="note-{key}" class="note" rows="2" placeholder="Opmerking (optioneel)"></textarea>
<div class="meta"><span class="saved"></span></div>
</article>''')
page=f'''<title>ACA TV-check</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@700;800&family=Inter:wght@400;500;600;700&display=swap">
<style>
/* Layout: dark control-room sheet, same navy as the TV slides, lime only for state and the brand tag */
:root{{--bg:#071321;--panel:#0d1b2d;--panel2:#132439;--line:#1f3350;--fg:#eef2ee;--mute:#9fb0c3;--lime:#CDEB4B;--amber:#f2b84b;--red:#ef6b6b;--green:#7bd389;--ink:#071321;--font:Inter,system-ui,sans-serif;--disp:"Inter Tight",Inter,system-ui,sans-serif;color-scheme:dark}}
@media (prefers-color-scheme: light){{:root:not([data-theme="dark"]){{--bg:#f3f5f1;--panel:#ffffff;--panel2:#e9eee6;--line:#d3dbcf;--fg:#0b1626;--mute:#56657a;--lime:#7a9a00;--amber:#b57b00;--red:#c43d3d;--green:#2f8f4a;--ink:#ffffff;color-scheme:light}}}}
:root[data-theme="light"]{{--bg:#f3f5f1;--panel:#ffffff;--panel2:#e9eee6;--line:#d3dbcf;--fg:#0b1626;--mute:#56657a;--lime:#7a9a00;--amber:#b57b00;--red:#c43d3d;--green:#2f8f4a;--ink:#ffffff;color-scheme:light}}
*{{box-sizing:border-box}}
body{{background:var(--bg);color:var(--fg);font-family:var(--font);margin:0;padding-block:0 48px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
.top{{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--bg);padding-block:18px 12px;border-bottom:1px solid var(--line);margin-bottom:20px}}
body::before{{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--bg)}}
h1{{font:800 clamp(24px,4vw,34px)/1.05 var(--disp);margin:0 0 6px;text-transform:uppercase;letter-spacing:-.01em}}
.sub{{color:var(--mute);margin:0 0 12px;max-width:70ch;font-size:15px}}
.bar{{display:flex;flex-wrap:wrap;gap:8px;align-items:center}}
.chip{{border:1px solid var(--line);background:var(--panel);color:var(--fg);border-radius:999px;padding:7px 13px;font:600 13px/1 var(--font);cursor:pointer}}
.chip.on{{background:var(--lime);color:var(--ink);border-color:var(--lime)}}
.counts{{margin-left:auto;display:flex;gap:14px;font:500 13px/1 var(--font);color:var(--mute);font-variant-numeric:tabular-nums}}
.counts b{{color:var(--fg)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:18px}}
.card{{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px;display:flex;flex-direction:column;gap:10px;min-width:0}}
.card[data-st="approved"]{{border-color:var(--green)}}
.card[data-st="changes"]{{border-color:var(--amber)}}
.card[data-st="rejected"]{{border-color:var(--red);opacity:.75}}
.ch{{display:flex;align-items:center;gap:10px;flex-wrap:wrap}}
.num{{font:800 13px/1 var(--disp);background:var(--panel2);padding:6px 8px;border-radius:6px;letter-spacing:.04em}}
.ch h2{{font:700 16px/1.2 var(--font);margin:0;flex:1;min-width:0}}
.tag{{font:700 11px/1 var(--font);letter-spacing:.06em;text-transform:uppercase;padding:5px 8px;border-radius:4px}}
.tag.new{{background:var(--lime);color:var(--ink)}}
.tag.chk{{background:var(--amber);color:var(--ink)}}
.media{{aspect-ratio:16/9;max-width:100%;background:#071321;border-radius:6px;overflow:hidden}}
.media img{{width:100%;height:100%;object-fit:cover;display:block}}
.seg{{display:inline-flex;border:1px solid var(--line);border-radius:999px;overflow:hidden;align-self:flex-start}}
.segbtn{{background:transparent;color:var(--fg);border:0;padding:7px 14px;font:600 13px/1 var(--font);cursor:pointer}}
.segbtn.on{{background:var(--panel2)}}
.txt{{margin:0;display:grid;grid-template-columns:auto 1fr;gap:4px 10px;font-size:13px}}
.txt dt{{color:var(--mute);font-weight:600}} .txt dd{{margin:0;min-width:0}}
.why{{margin:0;font-size:13px;color:var(--mute);border-left:3px solid var(--lime);padding-left:10px}}
.flag{{margin:0;font-size:13px;border-left:3px solid var(--amber);padding-left:10px}}
.actions{{display:flex;gap:6px;flex-wrap:wrap}}
.st{{flex:1;min-width:90px;border:1px solid var(--line);background:var(--panel2);color:var(--fg);border-radius:8px;padding:10px 8px;font:600 13px/1 var(--font);cursor:pointer}}
.st:focus-visible,.chip:focus-visible,.segbtn:focus-visible{{outline:2px solid var(--lime);outline-offset:2px}}
.card[data-st="approved"] .st[data-s="approved"]{{background:var(--green);color:var(--ink);border-color:var(--green)}}
.card[data-st="changes"] .st[data-s="changes"]{{background:var(--amber);color:var(--ink);border-color:var(--amber)}}
.card[data-st="rejected"] .st[data-s="rejected"]{{background:var(--red);color:#fff;border-color:var(--red)}}
.note{{width:100%;background:var(--bg);color:var(--fg);border:1px solid var(--line);border-radius:8px;padding:9px 10px;font:400 13px/1.4 var(--font);resize:vertical}}
.meta{{font-size:12px;color:var(--mute);min-height:14px}}
.hint{{margin:18px 0 0;color:var(--mute);font-size:13px}}
@media (prefers-reduced-motion:no-preference){{.card{{transition:border-color .2s}}}}
</style>
<div class="top">
<h1>TV-slides: check en akkoord</h1>
<p class="sub">46 slides voor het scherm bij Poort Padel. 8 zijn aangepast met de actuele info van allcourtacademy.com (winterreeks, voorjaarsreeks, Kids Kamp). Bij 6 andere staat een vraag. Kies per slide Goed, Aanpassen of Niet gebruiken. Alles wordt direct opgeslagen.</p>
<div class="bar">
<button type="button" class="chip on" data-f="all">Alles</button>
<button type="button" class="chip" data-f="new">Aangepast</button>
<button type="button" class="chip" data-f="chk">Even checken</button>
<button type="button" class="chip" data-f="open">Nog niet beoordeeld</button>
<div class="counts"><span>Goed <b id="c-approved">0</b></span><span>Aanpassen <b id="c-changes">0</b></span><span>Niet <b id="c-rejected">0</b></span><span>Open <b id="c-open">46</b></span></div>
</div></div>
<div class="grid" id="grid">
{''.join(cards)}
</div>
<p class="hint">Oud en Nieuw wissel je per aangepaste slide met de knop boven de tekst. Opmerkingen worden na een seconde opgeslagen.</p>
<script>
(function(){{
const COL='tvcheck_v1';
const cards=[...document.querySelectorAll('.card')];
const state={{}};
let db=null;
function ls(k,v){{try{{if(v===undefined)return JSON.parse(localStorage.getItem(k)||'null');localStorage.setItem(k,JSON.stringify(v));}}catch(e){{return null}}}}
function render(){{
  const c={{approved:0,changes:0,rejected:0,open:0}};
  for(const el of cards){{
    const r=state[el.dataset.id]||{{}};
    if(r.status) el.dataset.st=r.status; else delete el.dataset.st;
    c[r.status||'open']++;
    const ta=el.querySelector('.note');
    if(document.activeElement!==ta && (r.note||'')!==ta.value) ta.value=r.note||'';
    el.querySelector('.saved').textContent=r.updatedAt?('Opgeslagen '+new Date(r.updatedAt).toLocaleString('nl-NL',{{day:'numeric',month:'short',hour:'2-digit',minute:'2-digit'}})):'';
  }}
  for(const k in c) document.getElementById('c-'+k).textContent=c[k];
  applyFilter();
}}
let filter='all';
function applyFilter(){{
  for(const el of cards){{
    const r=state[el.dataset.id]||{{}};
    let show=true;
    if(filter==='new') show=el.dataset.kind==='new';
    else if(filter==='chk') show=el.dataset.kind==='chk';
    else if(filter==='open') show=!r.status;
    el.hidden=!show;
  }}
}}
async function save(id,patch){{
  const rec=Object.assign({{}},state[id]||{{}},patch,{{updatedAt:Date.now()}});
  state[id]=rec; render();
  ls(COL+':'+id,rec);
  if(db){{try{{await db.doc(COL+'/'+id).set(rec);}}catch(e){{console.warn('db set',e);}}}}
}}
for(const el of cards){{
  const id=el.dataset.id;
  const cached=ls(COL+':'+id); if(cached) state[id]=cached;
  el.querySelectorAll('.st').forEach(b=>b.addEventListener('click',()=>{{
    const cur=(state[id]||{{}}).status; save(id,{{status:cur===b.dataset.s?null:b.dataset.s}});
  }}));
  let t; const ta=el.querySelector('.note');
  ta.addEventListener('input',()=>{{clearTimeout(t);t=setTimeout(()=>save(id,{{note:ta.value}}),900);}});
  ta.addEventListener('blur',()=>{{clearTimeout(t);if((state[id]||{{}}).note!==ta.value)save(id,{{note:ta.value}});}});
  const img=el.querySelector('img');
  el.querySelectorAll('.segbtn').forEach(b=>b.addEventListener('click',()=>{{
    el.querySelectorAll('.segbtn').forEach(x=>x.classList.toggle('on',x===b));
    img.src=b.dataset.v==='new'?img.dataset.new:img.dataset.orig;
  }}));
  if(img.dataset.new) img.src=img.dataset.new;
}}
document.querySelectorAll('.chip').forEach(ch=>ch.addEventListener('click',()=>{{
  document.querySelectorAll('.chip').forEach(x=>x.classList.toggle('on',x===ch));
  filter=ch.dataset.f; applyFilter();
}}));
render();
(async()=>{{
  try{{
    if(!window.claude||!window.claude.use) return;
    db=await window.claude.use('db'); if(!db) return;
    db.collection(COL).onSnapshot(snap=>{{
      for(const d of snap.docs){{ const r=d.data(); if(!r) continue; const cur=state[d.id]; if(!cur||(r.updatedAt||0)>=(cur.updatedAt||0)){{state[d.id]=r; ls(COL+':'+d.id,r);}} }}
      render();
    }},e=>console.warn('db',e));
  }}catch(e){{console.warn('db init',e);}}
}})();
}})();
</script>
'''
open(OUTDIR+'/index.html','w').write(page)
print(len(cards),'cards', os.path.getsize(OUTDIR+'/index.html'),'bytes')

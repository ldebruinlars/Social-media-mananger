import json,sys
D=sys.argv[1]
o=json.load(open(D+'/tvwork/order.json')); seq=o['seq']; files=o['files']; theme=o['theme']
NEW=("09","11","12","41","42","43","44","47","48")
cells=''.join(f'<li class="o-{theme[n]}"><img src="{"nieuw" if n in NEW else "orig"}/{files[n]}" alt="" loading="lazy"><span>{i+1}</span><b>{n}</b></li>' for i,n in enumerate(seq))
sec=f'''
<section class="order" id="volgorde">
<h2 class="oh">Volgorde van de slideshow</h2>
<p class="sub">Zonder de 15 afgekeurde slides. Kids Kamp (11 en 48) komt als eerste en daarna elke zesde slide terug, elke 48 seconden. Daartussen jeugd, lessenreeks en All Court Academy. De loop is {len(seq)} slides, 8 seconden per slide, ruim 5 en een halve minuut.</p>
<ul class="legend"><li class="o-kamp">Kids Kamp ({sum(1 for s in seq if theme[s]=="kamp")}x)</li><li class="o-jeugd">Jeugd ({sum(1 for s in seq if theme[s]=="jeugd")}x)</li><li class="o-reeks">Lessenreeks ({sum(1 for s in seq if theme[s]=="reeks")}x)</li><li class="o-aca">All Court Academy ({sum(1 for s in seq if theme[s]=="aca")}x)</li></ul>
<ol class="strip">{cells}</ol>
<textarea id="note-volgorde" class="note" rows="2" placeholder="Opmerking over de volgorde (optioneel)"></textarea>
<div class="meta"><span class="saved" id="saved-volgorde"></span></div>
</section>
'''
css='''
.order{margin-top:36px;border-top:1px solid var(--line);padding-top:22px}
.oh{font:800 22px/1.1 var(--disp);text-transform:uppercase;margin:0 0 8px;letter-spacing:-.01em}
.legend{list-style:none;padding:0;margin:0 0 12px;display:flex;flex-wrap:wrap;gap:8px 16px;font:600 13px/1 var(--font)}
.legend li::before{content:"";display:inline-block;width:12px;height:12px;border-radius:3px;margin-right:6px;vertical-align:-1px;background:var(--c)}
.o-kamp{--c:var(--lime)} .o-jeugd{--c:var(--amber)} .o-reeks{--c:#5aa9ff} .o-aca{--c:var(--mute)}
.strip{list-style:none;padding:0;margin:0 0 12px;display:grid;grid-template-columns:repeat(auto-fill,minmax(96px,1fr));gap:8px}
.strip li{position:relative;aspect-ratio:16/9;max-width:100%;border-radius:4px;overflow:hidden;background:#071321;border-bottom:4px solid var(--c)}
.strip img{width:100%;height:100%;object-fit:cover;display:block}
.strip span{position:absolute;left:4px;top:4px;font:700 10px/1 var(--font);background:rgba(7,19,33,.8);color:#fff;padding:3px 4px;border-radius:3px}
.strip b{position:absolute;right:4px;top:4px;font:800 10px/1 var(--disp);background:var(--c);color:#071321;padding:3px 4px;border-radius:3px}
'''
p=D+'/tvcheck/index.html'; s=open(p).read()
assert 'id="volgorde"' not in s
s=s.replace('</style>',css+'</style>',1)
s=s.replace('<p class="hint">',sec+'<p class="hint">',1)
s=s.replace("document.querySelectorAll('.chip').forEach(ch=>","""(function(){const ta=document.getElementById('note-volgorde');const id='volgorde';const cached=ls(COL+':'+id);if(cached){state[id]=cached;ta.value=cached.note||'';}
let t;ta.addEventListener('input',()=>{clearTimeout(t);t=setTimeout(()=>save(id,{note:ta.value}),900);});})();
document.querySelectorAll('.chip').forEach(ch=>""",1)
s=s.replace("  for(const k in c) document.getElementById('c-'+k).textContent=c[k];","  for(const k in c) document.getElementById('c-'+k).textContent=c[k];\n  const v=state['volgorde'];const sv=document.getElementById('saved-volgorde');if(sv)sv.textContent=v&&v.updatedAt?('Opgeslagen '+new Date(v.updatedAt).toLocaleString('nl-NL',{day:'numeric',month:'short',hour:'2-digit',minute:'2-digit'})):'';",1)
open(p,'w').write(s); print('order section added')

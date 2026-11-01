import sys,subprocess,json,os,html
# Poster zonder tv-mockup, in meerdere formaten voor het schermsysteem van Poort Padel.
D=sys.argv[1]; P=D+'/posts'; OUT=P+'/tv_formats'
CH='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
posts=json.load(open(P+'/tv_posts.json')); only=sys.argv[2:]
FORMATS={ # naam: (breedte, hoogte, schaal van de tekst t.o.v. het 1180px-venster, hoogte verloop als deel van H)
 '1_staand_1080x1350':(1080,1350,0.92,0.56),
 '2_vierkant_1080x1080':(1080,1080,0.92,0.64),
 '3_liggend_1920x1080':(1920,1080,1.30,0.68),
}
def crop(src,dst,w,h,fx,fy,zoom=1.0):
    iw,ih=map(int,subprocess.run(['identify','-format','%w %h',src],capture_output=True,text=True).stdout.split())
    s=max(w/iw,h/ih)*zoom; cw,ch=int(w/s),int(h/s)
    x=int(min(max(fx*iw-cw/2,0),iw-cw)); y=int(min(max(fy*ih-ch/2,0),ih-ch))
    subprocess.run(['convert',src,'-crop',f'{cw}x{ch}+{x}+{y}','+repage','-resize',f'{w}x{h}!','-quality','92',dst],check=True)
def css(W,H,S,G):
    r=lambda v: f'{round(v*S)}px'
    return f'''html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:#0B131F}}
.s{{position:relative;width:{W}px;height:{H}px;font-family:Inter,sans-serif;color:#fff;overflow:hidden;background:#0B131F}}
.ph{{position:absolute;inset:0;background-size:cover;background-position:center}}
.gt{{position:absolute;left:0;right:0;top:0;height:{round(H*.22)}px;background:linear-gradient(180deg,rgba(11,19,31,.5),rgba(11,19,31,0))}}
.gb{{position:absolute;left:0;right:0;bottom:0;height:{round(H*G)}px;background:linear-gradient(0deg,rgba(11,19,31,.96) 0%,rgba(11,19,31,.9) 34%,rgba(11,19,31,.5) 66%,rgba(11,19,31,0) 100%)}}
.lock{{position:absolute;right:{r(56)};top:{r(44)};display:flex;align-items:center;gap:{r(30)}}}
.lock img{{height:{r(110)};width:auto;display:block;filter:drop-shadow(0 2px 6px rgba(0,0,0,.45))}}
.lock svg.x{{width:{r(34)};height:{r(34)};display:block;opacity:.92;filter:drop-shadow(0 2px 4px rgba(0,0,0,.5))}}
.txt{{position:absolute;left:{r(64)};right:{r(64)};bottom:{r(56)}}}
.kick{{display:flex;align-items:center;gap:{r(14)};color:#C4D44E;font:700 {r(28)}/1 Inter,sans-serif;letter-spacing:.12em;text-transform:uppercase;margin-bottom:{r(20)};text-shadow:0 1px 2px rgba(0,0,0,.6)}}
.kick::before{{content:"";width:{r(44)};height:3px;background:#C4D44E;flex:none}}
h1{{margin:0 0 {r(14)};font:800 var(--hs)/1.02 "Inter Tight",Inter,sans-serif;text-transform:uppercase;letter-spacing:-.005em;max-width:{round(W-128*S)}px}}
.sub{{font:500 {r(40)}/1.25 Inter,sans-serif;color:#F2F6F2;margin:0 0 {r(34)};max-width:{round(W-128*S)}px}}
.pill{{display:inline-flex;align-items:center;background:#C4D44E;color:#0B131F;font:800 {r(32)}/1 Inter,sans-serif;letter-spacing:.01em;text-transform:uppercase;padding:0 {r(46)};height:{r(98)};border-radius:999px;white-space:nowrap}}
'''
for name,(W,H,S,G) in FORMATS.items():
    od=f'{OUT}/{name}'; os.makedirs(od,exist_ok=True)
    for p in posts:
        if only and p['id'] not in only: continue
        src=D+'/drive/'+p['photo']; bg=f"{P}/{p['id']}_{name}_bg.jpg"
        crop(src,bg,W,H,p.get('fx',.5),p.get('fy',.5),p.get('z',1.0))
        hs=round((p.get('hs', 80 if max(len(l) for l in p['head'])<=14 else 70)+12)*S)
        lines='<br>'.join(html.escape(l) for l in p['head'])
        page=f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@800&family=Inter:wght@500;600;700;800&display=swap"><style>{css(W,H,S,G)}</style></head><body>
<div class="s" style="--hs:{hs}px"><div class="ph" style="background-image:url(file://{bg})"></div><div class="gt"></div><div class="gb"></div>
<div class="lock"><img src="file://{P}/aca_logo_new.png"><svg class="x" viewBox="0 0 34 34"><path d="M6 6L28 28M28 6L6 28" stroke="#fff" stroke-width="5" stroke-linecap="round"/></svg><img src="file://{P}/pp_logo_white.png"></div>
<div class="txt"><div class="kick">{html.escape(p['kick'])}</div><h1>{lines}</h1><p class="sub">{html.escape(p['sub'])}</p>
<span class="pill">{html.escape(p['cta'])}&nbsp;&nbsp;↗</span></div></div></body></html>'''
        hp=f"{P}/{p['id']}_{name}.html"; open(hp,'w').write(page); png=f"{P}/{p['id']}_{name}.png"
        subprocess.run([CH,'--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--allow-file-access-from-files',f'--window-size={W},{H+120}','--virtual-time-budget=8000',f'--screenshot={png}',f'file://{hp}'],capture_output=True)
        subprocess.run(['convert',png,'-crop',f'{W}x{H}+0+0','+repage','-quality','90',f"{od}/{p['id']}.jpg"]); print(name,p['id'],'ok')

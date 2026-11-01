import sys,subprocess,json,os,html
D=sys.argv[1]; P=D+'/posts'; OUT=P+'/tv_final'; os.makedirs(OUT,exist_ok=True)
CH='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
posts=json.load(open(P+'/tv_posts.json')); only=sys.argv[2:]
W,H=1920,1080
# window on the right: leaves the left 660px flat teal for the Poort Padel clock
WX,WY,WW,WH=700,40,1180,1000
def crop(src,dst,w,h,fx,fy,zoom=1.0):
    iw,ih=map(int,subprocess.run(['identify','-format','%w %h',src],capture_output=True,text=True).stdout.split())
    s=max(w/iw,h/ih)*zoom; cw,ch=int(w/s),int(h/s)
    x=int(min(max(fx*iw-cw/2,0),iw-cw)); y=int(min(max(fy*ih-ch/2,0),ih-ch))
    subprocess.run(['convert',src,'-crop',f'{cw}x{ch}+{x}+{y}','+repage','-resize',f'{w}x{h}!','-quality','92',dst],check=True)
CSS=f'''html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:#0091B1}}
.s{{position:relative;width:{W}px;height:{H}px;font-family:Inter,sans-serif;color:#fff;overflow:hidden;background:#0091B1}}
.win{{position:absolute;left:{WX}px;top:{WY}px;width:{WW}px;height:{WH}px;border-radius:44px;overflow:hidden;box-shadow:0 30px 80px rgba(0,40,60,.45)}}
.ph{{position:absolute;inset:0;background-size:cover;background-position:center}}
.gt{{position:absolute;left:0;right:0;top:0;height:240px;background:linear-gradient(180deg,rgba(11,19,31,.5),rgba(11,19,31,0))}}
.gb{{position:absolute;left:0;right:0;bottom:0;height:660px;background:linear-gradient(0deg,rgba(11,19,31,.96) 0%,rgba(11,19,31,.9) 34%,rgba(11,19,31,.5) 66%,rgba(11,19,31,0) 100%)}}
.lock{{position:absolute;right:56px;top:44px;display:flex;align-items:center;gap:26px}}
.lock img{{height:74px;width:auto;display:block;filter:drop-shadow(0 2px 6px rgba(0,0,0,.45))}}
.lock .x{{font:600 40px/1 Inter,sans-serif;color:#fff;opacity:.85}}
.txt{{position:absolute;left:64px;right:64px;bottom:56px}}
.kick{{display:flex;align-items:center;gap:14px;color:#C4D44E;font:700 28px/1 Inter,sans-serif;letter-spacing:.12em;text-transform:uppercase;margin-bottom:20px;text-shadow:0 1px 2px rgba(0,0,0,.6)}}
.kick::before{{content:"";width:44px;height:3px;background:#C4D44E;flex:none}}
h1{{margin:0 0 14px;font:800 var(--hs)/1.02 "Inter Tight",Inter,sans-serif;text-transform:uppercase;letter-spacing:-.005em;max-width:980px}}
.sub{{font:500 40px/1.25 Inter,sans-serif;color:#F2F6F2;margin:0 0 34px;max-width:980px}}
.cta{{display:flex;align-items:center;gap:24px}}
.pill{{background:#C4D44E;color:#0B131F;font:800 32px/1 Inter,sans-serif;letter-spacing:.01em;text-transform:uppercase;padding:0 46px;height:98px;display:flex;align-items:center;border-radius:999px;white-space:nowrap}}
.lb{{font:600 22px/1.25 Inter,sans-serif;letter-spacing:.04em;text-transform:uppercase;color:#DCE5DF}}
'''
for p in posts:
    if p['id'].startswith('s34'): continue
    if only and p['id'] not in only: continue
    src=D+'/drive/'+p['photo']; bg=f"{P}/{p['id']}_fbg.jpg"
    crop(src,bg,WW,WH,p.get('fx',.5),p.get('fy',.5),p.get('z',1.0))
    hs=p.get('hs', 80 if max(len(l) for l in p['head'])<=14 else 70)+12
    lines='<br>'.join(html.escape(l) for l in p['head'])
    page=f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@800&family=Inter:wght@500;600;700;800&display=swap"><style>{CSS}</style></head><body>
<div class="s" style="--hs:{hs}px"><div class="win"><div class="ph" style="background-image:url(file://{bg})"></div><div class="gt"></div><div class="gb"></div>
<div class="lock"><img src="file://{P}/aca_logo.png"><span class="x">×</span><img src="file://{P}/pp_logo_white.png"></div>
<div class="txt"><div class="kick">{html.escape(p['kick'])}</div><h1>{lines}</h1><p class="sub">{html.escape(p['sub'])}</p>
<div class="cta"><span class="pill">{html.escape(p['cta'])}&nbsp;&nbsp;↗</span></div></div></div></div></body></html>'''
    hp=f"{P}/{p['id']}_f.html"; open(hp,'w').write(page); png=f"{P}/{p['id']}_f.png"
    subprocess.run([CH,'--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--allow-file-access-from-files',f'--window-size={W},{H+120}','--virtual-time-budget=8000',f'--screenshot={png}',f'file://{hp}'],capture_output=True)
    subprocess.run(['convert',png,'-crop',f'{W}x{H}+0+0','+repage','-quality','90',f"{OUT}/{p['id']}.jpg"]); print(p['id'],'ok')

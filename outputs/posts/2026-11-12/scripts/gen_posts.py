import sys,subprocess,json,os,html
D=sys.argv[1]; P=D+'/posts'; OUT=P+'/out'; os.makedirs(OUT,exist_ok=True)
CH='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
posts=json.load(open(P+'/posts.json')); only=sys.argv[2:]
W,H=1080,1350
def crop(src,dst,w,h,fx,fy,zoom=1.0):
    iw,ih=map(int,subprocess.run(['identify','-format','%w %h',src],capture_output=True,text=True).stdout.split())
    s=max(w/iw,h/ih)*zoom; cw,ch=int(w/s),int(h/s)
    x=int(min(max(fx*iw-cw/2,0),iw-cw)); y=int(min(max(fy*ih-ch/2,0),ih-ch))
    subprocess.run(['convert',src,'-crop',f'{cw}x{ch}+{x}+{y}','+repage','-resize',f'{w}x{h}!','-quality','92',dst],check=True)
CSS=f'''html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:#0B131F}}
.p{{position:relative;width:{W}px;height:{H}px;font-family:Inter,sans-serif;color:#fff;overflow:hidden}}
.ph{{position:absolute;inset:0;background-size:cover;background-position:center}}
.gt{{position:absolute;left:0;right:0;top:0;height:260px;background:linear-gradient(180deg,rgba(11,19,31,.55),rgba(11,19,31,0))}}
.gb{{position:absolute;left:0;right:0;bottom:0;height:720px;background:linear-gradient(0deg,rgba(11,19,31,.97) 0%,rgba(11,19,31,.92) 38%,rgba(11,19,31,.55) 68%,rgba(11,19,31,0) 100%)}}
.aca{{position:absolute;left:60px;top:52px;width:250px}}
.pp{{position:absolute;right:60px;top:60px;width:150px}}
.txt{{position:absolute;left:60px;right:60px;bottom:56px}}
.kick{{display:flex;align-items:center;gap:14px;color:#C4D44E;font:700 25px/1 Inter,sans-serif;letter-spacing:.12em;text-transform:uppercase;margin-bottom:24px;text-shadow:0 1px 2px rgba(0,0,0,.6)}}
.kick::before{{content:"";width:44px;height:3px;background:#C4D44E;flex:none}}
h1{{margin:0 0 14px;font:800 var(--hs)/1.02 "Inter Tight",Inter,sans-serif;text-transform:uppercase;letter-spacing:-.005em}}
.sub{{font:500 28px/1.3 Inter,sans-serif;color:#DCE5DF;margin:0 0 34px}}
.cta{{display:flex;align-items:center;gap:22px}}
.pill{{background:#C4D44E;color:#0B131F;font:800 27px/1 Inter,sans-serif;letter-spacing:.01em;text-transform:uppercase;padding:0 42px;height:88px;display:flex;align-items:center;border-radius:999px;white-space:nowrap}}
.lb{{font:600 21px/1.25 Inter,sans-serif;letter-spacing:.04em;text-transform:uppercase;color:#DCE5DF}}
'''
for p in posts:
    if only and p['id'] not in only: continue
    src=D+'/drive/'+p['photo']; bg=f"{P}/{p['id']}_bg.jpg"
    crop(src,bg,W,H,p.get('fx',.5),p.get('fy',.5),p.get('z',1.0))
    hs=p.get('hs', 80 if max(len(l) for l in p['head'])<=14 else 70)
    lines='<br>'.join(html.escape(l) for l in p['head'])
    page=f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@800&family=Inter:wght@500;600;700;800&display=swap"><style>{CSS}</style></head><body>
<div class="p" style="--hs:{hs}px"><div class="ph" style="background-image:url(file://{bg})"></div><div class="gt"></div><div class="gb"></div>
<img class="aca" src="file://{P}/aca_logo.png"><img class="pp" src="file://{P}/pp_logo_white.png">
<div class="txt"><div class="kick">{html.escape(p['kick'])}</div><h1>{lines}</h1><p class="sub">{html.escape(p['sub'])}</p>
<div class="cta"><span class="pill">{html.escape(p['cta'])}&nbsp;&nbsp;↗</span><span class="lb">Link in bio · allcourtacademy.com</span></div></div></div></body></html>'''
    hp=f"{P}/{p['id']}.html"; open(hp,'w').write(page); png=f"{P}/{p['id']}.png"
    subprocess.run([CH,'--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--allow-file-access-from-files',f'--window-size={W},{H}','--virtual-time-budget=8000',f'--screenshot={png}',f'file://{hp}'],capture_output=True)
    subprocess.run(['convert',png,'-quality','92',f"{OUT}/{p['id']}.jpg"]); print(p['id'],'ok')

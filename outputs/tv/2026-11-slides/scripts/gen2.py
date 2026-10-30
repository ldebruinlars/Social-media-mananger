import sys,subprocess,json,os,html
D=sys.argv[1]; W=D+'/tvwork'; OUT=W+'/out2'; os.makedirs(OUT,exist_ok=True)
CH='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
K=D+'/drive/kamp/'; O=D+'/drive/open/'
slides=json.load(open(W+'/edits2.json'))
only=sys.argv[2:]
def crop(src,dst,w,h,fx=0.5,fy=0.5,zoom=1.0):
    # cover-crop src to w:h with focus point (fx,fy) in 0..1 and optional zoom-in
    iw,ih=map(int,subprocess.run(['identify','-format','%w %h',src],capture_output=True,text=True).stdout.split())
    s=max(w/iw,h/ih)*zoom
    cw,ch=int(w/s),int(h/s)
    x=int(min(max(fx*iw-cw/2,0),iw-cw)); y=int(min(max(fy*ih-ch/2,0),ih-ch))
    subprocess.run(['convert',src,'-crop',f'{cw}x{ch}+{x}+{y}','+repage','-resize',f'{w}x{h}!','-quality','92',dst],check=True)
CSS='''html,body{margin:0;width:1920px;height:1080px;overflow:hidden;background:#071321}
.slide{position:relative;width:1920px;height:1080px;background:#071321;font-family:Inter,sans-serif;color:#fff}
.logo{position:absolute;left:109px;top:86px;width:314px;height:136px}
.txt{position:absolute;left:110px;bottom:84px}
.kick{display:flex;align-items:center;gap:16px;color:#CDEB4B;font:700 26px/1 Inter,sans-serif;letter-spacing:.03em;text-transform:uppercase;margin-bottom:28px}
.kick::before{content:"";width:40px;height:4px;background:#CDEB4B}
h1{margin:0 0 16px;font:800 var(--hs,96px)/1.04 "Inter Tight",Inter,sans-serif;text-transform:uppercase;letter-spacing:-.005em;max-width:var(--tw,800px)}
.sub{font:400 32px/1.3 Inter,sans-serif;color:#E3E8E1;margin:0 0 38px;max-width:var(--tw,800px)}
.cta{display:flex;align-items:center;gap:36px}
.pill{background:#CDEB4B;color:#071321;font:700 26px/1 Inter,sans-serif;letter-spacing:.02em;text-transform:uppercase;padding:21px 32px;border-radius:999px}
.url{font:700 26px/1 Inter,sans-serif;letter-spacing:.03em;text-transform:uppercase;color:#fff}
.col{position:absolute;top:0;height:1080px;background-size:cover}
.c1{left:940px;width:486px}.c2{left:1434px;width:486px}
.photo{position:absolute;inset:0;background-size:cover}
.grad{position:absolute;inset:0;background:linear-gradient(90deg,rgba(7,19,33,.96) 0%,rgba(7,19,33,.88) 30%,rgba(7,19,33,.45) 52%,rgba(7,19,33,0) 70%),linear-gradient(0deg,rgba(7,19,33,.85) 0%,rgba(7,19,33,0) 45%)}
'''
for s in slides:
    if only and s['file'] not in only: continue
    base=s['file'][:-4]
    lines='<br>'.join(html.escape(l) for l in s['head'])
    txt=f'<div class="txt"><div class="kick">{html.escape(s["kick"])}</div><h1>{lines}</h1><p class="sub">{html.escape(s["sub"])}</p><div class="cta"><span class="pill">{html.escape(s["cta"])}</span><span class="url">allcourtacademy.com</span></div></div>'
    style=f'--hs:{s.get("hs",96)}px;--tw:{s.get("tw",800)}px'
    if s['tpl']=='panel':
        p1=f'{W}/{base}_c1.jpg'; p2=f'{W}/{base}_c2.jpg'
        a=s['p1']; b=s['p2']
        crop(K+a['f'],p1,486*2,1080*2,a.get('fx',.5),a.get('fy',.5),a.get('z',1))
        crop(K+b['f'],p2,486*2,1080*2,b.get('fx',.5),b.get('fy',.5),b.get('z',1))
        body=f'<div class="slide" style="{style}"><div class="col c1" style="background-image:url(file://{p1})"></div><div class="col c2" style="background-image:url(file://{p2})"></div><img class="logo" src="file://{W}/logo_t.png">{txt}</div>'
    else:
        p=f'{W}/{base}_bg.jpg'; a=s['p']
        src=(K if a['f'].startswith('frame') else O)+a['f']
        crop(src,p,1920,1080,a.get('fx',.5),a.get('fy',.5),a.get('z',1))
        body=f'<div class="slide" style="{style}"><div class="photo" style="background-image:url(file://{p})"></div><div class="grad"></div><img class="logo" src="file://{W}/logo_t.png">{txt}</div>'
    page=f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@700;800&family=Inter:wght@400;500;600;700&display=swap"><style>{CSS}</style></head><body>{body}</body></html>'
    hp=f'{W}/{base}_v2.html'; open(hp,'w').write(page)
    png=f'{W}/{base}_v2.png'
    subprocess.run([CH,'--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--allow-file-access-from-files','--window-size=1920,1080','--virtual-time-budget=8000',f'--screenshot={png}',f'file://{hp}'],capture_output=True)
    subprocess.run(['convert',png,'-quality','90',f'{OUT}/{s["file"]}'])
    print(s['file'],'ok')

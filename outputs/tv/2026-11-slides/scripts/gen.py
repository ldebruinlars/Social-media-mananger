import sys,subprocess,json,os,html,re
D=sys.argv[1]; W=D+'/tvwork'; SRC=D+'/tvzip/tv'; OUT=W+'/out'
CH='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
slides=json.load(open(W+'/edits.json'))
only=sys.argv[2:]  # optional subset
def bbox(path,y0,y1,xmax=1780):
    cmd=['convert',path,'-crop',f'{xmax}x{y1-y0}+0+{y0}','+repage','-colorspace','gray','-threshold','50%','-format','%@','info:-']
    out=subprocess.run(cmd,capture_output=True,text=True).stdout.strip()
    m=re.match(r'(\d+)x(\d+)\+(\d+)\+(\d+)',out)
    if not m: return None
    w,h,x,y=map(int,m.groups()); return (x, y+y0, x+w, y+y0+h)
BANDS=[(520,835),(835,905),(905,1040)]
for s in slides:
    if only and s['file'] not in only: continue
    src=f"{SRC}/{s['file']}"
    row=subprocess.run(['convert',src,'-crop','1920x1+0+300','+repage','-depth','8','txt:-'],capture_output=True,text=True).stdout.splitlines()[1:]
    cols=[]
    for ln in row:
        m=re.match(r'(\d+),0: \((\d+),(\d+),(\d+)',ln)
        if m: cols.append(tuple(map(int,m.groups())))
    panel = cols and abs(cols[40][1]-7)<4 and abs(cols[40][2]-19)<4 and abs(cols[40][3]-33)<4
    pe=1920
    if panel:
        for x,r,g,b in cols:
            if x>100 and (abs(r-7)>6 or abs(g-19)>6 or abs(b-33)>6): pe=x; break
    xm=[pe-12,pe-12,pe-12] if panel else [1400,1780,1400]
    boxes=[bbox(src,a,b,xm[i]) for i,(a,b) in enumerate(BANDS)]
    if panel:
        boxes=[(b[0],b[1],(pe+110 if b[2]>=pe-60 else b[2]),b[3]) if b else None for b in boxes]
    print(s['file'],'panel',panel,'pe',pe)
    covs=[]; info=[]
    top=None
    for i,(bx,(a,b)) in enumerate(zip(boxes,BANDS)):
        if not bx: continue
        x0,y0,x1,y1=bx
        if top is None: top=max(0,y0-150)
        cy0 = top if i==0 or not covs else BANDS[i][0]
        cy1 = BANDS[i][1] if i<2 else 1080
        if i==0: cy1=BANDS[1][0]
        cx1=min(1920,x1+40+220)
        feather = 'linear-gradient(180deg,transparent,#000 120px),' if not covs else ''
        covs.append(f'<div style="position:absolute;left:0;top:{cy0}px;width:{cx1}px;height:{cy1-cy0}px;background:#071321;-webkit-mask:{feather}linear-gradient(90deg,#000 calc(100% - 220px),transparent);-webkit-mask-composite:source-in;mask:{feather}linear-gradient(90deg,#000 calc(100% - 220px),transparent);mask-composite:intersect"></div>')
        info.append(bx)
    lines='<br>'.join(html.escape(l) for l in s['head'])
    page=f'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@700;800&family=Inter:wght@400;500;600;700&display=swap">
<style>html,body{{margin:0;width:1920px;height:1080px;overflow:hidden;background:#071321}}
.slide{{position:relative;width:1920px;height:1080px;background:url("file://{src}") center/cover no-repeat}}
.txt{{position:absolute;left:110px;bottom:84px;color:#fff;font-family:Inter,sans-serif}}
.kick{{display:flex;align-items:center;gap:16px;color:#CDEB4B;font:700 27px/1 Inter,sans-serif;letter-spacing:.03em;text-transform:uppercase;margin-bottom:30px}}
.kick::before{{content:"";width:40px;height:4px;background:#CDEB4B}}
h1{{margin:0 0 16px;font:800 {s.get('size',104)}px/1.04 "Inter Tight",Inter,sans-serif;text-transform:uppercase;letter-spacing:-.005em;max-width:{(pe+60) if panel else 1350}px}}
.sub{{font:400 34px/1.3 Inter,sans-serif;color:#E3E8E1;margin:0 0 40px;max-width:{(pe-160) if panel else 1300}px}}
.cta{{display:flex;align-items:center;gap:40px}}
.pill{{background:#CDEB4B;color:#071321;font:700 28px/1 Inter,sans-serif;letter-spacing:.02em;text-transform:uppercase;padding:22px 34px;border-radius:999px}}
.url{{font:700 28px/1 Inter,sans-serif;letter-spacing:.03em;text-transform:uppercase;color:#fff}}
</style></head><body><div class="slide">{''.join(covs)}
<div class="txt"><div class="kick">{html.escape(s['kick'])}</div><h1>{lines}</h1>
<p class="sub">{html.escape(s['sub'])}</p>
<div class="cta"><span class="pill">{html.escape(s['cta'])}</span><span class="url">allcourtacademy.com</span></div></div></div></body></html>'''
    hp=f"{W}/{s['file'][:-4]}.html"; open(hp,'w').write(page)
    png=f"{W}/{s['file'][:-4]}.png"
    subprocess.run([CH,'--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--allow-file-access-from-files','--window-size=1920,1080','--virtual-time-budget=8000',f'--screenshot={png}',f'file://{hp}'],capture_output=True)
    subprocess.run(['convert',png,'-quality','90',f"{OUT}/{s['file']}"])
    subprocess.run(['convert',src,f"{OUT}/{s['file']}",'-resize','900x','-append',f"{W}/cmp_{s['file'][:-4]}.png"])
    print(s['file'],info)

import json,os,subprocess,html,sys
D=sys.argv[1]; R='/home/user/Social-media-mananger/outputs/posts/2026-11-12/scripts'
posts=json.load(open(R+'/posts.json')); old=json.load(open(R+'/existing.json'))
items=[]
for p in posts:
    if p['id'].startswith('s34'): continue
    items.append(dict(id=p['id'],date=p['date'],dag=p['dag'],kop=' '.join(p['head']),pijler=p['pijler'],src=f'{D}/posts/tv_out/{p["id"]}.jpg',cap1=p['cta'],cap2='allcourtacademy.com',kind='new'))
num={'mc_01-competitie':'01-competitie','mc_02-instromen':'02-instromen','mc_03-kerstborrel':'03-kerstborrel','mc_04-jeugd':'04-jeugd','mc_05-coaches':'05-coaches','mc_06-kerstreeks':'06-kerstreeks','mc_07-feestje':'07-feestje','mc_08-voorjaarsreeks':'08-voorjaarsreeks'}
for p in old:
    if p['id']=='mc_02-instromen': continue
    items.append(dict(id=p['id'],date=p['date'],dag=p['dag'],kop=p['kop'],pijler=p['pijler'],src=f'{D}/drive/nov/{num[p["id"]]}.png',cap1='Meer weten? Vraag het aan de bar',cap2='allcourtacademy.com',kind='old'))
items.sort(key=lambda x:x['date'])
json.dump(items,open(f'{D}/tvmock/items.json','w'),ensure_ascii=False,indent=1)
TPL='''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@600;700;800&display=swap">
<style>html,body{margin:0}body{width:1920px;height:1080px;background:#0091B1;position:relative;overflow:hidden;font-family:Inter,Arial,sans-serif;color:#fff}
.logo{position:absolute;left:250px;top:140px;width:330px}
.clock{position:absolute;left:170px;top:310px}
.time{position:absolute;left:255px;top:810px;font:700 66px/1 Inter,Arial;letter-spacing:.02em}
.tag{position:absolute;left:165px;top:960px;font:800 26px/1 Inter,Arial;font-style:italic;color:#C8F23D;letter-spacing:.06em}
.panel{position:absolute;left:896px;top:60px;width:768px;height:960px;background:#000;overflow:hidden}
.panel img{width:100%;height:100%;object-fit:cover;display:block}
.cap{position:absolute;left:900px;top:860px;width:760px;text-align:center;font:700 36px/1.3 Inter,Arial}
</style></head><body>
<img class="logo" src="file://LOGO">
<svg class="clock" width="380" height="380" viewBox="-190 -190 380 380">
<g font-family="Inter,Arial" font-weight="700" font-size="34" fill="#fff" text-anchor="middle" dominant-baseline="central">NUMS</g>
<line x1="0" y1="0" x2="HX" y2="HY" stroke="#fff" stroke-width="9" stroke-linecap="round"/>
<line x1="0" y1="0" x2="MX" y2="MY" stroke="#fff" stroke-width="6" stroke-linecap="round"/>
<circle r="8" fill="#fff"/></svg>
<div class="time">TIME</div>
<div class="tag">MEET&nbsp;&nbsp;•&nbsp;&nbsp;SMASH&nbsp;&nbsp;•&nbsp;&nbsp;RELAX</div>
<div class="panel"><img src="file://SRC"></div>

</body></html>'''
import math
nums=''.join(f'<text x="{round(158*math.sin(math.radians(i*30)))}" y="{round(-158*math.cos(math.radians(i*30)))}">{i}</text>' for i in range(1,13))
hh,mm=17,20
ha=math.radians((hh%12+mm/60)*30); ma=math.radians(mm*6)
tpl=TPL.replace('NUMS',nums).replace('HX',str(round(85*math.sin(ha)))).replace('HY',str(round(-85*math.cos(ha)))).replace('MX',str(round(125*math.sin(ma)))).replace('MY',str(round(-125*math.cos(ma)))).replace('TIME',f'{hh:02d}:{mm:02d}').replace('LOGO',f'{D}/posts/pp_logo_white.png')
CH='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
only=sys.argv[2:] 
for it in items:
    if only and it['id'] not in only: continue
    h=tpl.replace('SRC',it['src']).replace('CAP1',html.escape(it['cap1'])).replace('CAP2',html.escape(it['cap2']))
    hp=f'{D}/tvmock/src/{it["id"]}.html'; open(hp,'w').write(h)
    png=f'{D}/tvmock/src/{it["id"]}.png'
    subprocess.run([CH,'--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--allow-file-access-from-files','--window-size=1920,1200','--virtual-time-budget=8000',f'--screenshot={png}',f'file://{hp}'],capture_output=True)
    subprocess.run(['convert',png,'-crop','1920x1080+0+0','+repage','-resize','1280x720','-quality','82',f'{D}/tvmock/img/{it["id"]}.jpg'])
    print(it['id'],os.path.getsize(f'{D}/tvmock/img/{it["id"]}.jpg')//1024,'KB')

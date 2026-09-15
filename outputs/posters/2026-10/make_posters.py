from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
W,H=1080,1350
M='media/'; D='drive/'
def font(sz,w=800):
    f=ImageFont.truetype(M+'Inter.ttf',sz); f.set_variation_by_axes([32,w]); return f
def hexc(h): return tuple(int(h[i:i+2],16) for i in (1,3,5))
NAVY=hexc('#0B131F'); LIME=hexc('#C4D44E'); SUB=hexc('#DCE5DF')
def crop45(path,fx=0.5,fy=0.5):
    im=Image.open(path).convert('RGB'); w,h=im.size
    if w*5>h*4: tw=int(h*4/5); th=h
    else: tw=w; th=int(w*5/4)
    x=int((w-tw)*fx); y=int((h-th)*fy)
    return im.crop((x,y,x+tw,y+th)).resize((W,H),Image.LANCZOS)
def overlay(img,start=0.50,strength=0.90):
    ov=Image.new('L',(1,H),0); px=ov.load()
    y0=int(H*start)
    for y in range(H):
        if y<y0: px[0,y]=0
        else:
            t=(y-y0)/(H-y0); t=min(1,t*1.9)
            px[0,y]=int(255*strength*(t*t*(3-2*t)))
    ov=ov.resize((W,H))
    navy=Image.new('RGB',(W,H),NAVY)
    return Image.composite(navy,img,ov)
def logo(img,path,width,x,y):
    lg=Image.open(M+path).convert('RGBA'); r=width/lg.width
    lg=lg.resize((int(lg.width*r),int(lg.height*r)),Image.LANCZOS)
    img.paste(lg,(x,y),lg)
def spaced(d,text,f,x,y,fill,sp):
    for ch in text:
        d.text((x,y),ch,font=f,fill=fill); x+=d.textlength(ch,font=f)+sp
def spaced_w(d,text,f,sp): return sum(d.textlength(c,font=f) for c in text)+sp*(len(text)-1)
def make(spec):
    img=crop45(spec['photo'],*spec.get('focus',(0.5,0.5)))
    # top shade for logos
    top=Image.new('L',(1,H),0); p=top.load()
    for y in range(260): p[0,y]=int(120*(1-y/260))
    top=top.resize((W,H)); img=Image.composite(Image.new('RGB',(W,H),NAVY),img,top)
    img=overlay(img,spec.get('ov',0.40),0.94)
    d=ImageDraw.Draw(img)
    logo(img,'aca_logo_white.png',270,60,52)
    logo(img,'poort_padel_white.png',150,W-60-150,64)
    # bottom block, anchored from pill upward
    pill_h=96; pill_y=H-70-pill_h
    fk=font(27,700); fh=font(spec.get('hsize',88),800); fs=font(30,500)
    lines=spec['head']; lh=int(spec.get('hsize',88)*1.02)
    sub_y=pill_y-46-36
    head_y=sub_y-16-lh*len(lines)
    kick_y=head_y-22-30
    # lime bar + kicker
    d.rectangle((60,kick_y+4,60+44,kick_y+7),fill=LIME)
    spaced(d,spec['kicker'],fk,117,kick_y-5,(0,0,0),5); spaced(d,spec['kicker'],fk,116,kick_y-6,LIME,5)
    for i,l in enumerate(lines):
        d.text((56,head_y+i*lh),l,font=fh,fill='white')
    d.text((60,sub_y),spec['sub'],font=fs,fill=SUB)
    # pill
    fp=font(28,800); t=spec['cta']+'  ↗'
    tw=d.textlength(t,font=fp); pw=int(tw+90)
    d.rounded_rectangle((60,pill_y,60+pw,pill_y+pill_h),radius=999,fill=LIME)
    d.text((60+45,pill_y+pill_h/2-18),t,font=fp,fill=NAVY)
    # small booking line right of pill
    fl=font(22,600); line='LINK IN BIO · ALLCOURTACADEMY.COM'
    d.text((60+pw+24,pill_y+pill_h/2-13),line,font=fl,fill=SUB)
    return img
SPECS=[
 dict(id='01_najaarsreeks',photo=D+'541525.jpg',focus=(0.5,0.35),kicker='NAJAARSREEKS · START 19 OKTOBER',head=['8 WEKEN','BETER','PADELLEN'],sub='Max 4 per groep, vaste coach, instromen kan altijd',cta='SCHRIJF JE IN'),
 dict(id='02_eerste_les',photo=D+'548441.jpg',focus=(0.5,0.3),kicker='NOOIT GEPADELD? GEEN PROBLEEM',head=['JE EERSTE LES','REGELEN','WIJ'],sub='Leenracket gratis, groep op jouw niveau, coach naast je',cta='BOEK EEN LOSSE LES'),
 dict(id='03_kids_kamp',photo=D+'549796.jpg',focus=(0.35,0.5),kicker='HERFSTVAKANTIE · 19 T/M 21 OKTOBER',head=['PADEL','KIDS KAMP'],sub='6 tot 14 jaar, 10:00 tot 12:30, rackets aanwezig, 195 euro all-in',cta='MELD JE KIND AAN'),
 dict(id='04_techniek',photo=D+'546391.jpg',focus=(0.5,0.3),kicker='TECHNIEK · LOSSE TRAINING',head=['JOUW SMASH,','ONZE','FOCUS'],sub='1 tot 4 spelers, jij kiest dag en tijd, trainer naar keuze',cta='BOEK EEN LOSSE LES'),
 dict(id='05_coach_lars',photo=M+'ACA_PoortPadel_29mei-32.jpg',focus=(0.5,0.3),kicker='ONS TEAM · 8 COACHES',head=['TRAIN MET','EEN VASTE','COACH'],sub='6 dagen per week, groepen op niveau, persoonlijke aandacht',cta='KIES JE COACH'),
 dict(id='06_clubgevoel',photo=D+'543611.jpg',focus=(0.5,0.3),kicker='PADEL MET JE VRIENDEN',head=['CLUBGEVOEL','ZONDER','LIDMAATSCHAP'],sub='Vaste groep, vaste tijd, 100+ actieve spelers bij Poort Padel',cta='SCHRIJF JE IN'),
 dict(id='07_laatste_plekken',photo=D+'545474.jpg',focus=(0.5,0.3),kicker='NOG 1 WEEK · START 19 OKTOBER',head=['LAATSTE','PLEKKEN','NAJAARSREEKS'],sub='8 lessen t/m 12 december, vervanger toegestaan',cta='SCHRIJF JE IN'),
 dict(id='08_jeugd',photo=D+'542742.jpg',focus=(0.42,0.5),kicker='JEUGDTRAINING · VANAF 19 OKTOBER',head=['VASTE COACH,','VASTE','GROEP'],sub='Vanaf 6 jaar, 8 lessen, een vriendje mag invallen',cta='MELD JE KIND AAN'),
]
os.makedirs('posters/out',exist_ok=True)
for s in SPECS:
    im=make(s); im.save(f"posters/out/{s['id']}.jpg",quality=92); print(s['id'])
# contact sheet
ims=[Image.open(f"posters/out/{s['id']}.jpg") for s in SPECS]
for im in ims: im.thumbnail((500,625))
sheet=Image.new('RGB',(4*510,2*635),'white')
for i,im in enumerate(ims): sheet.paste(im,((i%4)*510,(i//4)*635))
sheet.save('posters/contact.jpg',quality=85)

from PIL import Image, ImageDraw, ImageFont
import os
W,H=1080,1350
M='media/'; D='drive/'; D2='drive2/'
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
def vgrad(img,y0,strength,top=False):
    ov=Image.new('L',(1,H),0); px=ov.load()
    for y in range(H):
        if top:
            px[0,y]=int(strength*255*max(0,1-y/y0)) if y<y0 else 0
        else:
            if y>=y0:
                t=min(1,(y-y0)/(H-y0)*1.7); px[0,y]=int(255*strength*(t*t*(3-2*t)))
    ov=ov.resize((W,H))
    return Image.composite(Image.new('RGB',(W,H),NAVY),img,ov)
def logo(img,path,width,x,y):
    lg=Image.open(M+path).convert('RGBA'); r=width/lg.width
    lg=lg.resize((int(lg.width*r),int(lg.height*r)),Image.LANCZOS); img.paste(lg,(x,y),lg)
def spaced(d,text,f,x,y,fill,sp):
    for ch in text:
        d.text((x,y),ch,font=f,fill=fill); x+=d.textlength(ch,font=f)+sp
def make(spec):
    img=crop45(spec['photo'],*spec.get('focus',(0.5,0.5)))
    img=vgrad(img,240,0.45,top=True)
    lines=spec['head']; hs=spec.get('hsize',80); lh=int(hs*1.02)
    pill_h=88; pill_y=H-56-pill_h
    sub_y=pill_y-40-34
    head_y=sub_y-14-lh*len(lines)
    kick_y=head_y-26-30
    img=vgrad(img,max(600,kick_y-220),0.96)
    d=ImageDraw.Draw(img)
    logo(img,'aca_logo_white.png',250,60,52)
    logo(img,'poort_padel_white.png',140,W-60-140,62)
    fk=font(26,700); fh=font(hs,800); fs=font(28,500)
    d.rectangle((60,kick_y+4,104,kick_y+7),fill=LIME)
    spaced(d,spec['kicker'],fk,117,kick_y-5,(0,0,0),5); spaced(d,spec['kicker'],fk,116,kick_y-6,LIME,5)
    for i,l in enumerate(lines): d.text((56,head_y+i*lh),l,font=fh,fill='white')
    d.text((60,sub_y),spec['sub'],font=fs,fill=SUB)
    fp=font(27,800); t=spec['cta']+'  ↗'; tw=d.textlength(t,font=fp); pw=int(tw+84)
    d.rounded_rectangle((60,pill_y,60+pw,pill_y+pill_h),radius=999,fill=LIME)
    d.text((60+42,pill_y+pill_h/2-17),t,font=fp,fill=NAVY)
    fl=font(21,600); d.text((60+pw+22,pill_y+pill_h/2-12),'LINK IN BIO · ALLCOURTACADEMY.COM',font=fl,fill=SUB)
    return img
SPECS=[
 dict(id='01_najaarsreeks',photo=D+'541525.jpg',focus=(0.5,0.3),kicker='NAJAARSREEKS · START 19 OKTOBER',head=['8 WEKEN BETER','PADELLEN'],sub='Max 4 per groep, vaste coach, instromen kan altijd',cta='SCHRIJF JE IN'),
 dict(id='02_eerste_les',photo=D+'548441.jpg',focus=(0.5,0.25),kicker='NOOIT GEPADELD? GEEN PROBLEEM',head=['JE EERSTE LES','REGELEN WIJ'],sub='Leenracket gratis, coach naast je, les op jouw niveau',cta='BOEK EEN LOSSE LES'),
 dict(id='04_techniek',photo=D+'546391.jpg',focus=(0.5,0.25),kicker='TECHNIEK · LOSSE TRAINING',head=['JOUW SMASH,','ONZE FOCUS'],sub='1 tot 4 spelers, jij kiest dag en tijd, trainer naar keuze',cta='BOEK EEN LOSSE LES'),
 dict(id='06_clubgevoel',photo=D2+'ACA_PoortPadel_29mei-29.jpg',focus=(0.28,0.5),kicker='PADEL MET JE VRIENDEN',head=['CLUBGEVOEL ZONDER','LIDMAATSCHAP'],sub='Vaste groep, vaste tijd, 100+ actieve spelers bij Poort Padel',cta='SCHRIJF JE IN',hsize=74),
 dict(id='07_laatste_plekken',photo=D2+'ACA_PoortPadel_29mei-50.jpg',focus=(0.5,0.4),kicker='NOG 1 WEEK · START 19 OKTOBER',head=['LAATSTE PLEKKEN','NAJAARSREEKS'],sub='8 lessen t/m 12 december, vervanger toegestaan',cta='SCHRIJF JE IN',hsize=76),
 dict(id='09_lachen',photo=D2+'ACA_PoortPadel_29mei-38.jpg',focus=(0.45,0.5),kicker='PLEZIER · TECHNIEK · PRESTATIE',head=['ALS JE LACHT,','LEER JE SNELLER'],sub='Kleine groepen, coach naast je, groep op jouw niveau',cta='SCHRIJF JE IN'),
 dict(id='10_competitie',photo=D2+'ACA_PoortPadel_29mei-52.jpg',focus=(0.5,0.3),kicker='KNLTB COMPETITIE · START NOVEMBER',head=['KLAAR VOOR','DE COMPETITIE?'],sub='Wedstrijdtraining: tactiek, spelinzicht, druk zetten aan het net',cta='BOEK WEDSTRIJDTRAINING'),
 dict(id='11_jouw_coach',photo=D2+'all_footage_01_01_00_20.jpg',focus=(0.4,0.5),kicker='8 COACHES · JIJ KIEST',head=['JOUW COACH,','JOUW MOMENT'],sub='Losse training op de dag en tijd die jou past',cta='KIES JE COACH'),
 dict(id='14_samen',photo=D2+'all_footage_01_15_31_08.jpg',focus=(0.42,0.5),kicker='PADEL MET JE MAATJE',head=['SAMEN','INSCHRIJVEN?'],sub='Kom als duo of met meer vrienden, wij vullen de groep aan',cta='SCHRIJF JE IN'),
 dict(id='15_geen_racket',photo=D2+'ACA_PoortPadel_29mei-39.jpg',focus=(0.45,0.45),kicker='EERSTE KEER OP DE BAAN',head=['GEEN RACKET?','GEEN PROBLEEM'],sub='Leenracket gratis, wij regelen de rest',cta='BOEK EEN LOSSE LES'),
 dict(id='16_backhand',photo=D2+'APA_13_mei-34.jpg',focus=(0.4,0.5),kicker='TECHNIEK · LOSSE TRAINING',head=['BACKHAND','ONDER CONTROLE'],sub='Losse training met focus op techniek, trainer naar keuze',cta='BOEK EEN LOSSE LES'),
 dict(id='18_teamuitje',photo=D2+'ACA_PoortPadel_29mei-34.jpg',focus=(0.4,0.5),kicker='TEAMUITJE · TOT 100+ PERSONEN',head=['PADEL MET','JE TEAM'],sub='All-in event bij Poort Padel, catering in huis',cta='PLAN JE EVENT'),
 dict(id='20_vaste_plek',photo=D2+'APA_13_mei-16.jpg',focus=(0.5,0.3),kicker='100+ ACTIEVE SPELERS',head=['JOUW VASTE PLEK','OM TE SPELEN'],sub='Trainen, spelen en mensen ontmoeten bij Poort Padel',cta='SCHRIJF JE IN'),
]
os.makedirs('posters/out3',exist_ok=True)
for s in SPECS:
    make(s).save(f"posters/out3/{s['id']}.jpg",quality=92)
ims=[Image.open(f"posters/out3/{s['id']}.jpg") for s in SPECS]
for im in ims: im.thumbnail((400,500))
cols=5; rows=3
sheet=Image.new('RGB',(cols*410,rows*510),'white')
for i,im in enumerate(ims): sheet.paste(im,((i%cols)*410,(i//cols)*510))
sheet.save('posters/contact3.jpg',quality=82); print('ok')

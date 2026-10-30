import json,os,sys
D=sys.argv[1]
files=sorted(f for f in os.listdir(D+'/tvzip/tv') if f.endswith('.jpg'))
byn={f[:2]:f for f in files}
kamp=['11','48','49']
jeugd=['12','44','13','45','50','14','46','47','06']
reeks=['09','03','42','43','16','24','09','25','26','42','02','15','04','08','21','22','23','27','28','41']
aca=['01','05','36','29','30','40','31','32','10','37','38','39','07','33','34','35','01','36','10','40']
# K slots: kamp, jeugd, kamp, jeugd ... kamp always rotates 11,48,49
K=[]; ki=0; ji=0
for i in range(len(reeks)):
    if i%2==0: K.append(kamp[ki%3]); ki+=1
    else: K.append(jeugd[ji%len(jeugd)]); ji+=1
# jeugd leftover? 10 odd slots -> jeugd 9 items + wrap 1; drop the wrap by placing a kamp instead
seq=[]
for i in range(len(reeks)):
    seq += [K[i], reeks[i], aca[i%len(aca)]]
# ensure every slide appears at least once
missing=[n for n in byn if n not in seq]
assert not missing, missing
theme={**{n:'kamp' for n in kamp},**{n:'jeugd' for n in jeugd},**{n:'reeks' for n in reeks},**{n:'aca' for n in aca}}
json.dump({'seq':seq,'theme':theme,'files':byn},open(D+'/tvwork/order.json','w'),indent=1)
print(len(seq),'slides,',len(seq)*8/60,'min; kamp x',sum(1 for s in seq if s in kamp))
print(' '.join(seq))

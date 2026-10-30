import json,os,sys
D=sys.argv[1]
files=sorted(f for f in os.listdir(D+'/tvzip/tv') if f.endswith('.jpg'))
byn={f[:2]:f for f in files}
rejected={'05','06','10','15','22','23','24','25','26','28','30','32','40','49','50'}
kamp=['11','48']
jeugd=['12','44','13','45','47','14','46']
reeks=['09','03','42','43','16','02','09','04','08','21','42','27','41','03']
aca=['01','36','29','31','37','38','39','07','33','34','35','01','36','29']
for L in (kamp,jeugd,reeks,aca): assert not set(L)&rejected
K=[]; ki=ji=0
for i in range(len(reeks)):
    if i%2==0: K.append(kamp[ki%2]); ki+=1
    else: K.append(jeugd[ji%len(jeugd)]); ji+=1
seq=[]
for i in range(len(reeks)): seq+=[K[i],reeks[i],aca[i%len(aca)]]
missing=[n for n in byn if n not in seq and n not in rejected]; assert not missing, missing
theme={**{n:'kamp' for n in kamp},**{n:'jeugd' for n in jeugd},**{n:'reeks' for n in reeks},**{n:'aca' for n in aca}}
json.dump({'seq':seq,'theme':theme,'files':byn,'rejected':sorted(rejected)},open(D+'/tvwork/order.json','w'),indent=1)
print(len(seq),'slides',len(seq)*8/60,'min; kamp',sum(1 for s in seq if s in kamp),'jeugd',sum(1 for s in seq if s in jeugd))
print(' '.join(seq))

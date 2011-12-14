#!/usr/bin/python
import sys
def toHundred(n,base):
    s=''
    if n >= 100:
        s=s+base[str(n/100)]+base['100']
    n=n%100
    if n>20:
        s=s+base[str(n/10*10)]+base[str(n%10)]
    else:
        s=s+base[str(n)]
    return s
f=open(sys.argv[1],'r')
d=f.read()
f.close()
#d='3\n10\n21\n3234\n12000\n11000000\n'
l=d.split('\n')[:-1]
base={'0':'','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten','11':'Eleven','12':'Twelve','13':'Thirteen','14':'Fourteen','15':'Fifteen','16':'Sixteen','17':'Seventeen','18':'Eighteen','19':'Nineteen','20':'Twenty','30':'Thirty','40':'Forty','50':'Fifty','60':'Sixty','70':'Seventy','80':'Eighty','90':'Ninty','100':'Hundred','1000':'Thousand','1000000':'Million'}
for w in l:
    w=int(w)
    r=''
    m=w/1000000
    if m>0:
        s=toHundred(m,base)
        r=r+s+base['1000000']
        w=w%1000000
    m=w/1000
    if m>0:
        s=toHundred(m,base)
        r=r+s+base['1000']
        w=w%1000
    m=w%1000
    if m>0:
        s=toHundred(m,base)
        r=r+s+'Dollars'
    print r

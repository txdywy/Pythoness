#!/usr/bin/python
import sys
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
for w in l:
    i=0
    for x in w:
        if x=='1' or x=='0':
            break
        i+=1
    h,e=w[:i],w[i:]
    i,width=0,1
    map=dict()
    for x in h:
        #print i,'--'
        b=bin(i)[2:]
        #print b,'=='
        map['0'*(width-len(b))+b]=x
        #print i
        if i+1==2**width-1:
            i,width=0,width+1
        else:
            i+=1
    #print map
    width=int(e[:3],2)
    #print e
    e=e[3:]
    #print width,e
    r=''
    i=0
    while i<len(e):   
        #print i
        if e[i:i+width]!='1'*width:
            r+=map[e[i:i+width]]
            i+=width
        else:
            i+=width
            #print e[i:i+3]
            width=int(e[i:i+3],2)
            i+=3
    print r

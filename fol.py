#!/usr/bin/python
import sys
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
for w in l:
    w=[int(x) for x in w]
    s=w[:]
    s.sort()
    s.reverse()
    #print w,'---'
    if w==s:
        w.reverse()
        for i in range(len(w)):
            if w[i]>0:
                break;
        w[0],w[i]=w[i],w[0]
        w.insert(1,0)
        p=w[2:]
        p.sort()
        w=w[0:2]+p
        print ''.join([str(i) for i in w])
        continue
    for i in range(len(w)-1,0,-1):
        if w[i]>w[i-1]:
            break
    p=w[i:]
    p.sort()
    j=0
    while True:
        if p[j]>w[i-1]:
            break
        j=j+1
    t=w[i-1]
    w[i-1]=p[j]
    p[j]=t
    w=w[0:i]+p
    print ''.join([str(i) for i in w])

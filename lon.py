#!/usr/bin/python
import sys
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
k=[]
n=int(l[0])
l=l[1:]
for w in l:
    w=w.strip()
    if w=='':
        continue
    k.append((len(w),w))
k.sort()
#print k
for x in k[:-n-1:-1]:
    print x[1]

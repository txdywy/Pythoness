#!/usr/bin/python
import sys
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
for w in l:
    w=w.split(' ')
    h=w[:-1]
    m=int(w[-1])
    #print h,m
    if m>len(h):
        continue
    #h.sort()
    print h[-m]


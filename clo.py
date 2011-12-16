#!/usr/bin/python
import sys
import math
def closestPair(p):
    length=len(p)
    if length==1:
        return sys.maxint
    mid=length/2
    minL=closestPair(p[:mid])
    minR=closestPair(p[mid:])
    minD=min(minL,minR)
    r=minD
    for x in p[:mid]:
        for y in p[mid:]:
            if y[0]>=minD:
                break
            if x[1]-minD<=y[1]<=x[1]+minD:
                r=min(r,distance(x,y))
    return r
def distance(x,y):
    return math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
i=0
while True:
    w=l[i]
    if w=='0':
        break
    else:
        p=[]
        for j in range(i+1,i+int(w)+1):
            w=l[j]
            w=w.split(' ')
            p.append([int(w[0]),int(w[1])])
        p.sort()
        r=closestPair(p)
        if r>=10000:
            print 'INFINITY'
        else:
            print '%.4f' % r
        i=1+j
        

    

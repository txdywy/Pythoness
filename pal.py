#!/usr/bin/python
import sys
def checkPali(n):
    s0=str(n)
    s1=list(s0)
    s1.reverse()
    s1=''.join(s1)
    return s0==s1
def paliRange(l,r,p):
    if r==l+1:
        n=0
        if checkPali(l):
            p.append(0)
        else:
            n+=1
        if checkPali(r):
            p.append(1)
        else:
            n+=1
        n+=len(p)-1
    else:
        n=paliRange(l,r-1,p)
        if checkPali(r):
            for i in range(len(p)-1,-1,-2):
                if i-1>=0:
                    n+=p[i]-p[i-1]
                if i==0:
                    n+=p[i]-0+1
            p.append(r-l)
        else:
            if len(p)>0:
                n+=r-l-p[-1]
            else:
                n+=r-p[0]
            if len(p)<2:
                return n
            for i in range(len(p)-2,-1,-2):
                if i==0:
                    n+=p[i]-0+1
                if i>0:
                    n+=p[i]-p[i-1]
    return n
f=open(sys.argv[1],'r')
d=f.read()
f.close()
#d='1 2\n1 7\n87 88\n87 93\n2 9\n11 21\n'
l=d.split('\n')[:-1]
for w in l:
    left,right=[int(i) for i in w.split(' ')]
    p=[]
    print paliRange(left,right,p)

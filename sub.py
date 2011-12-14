#!/usr/bin/python
import sys
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
for w in l:
    s,c=w.split(';')
    c=c.split(',')
    for r in range(0,len(c),2):
        s=s.split('#')
        for j in range(len(s)):
            if j%2==0:
                s[j]=s[j].replace(c[r],'#'+c[r+1]+'#')
            else:
                s[j]='#'+s[j]+'#'
        s=''.join(s)
    print ''.join(s.split('#'))           


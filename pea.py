#!/usr/bin/python
import sys
import re
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')
if l[-1]=='':
    l=l[:-1]
send=dict()
for w in l:
    w=w.split('\t')[1:]
    if w[0] not in send:
        send[w[0]]=set()
    send[w[0]].add(w[1])
#print send
send0={}
for x in send:
    for i in send[x]:
        if i in send and x in send[i]:
            if i not in send0:
                send0[i]=set()
            send0[i].add(x)
send=send0
#print send
out=set()
for x in send:
    for i in send[x]:
        t=[x,i]
        t.sort()
        out.add(tuple(t))
#print out 
level=3
while True:
    num=0
    old=set(out)
    for x in old:
        for i in x:
            for j in send[i]:
                if j not in x:
                    t=True
                    for k in x:
                        if k in send[j]:
                            t=t&True
                        else:
                            t=False
                            break
                    if t==True:
                        t=list(x)
                        t.append(j)
                        t.sort()
                        #print out
                        out.add(tuple(t))
                        num+=1
                        if x in out:
                            out.remove(x)
    if num==0:
        break
    level+=1
out=[', '.join(x) for x in out if len(x)>2]
out.sort()
print '\n'.join(out)

#!/usr/bin/python
import sys
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
a=[]
for w in l:
	n=w.split(';')
	s=int(n[1])
	r=n[0].split(',')
	q=[]
	for i in r:
		t=s-int(i)
		if str(t) in r and t>int(i):
			q.append(str(i)+','+str(t))
	if len(q)==0:
		a.append('NULL')
	else:
		a.append( ';'.join(q))
print '\n'.join(a),

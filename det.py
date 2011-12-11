#!/usr/bin/python
import sys
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
for w in l:
	s=dict()
	r=list()
	w=w.strip()
	if w=='':
		continue
	#print w
	for x in w.split(' '):
		r.append(x)
		if x not in s:
			s[x]=len(r)-1
		else:
			break
	if len(s)==len(r):
		break
	q=[v for v in r[s[x]:-1]]
	print ' '.join(q)

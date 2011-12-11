#!/usr/bin/python
import sys
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
for w in l:
	r=[]
	s=set()
	for i in w:
		if i in s:
			r.remove(i)
		else:
			r.append(i)
			s.add(i)
	print r[0]

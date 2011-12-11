#!/usr/bin/python
import sys
import string
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
for w in l:
	w=w.lower()
	s=set()
	for x in w:
		if x>='a' and x <='z':
			s.add(x)
	p=set(string.lowercase[:])
	s=p-s
	if len(s)==0:
		print 'NULL'
	else:
		a=list(s)
		a.sort()
		print ''.join(a) 

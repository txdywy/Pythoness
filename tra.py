#!/usr/bin/python
import sys
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
for w in l:
	s,k=w.split(',')
	if s[-len(k):]==k:
		print 1
	else:
		print 0

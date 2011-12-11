#!/usr/bin/python
import sys
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
for w in l:
	s,k=[list(i) for i in w.split(', ')]
	print ''.join([i for i in s if i not in k])


#!/usr/bin/python
import sys
f=open(sys.argv[1],'r')
data=f.read()
f.close()
a=[list(set(l[0].split(',')) & set(l[1].split(','))) for l in [line.split(';') for line in data.split('\n')[:-1]]]
for s in a:
	s.sort()
	print ','.join(s)

#!/usr/bin/python
import sys
f = open(sys.argv[1], 'r')
data = f.read()
line = data.split("\n")[:-1]
for word in line:
	temp = word.split(",")
	d=dict()
	for i in temp:
		d[i]=i
	a=d.keys()
	a.sort()
	b=",".join(str(i) for i in a)
	print b
f.close()

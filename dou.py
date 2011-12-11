#!/usr/bin/python
import sys
import math
def ss(i):
	#print i,"---"
	if i==0 or i==1:
		return 1 
	m=int(math.floor(math.sqrt(i/2.0)))
	p=0
	for t in range(m+1):
		r=i-t**2
		if r < 0:
			break
		u=math.ceil(math.sqrt(r))
		if u**2==r:
			p=p+1
			#print t
	return p
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[1:-1]
for w in l:
	print ss(int(w))

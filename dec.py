#!/usr/bin/python
import sys
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
for w in l:
	r=[]
	#print w,'ee'
	t=int(w)

	while t>0:
		r.append(str(t%2))
		t=t/2
	r.reverse()	
	print ''.join(r)

#!/usr/bin/python
import sys
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
for w in l:
	i=0		
	while w!=w[::-1]:
		w=str((int(w)+int(w[::-1])))
		i=i+1
	print i,w

#!/usr/bin/python
import sys
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
#print l,"---"
for w in l:
	#print w,'=='	
	if w=='':
		continue
	#print w.split(';')
	n,s=[i for i in w.split(';')]
	n=int(n)
	s=[int(x) for x in s.split(',')]
	dup=0
	s.extend(range(n-1))
	dup=reduce(lambda x,y:x^y,s,0)
	print dup

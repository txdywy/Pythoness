#!/usr/bin/python
import sys
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
for w in l:
	#print w
	d=[]
	w=w.split(' ')
	for i in range(len(w)-1):
		d.append(abs(int(w[i])-int(w[i+1])))
	if d[1:]==list(xrange(len(w)-2,0,-1)):
		print 'Jolly'
	else:
		print 'Not jolly'



#!/usr/bin/python
import sys
def bitV(n,p):
	return n>>(p-1)&1
f=open(sys.argv[1],'r')
data=f.read()
f.close()
line=data.split('\n')[:-1]
for word in line: 
	n=[int(j) for j in word.split(",")]
	print "true" if bitV(n[0],n[1])==bitV(n[0],n[2]) else "false"

#!/usr/bin/python
import sys
def fil(a,b):
	return lambda x: check(x,a,b)   
def check(x,a,b):
	if x%a==0 and x%b==0:
		return 'FB'
	elif x%a==0:
		return 'F'
	elif x%b==0:
		return 'B'
	else:
		return str(x)
			
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
#print [map(fil(3,4),range(1,15))]
print '\n'.join([' '.join(t) for t in [map(fil(int(line.split(' ')[0]),int(line.split(' ')[1])) , range(1,int(line.split(' ')[2])+1)) for line in l]])

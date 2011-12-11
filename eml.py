#!/usr/bin/python
import sys
import re
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
for w in l:
	#print w
	emails = re.findall('[\w.-]+@[\w.-]+', w)
	if len(emails)==1 and emails[0]==w:
		#print emails[0],'--'
		print 'true'
	else:
		print 'false'


#! /usr/bin/python
import sys
test_cases = open(sys.argv[1], 'r')
data=test_cases.read()
test_cases.close()
lines=data.split("\n")[:-1]
words=[i.split() for i in lines]
for l in words:
	l.reverse()
print "\n".join([" ".join(l) for l in words])


#!/usr/bin/python
import sys 
from string import ascii_lowercase 
def expandFriends(word,h,s):
    #print word
    if word not in s:
        return
    if word in h:
        return
    else:
        h.add(word)
        for i in range(len(word)):
            expandFriends(word[0:i]+word[i+1:],h,s)
            for x in ascii_lowercase:
                expandFriends(word[0:i]+x+word[i+1:],h,s)
                expandFriends(word[0:i+1]+x+word[i+1:],h,s)
        for x in ascii_lowercase:
            expandFriends(x+word,h,s)
sys.setrecursionlimit(3500)
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
s=set(l)
h=set()
w='hello'
s.add(w)
expandFriends(w,h,s)
print(len(h)-1)

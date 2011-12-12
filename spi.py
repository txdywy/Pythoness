#!/usr/bin/python
import sys
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
for w in l:
    #print w
    w=w.split(';')
    #print w
    row=int(w[0])
    col=int(w[1])
    w=w[2].split(' ')
    #print w
    xc,yr,out=0,0,0
    o=[]
    while True:
        #print xc,yr,w[col*yr+xc],'+++'
        if xc==col/2 and yr==row/2:
            if col%2==1 and row%2==1:
                o.append(w[col*yr+xc])
            break
        if xc>=col/2:
            if xc==col/2:
                for y in range(yr,row-yr):
                    o.append(w[col*y+xc])
            break 
        if yr>=row/2:
            if yr==row/2:
                for x in range(xc,col-xc):
                    o.append(w[col*yr+x])
            break
            
        #print xc,col-1-xc,range(xc,col-1-xc),'__'
        for x in range(xc,col-1-xc):
            o.append(w[col*yr+x])
        xc=x+1
        #print xc,'='
        
        #print yr,row-1-yr,range(yr,row-1-yr),'__'
        for y in range(yr,row-1-yr):
            o.append(w[col*y+xc])
        yr=y+1
        #print xc,'='
        
        #print xc,col-1-xc,range(xc,col-1-xc,-1),'__'
        for x in range(xc,col-1-xc,-1):
            o.append(w[col*yr+x])
        xc=x-1
        #print xc,'='
        
        #print yr,row-1-yr,range(yr,row-1-yr,-1),'__'
        for y in range(yr,row-1-yr,-1):
            o.append(w[col*y+xc])
        yr=y
        xc=xc+1
        
    print ' '.join(o)


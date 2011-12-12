#!/usr/bin/python
import sys
class BST:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,node):
        #print self.data,node.data
        if self==None:
                self=node
        elif node.data<self.data:
            if self.left==None:
                self.left=node
            else:
                self.left.insert(node)
        else:
            if self.right==None:
                self.right=node
            else:
                self.right.insert(node)  
    def printBST(self):
        li=list([[self,1]])
        self.__printBST(li)
    def __printBST(self,printList):
        if printList !=[]:
            #print printList
            level=printList[0][1]
            #level=1
            print level,": ",
            print [i[0].data for i in printList if i[1]==level]
            newList=[i for i in printList if i[1]!=level]
            expandList=[]
            for i in [i[0] for i in printList if i[1]==level]:
                if i.left!=None:
                    expandList.append([i.left,level+1])
                if i.right!=None:
                    expandList.append([i.right,level+1])
            newList.extend(expandList)
            self.__printBST(newList)
        else:
            print
    def commonAncestor(self,d1,d2):
        """d1<=d2"""
        if self.data>=d1 and self.data<=d2:
            return self.data
        elif self.data>d2:
            return self.left.commonAncestor(d1,d2)
        else:
            return self.right.commonAncestor(d1,d2)
        
root=BST(30)
n=BST(8)
root.insert(n)
n=BST(52)
root.insert(n)
n=BST(3)
root.insert(n)
n=BST(20)
root.insert(n)
n=BST(10)
root.insert(n)
n=BST(29)
root.insert(n)
#root.printBST()
f=open(sys.argv[1],'r')
d=f.read()
f.close()
l=d.split('\n')[:-1]
for w in l:
    a,b=w.split(' ')
    i1=min(int(a),int(b))
    i2=max(int(a),int(b))
    print root.commonAncestor(i1,i2)


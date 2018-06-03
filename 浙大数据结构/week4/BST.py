# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 12:27:46 2018

@author: 715073608
"""
#我的思路是对于BST树，直接找根节点，后续递归处理即可。

from math import log

a=raw_input('')
b=map(int,raw_input('').strip().split(' '))
b.sort()
#b=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

c=[]
#找到根节点
def findroot(b):
    if len(b)==1:
        return 0
    else: 
        a=len(b)
        n=int(log(a+1,2))
        s1=2**(n-1)-1
        s2=min(2**(n-1),a-2**n+1)
        k=s1+s2
        return k

#恢复成bst树
def bst(b,c):
    tree=[]
    a=len(b)
    k=findroot(b)
    temp=[b[:k],b[k+1:]]
    tree.append(temp)
    c.append(str(b[k]))
    i=2
    while len(c)<a:
        s=tree[i/2-1]
        if i%2==0:
            temptree=s[0]
            if len(temptree)>0:
                k=findroot(temptree)
                #print k,len(temptree)
                if k<len(temptree)-1:
                    temp=[temptree[:k],temptree[k+1:]]
                else:
                    temp=[temptree[:k],[]]
                tree.append(temp)
                c.append(str(temptree[k]))
        else:
            temptree=s[1]
            if len(temptree)>0:
                k=findroot(temptree)
                #print k,len(temptree)
                if k<len(temptree)-1:
                    temp=[temptree[:k],temptree[k+1:]]
                else:
                    temp=[temptree[:k],[]]
                tree.append(temp)
                c.append(str(temptree[k]))
        i+=1
    return c,tree
c,tree=bst(b,c)
print ' '.join(c)
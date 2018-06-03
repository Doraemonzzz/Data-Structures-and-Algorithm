# -*- coding: utf-8 -*-
"""
Created on Mon May 14 21:54:23 2018

@author: Administrator
"""


n=int(raw_input().strip())
#print n
b=map(int,raw_input().strip().split())
'''
n=100000

b=[n-i for i in range(1,n+1)]
'''
s=0
for i in range(n):
    if b[i]!=i:
        s+=1

k=0
index=1

while(s>0):
    if (b[0]==0):
        while(index<=n-1):
            if (b[index]!=index):
                temp=b[index]
                b[index]=0
                b[0]=temp
                break
            index+=1
        s+=1
        k+=1
    else:
        temp=b[0]
        b[0]=b[temp]
        b[temp]=temp
        if(b[0]==0):
            s-=2
        else:
            s-=1
        k+=1

        
print k


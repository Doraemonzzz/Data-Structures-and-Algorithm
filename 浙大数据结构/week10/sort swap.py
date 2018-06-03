# -*- coding: utf-8 -*-
"""
Created on Mon May 14 22:52:47 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 14 21:54:23 2018

@author: Administrator
"""


n=int(raw_input().strip())

if n>0:
#print n
    b=map(int,raw_input().strip().split())
    
    
    
    '''
    n=100000
    
    b=[n-i for i in range(1,n+1)]
    '''
    
    c=[-1 for i in range(n)]
    
    
    s=0
    for i in range(n):
        if b[i]!=i:
            s+=1
    
    ans=set()
    dic={}
    
    def find(a,b):
        while(a[b]>0):
            b=a[b]
        return b
    
    def union(s,x,y):
        root1=find(s,x)
        root2=find(s,y)
        if(root1!=root2):
            if s[root1]<s[root2]:
                s[root1]+=s[root2]
                s[root2]=root1
            else:
                s[root2]+=s[root1]
                s[root1]=root2
    
    for i in range(n):
        #print c
        union(c,i,b[i])
    
    temp=0
    k=0
    for i in range(n):
        if c[i]<-1:
            temp+=c[i]
            k+=1
    
    if (temp==0):
        print 0
    else:
        print -temp+(k-2)
else:
    print 0

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 13:13:46 2018

@author: 715073608
"""


a=int(raw_input())
b=[]
while True:
    temp=raw_input().strip().split(' ')
    #print temp
    if temp[0]=='S':
        break        
    else:
        b.append(temp)

'''
b=[['C', '3', '2'],
 ['I', '3', '2'],
 ['C', '1', '5'],
 ['I', '4', '5'],
 ['I', '2', '4'],
 ['C', '3', '5']]


b=[['C', '3', '2'],
 ['I', '3', '2'],
 ['C', '1', '5'],
 ['I', '4', '5'],
 ['I', '2', '4'],
 ['C', '3', '5'],
 ['I', '1', '3'],
 ['C', '1', '5']]
'''
c={}
a=5
for i in range(1,a+1):
    c[i]=-1

def find(s,x):
    if s[x]<0:
        return x
    else:
        s[x]=find(s,s[x])
        return s[x]
    
def union(s,x,y):
    root1=find(s,x)
    root2=find(s,y)
    #print root1,root2
    if s[root1]<s[root2]:
        s[root1]+=s[root2]
        s[root2]=root1
    else:
        s[root2]+=s[root1]
        s[root1]=root2

for i in b:
    if i[0]=='I':
        union(c,int(i[1]),int(i[2]))
    else:
        root1=find(c,int(i[1]))
        root2=find(c,int(i[2]))
        if root1==root2:
            print 'yes'
        else:
            print 'no'
ans=0
for i in c:
    if c[i]<0:
         ans+=1
if ans==1:
    print 'The network is connected.'
else:
    print 'There are '+str(ans)+' components.' 

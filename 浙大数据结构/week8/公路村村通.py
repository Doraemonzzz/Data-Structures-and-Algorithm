# -*- coding: utf-8 -*-
"""
Created on Wed May 02 10:07:23 2018

@author: Administrator
"""
n,m=map(int,raw_input().split(' '))

#读入边
index=[]
length=[]
for i in range(m):
    a,b,c=map(int,raw_input().split(' '))
    length.append(c)
    index.append((a,b))
'''
index=[(1, 2),
 (1, 3),
 (1, 4),
 (1, 5),
 (1, 6),
 (2, 3),
 (2, 4),
 (2, 5),
 (2, 6),
 (3, 4),
 (3, 5),
 (3, 6),
 (4, 5),
 (4, 6),
 (5, 6)]

length=[5, 3, 7, 4, 2, 4, 6, 2, 6, 6, 1, 1, 10, 8, 3]

n=6
m=15
'''
#初始化点        
v=[-1 for i in range(n)]

#定义并查集
def find(s,x):
    if s[x]<0:
        return x
    else:
        return find(s,s[x])
    
#定义union,x1,x2为根节点
def union(s,x1,x2):
    if s[x1]<s[x2]:
        s[x1]+=s[x2]
        s[x2]=x1
    else:
        s[x2]+=s[x1]
        s[x1]=x2
        
#定义判断cycle
def cycle(s,x1,x2):
    v1=find(s,x1)
    v2=find(s,x2)
    return v1,v2

#定义已访问的个数
num=0
#mst边长
l=0

while(num<n and len(length)>0):
    #找到最短边
    lmin=min(length)
    #找到最短边的索引
    i=length.index(lmin)
    del length[i]
    #找到最短边对应的点
    edge=index.pop(i)
    #判断是否循环，根节点相同表示已联通
    x1,x2=cycle(v,edge[0]-1,edge[1]-1)
    if x1!=x2:
        union(v,x1,x2)
        l+=lmin
        if num==0:
            num+=2
        else:
            num+=1
            
#所有点都访问过表示存在mst
if num==n:
    print l
else:
    print -1
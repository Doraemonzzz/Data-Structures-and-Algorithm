# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 12:15:43 2018

@author: 715073608
"""

n,m,s,d=map(int,raw_input().strip().split())

#读入数据，存入字典
v={}
for i in range(n):
    v[i]={}

for j in range(m):
    a,b,c,e=map(int,raw_input().strip().split())
    #v[a][b]=(c,d)
    #v[b][a]=(c,d)
    v[b][a]=c*10**10+e
    v[a][b]=c*10**10+e

#记录未访问的节点
y=set(range(n))
#记录dist
x=[10**15 for i in range(n)]

'''
v={0: {1: (1, 20), 2: (2, 20), 3: (4, 10)},
 1: {0: (1, 20), 3: (2, 30)},
 2: {0: (2, 20), 3: (1, 20)},
 3: {0: (4, 10), 1: (2, 30), 2: (1, 20)}}
'''
'''
v={0: {1: 10000000020L, 2: 20000000020L, 3: 40000000010L},
 1: {0: 10000000020L, 3: 20000000030L},
 2: {0: 20000000020L, 3: 10000000020L},
 3: {0: 40000000010L, 1: 20000000030L, 2: 10000000020L}}

n=4
m=5
s=0
d=3

y=set(range(n))
x=[1000000000000000L, 1000000000000000L, 1000000000000000L, 1000000000000000L]
'''

#找到未收录顶点中dist最小者
def findmin(a,b):
    #记录最先的边长
    l=10**15
    #记录最小边对应的顶点
    m=-1
    for i in b:
        if a[i]<l:
            l=a[i]
            m=i
    return m

m={}
for i in range(n):
    m[i]=10**15
m[s]=0

while True:
    k=findmin(m,y)
    if k==-1:
        break
    y.remove(k)
    for j in v[k]:
        if j in y:
            if m[k]+v[k][j]<m[j]:
                m[j]=m[k]+v[k][j]
                #path[j]=k
print m[d]/(10**10),m[d]%(10**10)
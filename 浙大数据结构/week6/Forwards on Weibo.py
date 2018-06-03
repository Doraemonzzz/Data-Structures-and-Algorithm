# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 12:24:23 2018

@author: 715073608
"""
#先根据追随哪些人反取出每人的追随者
n,l=map(int,raw_input().strip().split())

u=[[] for i in range(n+1)]
for i in range(1,n+1):
    temp=map(int,raw_input().strip().split())
    if temp[0]>0:
        for j in temp[1:]:
            u[j].append(i)
v=map(int,raw_input().strip().split())
y=[0 for i in range(n+1)]

'''
u=[[], [4], [1], [1, 4, 5], [1, 5, 6], [3, 7], [3], []]
y=[0,0,0,0,0,0,0,0]
n=7
l=3
v=[2,2,6]
'''
#定义BFS
#m为图，x为开始节点,y为访问数组，记录是否访问过
def BFS(m,x,y):
	#记录层数，起点不算第一层
    count=0
    level=0
    q=[]
    last=x
    tail=0
    y[x]=1
    q.append(x)
    while(len(q)>0):
        v=q.pop(0)
        for i in m[v]:
            if y[i]==0:
                q.append(i)
                y[i]=1
                tail=i
                count+=1
        if v==last:
            level+=1
            last=tail
        if level==l:
            break
    return count
for i in v[1:]:
    print BFS(u,i,y[:])
            
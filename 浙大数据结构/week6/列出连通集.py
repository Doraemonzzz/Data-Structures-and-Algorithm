# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 12:18:53 2018

@author: 715073608
"""


#读取节点个数N，和边的个数E
N,E=map(int,raw_input().strip().split(' '))

#利用邻接表表示图
m=[[] for i in range(N)]
    
for i in range(E):
    x,y=map(int,raw_input().strip().split(' '))
    m[x].append(y)
    m[y].append(x)
for i in m:
    i.sort()

'''
m=[[1, 2, 7], [0, 4], [0, 4], [5], [1, 2], [3], [], [0]]
N=8
'''
#定义DFS
#m为图，x为开始节点,y为访问数组，记录是否访问过,s用来返回结果
def DFS(m,x,y,s):
    s.append(x)
    y[x]=1
    for i in m[x]:
        if y[i]==0:
            DFS(m,i,y,s)
    return s 

#对全部元素做DFS
def DFSall(m,N):
    #记录结果
    ans=[]
    #记录是否访问过，如果访问过，则不对该节点做BFS
    visited=[0 for i in range(N)]
    for i in range(N):
        if visited[i]==0:
            s=[]
            ans.append(DFS(m,i,visited,s))
    return ans

#产生结果
t=DFSall(m,N)

#定义输出函数
def output(x):
    for i in x:
        print "{ "+' '.join(map(str,i))+' }'

#输出结果
output(t)

#定义BFS
#m为图，x为开始节点,y为访问数组，记录是否访问过,s用来返回结果,q为程序中需要的队列
def BFS(m,x,y,s,q):
    y[x]=1
    s.append(x)
    q.append(x)
    while(len(q)>0):
        v=q.pop(0)
        for i in m[v]:
            if y[i]==0:
                y[i]=1
                q.append(i)
                s.append(i)
    return s

#对全部元素做BFS
def BFSall(m,N):
    visited=[0 for i in range(N)]
    ans=[]
    for i in range(N):
        if visited[i]==0:
            s=[]
            q=[]
            ans.append(BFS(m,i,visited,s,q))
    return ans

#产生结果
t=BFSall(m,N)

#输出结果
output(t)

    
        
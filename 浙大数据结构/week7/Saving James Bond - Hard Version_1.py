# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 22:38:53 2018

@author: Administrator
"""



#定义点的距离
def dis1(x,y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5

#定义离岸的距离
def dis2(x):
    return min(abs(x[0]-50),abs(x[0]+50),abs(x[1]-50),abs(x[1]+50))

def dis3(x):
    return abs(x[0])<=50 and abs(x[1])<=50


#读入鳄鱼个数n,以及跳跃距离d
n,d=map(int,raw_input().strip().split(' '))

#初始化图，注意增加原点
m=[[0,0]]

#读入数据
for i in range(n):
    temp=map(int,raw_input().strip().split(' '))
    #不在岛上和岸边的鳄鱼才算在内
    if dis1([0,0],temp)>=7.5 and dis3(temp):
        m.append(temp)

#有效鳄鱼个数
n=len(m)-1

#构造邻接表
s=[[] for i in range(n+1)]

#初始原点及其相邻点,第一个点为离原点最近的点
#step1读入距离
dis={}
for i in range(1,n+1):
    if dis1([0,0],m[i])<=d+7.5:
        dis[i]=dis1([0,0],m[i])

#step2找按距离从小到大排序,为了输出唯一
x=sorted(dis.items(),key=lambda item:item[1])

#step3将其余的点读入数组
for i in x:
    s[0].append(i[0])

#初始其余的节点,注意不取在岸边的鳄鱼
for i in range(1,n+1):
    for j in range(n+1):
        if i!=j and dis1(m[i],m[j])<=d:
            s[i].append(j)
'''
s=[[7, 12, 15],
 [7],
 [12, 13, 15, 16],
 [17],
 [9],
 [16],
 [13, 14],
 [0, 1],
 [10, 11, 17],
 [4],
 [8],
 [8, 12],
 [0, 2, 11, 15],
 [2, 6, 14],
 [6, 13, 15],
 [0, 2, 12, 14],
 [2, 5],
 [3, 8]]

m=[[0, 0],
 [10, -21],
 [10, 21],
 [-40, 10],
 [30, -50],
 [20, 40],
 [35, 10],
 [0, -10],
 [-25, 22],
 [40, -40],
 [-30, 30],
 [-10, 22],
 [0, 11],
 [25, 21],
 [25, 10],
 [10, 10],
 [10, 35],
 [-30, 10]]

d=15
n=17

s=[[1, 2, 3, 4], [], [], [], []]
m=[[0, 0], [-12, 12], [12, 12], [-12, -12], [12, -12]]

d=13
n=4

s=[[1,2],[2],[1]]
m=[[0,0],[25,0],[30,0]]
d=30
n=2

s=[[1, 2, 3, 4], [0,2,3], [0,1,3], [1,2]]
m=[[0,0],[20,0],[25,0],[30,0],[35,0]]
d=30
n=3
'''
#初始化访问矩阵，0表示未访问
y=[0 for i in range(n+1)]
y[0]=1

#定义BFS
#s为图，m为对应点，x为开始节点,y为访问数组，记录是否访问过,s用来返回结果,q为程序中需要的队列
def BFS(s,m,x,y):
    path=[-1 for j in range(n+1)]
    #记录是否到岸
    flag=0
    q=[]
    y[x]=1
    q.append(x)
    while(len(q)>0):
        v=q.pop(0)
        path.append(v)
        for i in s[v]:
            if y[i]==0:
                y[i]=1
                q.append(i)
                path[i]=v
                q.append(i)
                if dis2(m[i])<=d:
                    flag=1
                    return flag,path,i
    return flag,path,i

#能跳到第二个点
if len(s[0])>0:
    a,b,c=BFS(s,m,0,y)
#不能跳到第二个点
else:
    a=0

if a==0:
    print a
#一步跳
elif d>=50-7.5:
    print 1
else:
    u=c
    i=1
    ans=[]
    while(u!=0):
        ans.append(m[u])
        u=b[u]
        i+=1
    ans.reverse()
    print i
    for j in ans:
        print str(j[0])+' '+str(j[1])


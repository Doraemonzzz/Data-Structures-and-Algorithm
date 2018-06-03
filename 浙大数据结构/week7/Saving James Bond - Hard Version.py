# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 22:38:53 2018

@author: Administrator
"""
'''
#读入鳄鱼个数n,以及跳跃距离d
n,d=map(int,raw_input().strip().split(' '))

#初始化图，注意增加原点
m=[]
#n记录相邻定点及其距离
l={}
#记录是否访问过
flag={}
#记录最短距离
dis={}
#读入数据
for i in range(n):
    temp=tuple(map(int,raw_input().strip().split(' ')))
    m.append(temp)
    l[temp]=[]
    flag[temp]=0
'''
#定义点的距离
def dis1(x,y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5

#定义离岸的距离
def dis2(x):
    return min(abs(x[0]-50),abs(x[0]+50),abs(x[1]-50),abs(x[1]+50))


m=[(10, -21),
 (10, 21),
 (-40, 10),
 (30, -50),
 (20, 40),
 (35, 10),
 (0, -10),
 (-25, 22),
 (40, -40),
 (-30, 30),
 (-10, 22),
 (0, 11),
 (25, 21),
 (25, 10),
 (10, 10),
 (10, 35),
 (-30, 10)]
n=17
d=15
flag={(-40, 10): 0,
 (-30, 10): 0,
 (-30, 30): 0,
 (-25, 22): 0,
 (-10, 22): 0,
 (0, -10): 0,
 (0, 11): 0,
 (10, -21): 0,
 (10, 10): 0,
 (10, 21): 0,
 (10, 35): 0,
 (20, 40): 0,
 (25, 10): 0,
 (25, 21): 0,
 (30, -50): 0,
 (35, 10): 0,
 (40, -40): 0}


dis={(-40, 10): float('inf'),
 (-30, 10): float('inf'),
 (-30, 30): float('inf'),
 (-25, 22): float('inf'),
 (-10, 22): 24.166091947189145,
 (0, -10): 10.0,
 (0, 0): 0,
 (0, 11): 11.0,
 (10, -21): 23.259406699226012,
 (10, 10): 14.142135623730951,
 (10, 21): 23.259406699226012,
 (10, 35): float('inf'),
 (20, 40): float('inf'),
 (25, 10): 26.92582403567252,
 (25, 21): float('inf'),
 (30, -50): float('inf'),
 (35, 10): float('inf'),
 (40, -40): float('inf')}

#先初始原点的相邻点
l[(0,0)]={}
for i in m:
    l[i]={}
for i in m:
    if dis1(i,(0,0))<=15+d:
        l[(0,0)][i]=dis1(i,(0,0))

#初始非原点的相邻点
for i in range(n):
    for j in range(n):
        if i!=j and dis1(m[i],m[j])<=d:
            l[m[i]][m[j]]=dis1(m[i],m[j])
            l[m[j]][m[i]]=dis1(m[i],m[j])
'''
for i in m:
    if i in l[(0,0)]:
        dis[i]=l[0,0][i]
    else:
        dis[i]=float('inf')
'''

#路径path
path=[(0,0)]
flag[(0,0)]=1

#定义找到最小边
while (True):
    if dis2(path[-1])<=d or len(path)==n:
        break
    else:
    #首先找相邻最大值
        #print path
        s=0
        node=''
        for i in path:
            for j in l[i]:
                if flag[j]==0:
                    if l[i][j]>s:
                        s=l[i][j]
                        node=j
        flag[node]=1
        path.append(node)
        for k in l[node]:
            if flag[k]==0:
                if dis[node]+l[node][k]<dis[k]:
                    dis[k]=dis[node]+l[node][k]
                    #flag[k]=1
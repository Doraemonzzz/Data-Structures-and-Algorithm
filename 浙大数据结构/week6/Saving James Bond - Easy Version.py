# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 20:01:34 2018

@author: Administrator
"""


#读入鳄鱼个数n,以及跳跃距离d
n,d=map(int,raw_input().strip().split(' '))

#初始化图，注意增加原点
m=[[] for i in range(n)]
for i in range(n):
    temp=map(int,raw_input().strip().split(' '))
    #最后一个元素记录是否访问过
    temp.append(0)
    m[i]=temp
'''

m=[
 [25, -15,0],
 [-25, 28,0],
 [8, 49,0],
 [29, 15,0],
 [-35, -2,0],
 [5, 28,0],
 [27, -29,0],
 [-8, -28,0],
 [-20, -35,0],
 [-25, -20,0],
 [-13, 29,0],
 [-30, 15,0],
 [-35, 40,0],
 [12, 12,0]]
n=14
d=20


m=[[-12, 12,0], [12, 12,0], [-12, -12,0], [12, -12,0]]
d=13
n=4
'''

#定义点的距离
def dis1(x,y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5

#定义离岸的距离
def dis2(x):
    return min(abs(x[0]-50),abs(x[0]+50),abs(x[1]-50),abs(x[1]+50))

#定义DFS
#m为图，x为开始节点
def DFS(m,x,s):
    ans=s
    m[x][-1]=1
    #如果距离岸的最短距离小于等于d，返回Yes
    if dis2(m[x])<=d:
        ans='Yes'
    #否则进行DFS
    else:
        for i in range(n):
            if m[i][-1]==0 and dis1(m[x],m[i])<=d:
                ans=DFS(m,i,s)
                if ans=='Yes':
                    break
    return ans

#遍历所有的点
t=''
for i in range(n):
    if m[i][-1]==0 and dis1([0,0],m[i])<=7.5+d:
        t=DFS(m,i,'')
        if t=='Yes':
            break
if t=='Yes':
    print 'Yes'
else:
    print 'No'
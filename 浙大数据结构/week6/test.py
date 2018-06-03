# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 21:25:52 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 20:01:34 2018

@author: Administrator
"""

'''
#读入鳄鱼个数n,以及跳跃距离d
n,d=map(int,raw_input().strip().split(' '))

#初始化图，注意增加原点
m=[[] for i in range(n+1)]
m[0]=[0,0]
for i in range(1,n+1):
    m[i]=map(int,raw_input().strip().split(' '))

'''
m=[[0,0],
 [25, -15],
 [-25, 28],
 [8, 49],
 [29, 15],
 [-35, -2],
 [5, 28],
 [27, -29],
 [-8, -28],
 [-20, -35],
 [-25, -20],
 [-13, 29],
 [-30, 15],
 [-35, 40],
 [12, 12]]
n=14
d=20
'''
m=[[0, 0], [-12, 12], [12, 12], [-12, -12], [12, -12]]
d=13
n=4
'''

#记录是否访问过
y=[0 for i in range(n+1)]

#定义点的距离
def dis1(x,y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5

#定义离岸的距离
def dis2(x):
    return min(abs(x[0]-50),abs(x[0]+50),abs(x[1]-50),abs(x[1]+50))

#定义DFS
#m为图，x为开始节点,y为访问数组，记录是否访问过
def DFS(m,x,y):
    #如果距离岸的最短距离小于等于d，则输出Yes
    if x==0 and dis2(m[x])<=d+15:
        return 'Yes'
    elif dis2(m[x])<=d:
        return "Yes"
    #否则进行DFS
    else:
        y[x]=1
        for i in range(len(y)):
            if y[i]==0 and i==0 and dis1(m[x],m[i])<=15+d:
                DFS(m,i,y)
            elif y[i]==0 and dis1(m[x],m[i])<=d:
                DFS(m,i,y)
        return y

#遍历所有的点
ans=[]
for i in range(n+1):
    if y[i]==0:
        b=DFS(m,i,y)
    if b=='Yes':
        ans='Yes'
        break
    else:
        y=b
if ans=='Yes':
    print 'Yes'
else:
    print 'No'
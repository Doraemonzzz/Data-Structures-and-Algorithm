3,# -*- coding: utf-8 -*-
"""
Created on Wed May 02 12:50:58 2018

@author: Administrator
"""

n,m=map(int,raw_input().split(' '))

#记录点和边
l={}

#记录入度
r=[0 for i in range(n)]
#记录出度
c=[0 for i in range(n)]

#记录每个点指向的点
x={}
#记录指向每个点的点
y={}
for i in range(n):
    x[i]=()
    y[i]=()

for i in range(m):
    a,b,d=map(int,raw_input().split(' '))
    a=a-1
    b=b-1
    l[(a,b)]=d
    #入度
    r[b]+=1
    #出度
    c[a]+=1
    x[a]+=(b,)
    y[b]+=(a,)
#print r,c
    
'''
l={(0, 1): 4,
 (0, 2): 3,
 (1, 3): 5,
 (2, 3): 3,
 (3, 4): 1,
 (3, 5): 6,
 (4, 6): 5,
 (5, 6): 2}
n=7
m=8
x={0: (1, 2), 1: (3,), 2: (3,), 3: (4, 5), 4: (6,), 5: (6,), 6: ()}
y={0: (), 1: (0,), 2: (0,), 3: (1, 2), 4: (3,), 5: (3,), 6: (4, 5)}
r=[0, 1, 1, 2, 1, 1, 2]
c=[2, 1, 1, 2, 1, 1, 0]

l={(0, 1): 1, (0, 2): 2, (1, 3): 4, (2, 1): 3, (3, 2): 5}
n=4
m=5
x={0: (1, 2), 1: (3,), 2: (1,), 3: (2,)}
r=[0, 2, 2, 1]
'''
#记录时间
s=0
#记录访问个数
cnt=0
#记录入度为0的点
queue=[]
#至第n个点的花费时间
f=[0 for i in range(n)]

#将入度为0的点记录着队列中
for i in range(n):
    if r[i]==0:
        queue.append(i)

#记录earliest
while(len(queue)>0):
    v=queue.pop(0)
    cnt+=1
    for i in x[v]:
        r[i]-=1
        if r[i]==0:
            queue.append(i)
        temp=f[v]+l[(v,i)]
        if f[i]<temp:
            f[i]=temp

length=max(f)

#计算latest
g=[length for i in range(n)]

#存放出度为0的点
queue=[]
for i in range(n):
    if c[i]==0:
        queue.append(i)

while(len(queue)>0):
    v=queue.pop(0)
    for i in y[v]:
        c[i]-=1
        if c[i]==0:
            queue.append(i)
        temp=g[v]-l[(i,v)]
        if g[i]>temp:
            g[i]=temp

if cnt==n:
    print length
    for i in range(n-1):
        for j in range(n,-1,-1):
            if (i,j) in l:
                if (g[j]-f[i]-l[(i,j)])==0:
                    print str(i+1)+'->'+str(j+1)
else:
    print 0

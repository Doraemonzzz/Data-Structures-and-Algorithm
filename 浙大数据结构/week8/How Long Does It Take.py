# -*- coding: utf-8 -*-
"""
Created on Wed May 02 11:09:15 2018

@author: Administrator
"""

n,m=map(int,raw_input().split(' '))

#记录点和边
l={}

#记录入度
r=[0 for i in range(n)]

#记录每个点指向的点
x={}
for i in range(n):
    x[i]=()

for i in range(m):
    a,b,c=map(int,raw_input().split(' '))
    l[(a,b)]=c
    r[b]+=1
    x[a]+=(b,)
#print r
'''  
l={(0, 1): 6,
 (0, 2): 4,
 (0, 3): 5,
 (1, 4): 1,
 (2, 4): 1,
 (3, 5): 2,
 (4, 6): 9,
 (4, 7): 7,
 (5, 4): 0,
 (5, 7): 4,
 (6, 8): 2,
 (7, 8): 4}
n=9
m=12
x={0: (1, 2, 3),
 1: (4,),
 2: (4,),
 3: (5,),
 4: (6, 7),
 5: (4, 7),
 6: (8,),
 7: (8,),
 8: ()}
r=[0, 1, 1, 1, 3, 1, 1, 2, 2]
'''
'''
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
if cnt==n:
    print max(f)
else:
    print "Impossible"
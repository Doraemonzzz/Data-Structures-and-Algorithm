# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 12:52:47 2018

@author: 715073608
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 12:08:54 2018

@author: 715073608
"""

import numpy as np


#读入点和边的个数
a=map(int,raw_input().strip().split())
n=a[0]
l=a[1]

#初始矩阵
b=np.array([np.array([float('Inf') for j in range(n)]) for i in range(n)])

#读入数据
for i in range(l):
    temp=map(int,raw_input().strip().split())
    b[temp[0]-1][temp[1]-1]=temp[2]
    b[temp[1]-1][temp[0]-1]=temp[2]
'''

b=[[float('Inf'), 1, 70, float('Inf'), 100, float('Inf')],
 [1, float('Inf'), float('Inf'), 60, 80, 50],
 [70, float('Inf'), float('Inf'), 70, float('Inf'), 80],
 [float('Inf'), 60, 70, float('Inf'), 50, 60],
 [100, 80, float('Inf'), 50, float('Inf'), 60],
 [float('Inf'), 50, 80, 60, 60, float('Inf')]]
n=6
l=11
'''

#弗洛伊德算法
for k in range(n):
    for i in range(n):
        for j in range(n):
            if(i!=j and b[i][k]+b[k][j]<b[i][j]):
                b[i][j]=b[i][k]+b[k][j]
            if (i==j):
                b[i][i]=0
#定义最大值
def findmax(x):
    k=0
    l=0
    for i in range(len(x)):
        if x[i]>l:
            l=x[i]
            k=i
    return l,k

#index=[]
leng=[]
flag=0
for i in b:
    l=max(i)
    k=i.index(l)
    #l,k=findmax(i)
    if l==float('inf'):
        flag=1
        break
    else:
        leng.append(l)
        #index.append(k)

if flag:
    print('0')
else:
    l=min(leng)
    k=leng.index(l)
    print(str(k+1)+' '+str(l))
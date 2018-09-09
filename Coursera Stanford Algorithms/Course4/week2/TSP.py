# -*- coding: utf-8 -*-
"""
Created on Sat May 26 17:58:58 2018

@author: Administrator
"""

import matplotlib.pyplot as plt

x=[]
y=[]

#读取顶点坐标
with open(r'E:\CS161\coursera\4npcomplete\week2\tsp.txt') as text:
#with open(r'E:\CS161\stanford-algs-master\testCases\course4\assignment2TSP\input_float_55_15.txt') as text:
    text.readline()
    vertex=[]
    for i in text.readlines():
        temp=i.strip().split(' ')
        v=list(map(float,temp))
        x.append(v[0])
        y.append(v[1])
        vertex.append(v)
m=len(vertex)

#作图
plt.scatter(x,y)

#观察后发现可以拆成两部分,以横坐标为25000分隔
vertex1=[]
vertex2=[]

for i in vertex:
    if i[0]<=24300:
        vertex1.append(i)
    if i[0]>=23800:
        vertex2.append(i)

vertex1.reverse()

#距离函数
def distance(z1,z2):
    return ((z1[0]-z2[0])**2+(z1[1]-z2[1])**2)**0.5

#计算距离，点从1标注到25
dis={}
for i in range(1,m+1):
    for j in range(i+1,m+1):
        dis[(i,j)]=distance(vertex[i-1],vertex[j-1])


dis1={}
for i in range(1,len(vertex1)+1):
    for j in range(i+1,len(vertex1)+1):
        dis1[(i,j)]=distance(vertex1[i-1],vertex1[j-1])
        
dis2={}
for i in range(1,len(vertex2)+1):
    for j in range(i+1,len(vertex2)+1):
        dis2[(i,j)]=distance(vertex2[i-1],vertex2[j-1])

#用25位的二进制数表示子集,字符串表示
key=[]
def key(n):
    if n==1:
        return ["1","0"]
    else:
        result=[]
        ans=key(n-1)
        for i in ans:
            result.append("1"+i)
            result.append("0"+i)
        return result

#计算子集元素个数，即含有1的个数
def size(x):
    n=0
    for i in x:
        n+=int(i)
    return n

#找到元素值为1的位置，除去最后一个元素
def findone(x):
    ans=[]
    for i in range(len(x)):
        if x[i]=="1":
            ans.append(i+1)
    return ans

#对子集按长度分类
def proset(s,n):
    ans={}
    for i in range(n+1):
        ans[i]=[]
    for i in s:
        ans[size(i)].append(i)
    return ans

def TSP(x,dis):
    n=len(x)
    #构造子集
    subset=key(n)
    #按长度分类
    set1=proset(subset,n)
    #初始化
    A={}
    for i in subset:
        if i=="1"+"0"*(n-1):
            A[(i,1)]=0
        else:
            A[(i,1)]=float("inf")
    for m in range(2,n+1):
        for i in set1[m]:
            if i[0]=="1":
                one=findone(i)
                #print(one)
                for j in one:
                    small=float('inf')
                    if j!=1:
                        tempkey=i[:j-1]+"0"+i[j:]
                        #print(tempkey,i,j)
                        for k in range(1,n+1):
                            if k!=j:
                                keyx=min(k,j)
                                keyy=max(k,j)
                                #print(tempkey,k,A.keys())
                                if (tempkey,k) in A:
                                    small=min(A[(tempkey,k)]+dis[(keyx,keyy)],small)
                                    A[(i,j)]=small
    ans=float("inf")
    for j in range(2,n+1):
        if ("1"*n,j) in A:
            ans=min(A[("1"*n,j)]+dis[(1,j)],ans)
    return A,ans,set1


l=TSP(vertex1,dis1)[1]+TSP(vertex2,dis2)[1]-2*distance(vertex1[0],vertex2[0])
print(l)

#26442.730308954753
#https://www.coursera.org/learn/algorithms-npcomplete/discussions/weeks/2/threads/FNo8tpFPEeeH2hLapWklpg
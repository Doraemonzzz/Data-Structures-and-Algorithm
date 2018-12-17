# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 09:32:08 2018

@author: Administrator
"""

import random

#预处理，将数据读入
a = open("kargerMinCut.txt")
b = []
for i in a.readlines():
    b.append(list(map(int,i.strip('\n').strip('\t').split('\t'))))
    
#将原来的数组转换为1*201的数组，第一各元素表示点i，若i,j有边，则第j+1个元素为1,否则为0
def f(x):
    a = []
    a.append(x[0])
    for i in range(1,201):
        if i in x[1:]:
            a.append(1)
        else:
            a.append(0)
    return a

c = []
#对全部数据处理
for i in range(len(b)):
    c.append(f(b[i]))

#定义运算函数,a,b表示数组，a1,b1表示合并的点
def g(a,b,a1,b1):
    m = [a[0]]#记录新的数组
    n = a1+b1#记录进的合并点
    x = b[0]
    y = a[0]
    for i in range(1, len(a)):
        m.append(a[i] + b[i])
    #去除自循环
    m[x] = 0
    m[y] = 0
    return m, n
'''
测试使用
a=[1,0,1,0,0]
a1=[1]
b=[2,1,0,0,1]
b1=[2]
print g(a,b,a1,b1)
'''
   
def find(x):
    j = []
    for i in range(1,len(x)):
        if x[i] > 0:
            j.append(i-1)
    return j
#print find(c[0]),c[0]
    

#定义可使用的数组
shuzu = list(range(200))
#合并的点，第一个元素为代表元
d = []
for i in range(200):
    d.append([c[i][0]])
#作副本，方便重复使用
e = c[:]
flag = True
k = 0
while len(shuzu) > 2 and k < 1000:
    #定义随机初始值
    now = random.randint(0, len(shuzu)-1)
    #找到可以合并的点
    do1 = find(c[now])
    j = []
    for i in do1:
        if i in shuzu:
            j.append(i)
    if len(j) == 0:
        flag = False
    if flag:
        do = j[random.randint(0, len(j)-1)]
        temp1,temp2 = g(c[now],c[do],d[now],d[do])
        #print temp1,temp2,flag
        shuzu.remove(do)
        d[now] = temp2
        e[now] = temp1
    else:
        continue
    k += 1
    
#长度
L = [len(i) for i in d]
print(max(L))



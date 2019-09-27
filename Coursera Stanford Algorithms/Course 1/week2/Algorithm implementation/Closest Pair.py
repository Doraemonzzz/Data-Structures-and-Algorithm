# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 11:51:31 2019

@author: qinzhen
"""

import numpy as np
import functools
import time

#生成测试数据
def generate(n):
    return np.random.randn(n, 2)

#比较函数
def cmp1(a, b):
    return a[0] - b[0]

def cmp2(a, b):
    return a[1] - b[1]

#距离函数
def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

#直接解法
def Closest_Pair_bf(data):
    n = len(data)
    d_min = 1e9
    p = []
    q = []
    for i in range(n):
        for j in range(i + 1, n):
            d1 = dist(data[i], data[j])
            if d1 < d_min:
                d_min = d1
                p = data[i]
                q = data[j]
    
    return p, q, np.sqrt(d_min)

#将Px划分为前半部分以及后半部分
def Split(Px, Py):
    n = len(Px)
    m = n // 2
    #中间位置的x坐标
    x_mid = Px[m][0]
    #x部分直接划分即可
    Lx = Px[:m]
    Rx = Px[m:]
    #y部分遍历即可
    Ly = []
    Ry = []
    for i in range(n):
        if (Py[i][0] < x_mid):
            Ly.append(Py[i])
        else:
            Ry.append(Py[i])

    return Lx, Ly, Rx, Ry

def Closest_Split_Pair(Px, Py, d):
    n = len(Px)
    m = n // 2
    #左半部分最大坐标
    x_mid = Px[m - 1][0]
    #Sy为x坐标在[x_mid - d, x_mid + d]范围内的点，按y坐标排序
    Sy = []
    for i in range(n):
        if (Py[i][0] >= x_mid - d and Py[i][0] <= x_mid + d):
            Sy.append(Py[i])
    #Sy的长度
    l = len(Sy)
    #初始化
    d_min = 1e9
    p = []
    q = []
    if (l == 0):
        return p, q, np.sqrt(d_min)
    for i in range(l - 1):
        k = min(7, l - 1 - i)
        for j in range(1, k + 1):
            d1 = dist(Sy[i], Sy[i + j])
            if (d1 < d_min):
                d_min = d1
                p = Sy[i]
                q = Sy[i + j]
    return p, q, np.sqrt(d_min)

def Closest_Pair(Px, Py):
    n = len(Px)
    if (n <= 3):
        return Closest_Pair_bf(Px)
    else:
        #划分
        Lx, Ly, Rx, Ry = Split(Px, Py)
        p1, q1, d1 = Closest_Pair(Lx, Ly)
        p2, q2, d2 = Closest_Pair(Rx, Ry)
        d = min(d1, d2)
        p3, q3, d3 = Closest_Split_Pair(Px, Py, d)
        d_min = min(d3, d)
        #输出
        if (d_min == d1):
            return p1, q1, d1
        elif (d_min == d2):
            return p2, q2, d2
        else:
            return p3, q3, d3

####测试算法
#数据数量
N = 2000
#生成数据
data = generate(N)

#直接解法
t1 = time.time()
p1, q1, d_min1 = Closest_Pair_bf(data)
t2 = time.time()
print(p1, q1, d_min1)
print(t2 - t1)

#快速算法
t1 = time.time()
#按x坐标排序
Px = sorted(data, key=functools.cmp_to_key(cmp1))
#按y坐标排序
Py = sorted(data, key=functools.cmp_to_key(cmp2))
p2, q2, d_min2 = Closest_Pair(Px, Py)
t2 = time.time()
print(p2, q2, d_min2)
print(t2 - t1)
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 21:53:08 2019

@author: qinzhen
"""
import numpy as np

def Exchange(A, i, j):
    #交换元素的值
    p = A[i]
    A[i] = A[j]
    A[j] = p

def Partion(A, l, r, p):
    #找到p的位置
    for i in range(l, r + 1):
        if (A[i] == p):
            index = i
            break
    #交换位置
    Exchange(A, index, l)
    i = l + 1
    for j in range(l + 1, r + 1):
        if (A[j] < p):
            Exchange(A, i, j)
            i += 1
    Exchange(A, l, i - 1)
    
    return i - 1

def Deterministic_Selection(A, i):
    n = len(A)
    if (n == 1):
        return A[0]
    C = []
    for s in range(0, n, 5):
        t = min(n, s + 5)
        A[s: t].sort()
        #找到中间元素
        index = min(s + 2, n - 1)
        C.append(A[index])
    p = Deterministic_Selection(C, len(C) // 2)
    #返回位置
    j = Partion(A, 0, n - 1, p)
    #次序统计量
    k = j + 1
    if (i == k):
        return p
    elif (k > i):
        return Deterministic_Selection(A[: j], i)
    else:
        return Deterministic_Selection(A[j + 1:], i - k)

    return A

#测试
N = int(1e5)
#次序统计量
k = np.random.randint(1, N + 1)
data = np.random.rand(N)
data_sort = np.sort(data)
#测试结果
r1 = Deterministic_Selection(data, k)
r2 = data_sort[k - 1]
print(r1 == r2)
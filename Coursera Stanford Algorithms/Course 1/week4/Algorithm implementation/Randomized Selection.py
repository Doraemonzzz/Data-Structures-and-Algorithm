# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 21:05:49 2019

@author: qinzhen
"""

import numpy as np

def Exchange(A, i, j):
    #交换元素的值
    p = A[i]
    A[i] = A[j]
    A[j] = p

def Partion(A, l, r):
    #随机选择
    index = np.random.randint(l, r + 1)
    Exchange(A, index, l)
    #选择主元
    p = A[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if (A[j] < p):
            Exchange(A, i, j)
            i += 1
    Exchange(A, l, i - 1)
    
    return i - 1
    
def Randomized_Selection(A, i):
    n = len(A)
    if (n == 1):
        return A[0]
    #返回位置
    j = Partion(A, 0, n - 1)
    #次序统计量
    k = j + 1
    p = A[j]
    if (i == k):
        return p
    elif (k > i):
        return Randomized_Selection(A[: j], i)
    else:
        return Randomized_Selection(A[j + 1:], i - k)
    
#测试
N = int(1e5)
#次序统计量
k = np.random.randint(1, N + 1)
data = np.random.rand(N)
data_sort = np.sort(data)

#测试结果
r1 = Randomized_Selection(data, k)
r2 = data_sort[k - 1]
print(r1 == r2)
    
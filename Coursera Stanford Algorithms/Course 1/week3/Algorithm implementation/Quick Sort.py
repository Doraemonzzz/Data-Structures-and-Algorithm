# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:27:10 2019

@author: qinzhen
"""

import numpy as np

def Exchange(A, i, j):
    #交换元素的值
    p = A[i]
    A[i] = A[j]
    A[j] = p
    
def Partion(A, l, r):
    p = A[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if (A[j] < p):
            Exchange(A, i, j)
            i += 1
    Exchange(A, l, i - 1)
    
    return i - 1
    
def Quick_Sort(A, l, r):
    n = r - l + 1
    if (n <= 1):
        return
    #返回pivot的位置
    i = Partion(A, l, r)
    Quick_Sort(A, l, i - 1)
    Quick_Sort(A, i + 1, r)
    
def QuickSort(A):
    n = len(A)
    Quick_Sort(A, 0, n - 1)
    
#测试
N = 1000
Max = 1e5
data = np.random.randint(0, Max, size=N)
data_sort = np.sort(data)
#排序
QuickSort(data)
#测试结果
print(np.sum(data != data_sort))
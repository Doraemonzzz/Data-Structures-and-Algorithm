# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 22:53:42 2019

@author: qinzhen
"""

import numpy as np

def Merge(A, l, m, r):
    """
    l, ..., m为第一部分
    m + 1, ..., r为第二部分
    """
    #存储结果
    C = []
    #索引
    i = l
    j = m + 1
    while ((i <= m) and (j <= r)):
        if (A[i] < A[j]):
            C.append(A[i])
            i += 1
        else:
            C.append(A[j])
            j += 1
    #处理剩余部分
    while (i <= m):
        C.append(A[i])
        i += 1
    while (j <= r):
        C.append(A[j])
        j += 1
    #更新
    A[l: (r + 1)] = C

def MSort(A, l, r):
    '''
    对l, ... , r排序
    '''
    if (l < r):
        m = (l + r) // 2
        MSort(A, l, m)
        MSort(A, m + 1, r)
        Merge(A, l, m, r)
        
def Merge_Sort(A):
    n = len(A)
    MSort(A, 0, n - 1)

#测试
N = 1000
Max = 1e5
data = np.random.randint(0, Max, size=N)
data_sort = np.sort(data)
#排序
Merge_Sort(data)
#测试结果
print(np.sum(data != data_sort))


    
    
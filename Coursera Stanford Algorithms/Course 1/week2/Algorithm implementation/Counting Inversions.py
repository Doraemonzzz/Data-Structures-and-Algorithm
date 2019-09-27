# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:12:27 2019

@author: qinzhen
"""

import numpy as np

def Count_split_inv(A, l, m, r):
    """
    l, ..., m为第一部分
    m + 1, ..., r为第二部分
    """
    #存储结果
    C = []
    #索引
    i = l
    j = m + 1
    #逆序数
    cnt = 0
    while ((i <= m) and (j <= r)):
        if (A[i] <= A[j]):
            C.append(A[i])
            i += 1
        else:
            C.append(A[j])
            j += 1
            cnt += m - i + 1
    #处理剩余部分
    while (i <= m):
        C.append(A[i])
        i += 1
    while (j <= r):
        C.append(A[j])
        j += 1
    #更新
    A[l: (r + 1)] = C
    return cnt

def Sort_and_Count(A, l, r):
    '''
    对l, ... , r排序并计算逆序数
    '''
    if (l >= r):
        return 0
    else:
        m = (l + r) // 2
        x = Sort_and_Count(A, l, m)
        y = Sort_and_Count(A, m + 1, r)
        z = Count_split_inv(A, l, m, r)
        return x + y + z
        
def Count_inv(A):
    n = len(A)
    return Sort_and_Count(A, 0, n - 1)

def Count_inv_bf(A):
    cnt = 0
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if (A[i] > A[j]):
                cnt += 1
    
    return cnt

#测试
N = 1000
data = np.random.randn(N)
cnt1 = Count_inv_bf(data)
cnt2 = Count_inv(data)

print(cnt1, cnt2)
print(cnt1 == cnt2)
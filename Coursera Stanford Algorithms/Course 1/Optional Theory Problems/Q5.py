# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:06:26 2019

@author: qinzhen
"""

'''
Given an array of n distinct (but unsorted) elements x_1,x_2,\ldots,x_n with positive weights 
w_1,w_2,\ldots,w_n such that \sum_{i=1}^n w_i = W, 
a weighted median is an element x_k for which the total weight of all elements with value less than x_k(i.e., \sum_{x_i \lt x_k} w_i) is at most W/2, 
and also the total weight of elements with value larger than x_k (i.e., \sum_{x_i \gt x_k} w_i) is at most W/2. 
Observe that there are at most two weighted medians. Show how to compute all weighted medians in O(n) worst-case time.
'''

import numpy as np

def Generate_data(m):
    N = int(1e6)
    data = np.arange(N)
    array1 = np.random.choice(data, size=m, replace=False)
    array2 = np.random.choice(data, size=m, replace=False)
    
    return np.c_[array1, array2]

def Exchange(A, i, j):
    #交换元素的值
    p = np.array(A[i])
    A[i] = np.array(A[j])
    A[j] = p

#1维Partion
def Partion1(A, l, r, p):
    #找到p的位置
    index = l
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

#2维Partion 
def Partion2(A, l, r, p):
    #找到p的位置
    index = l
    for i in range(l, r + 1):
        if (A[i][0] == p):
            index = i
            break
    #交换位置
    Exchange(A, index, l)
    i = l + 1
    for j in range(l + 1, r + 1):
        #按第一个维度partion
        if (A[j][0] < p):
            Exchange(A, i, j)
            i += 1
    Exchange(A, l, i - 1)
    
    return i - 1

#找到A[l,...,r]中小于p的最大数
def Find_max(A, l, r, p):
    index = l
    for i in range(l, r + 1):
        if (A[i][0] > A[index][0]):
            index = i
            
    return A[index][0]

#找到A[l,...,r]中大于p的最小数
def Find_min(A, l, r, p):
    index = l
    for i in range(l, r + 1):
        if (A[i][0] < A[index][0]):
            index = i
            
    return A[index][0]

#判断是否满足条件
def Judge(A, p, W):
    W1 = 0
    W2 = 0
    for i in A:
        if (i[0] < p):
            W1 += i[1]
        elif (i[0] > p):
            W2 += i[1]
    return (W1 <= W / 2) and (W2 <= W / 2)
    

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
    j = Partion1(A, 0, n - 1, p)
    #次序统计量
    k = j + 1
    if (i == k):
        return p
    elif (k > i):
        return Deterministic_Selection(A[: j], i)
    else:
        return Deterministic_Selection(A[j + 1:], i - k)

def Weighted_median(A, B, W, Hash, res):
    '''
    A为原始序列（2维），B为当前序列（1维）, Hash记录是否访问过该位置的元素
    '''
    if (len(B) == 1):
        return B[0]
    #找到中位数
    p = Deterministic_Selection(B, len(B) // 2)
    n = len(A)
    #返回位置
    j = Partion2(A, 0, n - 1, p)
    #W1
    W1 = np.sum(A[: j, 1])
    #W2
    W2 = np.sum(A[j + 1:, 1])
    if (Hash[j] == 1):
        p1 = Find_max(A, 0, j - 1, p)
        if (Judge(A, p1, W) and (Hash[j - 1] == 0)):
            Hash[j - 1] = 1
            res.append(p1)
        p2 = Find_min(A, j + 1, n - 1, p)
        if (Judge(A, p2, W) and (Hash[j + 1] == 0)):
            Hash[j + 1] = 1
            res.append(p2)
        return
    else:
        Hash[j] = 1
    if ((W1 <= W / 2) and (W2 <= W / 2)):
        res.append(A[j][0])
    elif (W1 > W / 2):
        B = [i for i in B if i <= p]
        Weighted_median(A, B, W, Hash, res)
    else:
        B = [i for i in B if i >= p]
        Weighted_median(A, B, W, Hash, res)

#蛮力法计算Weighted_median
def Weighted_median_BF(A, W):
    res = []
    for i in A[:, 0]:
        index1 = (A[:, 0] < i)
        index2 = (A[:, 0] > i)
        W1 = np.sum(A[index1][:, 1])
        W2 = np.sum(A[index2][:, 1])
        
        if (W1 <= W / 2) and (W2 <= W / 2):
            res.append(i)
    
    return res

#判断列表是否相同
def JudgeList(a, b):
    n = len(a)
    m = len(b)
    if (n != m):
        return False
    else:
        for i in range(n):
            if (a[i] != b[i]):
                return False
        return True

tmp = []
N = 100
for k in range(N):
    for i in range(1, 4):
        #生成数据
        d = 10 ** i
        data = np.random.uniform(size=[d, 2])
        #计算权重
        W = np.sum(data[:, 1])
        #Hash表
        Hash = np.zeros(d)
        #计算结果
        p1 = []
        Weighted_median(data, np.array(data[:, 0]), W, Hash, p1)
        p2 = Weighted_median_BF(data, W)
        #保存比较结果
        tmp.append(JudgeList(p1, p2))

print(np.sum(tmp) == N * 3)
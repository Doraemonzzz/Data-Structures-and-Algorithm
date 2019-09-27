# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:13:52 2019

@author: qinzhen
"""

'''
You are given a sorted (from smallest to largest) array A of n distinct integers which can be positive, negative, or zero. 
You want to decide whether or not there is an index i such that A[i] = i. 
Design the fastest algorithm that you can for solving this problem.
'''
import numpy as np

def Generate_data(m):
    N = int(1e6)
    data = np.arange(N)
    array = np.random.choice(data, size=m, replace=False)
    
    return np.sort(array)

#判断函数
def Judge_(array, l, r):
    if (l > r):
        return False
    n = (l + r) // 2
    if (array[n] == n):
        return True
    elif (array[n] > n):
        r = n - 1
        return Judge_(array, l, r)
    else:
        l = n + 1
        return Judge_(array, l, r)

def Judge(array):
    n = array.shape[0]
    
    return Judge_(array, 0, n - 1)
    
#蛮力搜索
def Judge_BF(array):
    n = len(array)
    for i in range(n):
        if (array[i] == i):
            return True
    return False

#测试
M = range(1, 5)
for m in M:
    n = 10 ** m
    array = Generate_data(n)
    r1 = Judge(array)
    r2 = Judge_BF(array)
    
    print(r1 == r2)
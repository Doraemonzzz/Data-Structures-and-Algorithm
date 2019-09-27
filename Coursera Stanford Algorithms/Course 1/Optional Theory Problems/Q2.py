# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:23:16 2019

@author: qinzhen
"""

'''
You are a given a unimodal array of n distinct elements, meaning that its entries are in increasing order up until its maximum element, after which its elements are in decreasing order. 
Give an algorithm to compute the maximum element that runs in O(log n) time.
'''

import numpy as np

def Generate_data(max_n=1000):
    n = np.random.randint(1, max_n)
    m = np.random.randint(1, max_n)

    d1 = np.random.randn(n)
    d2 = np.random.randn(m)
    
    d1 = np.sort(d1)
    d2 = np.sort(d2)[::-1]
    data = np.append(d1, d2)
    
    return data

def Find_max(array):
    n = len(array)
    if (n <= 3):
        return np.max(array)

    n1 = n // 3
    n2 = 2 * n1
    
    #端点元素
    d1 = array[0]
    d2 = array[n1]
    d3 = array[n2]
    
    if ((d1 <= d2) and (d2 <= d3)):
        return Find_max(array[n1:])
    else:
        return Find_max(array[:n2])

#测试
for i in range(10):
    array = Generate_data()
    res = Find_max(array)
    print(res == np.max(array))
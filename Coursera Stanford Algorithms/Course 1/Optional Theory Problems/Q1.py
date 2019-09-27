# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:43:23 2019

@author: qinzhen
"""

'''
You are given as input an unsorted array of n distinct numbers, where n is a power of 2. 
Give an algorithm that identifies the second-largest number in the array, 
and that uses at most n + log_2n − 2 comparisons.
'''

import numpy as np

def Find_second_largest(array):
    n = len(array)
    #构造Hash，值为和键比较过且小于键的元素
    mp = dict()
    for i in range(n):
        mp[i] = []
    #索引集合
    index = range(n)
    #比较次数
    Cnt = 0
    
    while (len(index) != 1):
        new_index, cnt = Compare(array, index, mp)
        index = new_index[:]
        Cnt += cnt
        
    #和最大值比较过的元素
    index1 = mp[index[0]]
    array1 = [array[i] for i in index1]
    m = len(index1)

    #找到array1中的最大值
    res = array1[0]
    for i in range(1, m):
        Cnt += 1
        if (array1[i] > res):
            res = array1[i]
    
    return res, Cnt

#进行一轮比较
def Compare(array, index, mp):
    n = len(index)
    #记录下一轮的索引
    new_index = []
    for i in range(n // 2):
        i1 = index[2 * i]
        i2 = index[2 * i + 1]
        x = array[i1]
        y = array[i2]
        if (x > y):
            new_index.append(i1)
            mp[i1].append(i2)
        else:
            new_index.append(i2)
            mp[i2].append(i1)

    #判断奇偶性
    if n % 2 == 1:
        new_index.append(index[-1])
    
    return new_index, n // 2

#测试
factor = [2, 5, 10, 15]
for n in factor:
    N = 2 ** n
    array = np.random.rand(N)
    #理论比较次数
    m = N + np.log2(N) - 2
    #计算结果
    res, cnt = Find_second_largest(array)
    #计算第二大的元素
    ans = np.sort(array)[-2]
    #验证
    print(res == ans, cnt == m)
        
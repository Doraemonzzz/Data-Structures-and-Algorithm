# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:31:46 2019

@author: qinzhen
"""

'''
You are given an n by n grid of distinct numbers. 
A number is a local minimum if it is smaller than all of its neighbors. 
(A neighbor of a number is one immediately above, below, to the left, or the right.  Most numbers have four neighbors;  
numbers on the side have three; the four corners have two.) 
Use the divide-and-conquer algorithm design paradigm to compute a local minimum with only O(n) comparisons between pairs of numbers. 
'''

import numpy as np

#判断是否越界
def Judge(i, n):
    return (i >= 0) and (i < n) 

def Judge_node(i, j, n):
    return Judge(i, n) and Judge(j, n)

#判断是否为局部最小
def Judge_local_minimum(data, i, j):
    n = data.shape[0]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    d = data[i][j]
    for s in range(4):
        i1 = i + dx[s]
        j1 = j + dy[s]
        if (Judge_node(i1, j1, n) and (data[i1][j1] < d)):
            return False
    
    return True

def Find_local_minimum_(data, x1, y1, x2, y2):
    '''
    搜索区域的左上角为(x1, y1)，右下角为(x2, y2)
    '''
    if ((x1 == x2) and (y1 == y2)):
        return x1, y1
    
    x0 = (x1 + x2) // 2
    y0 = (y1 + y2) // 2
    #记录当前最小值
    local_minimum = data[x1][y1]
    #记录索引
    i = x1
    j = y1
    #找到最小值
    x = [x0, x1, x2]
    y = [y0, y1, y2]
    for s in x:
        for t in range(y1, y2 + 1):
            if (data[s][t] < local_minimum):
                i = s
                j = t
                local_minimum = data[s][t]
    for t in y:
        for s in range(x1, x2 + 1):
            if (data[s][t] < local_minimum):
                i = s
                j = t
                local_minimum = data[s][t]
    #判断是否为局部最优
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    i0 = i
    j0 = j
    for s in range(4):
        i1 = i + dx[s]
        j1 = j + dy[s]
        if (Judge_node(i1, j1, n) and (data[i1][j1] < data[i0][j0])):
            i0 = i1
            j0 = j1
    
    #如果为局部最优则直接返回
    if ((i == i0) and (j == j0)):
        return i, j

    #中心点
    if ((i == x0) and (j == y0)):
        return i, j
    elif ((i == x1) or (i == x2) or (j == y1) or (j == y2)):#边界区域
        #确定属于哪个区域
        u = int(i <= x0)
        v = int(j <= y0)
        x3 = x[u]
        y3 = y[v]
        if u:
            x4 = x[u - 1]
        else:
            x4 = x[u + 1]
        if v:
            y4 = y[v - 1]
        else:
            y4 = y[v + 1]
        
        return Find_local_minimum_(data, x3, y3, x4, y4)
    else:
        #找到局部最小值
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        i0 = i
        j0 = j
        for s in range(4):
            i1 = i + dx[s]
            j1 = j + dy[s]
            if (Judge_node(i1, j1, n) and (data[i1][j1] < data[i0][j0])):
                i0 = i1
                j0 = j1
        #如果为局部最小值则直接返回
        if ((i0 == i) and (j0 == j)):
            return i, j
        else:
            #确定属于哪个区域
            u = int(i <= x0)
            v = int(j <= y0)
            x3 = x[u]
            y3 = y[v]
            if u:
                x4 = x[u - 1]
            else:
                x4 = x[u + 1]
            if v:
                y4 = y[v - 1]
            else:
                y4 = y[v + 1]
            
            return Find_local_minimum_(data, x3, y3, x4, y4)
        
def Find_local_minimum(data):
    n = data.shape[0]
    i, j = Find_local_minimum_(data, 0, 0, n - 1, n - 1)
    print(Judge_local_minimum(data, i, j))

for i in range(1, 5):
    n = 10 ** i
    data = np.random.rand(n, n)
    Find_local_minimum(data)
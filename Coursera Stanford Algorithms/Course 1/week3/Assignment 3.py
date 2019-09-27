# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:24:34 2019

@author: qinzhen
"""

with open('data.txt') as a:
    b = []
    for i in a.readlines():
        b.append(int(i.strip()))
    
def Median(a,b,c):
    if a < b:
        if b < c:
            return b, 2
        else:
            if a > c:
                return a, 1
            else:
                return c, 3
    else:
        if c > a:
            return a, 1
        else:
            if c > b:
                return c, 3
            else:
                return b, 2
            
def Exchange(A, i, j):
    #交换元素的值
    p = A[i]
    A[i] = A[j]
    A[j] = p
        
def Quicksort(A, l, r, flag):
    if l >= r:
        return 0
    else:
        if flag == 1:
            p = A[l]
        elif flag == 2:
            #交换A[l],A[r]
            Exchange(A, l, r)
            p = A[l]
        else:
            u = A[l]
            v = A[(l + r) // 2]
            w = A[r]
            #计算中位数以及对应的位置
            m, n = Median(u, v, w)
            if n==1:
                pass
            elif n==2:
                Exchange(A, l, (l+r) // 2)
            else:
                Exchange(A, l, r)
            p = A[l]
        i = l + 1
        for j in range(l+1, r+1):
            if A[j] < p:
                #交换A[i]和A[j]
                Exchange(A, i, j)
                i += 1
        #交换A[l]和A[i-1]
        Exchange(A, l, i-1)
        #注意pivot在i-1的位置
        return Quicksort(A, l, i-2, flag) + Quicksort(A, i, r, flag) + r - l

#b= [3, 4, 1, 2]
for i in range(1, 4):
    with open('data.txt') as a:
        b = []
        for j in a.readlines():
            b.append(int(j.strip()))
    n = len(b)
    print(Quicksort(b, 0, n-1, i))
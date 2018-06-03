t# -*- coding: utf-8 -*-
"""
Created on Mon May 14 16:20:15 2018

@author: Administrator
"""
'''
n,k,m=map(int,raw_input().strip().split(' '))

##读取分值，加个元素方便后续处理
p=[0]
p+=map(int,raw_input().strip().split(' '))

a=[[0 for i in range(k+1)] for j in range(n+1)]
 
for i in range(m):
    x,y,z=map(int,raw_input().strip().split(' '))
    if(a[x][y]<z):
        a[x][y]=z
'''
        
a=[[0, 0, 0, 0, 0],
 [0, 18, 18, 4, 2],
 [0, 20, 25, 0, 18],
 [0, 0, 0, 0, 0],
 [0, 15, 0, 25, 0],
 [0, 20, 0, 22, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 25, 0, 17]]
p=[0, 20, 25, 25, 30]
n,k,m=(7, 4, 20)

#计算总分
#

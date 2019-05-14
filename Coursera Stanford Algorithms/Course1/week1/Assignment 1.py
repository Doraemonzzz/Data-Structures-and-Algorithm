# -*- coding: utf-8 -*-
"""
Created on Mon May  6 21:02:55 2019

@author: qinzhen
"""

def Karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    else:
        #计算位数
        k = min(len(str(x)), len(str(y))) // 2
        u = 10 ** k
        a = x // u
        b = x - a * u
        c = y // u
        d = y - c * u
        #递归
        ac = Karatsuba(a, c)
        bd = Karatsuba(b, d)
        abcd = Karatsuba(a+b, c+d)
        #合并结果
        adbc = abcd - ac - bd
        
        res = u ** 2 * ac + u * adbc + bd
        
        return res
    
x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

print(Karatsuba(x, y))
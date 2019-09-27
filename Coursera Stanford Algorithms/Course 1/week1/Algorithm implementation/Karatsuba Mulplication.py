# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 22:52:28 2019

@author: qinzhen
"""

import numpy as np

def Karatsuba_Mulplication(x, y):
    '''
    输入x, y为字符串，首先补0，使得数字长度一样
    '''
    #预处理，使得长度一样
    n1 = len(x)
    n2 = len(y)
    n = max(n1, n2)
    if (n1 < n2):
        x = "0" * (n2 - n1) + x
    else:
        y = "0" * (n1 - n2) + y
    
    #个位数
    if (n == 1):
        return int(x) * int(y)
    else:
        k = n // 2
        #将数分为前l位和剩余部分
        l = n - k
        u = 10 ** k
        a = x[:l]
        b = x[l:]
        c = y[:l]
        d = y[l:]
        ab = str(int(a) + int(b))
        cd = str(int(c) + int(d))
        #递归
        ac = Karatsuba_Mulplication(a, c)
        bd = Karatsuba_Mulplication(b, d)
        abcd = Karatsuba_Mulplication(ab, cd)
        #合并结果
        adbc = abcd - ac - bd
        res = u ** 2 * ac + u * adbc + bd
        
        return res

#测试
N = 1000
Max = 1e5

for i in range(N):
    x = np.random.randint(0, Max)
    y = np.random.randint(0, Max)
    z = x * y
    #转换为字符串
    x1 = str(x)
    y1 = str(y)
    z1 = Karatsuba_Mulplication(x1, y1)
    
    print(z == z1)
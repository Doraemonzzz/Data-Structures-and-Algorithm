# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:01:09 2019

@author: qinzhen
"""

'''
这是输出逆序数对改进版，在递归的时候将数组排序，
利用此计算组间的逆序数，需要利用归并排序。
'''

def merge_sort(x):
	a = len(x)
	b = []
	if a == 1:
		return 0, x
	else:
        #前一半数量
		c = a // 2
        #后一半数量
		d = a - c
		u0, u = merge_sort(x[:c])
		v0, v = merge_sort(x[c:])
        #记录u的下标
		i = 0
        #记录v的下标
		j = 0
        #记录循环次数
		k = 1
        #记录跨组逆序的个数
		s = 0
        #merge
		while k <= a:
			if i <= c-1 and j <= d-1:
				if u[i] <= v[j]:
					b.append(u[i])
					i += 1
					k += 1
				else:
					b.append(v[j])
					j += 1
					k += 1
                    #累加放入第二个数列元素时第一个数列还剩余的元素个数
					s += c - i
			elif i == c:
				b.append(v[j])
				j += 1
				k += 1
			elif j == d:
				b.append(u[i])
				i += 1
				k += 1
		return s, b		
    
def f(x):
	a = len(x)
	if a == 1:
		return 0
	else:
		b = a // 2
		c = x[:b]
		d = x[b:]
		e, g = merge_sort(x)
		return f(c) + f(d) + e

with open(r'IntegerArray.txt') as a:
    b = []
    for i in a.readlines():
        b.append(int(i.strip()))
    print(f(b))
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 15:38:06 2018

@author: Administrator
"""

'''
这是输出逆序数对改进版，在分治递归的时候将数组排序，
利用此计算组间的逆序数,需要利用归并排序。
'''
'''
这是输出逆序数对改进版，在分治递归的时候将数组排序，
利用此计算组间的逆序数,需要利用归并排序。
'''
def merge_sort(x):
	a = len(x)
	b = []
	if a == 1:
		return 0,x
	else:
		c = a//2
		d = a-c
		u0,u = merge_sort(x[:c])
		v0,v = merge_sort(x[c:])
		i = 0#记录u的下标
		j = 0#记录v的下标
		k = 1#记录循环次数
		s = 0#记录跨组逆序的个数
		#print c,d,u,v,x
		while k <= a:
			#print i,j,len(u),len(v),c,d,k
			if i <= c-1 and j <= d-1:
				if u[i] <= v[j]:
					b.append(u[i])
					i += 1
					k += 1
					#print i,j,b
				else:
					b.append(v[j])
					j += 1
					k += 1
					s += c-i#累加放入第二个数列元素时第一个数列还剩余的元素个数
					#print i,j,b
			elif i == c:
				b.append(v[j])
				j += 1
				k += 1
				#print i,j,b
			elif j == d:
				b.append(u[i])
				i += 1
				k += 1
				#print i,j,b
		return s,b		
		
def f(x):
	a = len(x)
	if a == 1:
		return 0
	else:
		b = a//2
		c = x[:b]
		d = x[b:]
		e,g = merge_sort(x)
		return f(c)+f(d)+e
    
a=open(r'IntegerArray.txt')
b=[]
for i in a.readlines():
	b.append(int(i.strip()))

print(f(b))
#2407905288
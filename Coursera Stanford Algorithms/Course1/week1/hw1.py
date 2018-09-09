# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 21:05:43 2018

@author: Administrator
"""  
def karatsuba(x,y):
	#转化为字符串
	x1=str(x)
	y1=str(y)
	#计算k
	k=min(len(x1),len(y1))//2
	if k>=1:
		#计算a,b,c,d
		a = x // (10**k)
		b = x - a*(10**k)
		c = y // (10**k)
		d = y - c*(10**k)
		return (10**(2*k))*karatsuba(a,c) + (10**k)*(karatsuba(a+b,c+d)-karatsuba(a,c)-karatsuba(b,d)) \
            + karatsuba(b,d)
	else:
		return x*y
print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))
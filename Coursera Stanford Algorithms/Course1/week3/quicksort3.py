# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 23:18:32 2018

@author: Administrator
"""

a=open('data.txt')
b=[]
for i in a.readlines():
	b.append(int(i.strip()))

def mid(a,b,c):
    if a<b:
        if b<c:
            return b,2
        else:
            if a>c:
                return a,1
            else:
                return c,3
    else:
        if c>a:
            return a,1
        else:
            if c>b:
                return c,3
            else:
                return b,2

def exchange(a,b):
    p=a
    a=b
    b=p

def quicksort(A,l,r):
    #比较次数
    if l>=r:
        #return
        return 0
    else:
        u=A[l-1]
        v=A[(l+r-2)/2]
        w=A[r-1]
        m,n=mid(u,v,w)
        if n==1:
            pass
        elif n==2:
            exchange(A[l-1],A[(l+r-2)/2])
        else:
            exchange(A[l-1],A[r-1])
        p=A[l-1]
        i=l
        for j in range(l,r):
            if A[j]<p:
                #交换A[j]和A[i]
                exchange(A[j],A[i])
                i+=1
        #交换A[l-1]和A[i-1]
        exchange(A[l-1],A[i-1])
        '''
        快速排序
        quicksort(A,1,i-1)
        quicksort(A,i+1,r)
        '''
        return quicksort(A,1,i-1)+quicksort(A,i+1,r)+r-l        
print len(b)
print quicksort(b,1,10000)
'''
c=b[:20]
print c
quicksort(c,1,20)
print c
'''

    
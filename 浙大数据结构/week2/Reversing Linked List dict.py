# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 22:15:09 2018

@author: Administrator
"""
##读取数据
a=raw_input('')
a=a.split(' ')

b=()
for i in range(int(a[1])):
    temp=raw_input('')
    temp=temp.split(' ')
    b+=(temp,)

##按顺序重新排列
c=()
pos=a[0]
for i in range(int(a[1])):
    for j in b:
        if j[0]==pos:
            #c.append(i)
            c+=(j[:-1],)
            pos=j[2]
            break

##reverse数据
k=int(a[2])
m=len(c)
n=m/k

d=()
for i in range(n):
    for j in range(i*k,(i+1)*k):
        d+=(c[(i+1)*k-j-1],)
i=n*k
while i<m:
    d+=(c[i],)
    i+=1
print d
#输出结果
for i in range(m-1):
    print d[i][0]+' '+d[i][1]+' '+d[i+1][0]
print d[-1][0]+' '+d[-1][1]+' '+'-1'
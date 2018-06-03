# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 22:44:37 2018

@author: Administrator
"""

##读取数据
a=input('')
a=a.split(' ')

b=[]
for i in range(int(a[1])):
    temp=input('')
    temp=temp.split(' ')
    b.append(temp)

##按顺序重新排列
c=[]
pos=a[0]
for i in range(int(a[1])):
    for j in b:
        if j[0]==pos:
            #c.append(i)
            c.append(j[:-1])
            pos=j[2]
            break

##reverse数据
k=int(a[2])
m=len(c)
n=m//k

d=[]
for i in range(n):
    temp=c[i*k:(i+1)*k][:]
    temp.reverse()
    d+=temp
d+=c[n*k:]

#输出结果
for i in range(m-1):
    print (d[i][0]+' '+d[i][1]+' '+d[i+1][0])
print (d[-1][0]+' '+d[-1][1]+' '+'-1')
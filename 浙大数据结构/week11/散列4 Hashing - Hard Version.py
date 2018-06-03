# -*- coding: utf-8 -*-
"""
Created on Mon May 21 21:52:59 2018

@author: Administrator
"""

n=int(raw_input().strip())

m=map(int,raw_input().strip().split(" "))

#记录指向每个边的点
l={}
for i in m:
    if i>0:
        l[i]=[]

count=0
for i in range(n):
    x=m[i]
    if(x>0):
        count+=1
        r=x%n
        if(i>r):
            for j in range(r,i):
                if(m[j]>0):
                    l[x].append(m[j])
        elif(i<r):
            for j in range(i):
                if(m[j]>0):
                    l[x].append(m[j])
            for j in range(r,n):
                if(m[j]>0):
                    l[x].append(m[j])

#记录入度为0的点
s=set()

for i in l:
    if(len(l[i]))==0:
        s.add(i)

ans=""

for k in range(count):
    small=min(s)
    ans+=str(small)+" "
    s.remove(small)
    for i in l:
        if small in l[i]:
            l[i].remove(small)
            if len(l[i])==0:
                s.add(i)
                
print(ans.strip())
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:49:19 2018

@author: Administrator
"""
import math

m,n=map(int,raw_input().strip().split())

num=map(int,raw_input().strip().split())
Hash={}

#找大于等于m的最小素数
def isPrime(x):
    if x==1:
        return False
    elif x==2:
        return True
    elif x%2==0:
        return False
    else:
        for i in range(3,int(math.sqrt(x)),2):
            if x%i==0:
                return False
        return True
    
while(True):
    if isPrime(m):
        break
    else:
        m+=1

ans=""       
#构造Hash表
for i in num:
    key=i%m
    if key in Hash.values():
        j=1
        flag=1
        while(key in Hash.values()):
            key+=j*j
            j+=1
            if(key>=m):
                flag=0
                break
        if(flag):
            Hash[i]=key
        else:
            Hash[i]='-'
    else:
        Hash[i]=key
    ans+=str(Hash[i])+" "
  
print(ans.strip())
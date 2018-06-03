# -*- coding: utf-8 -*-
"""
Created on Mon May 21 21:17:48 2018

@author: Administrator
"""

dic={}

n=int(raw_input().strip())
s=[]

for i in range(n):
    x,y,z=raw_input().strip().split(" ")
    #y=int(y)
    if x=="L":
        if y in dic:
            if dic[y]==z:
                ans="Login: OK"
            else:
                ans="ERROR: Wrong PW"
        else:
            ans="ERROR: Not Exist"
        s.append(ans)
    else:
        if y in dic:
            ans="ERROR: Exist"
        else:
            ans="New: OK"
            dic[y]=z
        s.append(ans)
            
for i in s:
    print(i)
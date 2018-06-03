# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:01:38 2018

@author: Administrator
"""

n=int(raw_input())

dic={}
#读入数据
for i in range(n):
    a,b=map(int,raw_input().strip().split())
    if a in dic:
        dic[a]+=1
    else:
        dic[a]=1
    if b in dic:
        dic[b]+=1
    else:
        dic[b]=1
'''        
dic={13005711862L: 1,
 13088625832L: 1,
 13505711862L: 1,
 13588625832L: 3,
 15005713862L: 1,
 18087925832L: 1}
'''       
#找到打电话的最多次数
m=max(dic.values())
#记录最小的电话号码
phone=20000000000
num=0

#遍历字典，找到最小的电话号码
for i in dic.keys():
    if dic[i]==m:
        num+=1
        if i<phone:
            phone=i

#key=dic.keys()[dic.values().index(m)]
if num>1:
    print(str(phone)+" "+str(m)+" "+str(num))
else:
    print(str(phone)+" "+str(m))
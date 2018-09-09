# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 14:15:35 2018

@author: Administrator
"""
import math
import random
import time

start=time.time()

#定义处理函数
def f(x,dic):
    value=[]
    for i in x:
        if i<0:
            value.append(1-dic[-i])
        else:
            value.append(dic[i])
    if(sum(value)==0):
        return 0
    else:
        return 1


#with open(r'E:\CS161\stanford-algs-master\testCases\course4\assignment4TwoSat\input_beaunus_38_80000.txt') as file:
with open(r'E:\CS161\coursera\4npcomplete\week4\2sat6.txt') as file:
    n=int(file.readline().strip())
    #一开始全初始化为1
    data={}
    #记录每个点链接的点
    node={}
    for i in range(1,n+1):
        data[i]=1
        node[i]=set()
        node[-i]=set()
    #记录result
    result=1
    #记录错误的点
    wdic={}
    #记录所有的点
    adic={}

    
    for i in file.readlines():
        temp=tuple(map(int,i.strip().split()))
        #记录负数的个数,因为一开始全取1，所以只有两个都为负数才不满足
        key1=temp[0]
        key2=temp[1]
        if (key1<0 and key2<0):
            tempresult=0
            wdic[temp]=tempresult
        else:
            tempresult=1
        adic[temp]=tempresult
        node[key1].add(key2)
        node[key2].add(key1)

for k in range(100):
    #记录每个点出现的次数，删除那些同号的
    CNT={}
    for i in range(1,n+1):
        CNT[i]=0
        CNT[-i]=0
    
    for i in adic:
        #记录次数
        CNT[i[0]]+=1
        CNT[i[1]]+=1
    
    for i in range(1,n+1):
        if CNT[i]==0 and CNT[-i]>0:
            for j in node[-i]:
                if (-i,j) in adic:
                    del adic[(-i,j)]
                elif (j,-i) in adic:
                    del adic[(j,-i)]
                if (-i,j) in wdic:
                    del wdic[(-i,j)]
                elif (j,-i) in wdic:
                    del wdic[(j,-i)]
        if CNT[i]>0 and CNT[-i]==0:
            for j in node[i]:
                if (i,j) in adic:
                    del adic[(i,j)]
                elif (j,i) in adic:
                    del adic[(j,i)]
                if (i,j) in wdic:
                    del wdic[(i,j)]
                elif (j,i) in wdic:
                    del wdic[(j,i)]

#错误的点
wkey=set(wdic.keys())
length=len(wkey)
l=len(adic)
print(l)

#循环次数         
N=int(math.log(2,l))+1

#记录标志
flag=0
for i in range(N):
    if(flag==0):
        for j in range(2*l**2):
            #随机取一个错误的点
            temp=random.choice(list(wkey))
            key=random.choice(temp)
#            key=temp[0]
#            #这样更新保证把这个点修改正确
#            if key<0:
#                value=0
#            else:
#                value=1
            #更新
            rkey=abs(key)
            data[rkey]=1-data[rkey]
            
            #先考虑正的
            r1=rkey
            for k in node[r1]:
                if (k,r1) in adic:
                    l=(k,r1)
                else:
                    l=(r1,k)
                #计算现在的值
                t=f(l,data)
                #值不对且不在错误集合中
                if t==0 and l not in wdic:
                    wdic[l]=t
                    wkey.add(l)
                    length+=1
                elif t==1 and l in wdic:
                    wkey.remove(l)
                    del wdic[l]
                    length-=1
                    
            #再考虑负的
            r1=-rkey
            for k in node[r1]:
                if (k,r1) in adic:
                    l=(k,r1)
                else:
                    l=(r1,k)
                #计算现在的值
                t=f(l,data)
                #值不对且不在错误集合中
                if t==0 and l not in wdic:
                    wdic[l]=t
                    wkey.add(l)
                    length+=1
                elif t==1 and l in wdic:
                    wkey.remove(l)
                    del wdic[l]
                    length-=1
            if(length==0):
                flag=1
                break
    else:
        break

print(flag)
end=time.time()
print(end-start)
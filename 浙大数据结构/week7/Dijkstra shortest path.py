# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 16:03:20 2018

@author: Administrator
"""

##预处理，将数据存入字典，缺失的点补1000000
#a=open(r'E:\CS161\coursera\2algorithms-graphs-data-structures\week2\dijkstraData.txt')
#a=open(r'E:\CS161\coursera\2algorithms-graphs-data-structures\week2\test1.txt')
#a=open(r'E:\CS161\stanford-algs-master\testCases\course2\assignment2Dijkstra\input_random_1_4.txt')
a=open(r'E:\CS161\stanford-algs-master\testCases\course2\assignment2Dijkstra\input_random_20_64.txt')
b={}
c=1
d=200

for i in a.readlines():
    i=i.strip().replace('\t',',').split(',')[1:]
    i=map(int,i)
    length=len(i)
    temp={}
    num=()
    for k in range(0,length,2):
        temp[i[k]]=i[k+1]
        num+=(i[k],)
    
    '''for j in range(1,d+1):
        if j not in num:
            temp[j]=1000000'''
    b[c]=temp
    c+=1       
#print b
#print b[200][103]

#start为点和此处的长度,path为可以走的路线,ans为最佳结果结果,set1为V
def dijkstraData(start,path):
    #记录最小值,键，值
    a=1000000
    keym=0
    #找对应的路径
    if len(start)<d:
        for i in start:
            path1=path[i].copy()
            keys=path1.keys()
            for j in start.keys():
                if j in keys:
                    del path1[j]
            if len(path1)>0:
                #找最小键值对
                key=min(path1,key=path1.get)
                value=path1[key]
                temp=value+start[i]
                #print key,value,path1
                if temp<=a:
                    a=temp
                    keym=key
            else:
                continue
        if a<1000000:
            start[keym]=a
            #print start,ans,len(path)
            return dijkstraData(start,path)
        else:
            return start
    else:
        return start
    
m=dijkstraData({1:0},b)
print m[7],m[37],m[59],m[82],m[99],m[115],m[133],m[165],m[188],m[197]
#2599,2610,2947,2052,2367,2399,2029,2442,2505,3068
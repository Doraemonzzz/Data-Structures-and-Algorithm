# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 23:35:39 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 22:36:10 2018

@author: Administrator
"""

import time

start=time.time()
data=[]
X=[]
Y=[]
dic={}
with open('nn.txt') as file:
#with open(r'E:\CS161\stanford-algs-master\testCases\course4\assignment3TSPHeuristic\input_simple_56_4000.txt') as file:
    n=int(file.readline().strip())
    for i in file.readlines():
        temp=list(map(float,i.strip().split()))
        data.append(temp)
        dic[temp[0]]=temp[1:]
        #X.append(temp[1])
        #Y.append(temp[2])

i=data[0]
start1=data[0]
#按横标坐标排序
data.sort(key=lambda i:i[1])
index=data.index(i)

#给索引排序
sort1=[i[0] for i in data]
del sort1[index]

end=time.time()
print(end-start)


def dis(x,y):
    return ((x[1]-y[1])**2+(x[2]-y[2])**2)**0.5

#邻接表表示图
'''
distance={}
for i in range(1,n+1):
    distance[i]={}

for i in data:
    for j in data:
        if(i!=j):
            distance[i]=dis(data[i],data[j])
'''

vertex=set([1])
#剩余的点
#leave=set(range(2,n+1))
leave=list(range(2,n+1))
result=0
last=1

count=0
while(len(vertex)<n):
    #计算最小值
    mind=10000000000
    minid=[n]
    for k in range(len(sort1)):
        #if j[0] in leave:
        if j[1]-i[1]>mind:
            break
        else:
            temp=dis(i,j)
            if temp<mind:
                index=k
                mind=temp
                minid=j
            elif temp==mind and j[0]<minid[0]:
                index=k
                mind=temp
                minid=j
    #leave.remove(minid)
    #print(minid)
    del data[index]
    leave.remove(minid[0])
    i=minid
    result+=mind
    vertex.add(minid[0])
    count+=1
    if(count%1000==0):
        print(count)
        print(time.time()-start)

result+=dis(start1,i)
print(result)         


'''
import matplotlib.pyplot as plt
plt.scatter(X,Y)
'''

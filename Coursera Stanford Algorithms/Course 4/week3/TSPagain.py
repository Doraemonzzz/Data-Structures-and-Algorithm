 # -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 21:04:07 2018

@author: Administrator
"""

import time

start=time.time()
data={}
X=[]
Y=[]
with open('nn.txt') as file:
#with open(r'E:\CS161\stanford-algs-master\testCases\course4\assignment3TSPHeuristic\input_simple_55_4000.txt') as file:
    n=int(file.readline().strip())
    for i in file.readlines():
        temp=list(map(float,i.strip().split()))
        data[temp[0]]=temp[1:]
        #X.append(temp[1])
        #Y.append(temp[2])
        
def dis(x,y):
    return (x[0]-y[0])**2+(x[1]-y[1])**2

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
i=1
count=0

while(len(vertex)<n):
    #计算最小值
    mind=10000000000
    minid=n
    for j in leave:
        temp=dis(data[i],data[j])
        if temp<mind:
            mind=temp
            minid=j
        '''
        elif temp==mind and j<minid:
            mind=temp
            minid=j
        '''
    #leave.remove(minid)
    leave.remove(minid)
    i=minid
    result+=mind**0.5
    vertex.add(minid)
    last=minid
    count+=1
    if(count%100==0):
        print(time.time()-start)

result+=dis(data[1],data[last])**0.5
print(result)         
end=time.time()
print(end-start)

'''
import matplotlib.pyplot as plt
plt.scatter(X,Y)
'''
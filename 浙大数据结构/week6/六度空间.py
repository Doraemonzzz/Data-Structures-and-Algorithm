# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 23:37:28 2018

@author: Administrator
"""

n,m=map(int,raw_input().strip().split(' '))

x=[[] for i in range(n+1)]
y=[0 for i in range(n+1)]

for i in range(m):
    a,b=map(int,raw_input().strip().split(' '))
    x[a].append(b)
    x[b].append(a)
'''
n=10
m=9
x=[[], [2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9]]
y=[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''

#定义BFS
#m为图，x为开始节点,y为访问数组，记录是否访问过
def BFS(m,x,y):
    q=[]
	#记录层数
    count=1
    level=0
	#last记录这层的最后一个节点，如果queue中抛出的元素等于last，表示这层遍历完毕，此时层数加一,last=tail
    last=x
	#tail表示下一层的最后一个节点
    tail=0
    y[x]=1
    q.append(x)
    while(len(q)>0):
        v=q.pop(0)
        for i in m[v]:
            if y[i]==0:
                y[i]=1
                q.append(i)
                count+=1
                tail=i
        if v==last:
            level+=1
            last=tail
        if level==6:
            break
    return count

for i in range(1,n+1):
    y1=y[:]
    print '{}: {:2.2f}%'.format(i,BFS(x,i,y1)*100.0/n)
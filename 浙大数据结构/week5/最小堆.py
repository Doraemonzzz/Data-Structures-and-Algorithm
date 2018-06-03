# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 12:22:45 2018

@author: 715073608
"""

#定义堆
class Heap():
    def __init__(self,x,y):
        self.heap=y
        self.len=len(y)
        #type定义堆类型，x=1表示递增,x=0表示递减
        self.type=x
    
    def insert(self,x):
        self.heap.append(x)
        self.len+=1
        i=self.len
        if self.type==1:
            while (i>=2):
                #print self.heap
                #不满足递增堆的定义时交换父子
                if self.heap[i-1]<self.heap[i/2-1]:     
                    self.heap[i-1],self.heap[i/2-1]=self.heap[i/2-1],self.heap[i-1]
                    i/=2
                else:
                    break
            #print self.heap,'1'
        elif self.type==0:
            while (i>=2):
                #print self.heap
                #不满足递减堆的定义时交换父子
                if self.heap[i-1]>self.heap[i/2-1]:
                    self.heap[i-1],self.heap[i/2-1]=self.heap[i/2-1],self.heap[i-1]
                    i/=2
                else:
                    break

def heaprd(x,i):
    a=''
    a+=str(x.heap[i-1])
    i/=2
    while i>0:
        a+=' '+str(x.heap[i-1])
        i/=2
    return a

heap=Heap(1,[])
a=map(int,raw_input().strip().split(' '))
b=map(int,raw_input().strip().split(' '))
c=map(int,raw_input().strip().split(' '))
for i in b:
    heap.insert(i)
for i in c:
    print heaprd(heap,i)
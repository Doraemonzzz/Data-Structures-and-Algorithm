# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 21:04:04 2018

@author: Administrator
"""

class Heap(object):
    #初始化,a为哨兵
    def __init__(self,x,a,M):
        #哨兵填入首元素
        s=[a]
        s+=x
        self.data=s
        self.len=len(x)
        self.size=M
     
    #将以第self.data[p]为根的子堆调整为最小堆
    def PerDown(self,p):
        x=self.data[p]
        parent=p
        while(parent<=self.len/2):
            child=2*parent
            #将child指向子节点中较小的值
            if (child<self.len and (self.data[child]>self.data[child+1])):
                child+=1
            if(x<=self.data[child]):
                break
            else:
                self.data[parent]=self.data[child]
            parent=child
        self.data[parent]=x
        #print self.data[p:],2
        
    def BuildHeap(self):
        i=self.len
        while(i>0):
            #print self.data,i
            self.PerDown(i)
            #print self.data
            i-=1
    
    #插入元素          
    def insert(self,x):
        if self.len==self.size:
            print('已满')
            #return False
        else:
            self.data.append(x)
            self.len+=1
            i=self.len
            while(self.data[i/2]>x):
                self.data[i]=self.data[i/2]
                i/=2
            self.data[i]=x
            #return True
    
    #抛出最小元素
    def extract(self):
        if self.len==0:
            print("堆为空")
        else:
            start=self.data[1]
            #从最后一个元素开始，找到小于
            x=self.data[-1]
            self.len-=1
            parent=1
            while(parent*2<=self.len):
                child=2*parent
                #将child指向子节点中较小的值
                if (child<self.len and (self.data[child]>self.data[child+1])):
                    child+=1
                if(x<=self.data[child]):
                    break
                else:
                    self.data[parent]=self.data[child]
                parent=child
        self.data[parent]=x
        del self.data[-1]
        return start
    
a=range(30,1,-2)
heap=Heap(a,0,100)
heap.BuildHeap()
print heap.data
heap2=Heap([],10000,1000)
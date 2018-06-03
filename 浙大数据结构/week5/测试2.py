# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 21:52:23 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 23:07:14 2018

@author: Administrator
"""
#定义堆
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
        #print self.data[p:],1
        x=self.data[p]
        parent=p
        while(parent<=self.len/2):
            child=2*parent
            #print child,parent
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
            self.BuildHeap()
            #return True
    
    #抛出最小元素
    def extract(self):
        if self.len==0:
            print("堆为空")
        else:
            start=self.data[1]
            #从最后一个元素开始，找到小于
            self.data[1]=self.data[-1]
            self.len-=1
            del self.data[-1]
            self.BuildHeap()
        return start
    
    
class Heap1():
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
        #print self.data[p:],1
        #print p,self.data
        x=self.data[p]
        parent=p
        while(parent<=self.len/2):
            child=2*parent
            #print child,parent
            #将child指向子节点中较小的值
            if (child<self.len and (self.data[child]<self.data[child+1])):
                child+=1
            if(x>=self.data[child]):
                break
            else:
                self.data[parent]=self.data[child]
            parent=child
        self.data[parent]=x
        #print self.data[p:],2
        
    def BuildHeap(self):
        i=self.len
        #print i,'len'
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
            self.BuildHeap()
            #return True
    
    #抛出最小元素
    def extract(self):
        if self.len==0:
            print("堆为空")
        else:
            start=self.data[1]
            #从最后一个元素开始，找到小于
            self.data[1]=self.data[-1]
            self.len-=1
            del self.data[-1]
            self.BuildHeap()
        return start
    
'''
a=Heap(1)

a.insert(4)
a.insert(4)
a.insert(8)
a.insert(9)
a.insert(4)
a.insert(12)
a.insert(9)
a.insert(11)
a.insert(13)
print a.heap,a.len
b=a.extract()

print a.heap
'''

#a=open(r'E:\CS161\coursera\2algorithms-graphs-data-structures\week3\data.txt')
a=open(r'E:\CS161\stanford-algs-master\testCases\course2\assignment3Median\input_random_29_1280.txt')

#利用两个堆求最中位数的思路求解
#构造small堆，存储大x(1),x(2)...x(k)的元素,表头为small中最大值
small=Heap1([],10000,100000)
sb=0
#构造big列表，存储x(k+1),x(k+2)...x(2k),表头为big中最小值
big=Heap([],0,100000)
bs=0

#初始化
temp=[]
for i in a.readlines()[:2]:
    i=int(i.strip('\t'))
    temp.append(i)
sum1=temp[0]
temp.sort()

small.insert(temp[0])
sb=temp[0]

big.insert(temp[-1])
bs=temp[-1]

#对前两个输入的中位数求和
sum1+=small.data[1]

a=open(r'E:\CS161\stanford-algs-master\testCases\course2\assignment3Median\input_random_29_1280.txt')
#a=open(r'E:\CS161\coursera\2algorithms-graphs-data-structures\week3\data.txt')


#批量处理数据
j=1

for i in a.readlines()[2:]:
    i=int(i.strip('\t'))
    #print big.data,small.data,i,'f'
    #print big.len,small.len
    if j%2==1:
        if i>big.data[1]:
            #print big.heap
            x=big.extract()
            #print x
            big.insert(i)
            small.insert(x)
        else:
            small.insert(i)
        j+=1
    else:
        if i<small.data[1]:
            x=small.extract()
            #print small.heap
            small.insert(i)
            big.insert(x)
        else:
            big.insert(i)
        j+=1
    #print big.heap,small.heap,i,'l'
    #print small.heap[0]
    sum1+=small.data[1]
    #print sum1

print sum1%10000
 
'''
a=[23, 22, 19, 15, 21, 14, 17, 2, 5, 9, 20]
#a=Heap(0,[23, 20, 22, 15, 21, 19, 17, 2, 5, 9, 13, 14, 8, 12])
#a=Heap(0,[22, 20, 19, 15, 21, 14, 17, 2, 5, 9, 13, 12, 8, 16, 7])
#a=Heap(0,[23, 20, 22, 15, 21, 19, 17, 2, 5, 9, 13, 14, 8, 12])
#a=Heap(0,[22, 20, 19, 15, 21, 14, 17, 2, 5, 9, 13, 12, 8, 16, 7])
print a.heap
a.extract()
a.insert(11)
print a.heap
'''
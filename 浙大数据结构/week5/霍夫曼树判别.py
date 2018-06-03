# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 21:41:46 2018

@author: Administrator
"""

'''首先构造哈夫曼树，计算WPL,如果输入的WPL不等于哈夫曼树的WPL，则输出no，否则，判断是否为前缀码
如果不是前缀码，则输出YES
'''


n=int(raw_input())
a=raw_input().strip().split(' ')
b={}
c=[]
for i in range(n):
    b[a[2*i]]=int(a[2*i+1])
    c.append(int(a[2*i+1]))

num=int(raw_input())

ans={}
#读入
for i in range(num):
    temp={}
    for j in range(n):
        s=raw_input().strip().split(' ')
        temp[s[0]]=s[-1]
    ans[i]=temp


'''
n=7
b={'A': 1, 'B': 1, 'C': 1, 'D': 3, 'E': 3, 'F': 6, 'G': 6}
c=[1,1,1,3,3,6,6]
d={'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}
num=4
ans={0: {'A': '00000', 'B': '00001', 'C': '0001', 'D': '001', 'E': '01', 'F': '10', 'G': '11'},
 1: {'A': '01010', 'B': '01011', 'C': '0100', 'D': '011', 'E': '10', 'F': '11', 'G': '00'},
 2: {'A': '000', 'B': '001', 'C': '010', 'D': '011', 'E': '100', 'F': '101', 'G': '110'},
 3: {'A': '00000', 'B': '00001', 'C': '0001', 'D': '001', 'E': '00', 'F': '10', 'G': '11'}}
'''
def isqz(x,y):
    if x==y:
        return 1
    elif len(x)<len(y):
        l1=len(x)
        if x==y[:l1]:
            return 0
        else:
            return 1
    else:
        l1=len(y)
        if y==x[:l1]:
            return 0
        else:
            return 1

#定义最小堆
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
            
#Node
class Node(object):
    def __init__(self):
        self.weight=0
        self.left=''
        self.right=''

def findkey(x,y):
    for i in x:
        if x[i]==y:
            return i

#x为heap,y为对应的权重
def Huffman(x,y):
    dic={}
    y1=y.copy()
    for i in y:
        dic[i]=0
    temp=x.len
    for i in range(1,temp):
        l=x.extract()
        r=x.extract()
        lk=findkey(y,l)
        del y[lk]
        rk=findkey(y,r)
        del y[rk]
        w=l+r
        for j in dic:
            if j in lk:
                dic[j]+=1
            if j in rk:
                dic[j]+=1
        x.insert(w)
        y[lk+rk]=w
    s=0
    for i in y1:
        s+=dic[i]*y1[i]
    return s
heap=Heap(c,0,100)
#print heap.data
score=Huffman(heap,b.copy())

def huffsum(x,y):
    s=0
    for i in x:
        s+=len(x[i])*y[i]
    return s

for i in range(num):
    if huffsum(ans[i],b)!=score:
        print 'NO'
    else:
        #print i
        flag=1
        for p in ans[i]:
            if flag==1:
                for q in ans[i]:
                    if isqz(ans[i][p],ans[i][q])==1:
                        flag*=1
                    else:
                        flag=0
                        break
            else:
                break
        if flag==1:
            print'YES'
        else:
            print 'NO'
            



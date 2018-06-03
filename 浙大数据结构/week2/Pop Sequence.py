# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 11:23:23 2018

@author: Administrator
"""

#定义栈
class Stack():
    def __init__(self,size):
        self.size=size
        self.stack=[]
        self.top=-1
        
    def isfull(self):
        return self.size==(self.top+1)
    
    def push(self,x):
        if self.isfull():
            return 'stack is full'
        else:
            self.stack.append(x)
            self.top+=1
    
    def isempty(self):
        return self.top==(-1)
    
    def pop(self):
        if self.isempty():
            return 'stack is empty'
        else:
            self.top-=1
            self.stack.pop()
            #return b
            
    def show(self):
        return self.stack
    
#读取数据 
a=raw_input()
b=map(int,a.split(' '))
c=[]

for i in range(b[2]):
    temp=raw_input()
    c.append(map(int,temp.split(' ')))


#思路是按照1到n输入，如果碰到栈尾的元素和给出的序列相同，则抛出这个元素，序列删除这个元素，以此循环

def isstack(x,size,num):
    b=[]
    a=Stack(size)
    for i in range(1,num+1):
        if not a.isfull():
            a.push(i)
        while not a.isempty() and a.show()[-1]==x[0]:
            del x[0]
            a.pop()
    if len(a.show())==0:
        print 'YES'
    else:
        print 'NO'

for i in c:
    isstack(i,b[0],b[1])    
'''
[1,2,3,4,5,6,7]
[3,2,1,7,5,6,4]
[7,6,5,4,3,2,1]
[5,6,4,3,7,2,1]
[1,7,6,5,4,3,2]
'''
'''
isstack([1,2,3,4,5,6,7],5,7)
isstack([3,2,1,7,5,6,4],5,7)
isstack([7,6,5,4,3,2,1],5,7)
isstack([5,6,4,3,7,2,1],5,7)
isstack([1,7,6,5,4,3,2],5,7)
'''




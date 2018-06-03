# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 11:11:38 2018

@author: Administrator
"""

#实现栈
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
            b=self.stack.pop()
            return b
            
    def show(self):
        return self.stack
    
a=Stack(5)
print a.isfull()
print a.isempty()

a.push(4)
print a.show()

b=a.pop()
print a.show(),b
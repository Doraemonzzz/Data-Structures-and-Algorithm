# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 12:15:02 2018

@author: Administrator
"""

class Queue():
    def __init__(self,size):
        self.size=size
        self.queue=[]
        self.front=0
        self.rear=0
        
    def isfull(self):
        return self.size==(self.rear-self.front+1)
    
    def addq(self,x):
        if self.isfull():
            return 'queue is full'
        else:
            self.queue.append(x)
            self.rear+=1
    
    def isempty(self):
        return self.front==self.rear
    
    def deleteq(self):
        if self.isempty():
            return 'queue is empty'
        else:
            self.front+=1
            b=self.queue.pop(0)
            return b
            
    def show(self):
        return self.queue
    
q=Queue(10)
for i in range(5):
    q.addq(i)
    print q.show(),q.front,q.rear
for i in range(5):
    print q.deleteq()
    print q.show(),q.front,q.rear
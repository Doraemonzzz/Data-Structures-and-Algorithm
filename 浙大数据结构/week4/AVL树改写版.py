# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 23:26:09 2018

@author: Administrator
"""
class Node(object):
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.height=0

class AVL(object):
    def __init__(self):
        self.root=None
        
    def height(self,node):
        if node is None:
            return -1
        else:
            return node.height
    
    #LL
    def SingleLeftRotation(self,node):
        B=node.left
        node.left=B.right
        B.right=node
        node.height=max(self.height(node.left),self.height(node.right))+1
        B.height=max(self.height(B.left),node.height)+1
        return B
        
    #RR
    def SingleRightRotation(self,node):
        B=node.right
        node.right=B.left
        B.left=node
        node.height=max(self.height(node.left),self.height(node.right))+1
        B.height=max(self.height(B.right),node.height)+1        
        return B
    
    #LR
    def DoubleLeftRightRotation(self,node):
        node.left=self.SingleRightRotation(node.left)
        return self.SingleLeftRotation(node)
    
    #RL
    def DoubleRightLeftRotation(self,node):
        node.right=self.SingleLeftRotation(node.right)
        return self.SingleRightRotation(node)
     
    def Insert(self,key,node):
        if node==None:
            node=Node(key)
        elif key<node.key:
            node.left=self.Insert(key,node.left)
            if (self.height(node.left)-self.height(node.right))==2:
                #LL
                if key<node.left.key:
                    node=self.SingleLeftRotation(node)
                #LR
                else:
                    node=self.DoubleLeftRightRotation(node)
        elif key>node.key:
            node.right=self.Insert(key,node.right)
            if (self.height(node.right)-self.height(node.left))==2:
                #RR
                if key>node.right.key:
                    node=self.SingleRightRotation(node)
                #Rl
                else:
                    node=self.DoubleRightLeftRotation(node)
        node.height=max(self.height(node.right),self.height(node.left))+1
        return node

a=int(raw_input())
b=map(int,raw_input().strip().split(' '))
node=Node(b[0])
tree=AVL()
for i in range(1,a):
    node=tree.Insert(b[i],node)
print node.key
        
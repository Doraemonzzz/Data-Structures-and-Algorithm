# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 15:09:14 2019

@author: qinzhen
"""

import numpy as np

class BST():
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
    
    def search(self, data):
        if (self.data == data):
            return data
        elif (data < self.data):
            if (self.lchild != None):
                return self.lchild.search(data)
            else:
                return None
        else:
            if (self.rchild != None):
                return self.rchild.search(data)
            else:
                return None
        
    def insert(self, data):
        if (data < self.data):
            if (self.lchild != None):
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if (self.rchild != None):
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
                
    def in_order(self):
        if (self.lchild != None):
            self.lchild.in_order()
        print(self.data)
        if (self.rchild != None):
            self.rchild.in_order()

####测试
lst = np.random.randint(0, 100, 30)
Bst = BST(0)
for i in lst:
    Bst.insert(i)
Bst.in_order()

lst = np.random.randint(0, 100, 5)
for i in lst:
    print(i, Bst.search(i))


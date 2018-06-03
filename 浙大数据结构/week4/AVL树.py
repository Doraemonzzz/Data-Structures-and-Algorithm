# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 21:18:06 2018

@author: Administrator
"""
'''
class AVL():
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=0
    
    def insert(self,x):
        if self.height==0:
            self.
            
    def findmax(self):
        if x.right==None:
            return x.data
        else:
            return x.right.findmax()
            
a=int(raw_input())
b=map(int,raw_input().strip().split(' '))
c={}
'''
c={}
#b=[88, 70, 61, 96, 120]
b=[88,70,61,96,120,90,65]

def insert(dic,start,x):
    if len(dic)==0:
        dic[x]=[None,None,None,0]
        dic['root']=x
        return dic
    else:
        if x>start:
            if dic[start][1]==None:
                dic[start][1]=x
                height=dic[start][-1]+1
                dic[x]=[None,None,start,height]
                return dic
            else:
                return insert(dic,dic[start][1],x)
        else:
            if dic[start][0]==None:
                dic[start][0]=x
                height=dic[start][-1]+1
                dic[x]=[None,None,start,height]
                return dic
            else:
                return insert(dic,dic[start][0],x)
c=insert(c,None,b[0])
#print c
c=insert(c,b[0],b[1])
#print c
c=insert(c,b[0],b[2])
#print c
c=insert(c,b[0],b[3])
#print c
c=insert(c,b[0],b[4])
#print c
c=insert(c,b[0],b[5])
#print c
c=insert(c,b[0],b[6])
print c






        

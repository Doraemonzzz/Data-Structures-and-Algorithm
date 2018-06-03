# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 12:28:35 2018

@author: 715073608
"""


def f(x,y):
    if len(x)!=len(y):
        return False
    else:
        if len(x)==0:
            return True
        else:
            if x[0]!=y[0]:
                return False
            else:
                a=x[0]
                x1=[]
                y1=[]
                x2=[]
                y2=[]
                for i in range(1,len(x)):
                    if x[i]<a:
                        x1.append(x[i])
                    elif x[i]>a:
                        x2.append(x[i])
                for i in range(1,len(y)):
                    if y[i]<a:
                        y1.append(y[i])
                    elif y[i]>a:
                        y2.append(y[i])
                return f(x1,y1) and f(x2,y2)
            
ans=[]
while (True):
    a=map(int,raw_input().split(' '))
    if a[0]==0:
        break
    else:
        b=[]
        tree=map(int,raw_input().split(' '))
        for i in range(a[1]):
            temp=map(int,raw_input().split(' '))
            b.append(f(tree,temp))
        ans.append(b)

for i in ans:
    for j in i:
        if j:
            print 'Yes'
        else:
            print 'No'

                
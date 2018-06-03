# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 21:43:05 2018

@author: Administrator
"""
#读取数据
a=int(raw_input(''))
b=[]
c=[]
stack=[]

for i in range(2*a):
    temp=raw_input('').split(' ')
    if temp[0]=='Push':
        b.append(temp[1])
        stack.append(temp[1])
    else:
        t=stack.pop()
        c.append(t)

#恢复二叉树
def f(b,c,dic,n):
    if len(dic)<n and len(b)>0 and len(c)>0:
        #print b,c
        temp=b[0]
        tempindex=c.index(temp)
        B=len(b)
        #print b,c
        #print B,dic,tempindex
        #print temp,tempindex,dic
        if B>=2 and B>=tempindex+2:
            if tempindex>0 and tempindex<B-1:
                dic[temp]={'l':b[1],'r':b[tempindex+1]}
            elif tempindex>0:
                dic[temp]={'l':b[1],'r':'-'}
            else:
                dic[temp]={'l':'-','r':b[tempindex+1]}
        elif B>=2:
            dic[temp]={'l':b[1],'r':'-'}
        elif B>=tempindex+2:
            dic[temp]={'l':'-','r':b[tempindex+1]}
        else:
            dic[temp]={'l':'-','r':'-'}
        f(b[1:tempindex+1],c[:tempindex],dic,n)
        f(b[tempindex+1:],c[tempindex+1:],dic,n)
    return dic

#测试数据
'''
def f(b,c,dic,n):
    if len(b)>0:
        temp=b[0]
        tempindex=c.index(temp)
        if len(B)>3:
            dic[temp]={'l':b[1],'r':b[tempindex+1]}
        elif len(B)==3:
'''         
'''
s=[['Push', '1'],
 ['Push', '2'],
 ['Push', '3'],
 ['Pop'],
 ['Pop'],
 ['Push', '4'],
 ['Pop'],
 ['Pop'],
 ['Push', '5'],
 ['Push', '6'],
 ['Pop'],
 ['Pop']]
'''
'''
s=[['Push','1'],
   ['Push','2'],
   ['Pop'],
   ['Pop'],
   ['Push','3'],
   ['Push','4'],
   ['Pop'],
   ['Pop'],
   ['Push','5'],
   ['Pop']]
'''
'''
a=6

for i in range(2*a):
    temp=s[i]
    if temp[0]=='Push':
        b.append(temp[1])
        stack.push(temp[1])
    else:
        t=stack.pop()
        c.append(t)
'''
'''
b=['D','B','A','C','E','G','F']
c=['A','B','C','D','E','F','G']
a=7
#ACBFGED
'''

'''
b=['B','C','A','D']
c=['C','B','A','D']
a=4
#CDAB
'''
'''
b=['a','b','d','c','e']
c=['d','b','a','c','e']
a=5
'''
'''
b=['A','B','D','F','E','C','G']
c=['F','D','B','E','A','C','G']
a=7
'''
ans=f(b,c,{},a)

#判断树是否为空
def flag(tree,start):
    if start=='-':
        return 0
    else:
        return 1

def show(tree,start):
    if flag(tree,start):
        show(tree,tree[start]['l'])
        show(tree,tree[start]['r'])
        print start,

show(ans,b[0])
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 20:33:45 2018

@author: Administrator
"""

#定义读取函数
def read():
    #记录输入的个数
    num=int(raw_input())
    #非空树
    if num>0:
    #利用字典存储二叉树
        tree={}
        #此数字用来做标记，用来找出根节点
        check=[0]*num
        for i in range(num):
            temp1=raw_input().split(' ')
            temp2={}
            temp2['l']=temp1[0]
            temp2['r']=temp1[1]
            tree[str(i)]=temp2
            if temp1[0]!='-':
                check[int(temp1[0])]=1
                if temp1[1]!='-':
                    check[int(temp1[1])]=1
        #找到根节点
        num=check.index(0)
        return tree,str(num)
    #空树
    else:
        return {'0': {'l': '-', 'r': '-', 'v': 'A'}},'0'

#判断树是否为空
def flag(tree,start):
    if start=='-':
        return 0
    else:
        return 1
    
#判断是否为叶节点
def isleaf(x):
    if x['l']=='-' and x['r']=='-':
        return 1
    else:
        return 0
    
#n记录层数,m记录叶节点及其层数
def show(tree,start,n,m):
    if flag(tree,start):
        n+=1
        if isleaf(tree[start]):
            m.append([start,n])
        else:
            show(tree,tree[start]['l'],n,m)
            show(tree,tree[start]['r'],n,m)
    return m

#读入数据
#tree1,num1=read()

#测试数据
'''
tree1={'0': {'l': '1', 'r': '-'},
 '1': {'l': '-', 'r': '-'},
 '2': {'l': '0', 'r': '-'},
 '3': {'l': '2', 'r': '7'},
 '4': {'l': '-', 'r': '-'},
 '5': {'l': '-', 'r': '-'},
 '6': {'l': '5', 'r': '-'},
 '7': {'l': '4', 'r': '6'}}
num1='3'
'''

b=show(tree1,num1,0,[])
c=set()
d=[]

#找出不同的层数
for i in b:
    c.add(i[-1])
    
#按照层数排序
for j in c:
    d.append(j)
d.sort()

#按照层数递增的顺序输出
ans=''
for i in d:
    for j in b:
        if j[-1]==i:
            ans+=(j[0]+' ')
print ans.strip(' ')

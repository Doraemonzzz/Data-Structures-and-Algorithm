# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 12:05:53 2018

@author: 715073608
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
            temp2['v']=temp1[0]
            temp2['l']=temp1[1]
            temp2['r']=temp1[2]
            tree[str(i)]=temp2
            if temp1[1]!='-':
                check[int(temp1[1])]=1
                if temp1[2]!='-':
                    check[int(temp1[2])]=1
        #找到根节点
        num=check.index(0)
        return tree,str(num)
    #空树
    else:
        return {'0': {'l': '-', 'r': '-', 'v': 'A'}},'0'

#读入数据
tree1,num1=read()
tree2,num2=read()

#测试数据
'''
tree1={'0': {'l': '1', 'r': '2', 'v': 'A'},
 '1': {'l': '3', 'r': '4', 'v': 'B'},
 '2': {'l': '5', 'r': '-', 'v': 'C'},
 '3': {'l': '-', 'r': '-', 'v': 'D'},
 '4': {'l': '6', 'r': '-', 'v': 'E'},
 '5': {'l': '7', 'r': '-', 'v': 'G'},
 '6': {'l': '-', 'r': '-', 'v': 'F'},
 '7': {'l': '-', 'r': '-', 'v': 'H'}}
num1='0'

tree2={'0': {'l': '-', 'r': '4', 'v': 'G'},
 '1': {'l': '7', 'r': '6', 'v': 'B'},
 '2': {'l': '-', 'r': '-', 'v': 'F'},
 '3': {'l': '5', 'r': '1', 'v': 'A'},
 '4': {'l': '-', 'r': '-', 'v': 'H'},
 '5': {'l': '0', 'r': '-', 'v': 'C'},
 '6': {'l': '-', 'r': '-', 'v': 'D'},
 '7': {'l': '2', 'r': '-', 'v': 'E'}}
num2='3'
'''
'''
tree1={'0': {'l': '5', 'r': '7', 'v': 'B'},
 '1': {'l': '-', 'r': '-', 'v': 'F'},
 '2': {'l': '0', 'r': '3', 'v': 'A'},
 '3': {'l': '6', 'r': '-', 'v': 'C'},
 '4': {'l': '-', 'r': '-', 'v': 'H'},
 '5': {'l': '-', 'r': '-', 'v': 'D'},
 '6': {'l': '4', 'r': '-', 'v': 'G'},
 '7': {'l': '1', 'r': '-', 'v': 'E'}}
num1='2'
tree2={'0': {'l': '6', 'r': '-', 'v': 'D'},
 '1': {'l': '5', 'r': '-', 'v': 'B'},
 '2': {'l': '-', 'r': '-', 'v': 'E'},
 '3': {'l': '-', 'r': '-', 'v': 'H'},
 '4': {'l': '0', 'r': '2', 'v': 'C'},
 '5': {'l': '-', 'r': '3', 'v': 'G'},
 '6': {'l': '-', 'r': '-', 'v': 'F'},
 '7': {'l': '1', 'r': '4', 'v': 'A'}}
num2='3'
'''
'''
tree1={'0':{'l': '-', 'r': '-', 'v': 'D'}}
num1='0'
tree2={'0':{'l': '-', 'r': '-', 'v': 'E'}}
num2='0'
'''

#判别函数
def f(treea,starta,treeb,startb):
    #两个都为空
    if (flag(treea,starta)==0 and flag(treeb,startb)==0):
        return 1
    #一个为空
    elif ((flag(treea,starta)==0 and flag(treeb,startb)>0) or (flag(treeb,startb)==0 and flag(treea,starta)>0)):
        return 0
    #对应值不相同
    elif treea[starta]['v']!=treeb[startb]['v']:
        return 0
    #无左子节点
    elif treea[starta]['l']=='-'and treeb[startb]['l']=='-':
        return f(treea,treea[starta]['r'],treeb,treeb[startb]['r'])
    #左子节点为相同
    elif treea[starta]['l']!='-'and treeb[startb]['l']!='-' and treea[treea[starta]['l']]['v']==treeb[treeb[startb]['l']]['v']:      
        return f(treea,treea[starta]['l'],treeb,treeb[startb]['l'])*f(treea,treea[starta]['r'],treeb,treeb[startb]['r'])
    #交换左右节点
    else:      
        return f(treea,treea[starta]['l'],treeb,treeb[startb]['r'])*f(treea,treea[starta]['r'],treeb,treeb[startb]['l'])

def flag(tree,start):
    if start=='-':
        return 0
    else:
        return 1
if f(tree1,num1,tree2,num2):
    print 'Yes'
else:
    print 'No'
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:15:32 2019

@author: qinzhen
"""

import numpy as np
import copy

V = {}
with open("kargerMinCut.txt") as f:
    for i in f.readlines():
        data = list(map(int, i.strip().split('\t')))
        #邻接表
        V[data[0]] = np.array(data[1:])

def Contraction(Vertex):
    while len(Vertex) > 2:
        #选择节点
        u = np.random.choice(list(Vertex.keys()))
        v = np.random.choice(Vertex[u])
        #更新u, v
        adj_v = Vertex[v]
        #合并相邻节点
        adj_u = np.append(Vertex[u], Vertex[v])
        adj_u = adj_u[(adj_u != v) & (adj_u != u)]
        Vertex[u] = adj_u
        #删除v
        Vertex.pop(v)
        #更新其余元素
        for i in adj_v:
            if i != u:
                #得到和i相邻的节点
                vec = Vertex[i]
                #将v替换为u
                vec[vec == v] = u
                Vertex[i] = vec
    
    n = []
    for i in Vertex:
        n.append(len(Vertex[i]))
    return np.min(n)

n = len(V)
N = int(n ** 2 * np.log(n))
N = 100
Res = []
for i in range(N):
    #深复制
    Vertex = copy.deepcopy(V)
    #计算结果
    num = Contraction(Vertex)
    Res.append(num)
    
print(np.min(Res))
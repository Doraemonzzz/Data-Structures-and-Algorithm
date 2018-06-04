# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 16:04:35 2018

@author: Administrator
"""

n=int(input())

post=list(map(int,input().strip().split()))

mid=list(map(int,input().strip().split()))
'''
n=7
post=[2, 3, 1, 5, 7, 6, 4]
mid=[1, 2, 3, 4, 5, 6, 7]
'''
def f(post,mid,l):
    #print(post,mid,l)
    if(len(post)<=1):
        return post
    elif (len(post)>=2):
        last=post[-1]
        #print(last)
        l.append(last)
        #找到索引
        index=mid.index(last)
        mid1=mid[:index]
        mid2=mid[index+1:]
        length=len(mid1)
        post1=post[:length]
        post2=post[length:-1]
        a=f(post1,mid1,[])
        b=f(post2,mid2,[])
        l=l+a+b
        return l

result=list(map(str,f(post,mid,[])))
print("Preorder: "+" ".join(result))
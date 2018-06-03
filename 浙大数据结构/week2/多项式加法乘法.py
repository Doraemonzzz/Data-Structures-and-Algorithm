# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 20:47:01 2018

@author: Administrator
"""

a=raw_input()
b=raw_input()

a=a.split(' ')
b=b.split(' ')


poly_1=[]
poly_2=[]

for i in a:
    if i!=' ' and i!='':
        poly_1.append(i)

for i in b:
    if i!=' ' and i!='':
        poly_2.append(i)

poly1=map(int,poly_1)
poly2=map(int,poly_2)

'''
poly1=[]
poly2=[]
'''
'''for i in poly_1:
    if i!=' ':
        poly1.append(i)

for i in poly_2:
    if i!=' ':
        poly2.append(i)'''

#读取每项对应的系数，要考虑常数项的情形
#a为次数，b为系数
if len(poly1)>1 and len(poly2)>1:
    poly1_a=poly1[1::2]
    poly1_b=poly1[2::2]    
    poly2_a=poly2[1::2]
    poly2_b=poly2[2::2]
elif len(poly1)==1 and len(poly2)>1:
    poly2_a=poly2[1::2]
    poly2_b=poly2[2::2]   
    poly1_a=[0]
    poly1_b=[0]
elif len(poly2)==1 and len(poly1)>1:
    poly1_a=poly1[1::2]
    poly1_b=poly1[2::2]
    poly2_a=[0]
    poly2_b=[0]        
else:
    poly2_a=[0] 
    poly2_b=[0]
    poly1_a=[0]    
    poly1_b=[0]
    
def polyplus(poly1a,poly1b,poly2a,poly2b):
    if poly1a[0]==0 and poly1b[0]==0:
        return poly2a,poly2b
    elif poly2a[0]==0 and poly2b[0]==0:
        return poly1a,poly1b
    else:
        l1=len(poly1a)
        l2=len(poly2a)
        
        #polya表示系数，polyb表示指数    
        poly3a=[]
        poly3b=[]
        
        i=0
        j=0
        while(i<l1 and j<l2):
            if poly1b[i]>poly2b[j]:
                poly3b.append(poly1b[i])
                poly3a.append(poly1a[i])
                i+=1
            elif poly1b[i]<poly2b[j]:
                poly3b.append(poly2b[j])
                poly3a.append(poly2a[j])
                j+=1
            else:
                temp=poly2a[j]+poly1a[i]
                if temp!=0:
                    poly3b.append(poly2b[j])
                    poly3a.append(temp)
                i+=1
                j+=1
        if i==l1:
            poly3b+=poly2b[j:]
            poly3a+=poly2a[j:]
        else:
            poly3b+=poly1b[i:]
            poly3a+=poly1a[i:]
        if poly3a!=[] and poly3b!=[]:
            return poly3a,poly3b
        else:
            return 0,0
        #print poly3a,poly3b

def polymultiply(poly1a,poly1b,poly2a,poly2b):
    if poly1a[0]==0 and poly1b[0]==0:
        return 0,0
    elif poly2a[0]==0 and poly2b[0]==0:
        return 0,0
    else:
        l1=len(poly1a)
        l2=len(poly2a)
        
        poly3_a=map(lambda x:x*poly1a[0],poly2a)
        poly3_b=map(lambda x:x+poly1b[0],poly2b)
        
        i=1
        while (i<l1):
            tempa=map(lambda x:x*poly1a[i],poly2a)
            tempb=map(lambda x:x+poly1b[i],poly2b)
            poly3_a,poly3_b=polyplus(poly3_a,poly3_b,tempa,tempb)
            i+=1
        return poly3_a,poly3_b

p1,p2=polyplus(poly1_a,poly1_b,poly2_a,poly2_b)
m1,m2=polymultiply(poly1_a,poly1_b,poly2_a,poly2_b)
if m1==0 and m2==0:
    print '0 0'
else:
    leng=len(m1)
    for i in range(leng):
        if i<leng-1:
            print m1[i],m2[i],
        else:
            print m1[i],m2[i]
if p1==0 and p2==0:
    print '0 0'
else:
    leng=len(p1)
    for i in range(leng):
        if i<leng-1:
            print p1[i],p2[i],
        else:
            print p1[i],p2[i]
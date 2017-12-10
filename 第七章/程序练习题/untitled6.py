# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 21:29:44 2017

@author: park
"""

import keyword
s=keyword.kwlist
#建立保留字列表  
n=input("输入一个文件名:")
f=open(n,"r")
f=f.readlines()
ls=[]
for line in f:
    line=line.split()
    line.append(line)
#建立一个以每行的所有单词为元素组成的一个列表组
fo=open(n,"w+")
for i in range(len(ls)):
    if f[i].isspace():
        fo.write(" "+"\n")
    for j in range(len(ls[i])):
        x=ls[i][j]
        if x not in s:
            x=x.upper()
        else:
            x=x.lower()
        if x==ls[i][len(ls[i])-1]:
            #判定是否遍历至每行的末尾
            fo.write(x+"\n")
        else:
            fo.write(x+" ")

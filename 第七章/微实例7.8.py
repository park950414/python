# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 19:03:43 2017

@author: park
"""

fo=open("price2016.csv","r")
ls=[]
for line in fo:
    line=line.replace("\n","")
    print(line)
    ls.append(line.split(","))
  
print(ls)
fo.close()
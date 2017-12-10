# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 19:18:23 2017

@author: park
"""

fo= open ("price2016.csv","r")
ls=[]
for line in fo:
    line=line.replace('\n','')
    ls=line.split(",")
    lns=""
    for s in ls:
        lns+="{}\t".format(s)
    print (lns)
fo.close()
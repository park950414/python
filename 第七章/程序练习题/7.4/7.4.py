# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 14:00:30 2017

@author: park
"""

import json
fr=open("price2016.csv",'r')
ls=[]
for line in fr:
    line=line.replace("\n","")
    ls.append(line.split(","))
fr.close()
print(ls)
fw=open("price2016.json","w")
for i in range(1,len(ls)):
    ls[i]=dict(zip(ls[0],ls[i]))
json.dump(ls[1:],fw,sort_keys=1,indent=4,ensure_ascii=0)
fw.close()
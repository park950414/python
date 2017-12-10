# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 19:39:27 2017

@author: park
"""

import json
fr=open("price2016.csv","r")
ls=[]
for line in fr:
    line=line.replace("\n","")
    ls.append(line.split(','))
fr.close()
fw=open("price2016.json","w")
for i in range(1,len(ls)):
    ls[i]=dict(zip(ls[0],ls[i]))
json.dump(ls[1:],fw,sort_keys=0,indent=4,ensure_ascii=False)
fw.close()
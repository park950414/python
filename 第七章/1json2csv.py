# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 19:50:51 2017

@author: park
"""

import json
fr=open("price2016.json","r")
ls=json.load(fr)
#print(ls)
data=[list(ls[0].keys())]
for item in ls:
    data.append(list(item.values()))
fr.close()
#print(data)
fw=open("price2016_from_json.csv","w")
for item in data:
    fw.write(",".join(item)+"\n")
    
fw.close()
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 19:32:37 2017

@author: park
"""
import json
dt={'b':2,'c':4,'a':6}
s1=json.dumps(dt)
s2=json.dumps(dt,sort_keys=True,indent=4)
print(s1,type(s1))
print(s2)
print(s1==s2)
dt2=json.loads(s2)
print(dt2,type(dt2))
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 20:11:14 2017

@author: park
"""

fo=open("price2016bj.csv","w")
ls=["北京","101.5","120.7","121.4"]
fo.write(",".join(ls)+"\n")
fo.close()
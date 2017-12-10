# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 19:57:04 2017

@author: park
"""
textFile=open("7.1.txt","rt")
print(textFile.readline())
textFile.close()
binFile=open("7.1.txt","rb")
print(binFile.readline())
binFile.close()
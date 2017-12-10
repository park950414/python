# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:17:05 2017

@author: park
"""
import keyword

fr= open ("123.py","r")
fw= open ("DAXIE7.9.py","w")
ls=[]
key=keyword.kwlist
key.append("print")
for line in fr:
    #line=line.replace("\n","")
    ls.append(line.split())
splits=str(ls).split("+") 
for i in range(len(ls)):
    for j in range(len(ls[i])):
        if  ls[i][j] in key:
            a =str(ls[i][j])
            fw.write(a+" ")
        else:
            LS=str(ls[i][j])
            LS=LS.upper()
            fw.write(LS+" ")
            
    fw.write("\n")
fr.close()
fw.close()
fs=open("DAXIE7.9.py","r")
fss=fs.read()
print(fss)
fs.close()
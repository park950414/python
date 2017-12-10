# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 20:03:13 2017

@author: park
"""

fr=open("price2016.csv","r")
fw=open("price2016out.csv","w")
ls=[]
for line in fr:
    line=line.replace("\n","")
    ls.append(line.split(","))

for i in range(len(ls)):
    for j in range(len(ls[i])):
        
        if (ls[i][j].replace(".","").isnumeric()):
                ls[i][j]="{:.2}%".format(float(eval(ls[i][j])/100))
                print(ls[i][j])
for row in ls:
    print(row)
    fw.write(",".join(row)+"\n")

       

fr.close()
fw.close()
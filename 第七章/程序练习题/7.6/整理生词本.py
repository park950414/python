# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 21:27:24 2017

@author: park
"""

im=open("我的生词本.txt","rt",encoding="utf-8_sig")
om=open("我的生词本(1).txt","w")
ls=im.readlines()
print(type(ls))
for i in range (len(ls)):
    if (ls[i][0]=="#"or ls[i][0]=="+"):
        om.write(ls[i][1:-1]+"\n")
im.close()
om.close()
        
   
        
    


    
    
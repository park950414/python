# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 15:09:04 2017

@author: park
"""

fr=open("ciku.txt","rt",encoding='utf_8_sig')    
ls=fr.readlines()
for line in ls:
    a=line.split()
    wordlist[a[0]]=a[1]
print(wordlist.items())

fr.close()
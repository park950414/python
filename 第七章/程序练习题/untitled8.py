# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 16:14:39 2017

@author: park
"""
wordlist={}
fr=open("ciku.txt","rt",encoding='utf-8_sig')    
ls=fr.readlines()
for line in ls:
    a=line.split(",")
    if a[-1][-1]=='\n':
        a[-1]=a[-1][:-1]#删去\n
    meanings=[]
    for i in range(1,len(a)):
        meanings.append(a[i])
    wordlist[a[0]]=meanings
    ln=str(wordlist.get(a[0])).strip("[]'")
    print(ln)
fr.close()
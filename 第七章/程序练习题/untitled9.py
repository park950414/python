# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 20:21:22 2017

@author: park
"""

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
word=input("请输入要查询的英文单词:")
if word in wordlist.keys():
    print("{}的含义为:{}".format(word,\
          wordlist.get(word)))
else:
    print("字典库中未找到这个单词")
fr.close()
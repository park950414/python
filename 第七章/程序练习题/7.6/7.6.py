# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 15:48:49 2017

@author: park
"""

import sys
global wordlist

def search():
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
        print("{}的含义为:{}".format(word,wordlist.get(word)))
    else:
        print("字典库中未找到这个单词")
        answer=input("你想要自行添加到词库吗？")
        if answer=="是":
            meaning=input("请输入单词的中文含义：")
            string="\n"+word+","+meaning
            fw=open("ciku.txt","a+",encoding='utf-8')  
            fw.write(string)
            print("恭喜您,添加成功!")
            fw.close()
    fr.close()
    choosefunction()
        
def add():
    word=input("请输入要添加的英文单词:")
    if word not in wordlist :
        meaning=input("请输入单词的中文含义：")
        string="\n"+word+","+meaning
        fw=open("ciku.txt","a+",encoding='utf-8')  
        fw.write(string)
        print("恭喜您,添加成功!")
    else:
        answer=input("该单词已存在!要添加多重释义吗?")
        if answer=="是":
            fr=open("ciku.txt","rt",encoding='utf-8_sig')    
            ls=fr.readlines()
            for line in ls:
                a=line.split(",")
                meanings=[]
                for i in range(1,len(a)):
                    meanings.append(a[i])
                wordlist[a[0]]=meanings
            fr.close()
            meaning=input("请输入要添加的中文含义：")
            strs=','.join(wordlist.get(word))
            if strs[-1]=='\n':
                strs=strs[:-1]#删去\n
            string="\n"+word+","+strs+","+meaning
            fw=open("ciku.txt","a+",encoding='utf-8')  
            fw.write(string)
            print("恭喜您，添加成功!")
        else:
            print("返回功能列表")
    fw.close()
    choosefunction()

def tuichu():
    sys.exit()
    
def choosefunction():
    func=input("请选择功能(添加,查询,退出):")
    if func=="添加":
        add()
    elif func=="查询":
        search()
    elif func=="退出":
        tuichu()
    else:
        print("输入有误")
        choosefunction()
    
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
fr.close()
choosefunction()

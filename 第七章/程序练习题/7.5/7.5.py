# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 14:15:24 2017

@author: park
"""
#dictionary
import sys
global wordlist

def search():
    fr=open("ciku.txt","rt",encoding='utf-8_sig')    
    ls=fr.readlines()
    for line in ls:
        a=line.split()
        wordlist[a[0]]=a[1]
    word=input("请输入要查询的英文单词:")
    if word in wordlist.keys():
        print("{}的含义为:{}".format(word,wordlist.get(word)))
    else:
        print("字典库中未找到这个单词")
    fr.close()
    choosefunction()
        
def add():
    fw=open("ciku.txt","a+",encoding='utf-8')    
    word=input("请输入要添加的英文单词:")
    if word not in wordlist :
        meaning=input("请输入单词的中文含义：")
        string="\n"+word+" "+meaning
        fw.write(string)
        print("添加成功!")
    else:
        print("该单词已存在于字典库")
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

choosefunction()

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 21:53:09 2017

@author: park
"""

f1 = open("TeleAddressBook.txt","rb")
f2 = open("EmailAddressBook.txt","rb")
f1.readline()
f2.readline()
lines1 = f1.readlines()
lines2 = f2.readlines()
dic1 = {}
dic2 = {}
for line in lines1:
    elements = line.split()
    dic1[elements[0]] = str(elements[1].decode("gbk"))
for line in lines2:
    elements = line.split()
    dic2[elements[0]] = str (elements[1].decode("gbk"))
lines = []
lines.append("姓名\t    电话   \t   邮箱\n")
for key in dic1:
    s=''
    if key in dic2.keys():
        s ='\t'.join([str(key.decode('gbk')),dic1[key],dic2[key]])
        s +='\n'
    else:
        s = '\t'.join([str(key.decode('gbk')),dic1[key],str('   -----   ')])
        s +='\n'
    lines.append(s)
for key in dic2:
    s =''
    if key not in dic1.keys():
        s = '\t'.join([str(key.decode('gbk')),str('   -----   '),dic2[key]])
        s +='\n'
    lines.append(s)
f3=open("AddressBook.txt","w")
f3.writelines(lines)
f1.close()
f2.close()
f3.close()
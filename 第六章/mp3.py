# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:27:36 2017

@author: park
"""

f=open('C:\Users\park\Desktop\Stay With Me.mp3','rb').read()
for each_line in f:
    print (each_line)
f.close()
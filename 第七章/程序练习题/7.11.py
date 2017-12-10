# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:53:36 2017

@author: park
"""

fr= open ("微实例7.9.py","r")
fw= open ("DAXIE7.9.py","w")
string=fr.read()
string=string.upper()
fw.write(string)
fr.close()
fw.close()
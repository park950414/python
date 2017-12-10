# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 21:42:47 2017

@author: park
"""

def func():
    print("func() in one.py")

print("top-level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")
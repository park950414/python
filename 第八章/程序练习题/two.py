# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 21:43:06 2017

@author: park
"""
import one        # start executing one.py

print("top-level in two.py")
one.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")




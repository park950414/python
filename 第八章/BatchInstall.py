# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 19:25:12 2017

@author: park
"""

import os 
libs={"numpy","matplotlib","pillow","sklearn","requests","jieba",\
      "jieba","beautifulsoup4","wheel","networkx","sympy",\
      "pyinstaller","django","flask","werobot","PyQt5","pandas",\
      "pyopengl","pypdf2","docopt","pygame"}
try:
    for lib in libs:
        os.system("pip install "+lib)
        print("Successful")
except:
    print("Failed Somehow")
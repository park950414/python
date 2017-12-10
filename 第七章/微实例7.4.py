# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 19:42:57 2017

@author: park
"""

from PIL import Image
im= Image.open('C:\\Users\\park\\Desktop\\python\\第七章\\football.gif')
try:
    im.save('picframe{:02d}.png'.format(im.tell()))
    while True:
        im.seek(im.tell()+1)
        im.save('picframe{:02d}.png'.format(im.tell()))
except:
    print("处理结束")

# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 13:21:53 2017

@author: park
"""
from PIL import Image
im=Image.open("birdnest.jpg")
size=im.size
x=size[0]
y=size[1]
factor=eval(input("请输入缩小的比例:"))
newx,newy=x*factor,y*factor
newsize=tuple((newx,newy))
im.thumbnail(newsize)
im.save("birdnestsmaller.jpg")
im.close()
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 20:39:29 2017

@author: park
"""
from PIL import Image
fname=input("请输入要处理的图片名称：")
im=Image.open(fname)
r,g,b=im.split()
newg=g.point(lambda i:i*0.9)
newb=b.point(lambda i:i<100)
om=Image.merge(im.mode,(r,newg,newb))
fnewname="new1"+fname
om.save(fnewname)
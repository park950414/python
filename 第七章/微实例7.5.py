# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 20:16:42 2017

@author: park
"""
from PIL import Image
fname=input("请输入要处理的图片名称:")
im=Image.open(fname)
r,g,b=im.split()
om=Image.merge("RGB",(b,g,r))
fnewname="new"+fname
om.save(fnewname)

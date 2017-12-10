# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 21:10:35 2017

@author: park
"""
from PIL import Image
from PIL import ImageEnhance
fname=input("请输入要处理的图片名称:")
im=Image.open(fname)
om=ImageEnhance.Contrast(im)
fnewname="Contrast"+fname
om.enhance(20).save(fnewname)
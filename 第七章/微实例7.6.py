# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 20:50:06 2017

@author: park
"""

from PIL import Image
from PIL import ImageFilter
fname=input("请输入要处理的图片名称：")
im=Image.open(fname)
om=im.filter(ImageFilter.BLUR)
om.save("BLUR"+fname)
om=im.filter(ImageFilter.CONTOUR)
om.save("CONTOUR"+fname)
om=im.filter(ImageFilter.DETAIL)
om.save("DETAIL"+fname)
om=im.filter(ImageFilter.EDGE_ENHANCE)
om.save("EDGE_ENHANCE"+fname)
om=im.filter(ImageFilter.EDGE_ENHANCE_MORE)
om.save("EDGE_ENHANCE_MORE"+fname)
om=im.filter(ImageFilter.EMBOSS)
om.save("EMBOSS"+fname)
om=im.filter(ImageFilter.FIND_EDGES)
om.save("FIND_EDGES"+fname)
om=im.filter(ImageFilter.SMOOTH)
om.save("SMOOTH"+fname)
om=im.filter(ImageFilter.SMOOTH_MORE)
om.save("SMOOTH_MORE"+fname)
om=im.filter(ImageFilter.SHARPEN)
om.save("SHARPEN"+fname)

    
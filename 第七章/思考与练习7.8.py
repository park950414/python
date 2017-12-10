# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 21:17:30 2017

@author: park
"""

from PIL import Image
im=Image.open("birdnest.jpg")
r,g,b=im.split()
newr=r.point(lambda i:i*0)
om=Image.merge("RGB",(newr,g,b))
om.save("birdnest0GB.jpg")
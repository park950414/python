# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 21:10:29 2017

@author: park
"""
from math import *
class Projectile:
    def __init__(self,angle,velocity,height):
        self.xpos = 0.0
        self.ypos = 0.0
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)
    def update(self,time):
        self.xpos = self.xpos + time *self.xvel
        yvell = self.yvel - time * 9.8
        self.ypos = self.ypos + time * (self.yvel+yvell)/2.0
        self.yvel = yvell
    def getY(self):
        return self.ypos
    def getX(self):
        return self.xpos

    
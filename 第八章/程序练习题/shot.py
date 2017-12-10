# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:50:04 2017

@author: park
"""

from turtle import *
from math import *

def getInputs():
    angle = eval(input("Enter the launch angle (in degrees):"))
    vel = eval(input("Enter the initial velocity (in meters/sec):"))
    h0 = eval(input("Enter the initial height (in meters):"))
    time = eval(input("Enter the time interval:"))
    return angle,vel,h0,time 

def getXYComponents(vel,angle):
    theta = radians(angle)
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)
    return xvel,yvel

def updatePosition(time,xpos,ypos,xvel,yvel):
    xpos = xpos + xvel * time
    yvell = yvel - 9.8 * time
    ypos = ypos + time * (yvel+yvell)/2.0
    yvel = yvell
    return xpos,ypos,yvel

def printPosition(xpos,ypos):
    goto(xpos*20,ypos*20)

angle,vel,h0,time = getInputs()
xpos,ypos = 0,h0
setup(400,400,200,200)
setposition(0,0)
goto(0,300)
setposition(0,0)
goto(300,0)
setposition(0,0)
printPosition(xpos,ypos)
xvel,yvel = getXYComponents(vel,angle)
while ypos >= 0.0:
    xpos,ypos,yvel = updatePosition(time,xpos,ypos,xvel,yvel)
    printPosition(xpos,ypos)
    
print("\nDistance traveled:{:0.1f}meters".format(xpos))

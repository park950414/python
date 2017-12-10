# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 21:44:27 2017

@author: park
"""
import turtle
turtle.title("词频统计结果柱状图")
turtle.setup(900,750,0,0)
t = turtle.Turtle()
t.hideturtle()
t.width(3)
def drawLine(t,x1,y1,x2,y2):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)
def drawRectangle(t,x,y):
    drawLine(t,x-5,0,x-5,y)
    drawLine(t,x-5,y,x+5,y)
    drawLine(t,x+5,y,x+5,0)
    drawLine(t,x+5,0,x-5,0)
def drawText(t,x,y,text):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.write(text)
drawRectangle(t,10,20)
drawText(t,10,20,"abc")

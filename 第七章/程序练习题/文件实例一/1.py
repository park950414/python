# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 19:54:15 2017

@author: park
"""

import turtle

turtle.title("数据驱动的动态路径绘制")
turtle.setup(800,600,0,0)
pen=turtle.Turtle()
pen.color("red")
pen.width(5)
pen.shape("turtle")
pen.speed(5)
result=[]#列表
file=open("data.txt","r")
for line in file:
    result.append(list(map(float,line.split(","))))
    #map()是python内置的高阶函数，它接收一个函数f和一个list，
    #并通过把函数f依次作用在list的每个元素上，得到一个新的list并返回

for i in range(len(result)):
    pen.color((result[i][3],result[i][4],result[i][5]))
    pen.fd(result[i][0])
    if result[i][1]:
        pen.rt(result[i][2])
    else:
        pen.lt(result[i][2])
pen.goto(0,0)

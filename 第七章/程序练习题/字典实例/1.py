# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 20:54:48 2017

@author: park
"""
import turtle

count = 10 #词频排列显示个数
data = [] #单词词频数组，作为y轴
words = [] #单词数组，作为x轴
yScale = 0.25 #y轴放大倍数
xScale = 35 #轴放大倍数

def processLine(line,wordCounts):
    line = replacePunctuations(line)#用空格替换标点符号
    words = line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1 

def replacePunctuations(line):
    for ch in line:
        if ch in "~!@#$%^&*()_-+=<>,./?;:'{}[]|\"\\":
            line = line.replace(ch,"")
    return line

infile = open('Hamlet.txt',"r")
wordCounts = {}
for line in infile:
    processLine(line.lower(),wordCounts)
pairs = list(wordCounts.items())
items = [[x,y] for (y,x) in pairs]
items.sort(reverse=1)
for i in range(count):
    words.append(items[i][1])
    data.append(items[i][0])
for i in range (count):
    print(words[i])
    print(data[i])

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

def drawText(t,x,y,text):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.write(text)

def drawRectangle(t,x,y):
    x = x*xScale
    y = y*yScale
    drawLine(t,x-5,0,x-5,y)
    drawLine(t,x-5,y,x+5,y)
    drawLine(t,x+5,y,x+5,0)
    drawLine(t,x+5,0,x-5,0)
    
def drawBar(t):
    for i in range (count):
        drawRectangle(t,i+1,data[i])

def drawGraph(t):
    drawLine(t,0,0,360,0)
    drawLine(t,0,0,0,360)

drawGraph(t)
drawBar(t)
for x in range(count):
    x = x+1
    drawText(t,x*xScale-4,-20,words[x-1])
    drawText(t,x*xScale-4,data[x-1]*yScale+10,data[x-1])
infile.close()

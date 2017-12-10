from datetime import *
from turtle import *

def drawLine(draw):
    if draw:
        pendown()
    else:
        penup()
    forward(40)
    right(90)

def drawDigit(d):
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    penup()
    left(180)
    forward(20)

def drawDate(date):
    for i in date:
        drawDigit(eval(i))

def main():
    setup(1000,350,200,200)
    penup()
    fd(-400)
    pensize(5)
    drawDate(datetime.now().strftime('%Y%m%d%H%M'))
    hideturtle()

main()

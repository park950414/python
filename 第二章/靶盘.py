from turtle import *
setup(500,500,200,200)
pensize(2)
pencolor("black")
a=0
for i in range (9):
    seth(0)
    penup()
    fd(20)
    pendown()
    a=a+20
    seth(90)
    circle(a)
done()

#Drawpython
from turtle import *
setup(650,350,200,200)
penup()
fd(-250)
pendown()
pensize(25)
seth(-60)
a=0
color=['red','blue','grey','green','yellow']
for i in range(5):
    pencolor(color[a])
    circle(40,120)
    circle(-40,120)
    a=a+1
circle(40,120/2)
fd(40)
circle(16,180)
fd(40*2/3)
turtle.done()

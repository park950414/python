import turtle
turtle.setup(1000,1000,200,200)
turtle.pensize(2)
a=1
for i in range (3):
    turtle.fd(200)
    turtle.seth(120*a)
    a=a+1
turtle.seth(-120)
a=1
for i in range (3):
    turtle.fd(200)
    turtle.seth(-120+120*a)
    a=a+1
turtle.seth(0)
turtle.penup()
turtle.fd(200)
turtle.pendown()
turtle.seth(-120)
a=1
for i in range (3):
    turtle.fd(200)
    turtle.seth(-120+120*a)
    a=a+1
turtle.done()

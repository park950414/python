import turtle
turtle.setup(500,500,200,200)
turtle.pensize(2)
a=0
for i in range (4):
    turtle.seth(90*a)
    turtle.penup()
    turtle.fd(50)
    turtle.pendown()
    turtle.fd(100)
    turtle.penup()
    turtle.fd(50)
    turtle.pendown()
    a=a+1
turtle.done()

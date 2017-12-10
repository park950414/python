import turtle
turtle.setup(500,500,200,200)
turtle.pensize(2)
a=1
for i in range (3):
    turtle.fd(200)
    turtle.seth(120*a)
    a=a+1
turtle.done()

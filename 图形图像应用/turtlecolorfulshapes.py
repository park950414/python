from turtle import *

pensize(3)
penup()
goto(-200,-50)
pendown()
begin_fill()
color("red")
circle(40,steps=3)
end_fill()

penup()
goto(-100,-50)
pendown()
begin_fill()
color("blue")
circle(40,steps=4)
end_fill()

penup()
goto(0,-50)
pendown()
begin_fill()
color("green")
circle(40,steps=5)
end_fill()

penup()
goto(100,-50)
pendown()
begin_fill()
color("yellow")
circle(40,steps=6)
end_fill()

penup()
goto(200,-50)
pendown()
begin_fill()
color("purple")
circle(40)
end_fill()
down()

color("green")
up()
goto(-100,50)
write(("Cool Colorful shapes"),font = ("Times",18,"bold"))
hideturtle()
done
      

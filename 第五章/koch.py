from turtle import *
def koch(size,n):
    if n==0:
        fd(size)
    else :
        for angle in [0,60,-120,60]:
            left(angle)
            koch(size/3,n-1)

def main():
    setup(800,400)
    speed(0)
    pencolor("red")
    penup()
    goto(-200,100)
    pendown()
    level=5
    pensize(2)
    koch(400,level)
    right(120)
    koch(400,level)
    right(120)
    koch(400,level)
    hideturtle()
main()

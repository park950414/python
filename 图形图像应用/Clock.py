from turtle import *
from datetime import *

def SetupClock(radius):
    #建立表的外框
    reset()
    pensize(7)
    for i in range(60):
        Skip(radius)
        if i % 5 ==0:
            fd(20)
            Skip(-radius-20)
        else:
            dot(5)
            Skip(-radius)
        right(6)

def Skip(step):
    penup()
    fd(step)
    pendown()

def mkHand(name,length):
    #注册Turtle形状，建立表针Turtle
    reset()
    Skip(-length*0.1)
    begin_poly()
    fd(length*1.1)
    end_poly()
    handForm = get_poly()
    register_shape(name,handForm)

def Init():#初始化
    global secHand,minHand,hurHand,printer
    mode("logo")#重置Turtle指向北
    #建立三个表针Turtle并初始化
    mkHand("secHand",125)
    mkHand("minHand",130)
    mkHand("hurHand",90)
    secHand = Turtle()
    secHand.shape("secHand")
    minHand = Turtle()
    minHand.shape("minHand")
    hurHand = Turtle("hurHand")
    hurHand.shape("hurHand")
    for hand in secHand,minHand,hurHand:
        hand.shapesize(1,1,3)#turtle.shapesize(stretch_wid=None, \
                             #stretch_len=None, outline=None)¶
        hand.speed(0)#“fastest”: 0“fast”: 10“normal”: 6“slow”: 3“slowest”: 1
    #建立输出文字Turtle
    printer = Turtle()
    printer.hideturtle()
    printer.penup()

def Week(t):
    week = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
    return week[t.weekday()]

def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d %d" %(y,m,d)

def Tick():
    #绘制表针的动态显示
    t = datetime.today()
    second = t.second + t.microsecond*0.000001
    minute = t.minute + second/60.0
    hour = t.hour + minute/60.0
    tracer(False)
    printer.fd(65)
    printer.write(Week(t),align='center',font=("Courier",14,"bold"))
    printer.back(130)
    printer.write(Date(t),align='center',font=("Courier",14,"bold"))
    printer.home()#归位到原点
    tracer(True)
    secHand.setheading(6*second)
    minHand.setheading(6*minute)
    hurHand.setheading(30*hour)
    ontimer(Tick,100)#100ms后继续调用tick

def main():
    tracer(False)#动画关闭
    Init()
    SetupClock(160)
    tracer(True)#恢复动画绘制
    Tick()
    mainloop()

main()
    
                  

from random import *
try :
    x=randint(0,100)
    count=0
    for i in range(101):
        count+=1
        a=eval(input("请输入所猜的数:"))
        if int(a)==a:
            if a==x:
                print("预测{}次，你猜中了!".format(count))
                break
            elif a>x:
                print("遗憾，太大了")
            else :
                print("遗憾，太小了")
        else :
            print("输入内容必须为整数！")
            continue
except NameError:
    print("输入内容必须为整数！")
    a=eval(input("请重新输入所猜的数:"))
except SyntaxError:
    print("输入内容必须为整数！")
    a=eval(input("请重新输入所猜的数:"))   


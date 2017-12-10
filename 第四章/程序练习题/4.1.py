from random import *
x=randint(0,9)
count=0
for i in range(10):
    count+=1
    a=eval(input("请输入所猜的数:"))
    if a==x:
        print("预测{}次，你猜中了!".format(count))
        break
    elif a>x:
        print("遗憾，太大了")
    else :
        print("遗憾，太小了")
    

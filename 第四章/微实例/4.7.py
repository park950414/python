try :
    alp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    idx=eval(input("请输入一个整数:"))
    print(alp[idx-1])
except NameError:
        print("输入错误，请输入一个整数！")
except:
        print("其他错误")
else:
        print("没有发生异常")
finally:
        print("程序执行完毕，不知道是否发生异常")

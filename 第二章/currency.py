#currency
money = input("请输入要兑换的金额及币种，如：100美元：")
if money[-3:] in ['人民币']:
    dollar= eval(money[0:-3])/6
    print("{}可以兑换{}美元".format(money,dollar))
elif money[-2:] in ['美元']:
    rmb=eval(money[0:-2])*6
    print("{}可以兑换{}人民币".format(money,rmb))
else :
    print("输入格式有误")
              

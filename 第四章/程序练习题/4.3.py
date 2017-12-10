a,b=eval(input("请输入两个数(用逗号隔开):"))
c=min(a,b)
while 1:
    if a%c==0 and b%c==0:
        GCD=c
        break
    else:
        c=c-1
LCM=a*b/GCD
print("{},{}的最大公约数是{},最小公倍数是{}".format(a,b,GCD,LCM))

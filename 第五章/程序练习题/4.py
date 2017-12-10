def multi(a):
    product=1
    for i in a:
        product=product*i
    return product

a=eval(input("请输入参数:"))
print("所有参数的乘积为:{:.2f}".format(multi(a)))

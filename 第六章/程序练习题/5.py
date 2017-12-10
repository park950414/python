from random import *
TIMES=eval(input("请输入随机样本数量:"))
count=0
for a in range (TIMES):
    birthday=[]
    for i in range (23):
        birthday.append(randint(1,366))
    if len(set(birthday))<len(birthday):
        count+=1

print("23个人中至少两个人生日相同的概率为:{}".format(count/TIMES))

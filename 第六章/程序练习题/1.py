from random import *

def newpassword(n):
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    password=''
    for i in range(n):
        password=password+choice(a)
    return password


n,m=eval(input("请输入密码的位数和密码个数(例如:3,4):"))

for i in range (m):
     print("生成的密码为:{}".format(newpassword(n)))

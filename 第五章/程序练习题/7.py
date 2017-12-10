def move(n,a,b,c):
    if n==1:
        print(a,"→",c)
        return #退出函数
    move(n-1,a,c,b)
    move(1,a,b,c)
    move(n-1,b,a,c)
n=eval(input("请输入汉诺塔的层数:"))
move(n,"a","b","c")

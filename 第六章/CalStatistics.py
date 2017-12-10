from math import sqrt

def getNum(): #获取用户输入
    nums=[]
    iNumStr=input("请输入数字(直接输入回车退出):")
    while iNumStr!="":
        nums.append(eval(iNumStr))
        iNumStr=input("请输入数字(直接输入回车退出):")
    return nums

def mean(numbers):   #计算平均值
    s=0.0
    for num in numbers:
        s+=num
    return s/len(numbers)

def dev(numbers):       #计算方差
    sdev=0.0
    for num in numbers:
        sdev=sdev+(num-mean(n))**2
    return sqrt(sdev/(len(numbers)-1))


def median(numbers):   #计算中位数
    sorted(numbers)
    size=len(numbers)
    if size%2==0:
        med=(numbers[size//2]+numbers[size//2-1])/2
    else:
        med=numbers[size//2]
    return med



n=getNum()
m=mean(n)
print("平均值：{:.2f},方差：{:.2f},中位数：{:},最大值：{},最小值：{}.".format(m,dev(n),median(n),max(n),min(n)))
        

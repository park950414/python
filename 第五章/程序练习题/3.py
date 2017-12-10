def isNum(string):
    try:
        if type(eval(string))==complex or type(eval(string))==int or type(eval(string))==float:
            return True
    except:
        return False

string=input("请输入一个字符串:")
print(isNum(string))

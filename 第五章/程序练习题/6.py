from datetime import *

def birthdaydate(day):
    print(day.strftime("%Y-%m-%d"))
    print(day.strftime("%Y年%m月%d日"))
    print(day.strftime("%B %dth,%Y"))
    print(day.strftime("%b %dth,%Y"))
    print(day.strftime("%A,%B %d,%Y"))
    print(day.strftime("%a,%b %d,%Y"))
    print(day.strftime("%F"))
    print(day.strftime("%D"))
    print(day.strftime("%g/%m/%d"))
    print(day.strftime("%c"))
                       


day=datetime.strptime(input("请输入你的生日(格式：年，月，日）："),'%Y,%m,%d')
birthdaydate(day)


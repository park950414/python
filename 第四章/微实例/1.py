score=eval(input("请输入分数:"))
if score >=60.0:
    grade='D'
elif score >=70.0:
    grade='C'
elif score >=80.0:
    grade='B'
elif score>=90.0:
    grade='A'
print("成绩是:{}".format(grade))

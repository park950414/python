import math
dayup=1
for i in range (365):
    if i%7 in [3,4,5,6]:
        dayup=dayup*(1+0.01)
    else:
        +dayup
print("7天为周期，连续学习365天后能力值是:{:.2f}".format(dayup))

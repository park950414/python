#DayDayup
import math
dayup,dayfactor=1,0.01
for i in range (365):
    if i%7 in [6,0]:
        dayup=dayup*(1-dayfactor)
    else:
        dayup=dayup*(1+dayfactor)
print("向上五天向下两天的力量:{:.2f}".format(dayup))

#DayDayup
dayup=1
for i in range(365):
    if (i+1)%10 in[4,5,6,7]:
        dayup=dayup*(1+0.01)
    else:
        +dayup
print("固定每10天休息一天，365天后能力值是{:.2f}.".format(dayup))

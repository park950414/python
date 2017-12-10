from random import *
first_choice=0
change_choice=0
TIMES=10000
a=['山羊1','山羊2','车']
for i in range (TIMES):
    car_in_door=choice(a)
    my_guess=choice(a)
    if my_guess==car_in_door:
        first_choice+=1
    else:
        change_choice+=1
print("改变选择获胜的机率:{1}\n坚持选择获胜的机率:{0}".format(first_choice/TIMES,change_choice/TIMES))

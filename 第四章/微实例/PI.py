#PI
from random import *
from math import *
from time import *
DARTS=1000000
hits=0.0
clock()
for i in range (DARTS):
    x,y=random(),random()
    dist=sqrt(x**2+y**2)
    if dist<=1.0:
        hits=hits+1
pi=4*(hits/DARTS)
print("Pi值是{}.".format(pi))
print("运行时间是：{:5.5}s".format(clock()))

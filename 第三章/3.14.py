import math
N=0
for b in range (10):
    a=1.0
    N=N+0.001
    for i in range (365):
        if i%7 in [1,2,3,4,5,6]:
            a=a+N
    print("年终值:{:.3f}".format(a))

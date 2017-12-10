import math
N=0
for b in range (10):
    a=1.0
    N=N+0.001
    for i in range (360):
        if i%30 in [1,2,3,4,5,6,7,8,9,10]:
            a=a+N
    print("年终值:{:.3f}".format(a))

#TextProgressBar.py
import time
for i in range(4):
    a="Starting"+"*"*i
    print("\r{}".format(a),end=' ')
    time.sleep(1)
b= a+"Done!"
print("\r{}".format(b))
time.sleep(1)

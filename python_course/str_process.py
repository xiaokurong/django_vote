import time
from math import sin

'''
print("==========start===========")
scale = 10
start=time.perf_counter()
for i in range (scale+1):
    a="+"*i
    b="-"*(10-i)
    c=i*10
    d=time.perf_counter()-start
    print("\r{:^3.0f}%{}=>{}{:3.2f}S".format(c,a,b,d),end="")
    time.sleep(0.5)


print("\n" +"===========end============")
          


for i in range(101):
    print("\r{:3}%".format(i),end="")
    time.sleep(0.1)

'''
pai=3.1415

def speed_up(x):
    y=x+(1-sin(x*pai*2+pai/2))/-8
    return y

    

for i in range(101):
    print("\r{}%".format(speed_up(i),end=""))
    time.sleep(0.5)

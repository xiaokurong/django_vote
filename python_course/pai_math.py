import random
import time
'''
圆的面积是：pai*r*r ,所以当r为1时，圆的面积就是pai。计算方法：蒙塔卡罗计算方法。
'''
c=0
count=1000000
start=time.perf_counter()
for i in range(count+1):
    a=random.random()
    b=random.random()
    if pow((a*a+b*b),1/2)<=1 :
        c +=1

pai=(c/count)*4
print("pai is : {:.10f}".format(pai))
use_time=time.perf_counter()-start
print("use time is : {:.2f}".format(use_time))

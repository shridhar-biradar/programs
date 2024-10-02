import math
print('factorial of 5 is',math.factorial(5))
print('pi values is ',math.pi)
print('square root of 25 is ',math.sqrt(25))

for i in range(1,6):
    print('factorial of {} is {}'.format(i,math.factorial(i)))
print('*******')

# predefined modules
from math import factorial,sqrt,pi,pow
print(pow(2,3))
print(factorial(6))
print(int(sqrt(100)))

import random as r
print(r.randint(1,100))

for i in range(1,6):
    print(r.randint(10,50))

import calendar as cal
print(cal.month(2024,10))
print(cal.month(2025,4))
print(cal.month(2025,7))
    


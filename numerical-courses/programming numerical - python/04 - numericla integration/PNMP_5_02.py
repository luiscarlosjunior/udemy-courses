'''
Method: Simpson's 1/3 Rule
Section: Numerical Integration
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_5_02.py
Date: Aug. 6, 2017
''' 
from math import sin, pi
f = lambda x: x*sin(x)
a = 0
b = pi/2
n = 6
h = (b - a) / n
S = f(a)+f(b)
for i in range(1,n,2):
    S += 4*f(a + i*h)
for i in range(2,n,2):
    S += 2*f(a + i*h)
Integral = h/3 * S
print('Integral = %f' % Integral)

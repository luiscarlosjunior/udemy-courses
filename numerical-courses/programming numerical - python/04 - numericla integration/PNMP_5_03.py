'''
Method: Simpson's 3/8 Rule
Section: Numerical Integration
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_5_03.py
Date: Aug. 6, 2017
''' 
from math import sin, pi
f = lambda x: x*sin(x)
a = 0
b = pi/2
n = 6
h = (b - a) / n
S = (f(a) + f(b))
for i in range(1, n, 3):
    S += 3*(f(a + i*h) + f(a + (i+1)*h))
for i in range(3, n, 3):
    S += 2*f(a + i*h)
Integral = 3*h/8 * S
print('Integral = %f' % Integral)

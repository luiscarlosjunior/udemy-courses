'''
Method: Trapezoidal Rule
Section: Numerical Integration
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_5_01.py
Date: Aug. 6, 2017
''' 
from math import sin, pi
f = lambda x: x*sin(x)
a = 0
b = pi/2
n = 5
h = (b - a) / n
S = 0.5*(f(a)+f(b))
for i in range(1,n):
    S += f(a + i*h)
Integral = h * S
print('Integral = %f' % Integral)

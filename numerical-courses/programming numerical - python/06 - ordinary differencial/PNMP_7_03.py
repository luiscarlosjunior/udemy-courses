'''
Method: 4th order Runge-Kutta
Section: Ordinary Differential Equations
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_7_03.py
Date: Aug. 6, 2017
''' 
from math import exp
dy = lambda x,y: x*y
f = lambda x: exp(x**2/2)
x = 0
xn = 2
y = 1
h = 0.5
n = int((xn-x)/h)
print ('x  \t\t y (RK4) \t y (analytical)')  
print ('%f \t %f \t %f'% (x,y,f(x)))   
# main loop 
for i in range(1,n+1):
    K1 = h*dy(x, y)
    K2 = h*dy(x + h/2, y + K1/2)
    K3 = h*dy(x + h/2, y + K2/2)
    K4 = h*dy(x +h, y + K3)
    y += (K1 + 2*K2 + 2*K3 + K4)/6
    x += h
    print ('%f \t %f \t %f'% (x,y,f(x)))

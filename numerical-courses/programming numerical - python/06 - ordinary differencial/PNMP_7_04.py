'''
Method: First Order ODE using 4th order Runge-Kutta (Plot)
Section: Ordinary Differential Equations
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_7_04.py
Date: Aug. 6, 2017
''' 
import numpy as np
import matplotlib.pyplot as plt
dy = lambda x,y: y+3
f = lambda x: np.exp(x-2) - 3
x = 2
xn = 4
y = -2
h = 0.1
n = int((xn-x)/h)
xp = np.linspace(x,xn,n+1) # x array for plot
fp = f(xp)                  # f(x) array for plot 
yp = np.empty(n+1, float) # y array for plot
yp[0] = y
print ('x  \t\t y (RK4) \t y (analytical)')  
print ('%f \t %f \t %f'% (x,y,f(x)))   
# main loop 
for i in range(1,n+1):
    K1 = h*dy(x, y)
    K2 = h*dy(x + h/2, y + K1/2)
    K3 = h*dy(x + h/2, y + K2/2)
    K4 = h*dy(x +h, y + K3)
    y += (K1 + 2*K2 + 2*K3 + K4)/6
    yp[i] = y
    x += h
    print ('%f \t %f \t %f'% (x,y,f(x)))
# Plot
plt.plot(xp,yp,'ro', xp,fp)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['RK4', 'Analytical'])
plt.show()

'''
Method: Second Order ODE using 4th order Runge-Kutta
Section: Ordinary Differential Equations
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_7_05.py
Date: Aug. 6, 2017
''' 
from math import sin, cos, pi
# system of the first order ODE's
dy = lambda x, y, u: u
du = lambda x, y, u: 4*x + 10 * sin(x) - y
# the analytical solution
f = lambda x: 9*pi*cos(x) + 7*sin(x) + 4*x - 5*x*cos(x)
df = lambda x: -9*pi*sin(x) + 7*cos(x) + 4 - 5*(cos(x) - x*sin(x))
# initial values
x = pi
xn = 2*pi
y = 0.0
u = 2
h = 0.1
n = int((xn-x)/h)

# the header of the output table
print('x \t\t y\'(RK4) \t y(RK4) \t y\'(Exact) \t y(Exact)')
print('%f \t %f \t %f \t %f \t %f'%(x, u, y, df(x), f(x)))
for i in range(1, n+1):
    L1 = h*du(x, y, u)
    K1 = h*dy(x, y, u)
    
    L2 = h*du(x+h/2, y+K1/2, u+L1/2)
    K2 = h*dy(x+h/2, y+K1/2, u+L1/2)
    
    L3 = h*du(x+h/2, y+K2/2, u+L2/2)
    K3 = h*dy(x+h/2, y+K2/2, u+L2/2)
    
    L4 = h*du(x+h, y+K3, u+L3)
    K4 = h*dy(x+h, y+K3, u+L3)

    u += (L1 + 2*L2 + 2*L3 + L4)/6
    y += (K1 + 2*K2 + 2*K3 + K4)/6
    x += h
    print('%f \t %f \t %f \t %f \t %f'%(x, u, y, df(x), f(x)))

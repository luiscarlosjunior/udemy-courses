'''
Method: Second Order ODE using 4th order Runge-Kutta (Plot)
Section: Ordinary Differential Equations
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_7_06.py
Date: Aug. 6, 2017
''' 
import numpy as np
import matplotlib.pyplot as plt
# system of the first order ODE's
dy = lambda x, y, u: u
du = lambda x, y, u: 4*x + 10 * np.sin(x) - y
# the analytical solution
f = lambda x: 9*np.pi*np.cos(x) + 7*np.sin(x) + 4*x - 5*x*np.cos(x)
df = lambda x: -9*np.pi*np.sin(x) + 7 * np.cos(x) + 4 - 5*(np.cos(x) - x*np.sin(x))
# initial values
x = np.pi
xn = 2*np.pi
y = 0.0
u = 2
h = 0.1
n = int((xn-x)/h)
# plot arrays
xp = np.linspace(x, xn, n+1)
yp = np.empty(n+1, float)
up = np.empty(n+1, float)
yp[0] = y
up[0] = u
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
    up[i] = u
    y += (K1 + 2*K2 + 2*K3 + K4)/6
    yp[i] = y
    x += h
    print('%f \t %f \t %f \t %f \t %f'%(x, u, y, df(x), f(x)))

# Plot
plt.plot(xp, yp, color = 'r', marker = 'o', ls = '', label='y (RK4)')
plt.plot(xp, up, color = 'b', marker = 's', ls = '', label='y\' (RK4)')
plt.plot(xp, f(xp), color = 'k', lw = 1.5, ls = '-', label='y (Exact)')
plt.plot(xp, df(xp), color = 'k', lw = 1.5, ls = '--', label='y\' (Exact)')
plt.xlabel('x')
plt.ylabel('y, y\'')
plt.legend(loc = 'upper left')
plt.grid()
plt.axis([np.pi, 2*np.pi, None, None])
plt.show()

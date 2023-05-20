'''
Method: Simple Iterations (while-loop) with Convergence Plot
Section: Roots of Higher-Degree Equations
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_2_02_plot.py
Date: Jan. 23, 2020
'''

import numpy as np
import matplotlib.pyplot as plt


fn = lambda x: (2*x**2 + 3)/5 # function 1: convergence example
#fn = lambda x:  1/np.cos(x)  # function 2: divergence example

# Lists to save values for plotting
xlist = list()
xnewlist = list()
itrlist = list()

x = 0
for iteration in range(1,50):
    xnew = fn(x)
    # saving for plotting
    xlist.append(x)
    xnewlist.append(xnew)
    itrlist.append(iteration)
    # convergence condition
    if abs(xnew - x) < 0.000001:
        break
    x = xnew
print('The root : %0.5f' % xnew)
print('The number of iterations : %d' % iteration)
                                  



#plotting
plt.plot(itrlist, xlist,'b-o',itrlist,xnewlist,'r-*')
plt.legend(['x','xnew'],loc = 'lower right')
plt.xlabel('iterations')
plt.ylabel('x')
plt.grid()
plt.show()

'''
Method: Simple Iterations (while-loop)
Section: Roots of Higher-Degree Equations
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_2_02.py
Date: Aug. 6, 2017
''' 
x = 5 # arbitrary value
xnew = 0 # initial guess
iteration = 0
while abs(xnew - x) >= 0.000001:
    iteration += 1
    x = xnew
    xnew = (2*x**2 + 3)/5
    
print('The root : %0.5f' % xnew)
print('The number of iterations : %d' % iteration)

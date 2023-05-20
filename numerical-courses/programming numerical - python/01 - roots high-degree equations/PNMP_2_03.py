'''
Method: Newton-Raphson
Section: Roots of Higher-Degree Equations
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_2_03.py
Date: Aug. 6, 2017
''' 
x = 0
for iteration in range(1,101):
    xnew = x - (2*x**2 - 5*x + 3)/(4*x - 5) # the Newton-Raphson's formula
    if abs(xnew - x) < 0.000001:
        break
    x = xnew
print('The root : %0.5f' % xnew)
print('The number of iterations : %d' % iteration)
                                  

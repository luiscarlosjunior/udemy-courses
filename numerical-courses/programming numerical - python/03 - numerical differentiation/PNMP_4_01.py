'''
Method: Forward Differences Approximation
Section: Numerical Differentiation
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_4_01.py
Date: Aug. 6, 2017
''' 
f = lambda x: 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2
h = 0.05
x = 0.1

dff1 = (f(x+h) - f(x))/h
dff2 = (f(x+2*h) - 2*f(x+h) + f(x))/h**2
print('Solution by forward differences:')
print('f\'(%f) = %f'%(x,dff1))
print('f\'\'(%f) = %f'%(x,dff2))

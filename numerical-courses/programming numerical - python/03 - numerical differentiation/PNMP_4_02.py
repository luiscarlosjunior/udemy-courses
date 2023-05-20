'''
Method: Finite Differences Approximation
Section: Numerical Differentiation
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_4_02.py
Date: Aug. 6, 2017
''' 
def f(x):
    return 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2
h = 0.05
x = 0.1

# Forward differences approximation
dff1 = (f(x+h) - f(x))/h
dff2 = (f(x+2*h) - 2*f(x+h) + f(x))/h**2
print('Solution by forward differences:')
print('f\'(%f) = %f'%(x,dff1))
print('f\'\'(%f) = %f'%(x,dff2))

# Central differences approximation
dfc1 = (f(x+h)-f(x-h))/(2*h)
dfc2 = (f(x+h)-2*f(x)+f(x-h))/h**2
print('\nSolution by central differences:')
print('f\'(%f) = %f'%(x,dfc1))
print('f\'\'(%f) = %f'%(x,dfc2))

# Backward differences approximation
dfb1 = (f(x)-f(x-h))/h
dfb2 = (f(x)-2*f(x-h)+f(x-2*h))/h**2
print('\nSolution by backward differences:')
print('f\'(%f) = %f'%(x,dfb1))
print('f\'\'(%f) = %f'%(x,dfb2))

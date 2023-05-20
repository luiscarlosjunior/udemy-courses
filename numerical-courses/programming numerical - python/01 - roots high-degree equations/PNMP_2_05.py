'''
Method: Bisections
Section: Roots of Higher-Degree Equations
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_2_05.py
Date: Aug. 6, 2017
''' 
def y(x):
    return 2*x**2 - 5*x + 3

x1 = float(input('Enter the value x1 : '))
x2 = float(input('Enter the value x2 : '))
y1 = y(x1)
y2 = y(x2)

if y1*y2 > 0:
    print('No root exist within given interval')
    exit
    
for i in range(1, 101): # 100 bisections
    xh = (x1 + x2) / 2
    yh = y(xh)
    y1 = y(x1)
    if abs(y1) < 1.0E-6:
        break
    elif y1 * yh < 0: # if the root is in the first half-interval
        x2 = xh
    else:
        x1 = xh
print('The root : %.5f' % x1)
print('The number of bisections : %d' % i)

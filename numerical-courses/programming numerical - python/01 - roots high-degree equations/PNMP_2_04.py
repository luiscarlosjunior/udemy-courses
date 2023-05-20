'''
Method: Bisection
Section: Roots of Higher-Degree Equations
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_2_04.py
Date: Aug. 6, 2017
''' 
x1 = 0              
x2 = 1.2            
y1 = 2*x1**2-5*x1+3 
y2 = 2*x2**2-5*x2+3 

if y1*y2 > 0:       
    print('No roots exist within given interval')
    exit            

for i in range(1,101): 
    xh = (x1+x2)/2 
    yh = 2*xh**2-5*xh+3 
    y1 = 2*x1**2-5*x1+3 
    if abs(y1) < 1.0e-6: 
        break 
    elif y1*yh < 0: 
        x2 = xh 
    else: 
        x1 = xh 
print('The root: %.5f' % x1)
print('Number of bisections: %d' % i)

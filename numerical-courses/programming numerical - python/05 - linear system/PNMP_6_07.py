'''
Method: Gauss-Jordan Method
Section: Systems of Linear Equations
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_6_07.py
Date: Dec. 12, 2019
''' 

import numpy as np

def gssjrdn(a,b):
    a = np.array(a, float)
    b = np.array(b, float)
    n = len(b)

    #main loop
    for k in range(n):
        #Partial Pivoting
        if np.fabs(a[k,k]) < 1.0e-12:
            for i in range(k+1,n):
                if np.fabs(a[i,k]) > np.fabs(a[k,k]):
                    a[[k,i]] = a[[i,k]]
                    b[[k,i]] = b[[i,k]]
                    break
        #Division of the pivot row
        pivot = a[k,k]
        a[k] /= pivot
        b[k] /= pivot
        #Elimination loop
        for i in range(n):
            if i == k or a[i,k] == 0: continue
            factor = a[i,k]
            a[i] -= factor * a[k]
            b[i] -= factor * b[k]
    return b,a


a = [[0,2,0,1],[2,2,3,2],[4,-3,0,1],[6,1,-6,-5]]
b = [0,-2,-7,6]

X,A = gssjrdn(a,b)

print("The solution of the system:")
print(X)
print("The coefficient matrix after transformation:")
print(A)
        
    

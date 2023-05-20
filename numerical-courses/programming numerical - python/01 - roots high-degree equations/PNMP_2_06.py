from math import cos

def rfalsi(fn, x1, x2, tol = 0.001, ilimit = 100):
    y1 = fn(x1)
    y2 = fn(x2)
    xh = 0			
    ipos = 0 			# counts false positions
    if y1 == 0: xh = x1		# if x1 is a root	
    elif y2 == 0: xh = x2	# if x2 is a root
    elif y1 * y2 > 0:		# if y1 and y2 have the same sign
        print('No root exists within the given interval.')
    else:    
        for ipos in range(1,ilimit+1):
            xh = x2 - (x2-x1)/(y2-y1) * y2
            yh = fn(xh)
            if abs(yh) < tol:
                break
            elif y1 * yh < 0: # if y1 and yh have opposite signs
                x2 = xh
                y2 = yh
            else:
                x1 = xh
                y1 = yh
    return xh, ipos

def y(x): return 2*x**2 - 5*x + 3       # Example 1
# y = lambda x: x**2 + cos(x)**2 - 4*x  # Example 2

x1 = float(input('Enter the value x1: '))
x2 = float(input('Enter the value x2: '))
x, n = rfalsi(y,x1,x2)
# Output results
print('The root: %f' % x)
print('The number of computed false positions: %d' % n)

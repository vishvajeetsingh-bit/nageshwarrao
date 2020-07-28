# using where() function
from numpy import *
a = array([10, 20, 30, 40, 50], int)
b = array([1, 21, 3, 40, 51], int)
# if a>b then take element from a else from b
c = where(a>b, a, b)
print(c)

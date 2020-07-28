# aliasing an array 
from numpy import *
a = arange(1, 6)
b = a  # give another name b to a
print('Original array = ', a)
print('Alias array = ', b)
b[0] = 99
print('Original array after adding 99 = ', a)
print('Alias array after adding 99 = ', b)
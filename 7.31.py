# creating view for an array
from numpy import *
a = arange(1, 6)
b = a.view()  # create a view of a and call it b
print('Original array = ', a)
print('New array = ', b)

b[0] =  99
print('Original array after adding = ', a)
print('new array after adding = ', b)

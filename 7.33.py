# slicing an array
from numpy import *
# create array a with elements 10 to 15
a = arange(10, 16)
print(a)

# retrieve from 1st to one element prior to 6th element in steps of 2
b = a[1:6:2]
# retrieve all elements from a
b = a[::]
print(b)

# retrieving from 6-2 = 4th to one element prior to 2nd element in
# decreasing step size
b =a[-2:2:-1]
print(b)

# retrieve from 0th to one element prior to the 4th element (6-2 = 4th )
b =a[:-2:]
print(b)


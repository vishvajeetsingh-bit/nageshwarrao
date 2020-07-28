# accesing elements of an array using indexing -v2.0
from array import *

x = array('i', [10, 20, 30, 40, 50])
# find the number of elements in the array
n = len(x)
# display array elements using indexing
i = 0
while i < n:
    print(x[i])
    i += 1

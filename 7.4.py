# creating an array from another array
from array import *
arr1 = array('d', [1.5, 2.5, 3.5, 4.5])
# use same type code and multiply each arr1 element with 3
arr2 = array(arr1.typecode, [a*3 for a in arr1])
print('The arr2 elements are:')
for i in arr2:
    print(i)
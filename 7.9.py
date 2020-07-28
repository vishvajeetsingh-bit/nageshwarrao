# operations on arrays
from array import *

arr = array('i', [10, 20, 30, 40])
print('Original array:', arr)

# append
arr.append(30)
arr.append(60)
print('After append, array =', arr)

# insert 99 at position number 1 in arr
arr.insert(1,99)
print('After inserting, array =', arr)

# remove an element from array
arr.remove(20)
print('After removing element,array = ', arr)

# remove last element from array
n = arr.pop()
print('After using pop, array = ', arr)
print('popped element=', n)

# finding position of an element using indexing
n = arr.index(30)
print('The location of 30 in the array:', n)

# convert an array into list using tolist method
lst = arr.tolist()
print('list = ', lst)
print('Array = ', arr)



# using nonzero() function
from numpy import *
a = array([1, 2, 3, 0, 4, 0, -6], int)
# retrieve indexes of non zero elements from a
c = nonzero(a)
# display indexes
for i in c:
    print(i)
# display the elements    
print(a[c])


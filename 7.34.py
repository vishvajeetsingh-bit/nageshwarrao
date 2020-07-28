# indexing an array
from numpy import *
# create array a with elements 10 to 15
a = arange(10, 16)
print(a)
# retrieve from 1st to one element prior to 6th element in steps of  2 
a = a[1:6:2]
print(a)

# display elements using indexing
i = 0
while(i<len(a)):
    print(a[i])
    i = i + 1
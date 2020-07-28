# retrieving the elements from a 2D array using indexing
from numpy import *

# create a 2d array with 3 rows and 3 cols
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# display only rows
for i in range(len(a)):
    print(a[i])

# display element by element
for i in range(len(a)):
    for j in range (len(a[i])):
        print(a[i][j] , end =' ')
        
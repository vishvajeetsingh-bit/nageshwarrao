#  retrieving the elements from a 3d array using indexing
from numpy import *
# create a 3d array with 2*2*3
a = [[[1, 2, 3], [4, 5, 6]],[[7, 8, 9],[10, 11 ,12]]]
# display element by element
for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(a[i][j])):
            print(a[i][j][k], end='\t')
        print()
    print()
    
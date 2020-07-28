# matrix multiplication 
import sys
from numpy import *

# accept number of rows and cols of first matrix r1, c1
r1, c1 = [int(a) for a in input("First matrix rowsc, cols: ").split()]

# accept number of rows and cols of second matrix r2, c2
r2, c2 = [int(a) for a in input("Second matrix rows , cols: ").split()]

# test the condition if c1!=r2, then multiplication is not possible 
if c1!=r2:
    print('multiplication is not possible')
    sys.exit()
    
# accept first matrix elements as a string into str1
str1 = input('Enter first matrix elements:\n')

# convert str1 into a matrix with size r1*c1
x = reshape(matrix(str1), (r1, c1))

# accept first matrix elements as a string into str1
str2 = input('Enter second matrix elements:\n')

# convert str1 into a matrix with size r1*c1
y = reshape(matrix(str1), (r2, c2))
print('The product of matrix x and y :\n')
z = x*y
print(z)

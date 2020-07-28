# transpose of a matrix
from numpy import *

# accept number of rows and cols into r, c
r, c = [int(a) for a in input("Enter rows, cols: ").split()]

# accept matrix elements as a string into str
str = input("Enter the elements:\n")

# convert the string into matrix with size r*c
x = reshape(matrix(str), (r, c))
print("The original matrix: ")
print(x)

print('The transpose matrix: ')
y = x.transpose()
print(y)


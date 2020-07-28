# mathematical operations on array
# import all numpy modules
from numpy import *

# creating a numpy array using array() function
arr = array([10, 20, 30, 40,  50], int)
print('Original array = ', arr)

# do arithmetic operations 
print('After adding 5= ', arr+5)
print('After subtracting 5 = ', arr-5)
print('After product of 5 = ', arr*5)
print('After divide by 5 = ', arr/5)
print('After modulus by 5 = ', arr%5)

# we can use the arrays in the expressions also
print('Expression value = ', (arr+5)**2-10)
# do some math functions
print('Sine value  = ', sin(arr))
print('cosine value = ', cos(arr))
print('Tangent value = ', tan(arr))
print('Biggest element  = ', max(arr))
print('Smallest value = ', min(arr))
print('Sum of all elements = ', sum(arr))
print('Mean of all elements = ', mean(arr))
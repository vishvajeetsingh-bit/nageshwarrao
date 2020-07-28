# searching ana array for an element
from array import *
# create an empty array to store integers
x = array('i', [])
# store element in array
print('How many elements', end='')
n = int(input())

for i in range(n):
    print('Enter element:', end='')
    x.append(int(input()))
    
print('original array= ', x)
print('Enter element to search:', end='')
s = int(input())
# index method gives the position of the element in the array
try:
    pos = x.index(s)
    print('Found at position: ', pos+1)
except ValueError:
    print('Not found in the array')
    
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
# linear search or sequential search
flag = False
for i in range(len(x)):
    if s == x[i]:
        print("Found at position:", i+1)
        flag = True
    
if flag == False:
    print('Not found')
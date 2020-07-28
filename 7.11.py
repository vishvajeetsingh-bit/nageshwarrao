# sorting an array using bubble sort technique
from array import *
# create an emppty array to store integers
x = array('i', [])
# store elements into the array x
print('How many elements in the array?', end='')
n = int(input())
for i in range(n):
    print('Enter element:', end='')
    x.append(int(input()))  # add element to the array x
    
print('Original array:', x)

# bubble sort
flag = False  # when swapping is done, flag becomes true
for i in range(n-1):  # i is from 0 to n-1
    for j in range(n-1-i):  # j is from than one element lesser than i
        if x[j] > x[j+1]: # if first element is bigger than 2nd element
           t = x[j]  # swap j and j+1 element
           x[j] = x[j+1]
           x[j+1] = t
           flag = True   # swapping is done, flag value becomes true
    if flag ==  False:
        break
    else:
        flag = False  # assign initial value to flag
        
print("Sorted array:", x)
        
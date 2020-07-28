# program to accept marks and find percentage
from array import *

str1 = input('enter the marks:').split(' ')
# store the marks into marks array
marks = [int(num) for num in str1]
# display the marks and find total
sum1 = 0
for x in marks:
    print(x)
    sum1 = sum1 + x
print('Total marks:', sum1)

# display percentage
n = len(marks)  # n = no. of elements in an array
percent = sum1/n
print('Percentage:', percent)

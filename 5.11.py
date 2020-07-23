# accepting 3 numbers seperated by space
# program 11,12,13 in this file only
var1, var2, var3 = [int(x) for x in input("Enter the numbers: ").split()]
print("Sum is", var1 + var2 + var3)

# accepting 3 numbers seperated by comma
var1, var2, var3 = [int(x) for x in input("Enter the numbers: ").split(',')]
print("Sum is", var1 + var2 + var3)

# accepting a group of strings from keyboard
lst = [x for x in input("Enter the strings: ").split(',')]
print("You entered:\n", lst)

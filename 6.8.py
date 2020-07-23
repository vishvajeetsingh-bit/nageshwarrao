# understanding assert statement
x = int(input("Enter a number greater than 0:"))
assert x > 0, "Wrong number entered"
print('You Entered: ', x)

# to handle AssertionError raised by assert
x = int(input("Enter a number greater than 0: "))
try:
    assert(x > 0)  # exception may occur here
    print("You entered: ", x)
except AssertionError:
    print("Wrong number entered")

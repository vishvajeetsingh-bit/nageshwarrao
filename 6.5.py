# to display stars in equilateral triangular form
n = 40
for i in range(1, 11):
    print(' ' * n, end="")  # to repeat space for n times
    print('* ' * i)  # repeat stars for i times
    n = n-1

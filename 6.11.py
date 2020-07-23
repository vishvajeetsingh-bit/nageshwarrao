# program to evaluate sine series
# accept user input
x, n = [int(i) for i in input("Enter angle values, no. of iterations").split(',')]
# convert the angle from degree into radians
r = (x * 3.14159) / 180
# the first term
t = r
# find the sum till now
sum1 = r
# display the iteration number and sum
print('Iteration = %d\tSum = %f' % (1, sum1))
# denominator for the second term
i = 2
# repeat for 2nd to nth terms
for j in range(2, n + 1):
    t = (-1) * t * r * r / (i * (i + 1))  # find the next term
    sum1 = sum1 + t
    print('Iteration = %d\tSum = %f' % (j, sum1))
    i +=2  # increase i by the value of 2

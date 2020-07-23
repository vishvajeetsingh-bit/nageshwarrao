# program to evaluate Exponential Series
# accept user input
x, n = [int(i) for i in input("Enter power of e, no. of iterations").split(',')]
t = 1
sum1 = t
print('Iteration = %d\tSum = %f' % (1, sum1))
for j in range(1, n):
    t = t * x/j
    sum1 = sum1 + t
    print('Iteration = %d\tSum = %f' % (j, sum1))

# to find sum of even numbers
import sys

# read command line arguments except the program name
args = sys.argv[1:]
print(args)
summ = 0

# find sum  of even numbers
for a in args:
    x = int(a)
    if x % 2 == 0:
        summ = summ+x

print('sum of evens=', summ)

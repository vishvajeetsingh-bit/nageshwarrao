# to find power value of a number
import argparse

# call the ArgumentParser()
parser = argparse.ArgumentParser()

# Add the arguments to the parser
parser.add_argument('nums', nargs=2)

# retrieve  the argument into args object
args = parser.parse_args()

# find the power value
# args.nums represent a line
print('number=', args.nums[0])
print('It power =', args.nums[1])

# convert the arguments into float  and  find power
result = float(args.nums[0])**float(args.nums[1])
print('Result=', result)

# to find power value of a number
import argparse

# call the ArgumentParser()
parser = argparse.ArgumentParser()

# add the argument to the parser
parser.add_argument('nums', nargs='+')

# retrieve the arguments into the args object
args = parser.parse_args()

# display the arguments from the list: args.nums
for x in args.nums:
    print(x)

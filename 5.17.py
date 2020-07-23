# to display command line args.
import sys
n = len(sys.argv)  # n is the number of arguments
args = sys.argv  # args contains list of arguments
print("No. of command line args=", n)
print("the args are", args)
print("The args one by one:")
for a in args:
    print(a)

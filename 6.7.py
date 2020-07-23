# to display numbers in 10 rows and 10 columns
for x in range(1, 11):
    for y in range(1, 11):
        print(x * y, end='')
    print()

# to display numbers in 10 rows and 10 columns - v2.0
for x in range(1, 11):
    for y in range(1, 11):
        print('{:8}'.format(x * y), end='')
    print()

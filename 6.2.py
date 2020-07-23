# to display even numbers between m and n
m, n = [int(i) for i in input('Enter minimum and maximum range:').split(",")]
x = m
if x % 2 != 0:
    x = x + 1

while m <= x <= n:
    print(x)
    x += 2

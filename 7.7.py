from array import *

x = array('i', [10, 20, 30, 40, 50, 60, 70])
y = x[1:4]
print(y)

y = x[0:]
print(y)

y = x[:4]
print(y)

y = x[-4:]
print(y)

y = x[-4: -1]
print(y)

y = x[0:7:2]
print(y)


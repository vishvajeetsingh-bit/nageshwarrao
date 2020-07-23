# input from other number systems
string = input("Enter the hexadecimal string:")
n = int(string, 16)  # inform the number base is 16
print("Hexadecimal to decimal:", n)
string = input("Enter octal number:")
n = int(string, 8)  # inform the number base is 8
print("Octal to decimal:", n)
string = input("Enter binary number:")
n = int(string, 2)  # inform the number base is 2
print("binary to decimal:", n)

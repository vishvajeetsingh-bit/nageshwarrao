# to print prime numbers upto a given number
# accept upto what number the user wants
maxy = int(input("Upto what number?: "))

for num in range(2, maxy+1):
    for i in range(2, num):
        if(num % i) == 0:
            break  # then it is not prime, hence go back and check next number
        else:
            print(num)  # otherwise it is prime and display the number

#!/usr/bin/python3

def fizzbuzz():
    for num in range(1, 101):
        value = ''
        if num % 15 == 0:
            value = "FizzBuzz"
        elif num % 3 == 0:
            value = "Fizz"
        elif num % 5 == 0:
            value = "Buzz"
        else:
            value = str(num)
        print("{:s}".format(value), end=" ")

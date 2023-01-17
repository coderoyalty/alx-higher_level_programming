#!/usr/bin/python3

def print_last_digit(number):
    if int(number) < 0:
        number = -number
    last_digit = int(number) % 10
    print(last_digit, end="")
    return last_digit

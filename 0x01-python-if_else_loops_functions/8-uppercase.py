#!/usr/bin/python3

def uppercase(str):
    for ch in str:
        in_ascii = ord(ch)
        char = ''
        if in_ascii in range(ord('a'), ord('z') + 1):
            char = chr(in_ascii - 32)
        else:
            char = ch
        print("{:s}".format(char), end="")
    print('')

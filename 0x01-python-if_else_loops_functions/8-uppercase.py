#!/usr/bin/python3

def uppercase(str):
    for ch in str:
        in_ascii = ord(ch)
        if in_ascii in range(ord('a'), ord('z') + 1):
            print("{}".format(chr(in_ascii - 32)), end="")
        else:
            print(ch, end="")

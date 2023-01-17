#!/usr/bin/python3
for val in range(ord('a'), ord('z') + 1):
    if val == ord('e') or val == ord('q'):
        continue
    print("{:c}".format(val), end="")

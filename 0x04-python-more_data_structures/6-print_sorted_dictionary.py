#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for val in sorted(a_dictionary.keys()):
        dict_val = a_dictionary[val]
        print(f"{val:s}: {dict_val}")

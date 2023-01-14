#!/bin/usr/python3

def simple_delete(dictionary, key=""):
    if key in dictionary:
        del dictionary[key]
    return dictionary

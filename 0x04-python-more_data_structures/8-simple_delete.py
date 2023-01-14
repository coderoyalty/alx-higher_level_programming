#!/bin/usr/python3

def simple_delete(dictionary, key=""):
    try:
        del dictionary[key]
        return dictionary
    except KeyError:
        return dictionary

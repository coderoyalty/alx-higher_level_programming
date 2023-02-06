#!/usr/bin/python3
""" function that returns the list
of available attributes of an object
"""

def lookup(obj):
    """ function: lookup()
    Returns a list of object
    """

    return dir(obj)


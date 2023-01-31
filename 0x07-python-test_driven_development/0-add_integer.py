#!/usr/bin/python3
"""define an integer addition function."""

def add_integer(a, b=98):
    """return the integer sum of a and b.

    Float arguments are typecasted into integer.

    Raises:
        TypeError: If either a or b is non-integer or non-float.
    """
    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int)) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))

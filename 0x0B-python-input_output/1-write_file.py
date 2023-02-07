#!/usr/bin/python3
"""
function that writes to a file
"""

def write_file(filename="", text=""):
    """module write_file 
    """
    with open(filename, mode="w") as myFile:
        return myFile.write(text)

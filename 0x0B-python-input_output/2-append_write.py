#!/usr/bin/python3
"""
function that appends a string at the end of a text file (UTF8) and returns the number of characters added
"""

def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF8 text file.
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)

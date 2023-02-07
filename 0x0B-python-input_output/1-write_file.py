#!/usr/bin/python3
"""
function that writes to a file
"""

def write_file(filename="", text=""):
    """writes a text to a text file
    Returns none
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)

#!/usr/bin/python3
"""
fetches a url and displays the value of a variable
in the header of the response.
"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as resp:
        var = 'X-Request-Id'
        print(resp.headers.get(var))

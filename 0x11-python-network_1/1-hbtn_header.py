#!/usr/bin/python3
'''
script to send a request to a URL and displays the value
of the X-Request-Id variable in the header of the response
from the URL.
'''
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers['X-Request-Id'])

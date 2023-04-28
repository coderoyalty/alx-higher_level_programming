#!/usr/bin/python3
"""
sends a request to a URL and displays the body
of the response.
"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as resp:
            content = resp.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))

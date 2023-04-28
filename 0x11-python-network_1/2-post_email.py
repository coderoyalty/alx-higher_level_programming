#!/usr/bin/python3
'''
script that sends a post request to the passed URL
with the email as a parameter, and displays the body
of the response
'''
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    value = sys.argv[2]
    data = {"email": value}

    data = urllib.parse.urlencode(data).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))

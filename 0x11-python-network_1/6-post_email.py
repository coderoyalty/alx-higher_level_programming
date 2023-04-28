#!/usr/bin/python3
'''
script that sends a post request to the passed URL
with the email as a parameter, and displays the body
of the response
'''
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    value = sys.argv[2]
    data = {"email": value}

    resp = requests.post(url, data=data)
    print(resp.text)

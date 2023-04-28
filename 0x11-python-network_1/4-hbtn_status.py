#!/usr/bin/python3
'''
scripts that fetches a url using requests module.
'''
import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    resp = requests.get(url)
    content = resp.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))

#!/usr/bin/python3
'''
python script that takes your github credentials
and uses the GitHub API to display your id.
'''
import requests
from requests import auth
import sys

if __name__ == '__main__':
    user, pat = sys.argv[1:]
    url = 'https://api.github.com/{}'.format(user)
    res = requests.get(url, auth=auth.HTTPBasicAuth(user, pat))
    print(res.json().get('id'))

#!/usr/bin/python3
'''
python script that takes your github credentials
and uses the GitHub API to display your id.
'''
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    pat = sys.argv[2]
    url = 'https://api.github.com/users/{}'.format(user)
    res = requests.get(url, auth=(user, pat))
    print(res.json().get('id'))

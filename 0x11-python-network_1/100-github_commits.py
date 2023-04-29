#!/usr/bin/python3
'''
python script that takes your github credentials
of a repo.
'''
import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    parameters = {"per_page": 10}
    res = requests.get(url, params=parameters)
    if res.status_code == 200:
        commits = res.json()
        for commit in commits:
            sha_code = commit.get('sha')
            author_data = commit.get('commit').get('author')
            if author_data is not None:
                name = author_data.get('name')
                print(f"{sha_code}: {name}")

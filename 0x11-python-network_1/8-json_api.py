#!/usr/bin/python3
'''
sends a POST request to 0.0.0.0:5000/search_user with
the letter as a parameter.
'''
import requests
import sys

if __name__ == '__main__':
    q = sys.argv[1] if len(sys.argv) == 2 else ""
    url = 'http://0.0.0.0:5000/search_user'
    data = {"q": q}
    response = requests.post(url, data=data)
    try:
        rjson = response.json()
        id = rjson.get('id')
        name = rjson.get('name')
        if not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except Exception as err:
        print("Not a valid JSON")

#!/bin/bash
# sends a POST request to a URL.
curl -s -X POST --data-urlencode "email=test@gmail.com" --data-urlencode "subject=I will always be here for PLD" $1

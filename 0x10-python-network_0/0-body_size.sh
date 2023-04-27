#!/bin/bash
# takes a URL and display the URL body size.
curl -sS $1 | wc -c

#!/bin/bash
# sends a GET request to a URL and display only body of
# a 200 status code response


response=$(curl -s -w "\n%{http_code}\n" "$1")
status_code=$(echo "$response" | tail -n 1)

if [ "$status_code" -eq 200 ]; then
	echo "$response" | head -n -2
fi

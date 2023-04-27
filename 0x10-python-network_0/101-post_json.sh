#!/bin/bash
#sends a post request with the contents of a file
curl -s -H "Content-Type: application/json" -X POST -d "@$1" "$2" 

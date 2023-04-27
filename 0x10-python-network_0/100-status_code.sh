#!/bin/bash
# displays only the status code of the response
curl -s -I "$1" | grep "HTTP" | cut -d " " -f2

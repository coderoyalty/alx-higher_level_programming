#!/bin/bash
#displays only the status code of the response from a URL
curl -s -I $1 | grep "HTTP" | cut -d " " -f2

#!/bin/bash
# displays only the status code of the response
curl -s -L -w "%{http_code}\n" -o /dev/null "$1"

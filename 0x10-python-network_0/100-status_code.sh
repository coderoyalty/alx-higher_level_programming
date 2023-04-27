#!/bin/bash
# displays only the status code of the response
curl -s -L -w "%{http_code}" -o /dev/null "$1"

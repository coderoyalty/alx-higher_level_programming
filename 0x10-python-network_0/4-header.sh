#!/bin/bash
# sends a GET request to a URL with an header variable sets.
curl -s -H "X-School-User-Id: 98" $1

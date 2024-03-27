#!/bin/bash
# This script sends a GET request to the URL passed as the first argument, including a custom header X-School-User-Id with the value 98, and displays the body of the response
curl -s -X GET -H "X-School-User-Id: 98" "$1"

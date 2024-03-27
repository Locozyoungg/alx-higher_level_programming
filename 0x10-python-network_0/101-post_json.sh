#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument,
# with the contents of a file passed as the second argument in the body of the request,
# and displays the body of the response.

file_content=$(cat "$2")

# Check if the file content is valid JSON
if ! jq -e . >/dev/null 2>&1 <<<"$file_content"; then
    echo "Not a valid JSON"
    exit 1
fi

# Send POST request and display response body
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"

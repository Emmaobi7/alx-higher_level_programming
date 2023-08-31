#!/bin/bash
# sends POST request with file
curl -sH "content-Type: application/json" -d @$2 $1

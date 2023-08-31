#!/bin/bash
# sends OPTION http method request
curl -sIX OPTIONS $1 | grep "Allow" | cut -d' ' -f 2-

#!/usr/bin/bash
# sends a POST request with data
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1

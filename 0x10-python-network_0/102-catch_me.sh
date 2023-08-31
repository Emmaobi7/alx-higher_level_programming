#!/bin/bash
# catch me
curl -sw "You got me!" 0.0.0.0:5000/catch_me | sed -n 's/.*\(You got me!\).*/\1/p'


#!/usr/bin/python3
"""using requests display header var"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers.get('X-Request-Id'))

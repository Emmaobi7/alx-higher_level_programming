#!/usr/bin/python3
"""sends a POST request"""

import sys
import urllib.request
import urllib.parse

if __name__ == '__main__':
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    code = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url, code)

    with urllib.request.urlopen(request) as response:
        print(response.decode('utf-8'))

#!/usr/bin/python3
"""send POST using requests"""

import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]

    data = {"email": sys.argv[2]}
    res = requests.post(url, data)
    print(res.text)

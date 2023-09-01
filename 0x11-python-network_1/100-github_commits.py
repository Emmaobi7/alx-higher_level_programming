#!/usr/bin/python3
"""holberton interview"""

import sys
import requests

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{owner}/{repo}/commits'
    res = requests.get(url)
    print(res.json())


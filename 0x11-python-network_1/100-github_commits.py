#!/usr/bin/python3
"""holberton interview"""

import sys
import requests

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    res = requests.get(url)
    commit = res.json()

    for index in range(10):
        sha = commit[index].get('sha')
        author = commit[index].get('commit').get('author').get('name')
        print(f'{sha}: {author}')

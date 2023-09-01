#!/usr/bin/python3
"""holberton interview"""

import sys
import requests

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    res = requests.get(url)
    commits = res.json()

    for commit in commits[0:10]:
        print(commit['sha'] + ':', commit['commit']['author']['name'])

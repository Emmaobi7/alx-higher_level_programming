#!/usr/bin/python3
"""send POST with json"""

import sys
import requests


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    data = {"q": letter}

    res = requests.post(url, data)

    try:
        res_data = res.json()
        if res_data == {}:
            print('No result')
        else:
            print('[{}] {}'.format(res_data.get('id'), res_data.get('name')))
    except ValueError as e:
        print('Not a valid JSON')

#!/usr/bin/python3
"""my github id haha"""

import sys
import requests

if __name__ == '__main__':
    user = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user'

    login = requests.get(url, auth=(user, token))
    login_data = login.json()
    print(login_data.get('id'))

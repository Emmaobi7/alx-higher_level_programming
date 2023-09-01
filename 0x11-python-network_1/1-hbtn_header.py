#!/usr/bin/python3
"""dispaly value of a var in header of response"""

import sys
import urllib.request

if __name__ == '__main__':
    
    with urllib.request.urlopen(sys.argv[1]) as response:
        content = response.getheader('X-Request-Id')
    print(content)

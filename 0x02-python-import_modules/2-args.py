#!/usr/bin/python3
import sys

if __name__ == "__main__":
    n = len(sys.argv) - 1

    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(n))

    i = 1
    while i <= n:
        print("{:d}: {}".format(i, sys.argv[i]))
        i += 1



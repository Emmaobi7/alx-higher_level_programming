#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
    except (TypeError, ZeroDivisionError):
        res = None
    finally:
        print("inside result: {}".format(res))

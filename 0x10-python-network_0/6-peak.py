#!/usr/bin/python3
""" a script peak in an unsorted list"""


def find_peak(list_of_integers):

    """
    find_peak: function to find peak
    (list_of_integers): a list of int
    """
    if list_of_integers:
        return max(list_of_integers)
    else:
        return None

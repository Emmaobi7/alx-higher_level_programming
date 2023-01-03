#!/usr/bin/python3
def max_integer(my_list=[]):
    count = len(my_list)
    max = my_list[0]
    if count == 0:
        return None
    else:
        for i in my_list:
            if i > max:
                max = i
    return max


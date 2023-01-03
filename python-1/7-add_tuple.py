#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)







    if len(tuple_a) < 2:
        list_a.append(0)
    if len(tuple_b) < 2:
        list_b.append(0)
    if len(tuple_b) > 2:
        pass
    new = [tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]]
    new_t = tuple(new)
    return new_t

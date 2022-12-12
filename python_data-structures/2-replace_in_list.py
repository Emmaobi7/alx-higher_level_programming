def replace_in_list(my_list, idx, element):
    lent = len(my_list)
    if idx <= lent:
        if idx >= 0 and idx < lent:
            my_list[idx] = element
            return my_list
        else:
            return (my_list)
    else:
        return (my_list)


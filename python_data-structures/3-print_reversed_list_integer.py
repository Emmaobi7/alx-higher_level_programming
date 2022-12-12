def print_reversed_list_integer(my_list=[]):
    lent = len(my_list)
    my_list.reverse()
    i = 0
    for i in range(lent):
        print("{:d}".format(my_list[i]))

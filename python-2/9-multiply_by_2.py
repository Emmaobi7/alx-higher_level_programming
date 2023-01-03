def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary
    for value in b_dictionary.values():
        value = value * 2
    return b_dictionary

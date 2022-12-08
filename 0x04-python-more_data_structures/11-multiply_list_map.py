def multiply_list_map(my_list=[], number=0):
    multiple_list = my_list and list(map(lambda x: x * number, my_list))
    return multiple_list

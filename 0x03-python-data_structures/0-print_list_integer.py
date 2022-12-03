#!/usr/bin/python3

# function that prints numbers in a list
def print_list_integer(my_list=[]):
    if not my_list:
        return
    else:
        for i in my_list:
            print("{}".format(i))

#!/usr/bin/python3

# print elements of list in reverse order
def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for i in my_list:
            print("{}".format(i))
#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    multiple_list = my_list and [item * number for item in my_list]
    return multiple_list

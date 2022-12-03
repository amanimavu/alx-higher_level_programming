#!/usr/bin/python3

# replace an element in a list without modifying the original
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    new_list = my_list[:]
    new_list[idx] = element
    return new_list

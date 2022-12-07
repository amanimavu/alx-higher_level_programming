#!/usr/bin/python3


def uniq_add(my_list=[]):
    y = 0
    sum_of_unique_num = 0
    if my_list:
        for i in set(my_list):
            sum_of_unique_num += i
    return sum_of_unique_num

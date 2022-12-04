#!/usr/bin/python3

def turn_to_array(tpl):
    lst = list(tpl)
    if len(lst) < 2:
        for i in range(2 - len(lst)):
            lst.append(0)
    if len(lst) > 2:
        lst = lst[:2]
    return lst

def add_tuple(tuple_a=(), tuple_b=()):
    array_a = turn_to_array(tuple_a)
    array_b = turn_to_array(tuple_b)

    result_array = [(x + y) for x, y in zip(array_a, array_b)]
    return tuple(result_array)

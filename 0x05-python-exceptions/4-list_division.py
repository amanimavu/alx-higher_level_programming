#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(0, list_length):
        try:
            operand1 = my_list_1[i]
            operand2 = my_list_2[i]
            result = operand1 / operand2
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            result_list.append(result)
            continue
    return (result_list)

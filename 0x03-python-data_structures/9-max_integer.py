#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    for i in range(1, len(my_list)):
        if my_list[i] < my_list[i - 1]:
            my_list[i] = my_list[i - 1]
    return (my_list[len(my_list) - 1])

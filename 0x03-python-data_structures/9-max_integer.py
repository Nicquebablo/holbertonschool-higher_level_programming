#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    largest = my_list.copy()
    largest.sort()
    return largest[-1]

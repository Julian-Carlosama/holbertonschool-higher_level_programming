#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        number = my_list[0]
        for x in my_list:
            if x > number:
                number = x
        return number
    return (None)

#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    len_lis = len(my_list)

    if idx < 0 or idx > (len_lis - 1):
        return(my_list)
    else:
        my_list[idx] = element
        return(my_list)

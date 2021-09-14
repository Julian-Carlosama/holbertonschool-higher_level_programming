#!/usr/bin/python3
def element_at(my_list, idx):

    leng_lis = len(my_list)

    if idx < 0 or idx > leng_lis - 1:
        return(None)
    else:
        return (my_list[idx])

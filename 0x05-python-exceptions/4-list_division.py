#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list3 = []
    i = 0

    while i < list_length:
        try:
            total = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            total = 0
        except ZeroDivisionError:
            print("division by 0")
            total = 0
        except IndexError:
            print("out of range")
            total = 0
        finally:
            my_list3.append(total)
        i += 1
        pass
    return(my_list3)

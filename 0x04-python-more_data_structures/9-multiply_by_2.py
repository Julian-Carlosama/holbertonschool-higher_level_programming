#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for i in new_dic:
        new_dic[i] *= 2 #a_dictionary[i]
    return (new_dic)
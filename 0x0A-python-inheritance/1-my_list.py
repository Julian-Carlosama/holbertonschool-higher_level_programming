#!/usr/bin/python3
"""
Class that print a list
"""


class MyList(list):
    """ method that prints the list, but sorted
    """
    def print_sorted(self):
        pr_list = self.copy()
        pr_list.sort()
        print(pr_list)

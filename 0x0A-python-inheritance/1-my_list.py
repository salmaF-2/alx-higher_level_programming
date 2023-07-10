#!/usr/bin/python3
"""
prints listsorted
"""


class MyList(list):
    """
    MyList class
    """
    
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        the elements of the list will be of type int
        """
        print(sorted(self))

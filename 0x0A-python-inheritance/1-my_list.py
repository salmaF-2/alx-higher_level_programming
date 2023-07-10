#!/usr/bin/python3
class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        the elements of the list will be of type int
        """
        sorte = sorted(self)
        print(sorte)

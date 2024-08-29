#!/usr/bin/python3
"""
This is the "4-print_square" module
"""


def print_square(size):
    """
    Description:
         function that prints a square with the character #.
    Args:
         size: the size length of the square
    Raise:
         TypeError:size must be an integer
         ValueError:size must be >= 0
    Return:
         square with "#"
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")

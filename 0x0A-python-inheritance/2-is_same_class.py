#!/usr/bin/python3
"""
check instance of the specified clas
"""


def is_same_class(obj, a_class):
    """
    type() function that returns True if the object
    is exactly an instance of the specified class
    otherwise False.
    """
    return (type(obj) is a_class)

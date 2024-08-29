#!/usr/bin/python3
"""
add_integer:
the "0-add_integer" module
define the function add_integer(a, b)
"""


def add_integer(a, b=98):
    """
    Description:
            this function return an integer: the addition of a and b
    Parameters:
            a (int or float): The first number.
            b (int or float): The second number. Default is 98.

    Returns:
            int: The addition of a and b.

    Raises:
            TypeError: If a or b is not an integer or float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b

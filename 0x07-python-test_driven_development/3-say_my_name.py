#!/usr/bin/python3
"""
function Prints "My name is <first_name> <last_name>"
"""


def say_my_name(first_name, last_name=""):
    """
    Description:
        Prints "My name is <first_name> <last_name>".
    Args:
        first_name (str): The first name.
        last_name (str): The last name. (Default is an empty string)
    Raises:
        TypeError: If first_name or last_name is not a str
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)

#!/usr/bin/python3
"""
module
"""


def read_file(filename=""):
    """ read_file function """
    with open(filename, 'r', encoding="utf-8") as f:
        read = f.read()
        print(read, end="")

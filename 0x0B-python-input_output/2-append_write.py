#!/usr/bin/python3
""" module """


def append_write(filename="", text=""):
    """ Append to a file function """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        return len(text)

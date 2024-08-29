#!/usr/bin/python3
""" modul """


def write_file(filename="", text=""):
    """ Write to a file function """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        return len(text)

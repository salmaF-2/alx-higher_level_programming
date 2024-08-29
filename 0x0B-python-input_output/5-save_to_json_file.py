#!/usr/bin/python3
""" module """
import json


def save_to_json_file(my_obj, filename):
    """ Save Object to a file function """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

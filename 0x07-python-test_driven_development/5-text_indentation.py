#!/usr/bin/python3
"""
This is the "5-text_indentation" module
"""


def text_indentation(text):
    """
    Description:
        function that prints a text with 2 new lines after each of characters
    Args:
        text:string
    Raise:
        TypeError:if text is not string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    marks = [".", "?", ":"]


    i = 0
    for items in text:
        if items in marks:
            if text[i + 1] == " ":
                text = text[:i + 1] + text[i + 2:]
        else:
            i += 1

    # Cats '\n\n' after the special char with removed space
    i = 0
    for items in text:
        if items in marks:
            text = text[:i + 1] + '\n\n' + text[i + 1:]
            i += 3
        else:
            i += 1

    print(text, end='')

#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            upper += chr(ord(char) - 32)
        else:
            upper += char
    return upper
for ascii in range(122, 97 - 1, -1):
    if ascii % 2 == 1:
        ascii = ord(uppercase(chr(ascii)))
    print("{}".format(chr(ascii)), end='')

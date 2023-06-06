#!/usr/bin/python3
for ascii in range(97, 123):
    if chr(ascii) not in [101, 113]:
        print("{}".format(chr(ascii)), end='')

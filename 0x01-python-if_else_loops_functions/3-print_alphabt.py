#!/usr/bin/python3
import itertools
ranges = [range(97, 101),range(102,113),range(114,123)]
for ascii in itertools.chain(*ranges):
    print("{}".format(chr(ascii)), end='')

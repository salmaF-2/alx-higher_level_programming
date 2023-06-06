#!/usr/bin/python3
for number in range(0, 100):
    if number == 99:
        separator = "\n"
    else:
        separator = ", "
    print("{:02d}".format(number), end=separator)


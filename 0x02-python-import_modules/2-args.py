#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number_args = len(argv) - 1
    if number_args == 0:
        print("0 arguments.")
    elif number_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(number_args))

    if number_args > 0:
        for i in range(1, number_args + 1):
            print("{}: {}".format(i, argv[i]))

#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0

    try:
        for i in my_list:
            if nb_print >= x:
                break
            if isinstance(i, int):
                print("{:d}".format(my_list[i]), end="")
                nb_print += 1
    except IndexError:
        pass
    print()
    return nb_print

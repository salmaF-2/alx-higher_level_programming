#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_print = 0

    try:
        for y in my_list:
            if nb_print < x:
                print(y, end="")
                nb_print += 1
    except error as e:
        print("An error occurred:", e)

    print()
    return nb_print

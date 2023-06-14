#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = list(set(my_list))
    sum = 0
    for element in uniq:
        sum += element
    return sum

#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is []:
        return None
    else:
        large = my_list[0]
        for number in my_list:
            if number > large:
                large = number
                return number

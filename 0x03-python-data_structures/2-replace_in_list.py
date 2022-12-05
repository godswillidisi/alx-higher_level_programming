#!/usr/bin/python3
def replace_in_list(my_list, idx, new_element):
    for i in range(len(my_list)):
        if idx < 0:
            return my_list
        if idx > len(my_list):
            return my_list
        else:
            return my_list[idx] = new_element


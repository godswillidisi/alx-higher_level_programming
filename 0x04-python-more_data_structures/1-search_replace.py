#!/usr/bin/python3
def search_replace(my_list, search, replace):
    search = 2
    replace = 89
    my_list = list(map(lambda x: x.replace(2, 89), my_list))
    return my_list

#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for q, w in sorted(a_dictionary.items()):
        print("{}: {}".format(q, w))

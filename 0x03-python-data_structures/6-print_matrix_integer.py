#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    [[row[i] for row in matrix] for i in range(3)]
    print("{}".format(matrix[i]))

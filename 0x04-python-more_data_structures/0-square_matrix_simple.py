#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 1 and any(matrix) is False:
        return

    new_matrix = []

    for x in matrix:
        val = list(map(lambda mul: mul ** 2, x))
        new_matrix.append(val)

    return(new_matrix)

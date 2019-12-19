#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for x in matrix:
        val = list(map(lambda mul: mul ** 2, x))
        new_matrix.append(val)

    return(new_matrix)

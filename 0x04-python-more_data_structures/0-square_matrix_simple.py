#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    squared_matrix = matrix and [[(col ** 2) for col in row] for row in matrix]
    return squared_matrix

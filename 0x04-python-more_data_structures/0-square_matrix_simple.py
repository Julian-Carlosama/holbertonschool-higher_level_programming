#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        obje = map(lambda x: x**2, matrix[i])
        new_matrix[i] = list(obje)

    return (new_matrix)
    return (matrix)

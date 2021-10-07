#!/usr/bin/python3
def matrix_divided(matrix, div):

    printE = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(printE)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    elements = 0

    for items in matrix:
        if not isinstance(items, list) or not items:
            raise TypeError(printE)

        if len(items) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for i in items:
            if not isinstance(i, (int, float)):
                raise TypeError(printE)

    new = matrix

    for items in range(len(matrix)):
        result = (list(map(lambda x: round(x / div, 2), matrix[items])))
        new[items] = result
    return(new)

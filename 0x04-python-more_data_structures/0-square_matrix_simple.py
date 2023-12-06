#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix."""
    # Use map and lambda to apply the square operation to each element
    new_matrix = list(map(lambda row: list(map(lambda x: x**2, row)), matrix))

    return new_matrix

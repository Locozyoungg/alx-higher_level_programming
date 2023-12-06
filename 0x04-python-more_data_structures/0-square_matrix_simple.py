#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix."""
    # Initialize an empty list to store the new matrix
    new_matrix = []

    # Iterate over each row in the input matrix
    for row in matrix:
        # Use list comprehension to create a new row with squared values
        new_row = [x**2 for x in row]
        
        # Append the new row to the new matrix
        new_matrix.append(new_row)

    # Return the resulting new matrix
    return new_matrix

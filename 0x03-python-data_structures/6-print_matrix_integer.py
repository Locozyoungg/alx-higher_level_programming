#!/usr/bin/python3

def print_matrix_integer(matrix=None):
    if matrix is None:
        return

    for row in matrix:
        for num in row[:-1]:
            print("{:d} ".format(num), end="")
        if row:
            print("{:d}".format(row[-1]))
        else:
            print()

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()

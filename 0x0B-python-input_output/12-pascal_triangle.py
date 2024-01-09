#!/usr/bin/python3
"""
12-pascal_triangle
"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the given number of rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle

def print_triangle(triangle):
    """
    Print the triangle.

    Args:
        triangle (list): A list of lists representing Pascal's Triangle.
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))


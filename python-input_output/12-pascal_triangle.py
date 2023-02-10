#!/usr/bin/python3
"""12-pascal_triangle.py"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s triangle of n."""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        triangle.append([1] + [triangle[i - 1][j] + triangle[i - 1][j + 1] for j in range(i - 1)] + [1])
    return triangle

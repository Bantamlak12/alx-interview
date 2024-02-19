#!/usr/bin/python3
"""
A module that rotates a 2D Matrix 90 degree
"""


def rotate_2d_matrix(matrix):
    """ A function that rotates a matrix by 90 degree clockwise in-place.

    Arg:
    - matrix: A `n` X `n` 2D matrix
    """
    if len(matrix) == 0:
        return

    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(i + 1, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix[i].reverse()

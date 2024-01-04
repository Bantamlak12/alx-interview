#!/use/bin/python3
"""A module that returns a pascals triangle"""


def pascal_triangle(n):
    """Solves a pascal's triangle"""
    if n <= 0:
        triangle = []
        return triangle

    triangle = [[1]]

    for i in range(n - 1):
        temp = [0] + triangle[-1] + [0]
        row = []
        for j in range(len(temp) - 1):
            row.append(temp[j] + temp[j + 1])
        triangle.append(row)
    return triangle

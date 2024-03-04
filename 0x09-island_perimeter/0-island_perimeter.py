#!/usr/bin/python3
""" Island perimeter
"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid

    Args:
    - grid(List[list])
        - 0 represents water
        - 1 represents land
        - Each cell is square, with side length of 1
        - Cells are connected horizontally/vertically(not diagonally)
        - grid is rectangular, with its width and height exceeding 100
    """
    perimeter = 0
    len_row = len(grid)
    len_col = len(grid[0])

    if len_row > 100 or len_col > 100 or not isinstance(grid, list):
        return

    for row in range(len_row):
        for col in range(len_col):
            if grid[row][col] == 1:
                if grid[row][col] == 1:
                    # Check top
                    if row == 0 or grid[row - 1][col] == 0:
                        perimeter += 1
                        # Check left
                    if col == 0 or grid[row][col - 1] == 0:
                        perimeter += 1
                        # Check right
                    if col == len_col - 1 or grid[row][col + 1] == 0:
                        perimeter += 1
                    # Check bottom
                    if row == len_row - 1 or grid[row + 1][col] == 0:
                        perimeter += 1
    return perimeter

#!/usr/bin/python3
import sys


def is_safe(column, row, placed_queens):
    """
    parameters:
    - column (int): Column of the queen placement
    - row (int): Row of the queen placement
    placed_queens (list): Lists of existing queens placed

    Returns:
    - True if the placement is safe else False
    """
    # Check for horizontal attack
    for c, r in placed_queens:
        if row == r:
            return False
    # Check for diagonal attack
    for c, r in placed_queens:
        x = column - c
        y = row - r
        if abs(x) == abs(y):
            return False
    return True


def solve_n_queens(n):
    """
    parameters:
    - n (int): Number of queens

    Returns:
    - List of list, where each inner list represent a position of
      a queen as [column, row]
    """
    solutions = []
    # To keep track of placed queens
    placed_queens = []

    def solve_backtrack(column):
        if column == n:
            return solutions.append(placed_queens[:])
        for row in range(n):
            if is_safe(column, row, placed_queens):
                placed_queens.append([column, row])
                solve_backtrack(column + 1)
                # Backtrack
                placed_queens.pop()

    # Start with the first column
    solve_backtrack(0)
    return solutions


def main():
    """ Main """
    try:
        try:
            n = int(sys.argv[1])
        except ValueError:
            print("N must be a number")
            exit(1)
        if n >= 4:
            solutions = solve_n_queens(n)
            for solution in solutions:
                print(solution)
        else:
            print("N must be at least 4")
            exit(1)
    except IndexError:
        print("Usage: nqueens N")
        exit(1)


if __name__ == "__main__":
    main()

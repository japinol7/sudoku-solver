__author__ = 'Joan A. Pinol  (japinol)'

from sudokusolver.config.config import SUDOKU_SIZE


def solve_backtracking(sudoku):
    """Solves a given sudoku using a simple backtracking technique."""
    empty_cell = sudoku.find_empty_cell()
    if not empty_cell:
        return True
    row, col = empty_cell

    for i in range(1, SUDOKU_SIZE + 1):
        if sudoku.valid(i, (row, col)):
            sudoku.board[row][col] = i
            if solve_backtracking(sudoku):
                return True
            sudoku.board[row][col] = 0
    return False

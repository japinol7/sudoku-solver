"""Module controller."""
__author__ = 'Joan A. Pinol  (japinol)'

from sudokusolver.tools.logger.logger import log
from sudokusolver.tools.utils.time_it import time_it
from sudokusolver.model.sudoku import Sudoku
from sudokusolver.solver.backtracking import solve_backtracking


class SudokuController:

    @staticmethod
    def load_sudoku(name, print_input_sudoku):
        sudoku = Sudoku(name)
        log.info(f"Load sudoku: {sudoku.name}")
        time_it(sudoku.load)
        log.info(f"Sudoku loaded: {sudoku.name}\n"
                 f"{sudoku}")
        if print_input_sudoku:
            SudokuController.print_board(sudoku)
        return sudoku

    @staticmethod
    def solve_sudoku(sudoku, print_solution=None):
        log.info(f"Solve sudoku: {sudoku.name}")
        is_solved = time_it(solve_backtracking, sudoku)
        sudoku.is_solved = True
        if not is_solved:
            sudoku.is_solved_successfully = False
            log.warning(f"No solutions found for sudoku: {sudoku.name}")
            return None

        sudoku.is_solved_successfully = True
        log.info(f"Solution found for sudoku: {sudoku.name}\n"
                 f"{sudoku}")

        if print_solution:
            SudokuController.print_board(sudoku)
        return sudoku

    @staticmethod
    def print_board(sudoku):
        if sudoku.is_solved and not sudoku.is_solved_successfully:
            print(f"No solutions found for sudoku: {sudoku.name}")
            return

        if sudoku.is_solved and sudoku.is_solved_successfully:
            print(f"Solution found for sudoku: {sudoku.name}")
        else:
            print(f"Sudoku board: {sudoku.name}")

        print(sudoku)

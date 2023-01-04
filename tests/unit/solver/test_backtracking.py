import pytest

from sudokusolver.controller.controller import SudokuController
from sudokusolver.model.sudoku import Sudoku
from sudokusolver.solver.backtracking import solve_backtracking
from tests.unit.solver.conftest import SUDOKU_TESTS


class TestSudokuBacktrackingSolver:
    @pytest.mark.parametrize('sudoku_name, sudoku_board, expected', [
        ('test1', SUDOKU_TESTS[0]['sudoku'], SUDOKU_TESTS[0]['sudoku_solved']),
        ('test2', SUDOKU_TESTS[1]['sudoku'], SUDOKU_TESTS[1]['sudoku_solved']),
        ])
    def test_sudoku_solver(self, sudoku_name, sudoku_board, expected):
        sudoku = Sudoku(sudoku_name)
        sudoku.board = sudoku_board
        is_solved = solve_backtracking(sudoku)
        assert is_solved is True

        result = sudoku.board
        assert result == expected
        print('\n')
        SudokuController.print_board(sudoku)

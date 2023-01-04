__author__ = 'Joan A. Pinol  (japinol)'

import os

from sudokusolver.config.config import (
    SUDOKU_SIZE,
    SUDOKU_BOX_SIZE,
    CELL_SEPARATOR,
    FILE_INPUT_PATH,
    FILE_TXT_EXT,
    )


class Sudoku:
    def __init__(self, name):
        self.name = name
        self.file_name = f'{self.name}.{FILE_TXT_EXT}'
        self.board = None
        self.is_empty = True
        self.is_solved = False
        self.is_solved_successfully = False

    def load(self):
        file_path_name = os.path.join(FILE_INPUT_PATH, self.file_name)
        with open(file_path_name, 'r', encoding='utf8') as fin:
            lines = fin.readlines()

        self.board = []
        for line in lines:
            row = []
            cols = line.strip().split(CELL_SEPARATOR)
            for col in cols:
                row.append(int(col))
            self.board.append(row)
        self.is_empty = False

    def valid(self, num, pos):
        for row in range(len(self.board[0])):
            if self.board[pos[0]][row] == num and pos[1] != row:
                return False
        for col in range(len(self.board)):
            if self.board[col][pos[1]] == num and pos[0] != col:
                return False

        # Check box
        box_x = pos[1] // SUDOKU_BOX_SIZE
        box_y = pos[0] // SUDOKU_BOX_SIZE
        for row in range(box_y * SUDOKU_BOX_SIZE, box_y * SUDOKU_BOX_SIZE + SUDOKU_BOX_SIZE):
            for col in range(box_x * SUDOKU_BOX_SIZE, box_x * SUDOKU_BOX_SIZE + SUDOKU_BOX_SIZE):
                if self.board[row][col] == num and (row, col) != pos:
                    return False
        return True

    def find_empty_cell(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 0:
                    return row, col
        return None

    def __str__(self):
        if not self.board:
            return ''

        res = []
        for row in range(len(self.board)):
            if row % SUDOKU_BOX_SIZE == 0 and row != 0:
                res += ['- ' * (SUDOKU_BOX_SIZE * SUDOKU_BOX_SIZE + SUDOKU_BOX_SIZE), '\n']
            for col in range(len(self.board[0])):
                if col % SUDOKU_BOX_SIZE == 0 and col != 0:
                    res += [' | ']
                if col == SUDOKU_SIZE - 1:
                    res += [str(self.board[row][col] if self.board[row][col] != 0 else ' '), '\n']
                else:
                    res += [str(self.board[row][col] if self.board[row][col] != 0 else ' ') + ' ']
        return ''.join(res[:-1])

    def __repr__(self):
        return f"{self.__class__.__name__}(" \
               f"name='{self.name}')"

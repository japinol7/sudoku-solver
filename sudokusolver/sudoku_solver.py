"""Solves sudokus."""

__author__ = 'Joan A. Pinol  (japinol)'

import os
import time

from sudokusolver.tools.logger.logger import log
from sudokusolver.controller.controller import SudokuController
from sudokusolver.config.config import FILE_INPUT_PATH, FILE_TXT_EXT


def _sudoku(controller, sudoku_name, print_input_sudoku, print_solution):
    time_start = time.perf_counter()
    sudoku = controller.load_sudoku(sudoku_name, print_input_sudoku)
    controller.solve_sudoku(sudoku, print_solution)
    log.info(f'Total time processing sudoku {sudoku_name}: {time.perf_counter() - time_start:.{8}f} s')


def sudokus(sudoku_name, process_folder, print_input_sudoku, print_solution):
    controller = SudokuController()

    if process_folder:
        file_names = [file[:-4] for file in os.listdir(FILE_INPUT_PATH) if file.endswith(FILE_TXT_EXT)]
        log.info("Processing all sudokus from input directory")
        sudokus_total = len(file_names)
        for i, file_name in enumerate(file_names, start=1):
            log.info('-' * 15)
            log.info(f"Processing sudoku {i:3} of {sudokus_total:3}")
            _sudoku(controller, file_name, print_input_sudoku, print_solution)
        log.info('-' * 15)
        return

    _sudoku(controller, sudoku_name, print_input_sudoku, print_solution)

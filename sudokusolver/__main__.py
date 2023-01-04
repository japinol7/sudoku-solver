"""Module __main__. Entry point."""
__author__ = 'Joan A. Pinol  (japinol)'

from argparse import ArgumentParser
import traceback
import sys

from sudokusolver.tools.logger import logger
from sudokusolver.tools.logger.logger import log, LOGGER_FORMAT, LOGGER_FORMAT_NO_DATE
from sudokusolver.config.config import (
    LOG_START_APP_MSG,
    LOG_END_APP_MSG,
    LOG_CRITICAL_ERROR_MSG,
    SUDOKU_NAME_DEFAULT,
    )
from sudokusolver.sudoku_solver import sudokus


def main():
    """Entry point of The Sudoku Solver program."""
    # Parse optional arguments from the command line
    parser = ArgumentParser(description="Sudoku Solver.",
                            prog='sudokusolver')
    parser.add_argument('-n', '--name', default=None,
                        help="the sudoku's name.")
    parser.add_argument('-l', '--multiplelogfiles', default=False, action='store_true',
                        help='A log file by app execution, instead of one unique log file')
    parser.add_argument('-m', '--stdoutlog', default=False, action='store_true',
                        help='Print logs to the console along with writing them to the log file')
    parser.add_argument('-p', '--nologdatetime', default=False, action='store_true',
                        help='Logs will not print a datetime')
    parser.add_argument('-d', '--debug', default=None, action='store_true',
                        help='Debug actions when pressing the right key, information and traces')
    parser.add_argument('-pd', '--processinputdir', default=False, action='store_true',
                        help="solve all sudokus from the input directory.")
    parser.add_argument('-t', '--debugtraces', default=None, action='store_true',
                        help='Show debug back traces information when something goes wrong')
    args = parser.parse_args()

    def _logger_init():
        logger_format = LOGGER_FORMAT_NO_DATE if args.nologdatetime else LOGGER_FORMAT
        args.stdoutlog and logger.add_stdout_handler(logger_format)
        not args.stdoutlog and print(LOG_START_APP_MSG)
        logger.add_file_handler(args.multiplelogfiles, logger_format)
        log.info(LOG_START_APP_MSG)
        log.info(f"App arguments: {' '.join(sys.argv[1:])}")

    try:
        _logger_init()
        sudoku_name = args.name or SUDOKU_NAME_DEFAULT
        process_folder = args.processinputdir
        sudokus(sudoku_name, process_folder, print_input_sudoku=True, print_solution=True)
    except FileNotFoundError as e:
        if args.debugtraces or args.debug:
            traceback.print_tb(e.__traceback__)
        log.critical(f'File not found error: {e}')
        not args.stdoutlog and print(f'{LOG_CRITICAL_ERROR_MSG}{e}')
    except Exception as e:
        if args.debugtraces or args.debug:
            traceback.print_tb(e.__traceback__)
        log.critical(f'ERROR. Abort execution: {e}')
        not args.stdoutlog and print(f'{LOG_CRITICAL_ERROR_MSG}{e}')

    log.info(LOG_END_APP_MSG)
    not args.stdoutlog and print(LOG_END_APP_MSG)


if __name__ == '__main__':
    main()

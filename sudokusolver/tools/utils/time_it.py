"""Module time_it."""
__author__ = 'Joan A. Pinol  (japinol)'

import time

from sudokusolver.tools.logger.logger import log


def time_it(func, *args, **kwargs):
    """Benchmarks a given function."""
    start = time.perf_counter()
    res = func(*args, **kwargs)
    log.info(f'{func.__name__} t: {time.perf_counter() - start:.{8}f} s')
    return res

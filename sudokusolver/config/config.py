from datetime import datetime
import os
import sys

from sudokusolver.version import version

APP_NAME = 'sudokusolver'

SUDOKU_SIZE = 9
SUDOKU_BOX_SIZE = 3
CELL_SEPARATOR = ','

SUDOKU_NAME_DEFAULT = 'sudoku_01'

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 900

FILE_INPUT_PATH = os.path.join('files', 'input')
FILE_OUTPUT_PATH = os.path.join('files', 'output')
FILE_TXT_EXT = 'txt'

LOG_START_APP_MSG = f"Start app {APP_NAME} version: {version.get_version()}"
LOG_END_APP_MSG = f"End app {APP_NAME}"

LOG_INPUT_ERROR_PREFIX_MSG = "User input error. "
LOG_CRITICAL_ERROR_MSG = "CRITICAL ERROR. Abort execution: "

LOG_FILE = os.path.join('logs', f"log_{datetime.now().strftime('%Y-%m-%d_%H_%M_%S_%f')}.log")
LOG_FILE_UNIQUE = os.path.join('logs', "log.log")
SYS_STDOUT = sys.stdout
SCORES_FILE = os.path.join('files', 'scores.txt')


SOUND_FORMAT = 'ogg'
MUSIC_FORMAT = 'ogg'

MUSIC_BOX = (
    f'action_song__192b.{MUSIC_FORMAT}',
    )

FILE_NAMES = {
    'im_background': ('background', 'png'),
    'im_screen_help': ('screen_help', 'png'),
    'im_logo_japinol': ('logo_japinol_ld', 'png'),
    'im_help_key': ('help_key', 'png'),
    'bg_blue_t1_big_logo': ('bg_blue_t1_big_logo', 'png'),
    'im_bg_blue_t1': ('bg_blue_t1', 'png'),
    'im_bg_blue_t2': ('bg_blue_t2', 'png'),
    'im_bg_black_t1': ('bg_black_t1', 'png'),
    'im_board': ('board', 'png'),
    'im_piece': ('piece', 'png'),
    'life_heart': ('heart', 'png'),
    'im_clocks': ('clock', 'png'),
    'snd': ('snd', SOUND_FORMAT),
    }

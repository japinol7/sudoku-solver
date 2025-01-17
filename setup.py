from setuptools import setup

setup(
    name='sudokusolver',
    author='Joan A. Pinol  (japinol)',
    version='0.0.2',
    license='MIT',
    description="Solves sudokus.",
    long_description="Solves sudokus.",
    url='https://github.com/japinol7/sudoku-solver',
    packages=['sudokusolver'],
    python_requires='>=3.13',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'sudokusolver=sudokusolver.__main__:main',
            ],
    },
)
